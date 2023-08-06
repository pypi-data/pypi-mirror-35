"""
HawkEncrypt API Python bindings by Dalen Bernaca

hcrypt.c Version: 0.91 beta
crypt.py Version: 1.0  beta

HawkCrypt is a cryptographic library for password protecting data. It uses MD5
to produce 128 bit encryption keys and random 128 bit (16 byte) salt values.
Blowfish is used to perform 128 bit encryption. It also provides MD5 hashing
to add a 32 bit message authentication code (MAC) to packets using a shared
password. The MAC is separate from encryption so you can authenticate without
encrypting if you choose. The 32 bit MAC is created by folding the 128 bit MD5
hash down to 32 bits.

If you want to use encryption with a MAC, I suggest you encrypt then add the
MAC. That way you can validate before you decrypt and save some CPU cycles if
you need to discard an invalid packet.

* Higher level encryption classes are added by Dalen
  to simplify use of the encryption/decryption and
  provide more Pythonic interface.
"""

from structures import BF_KEY, hcrypt_key, hcrypt_salt
from tweaks import String as _str
import lib

for func in lib.hcrypt_funcs:
    globals()[func] = getattr(lib, func)
del func

class Key:
    """
    Instantiates a higher level Key() object to use with Packet() class and with Encoder() and Decoder()
    classes from hvdi.hvdi module.
    """
    import tweaks as c
    def __init__ (self, password=None, salt=None):
        """
        If password is None the output of:
        os.urandom(32) will be used instead.
        You can always find out what it is by using the method getpassword().

        If salt is None it will be generated.
        You can retrieve its string value using the getsalt() method.
        You can get it in the list form using the getsaltlist() method.
        You can get the ctypes array in which it is stored using the getsaltarray() method.
        You can get the ctypespointer to initialized hcrypt_salt structure using the getsaltptr() method.
        You can get the initialized ctypes hcrypt_salt structure itself using the getsaltobj() method.

        If you already have a salt then provide it as a 16 characters long string,
        an initialized hcrypt_salt structure, a pointer to initialized hcrypt_salt structure
        (as returned by hvdi.crypt.NewSalt()) or an iterable sequence
        of 16 integers ranging from 0 to 256.

        If you set salt to False or 0 the salt will not be used
        and your encryptions will be vulnerable to dictionary attacks.

        If you want to use only one Key() object in your program but multiple keys,
        you can use the change() function to reinitialize the object.

        To get to the ctypes pointer to initialized hcrypt_key structure, use the attribute "key".
        """
        c = self.c
        if salt==None:
            self.salt = NewSalt()
        elif not salt:
            self.salt = None
        elif hasattr(salt, "contents") and isinstance(salt.contents, hcrypt_salt):
            self.salt = salt
        elif isinstance(salt, hcrypt_salt):
            self.salt = c.pointer(salt)
        else:
            if len(salt)!=16:
                raise ValueError, "16 items required!"
            a = (c.c_ubyte*16)()
            if isinstance(salt, (str, bytes)):
                a[:] = map(ord, salt)
            else:
                salt = map(int, salt)
                if any((x<0 or x>255) for x in salt):
                    raise ValueError, "Value out of range. Items must be >= 0 and <= 255"
                a[:] = salt
            s = hcrypt_salt()
            s.data = a
            self.salt = c.pointer(s)
        if password: self.password = password
        else:
            import os
            self.password = os.urandom(32)
        self.key = NewKey(self.password, self.salt)

    def __del__ (self):
        """
        Clean up the memory.
        """
        try:
            if self.key:
                DeleteKey(self.key)
                del self.key
        except: pass
        try: 
            if self.salt:
                DeleteSalt(self.salt)
                del self.salt
        except: pass

    def change (self, password=None, salt=None):
        """
        Resets the object to the new values.
        See the __doc__ string for the __init__() method.
        """
        self.__del__()
        self.__init__(password, salt)

    def getsalt (self):
        """
        Returns the salt as a string of bytes.
        """
        return "".join(map(chr, self.salt.contents.data[:]))

    def getsaltptr (self):
        """
        Returns the ctypes pointer to the hcrypt_salt initialized structure.
        """
        return self.salt

    def getsaltobj (self):
        """
        Returns the ctypes hcrypt_salt initialized structure.
        """
        return self.salt.contents

    def getsaltarray (self):
        """
        Returns the ctypes.c_ubyte array housing the salt data.
        """
        return self.salt.contents.data

    def getsaltlist (self):
        """
        Returns the salt as a list of integers.
        """
        return self.salt.contents.data[:]

    def getpassword (self):
        """
        Returns the password used to generate the key.
        """
        return self.password

    def copy (self):
        """
        Returns a new copy of this Key() object.
        """
        return Key(self.password, self.getsalt())

    def tostring (self):
        """
        Returns a serialized version of complete key
        (password and salt) that can be used to store
        or transfer the key. The key is self signed for corruption checks.
        To get the Key() object back from the string
        use the class method Key.fromstring().
        """
        data = self.getsalt()+self.password
        return Packet(data, self).sign().getdata()

    @classmethod
    def fromstring (cls, key):
        """
        Returns a deserialized Key() object.
        key --> A string as returned by tostring() method
        """
        if len(key)<20:
            raise ValueError, "Input too short"
        salt   = key[:16]
        passwd = key[16:-4]
        k = Key(passwd, salt)
        if Packet(key, k, signed=1).verify():
            return k
        raise ValueError, "Key verification failed!"

    def __eq__ (self, other):
        """
        Two Key()s are considered equal when both
        their password and salt match.
        """
        if not isinstance(other, Key):
            return False
        if id(self)==id(other): return True
        if self.password!=other.password:
            return False
        return self.getsalt()==other.getsalt()

class Packet (_str):
    """
    This class represents one encryptable/decryptable packet.
    The class is ultimately inheriting from UserString() to provide
    direct access to the data involved.
    encrypt(), decrypt() or sign() methods will change the Packet()
    in place and return a reference to it self to use
    in chained operations.
    If you do not wish to mess up an old Packet(), then use the method copy() like this:
        op = Packet("something").sign()
        np = op.copy().encrypt()
    The method verify() will only return True/False depending on the result of verification.
    The method getkey() will return the Key() object being used as default key.
    All other methods return the Packet() object and can be used in chained operations.

    You can think about the Packet() as of a string with additional, useful methods.

    Be careful about the order of encrypting and signing if you use both.
    If you encrypt and sign in one order, then try to decrypt and verify in another, the verification will fail.
    """
    def __init__ (self, data, key=None, encrypted=0, signed=0, password=None, salt=None):
        """
        To initialize a new Packet() you need the following arguments:
        data      --> A Packet() data to be used
                      data can be another Packet() object too.
                      To learn how the data is inherited in such
                      a circumstance, see the __doc__ strings of
                      verify() and packet() methods.
        key       --> A Key() object to use in all operations
                      It can be None (default)
                      In this case a new key will be constructed using:
                      key = Key(password, salt)
                      To see how this will work see the Key()'s
                      class __doc__ string.
                      You can later access the generated key using the
                      Packet()'s "key" attribute.
                      If key is a string Key.fromstring() will be called.
        encrypted --> Is the data you provided encrypted or plain? (0 - plain - default)
        signed    --> Is the data you provided signed or not? (0 - not signed - default)
                      If signed is 1 then last 4 bytes of data
                      are considered a signature and are
                      separated from others.
                      They will be living in "signature" attribute.
                      To get complete data either extract the signature from the attribute or use
                      Packet().getdata() to get the whole buffer string.

        """
        if isinstance(data, Packet):
            p = data
            data = str(data)
            if signed and p.signed and not p.verified:
                signature = p.signature
            elif signed and p.signed and p.verified:
                signature = data[-4:]
                data = data[:-4]
            elif signed and not p.signed:
                signature = data[-4:]
                data = data[:-4]
            else:
                signature = ""
        else:
            signature = ""
            if signed:
                signature = data[-4:]
                data = data[:-4]
        _str.__init__(self, data)
        self.encrypted = encrypted
        self.signed    = signed
        self.signature = signature
        self.verified  = 0
        self.key       = key if key else Key(password, salt)

    def getdata (self):
        """
        Returns complete data along with signature if
        the Packet() was signed. The data is a str().
        """
        return str(self)+self.signature

    def encrypt (self, key=None):
        """
        Encrypts a Packet().
        If key is specified it overrides the default one.
        """
        if self.encrypted:
            raise ValueError, "Packet specified as already encrypted!"
        key = key.key if key else self.key.key
        if not self.signed:
            EncryptPacket(self, self, len(self), key)
            self.encrypted = 1
            return self
        buf = str(self)+self.signature
        EncryptPacket(buf, buf, len(buf), key)
        self.signature = buf[-4:]
        self[:] = buf[:-4]
        self.encrypted = 1
        return self

    def decrypt (self, key=None):
        """
        Decrypts a Packet().
        If key is specified it overrides the default one.
        """
        if not self.encrypted:
            raise ValueError, "Packet not specified as encrypted!"
        key = key.key if key else self.key.key
        if not self.signed:
            DecryptPacket(self, self, len(self), key)
            self.encrypted = 0
            return self
        buf = str(self)+self.signature
        DecryptPacket(buf, buf, len(buf), key)
        self.signature = buf[-4:]
        self[:] = buf[:-4]
        self.encrypted = 0
        return self

    def sign (self, key=None):
        """
        Signs a Packet().
        If key is specified it overrides the default one.
        It is advisable to use different keys for encryption and signing.
        """
        if self.signed:
            raise ValueError, "Packet() already signed. For multiple signings use multiple packets."
        key = key.key if key else self.key.key
        buf = str(self)+"    "
        SignPacket(buf, len(self), key)
        self.signature = buf[-4:]
        self.signed = 1
        return self

    def verify (self, key=None, remember=1, throw=0):
        """
        Verifies a Packet() by returning a boolean
        confirming or denying the authenticity
        of the Packet()'s data.
        If key is specified it overrides the default one.
        It is advisable to use different keys for encryption and signing.

        If remember is 1 (default) then Packet() will remember that it has been
        already verified (if verification passed). If trying to verify() it again an error will be raised.
        Also, Packet() that remembers that it was successfully verified
        will not propagate its signature when using the pack() method or
        doing the Pack(Pack()) call but use only its data instead.
        This behaviour is desirable in most cases.
        If for some reason you want to forget it was verified later on,
        you can use the forget() method.

        If you set throw to 1 (0 default), then verify() will return
        the Packet()'s reference instead of the boolean and
        raise an error if the verification fails.
        """
        if not self.signed:
            raise ValueError, "Packet() not specified as signed."
        if self.verified:
            raise TypeError, "Packet() already successfully verified!"
        key = key.key if key else self.key.key
        buf = str(self)+self.signature
        r = AuthenticatePacket(buf, len(buf), key)
        self.verified = r
        if throw:
            if r: return self
            raise Exception, "Verification failed!"
        return bool(r)

    def forget (self):
        """
        Forgets that the packet has already been verified.
        To learn more, see the __doc__ string for method verify().
        forget() method returns a reference to this Packet() so that
        it can be used in chained calls if needed.
        """
        self.verified = 0
        return self

    def pack (self, key=None, encrypted=0, signed=0, password=None, salt=None):
        """
        Enables you to chain this Packet() directly to another one.
        Complete data from this Packet() will be transfered to a new one.
        The returned Packet() will be considered as unencrypted
        and will be considered as unsigned unless you force the change
        by using the corresponding arguments.
        If key is None this Packet()'s key will be passed on.
        If it is not or password or salt are given, they will be used
        as in Packet()'s __init__() method.

        If you set signed to 1 and this Packet() has already been verified then its signature will not propagate as it is.
        Last four bytes of the data will be used instead.

        Example usage for double encryption:
        k1 = Key()
        k2 = Key()
        k3 = Key()
        k4 = Key()
        p = Packet("blah", k1)
        # Sign the plain textwith k1, encrypt it and the signature with k2, then encrypt them once more
        # with k3, and sign all together as encrypted with k4.
        p = p.sign().encrypt(k2).pack(k3).encrypt().sign(k4)
        # And to get it back:
        q = Packet(p, k4, encrypted=1, signed=1)
        if q.verify():
            q = q.decrypt(k3).pack(k2, encrypted=1, signed=1).decrypt()
            if q.verify(k1):
                print "Decrypted packet verified with k1!"
                print "It says:", q
            else:
                print "Decrypted packet corrupt or not authentic!"
        else:
            print "Packet corrupt or not authentic!"
        # Or like this:
        q = Packet(p, k4, encrypted=1, signed=1)
        try:
            q = q.verify(throw=1).decrypt(k3).pack(k2, encrypted=1, signed=1).decrypt().verify(k1, throw=1)
            print "Decrypted packet verified with k1!"
            print "It says:", q
        except Exception, e:
            print e
        """
        key    = key if key else self.key
        signed    = signed    if signed!=None    else self.signed
        encrypted = encrypted if encrypted!=None else self.encrypted
        signature = self.signature if not self.verified else ""
        return Packet(str(self)+signature, key, encrypted, signed, password, salt)

    def copy (self, copykey=0):
        """
        Returns a new exact copy of this Packet().

        If copykey is 1 then the Key() object is also copied a new.
        If it is not, (0 default) then the reference of the Key() is passed onto the copy
        and if you make changes on a Key()
        in old Packet(), they will be reflected in the copy as well.
        """
        p = Packet(str(self), (self.key.copy() if copykey else self.key))
        p.signed = self.signed
        p.signature = self.signature
        p.verified = self.verified
        p.encrypted = self.encrypted
        return p

    def setkey (self, key=None, password=None, salt=None):
        """
        Sets the key. Key must be the Key() object.
        If it is None then password and salt will be used to construct it as in
        key = Key(password, salt)
        Returns this Packet() object for chaining when wanting to generate new key on the fly as in:
        signkey = Key()
        p = Packet("blah", signkey).sign().setkey().encrypt()
        encryptionkey = p.getkey()
        """
        self.key = key if key else Key(password, salt)

    def getkey (self):
        """
        Returns a reference to the currently used Key() object.
        """
        return self.key

    issigned    = lambda self: self.signed
    isverified  = lambda self: self.verified
    isencrypted = lambda self: self.encrypted
