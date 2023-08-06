# HawkVoiceDI structures from hvdi.h, hcrypt.h and rate.c

from tweaks import *

# Construct the __all__ list for "from structures import *"
# importing mode
s = set(dir())
s.add("s") # Include the s to avoid it later

# Structures from hcrypt.h:
class BF_KEY (Structure):
    """
    A BlowFish key structure. Used privately in hcrypt_key structure.
    Not really relevant as part of the API as there is no need
    for a developer to access it or its attributes directly.
    """
    __slots__ = ['P', 'S']
    _fields_ = [
        ('P', c_ulong * (16 + 2)),
        ('S', c_ulong * (4 * 256))
        ]

class hcrypt_key (Structure):
    """
    A structure that holds a key for packet encryption/decryption.
    Use the hvdi.crypt.NewKey() function to get its properly initialized
    and usable instance, and hvdi.crypt.DeleteKey() to remove it from memory.
    There is no need for a developer to access any of its attributes directly,
    just to pass its instance as an argument to:
    hvdi.crypt.[EncryptPacket(), DecryptPacket(), SignPacket(), AuthenticatePacket()] and
    to some more functions of the same nature, and possibly to the higher level
    interface class hvdi.crypt.Key().
    """
    __slots__ = [
        'bf',
        'iv',
        'digest',
        'n'
        ]
    _fields_ = [
        ('bf', BF_KEY),
        ('iv', c_ubyte * 8),
        ('digest', c_ubyte * 16),
        ('n', c_int),
        ]

class hcrypt_salt (Structure):
    """
    A structure that holds a salt for packet encryption/decryption.
    It is used in the key creation by the
    hvdi.crypt.NewKey() function or possibly by the higher level
    interface class hvdi.crypt.Key().
    Use the hvdi.crypt.NewSalt() function to get its properly initialized
    and usable instance, and hvdi.crypt.DeleteSalt() to remove it from memory.
    As the salt is necessary on the receiving end of encrypted packets,
    along with the password, to recreate the decryption key,
    a developer can extract its 16-byte value from hcrypt_salt's
    single attribute data. Also, the structure may be manually initialized
    and filled on the receiving end to pass it to the
    hvdi.crypt.NewKey() function by setting the said data attribute.
    """
    __slots__ = ['data']
    _fields_ = [
        ('data', c_ubyte * 16) # 128 bit salt for encryption key generation
        ]

# Structures from hvdi.h:
class hvdi_vox (Structure):
    """
    A structure used to hold VOX information.
    Use hvdi.hvdi.NewVOX() function to get its properly initialized
    and usable instance, and hvdi.hvdi.DeleteVOX() to remove it from memory.
    It is used by the hvdi.hvdi.VOX() function and
    there is generally no need for a developer to access
    any of its attributes directly.
    """
    __slots__ = [
        'rate',
        'noisethreshold',
        'samplecount',
        ]
    _fields_ = [
        ('rate', c_int),
        ('noisethreshold', c_int),
        ('samplecount', c_int),
        ]

class hvdi_state (Structure):
    """
    A structure used privately in hvdi_enc_state and hvdi_dec_state structures
    to hold the state's properties. There is generally no need
    for a developer to access it or its attributes directly.
    """
    __slots__ = [
        'gsm_lpt',
        'celp_codebook',
        'celp_fast_gain',
        'sequence',
        'autoVOX',
        'VOXlevel',
        'VOXspeed',
        'comfortnoise',
        'noiselevel',
        ]
    _fields_ = [
        ('gsm_lpt', c_int),
        ('celp_codebook', c_int),
        ('celp_fast_gain', c_int),
        ('sequence', c_int),
        ('autoVOX', c_int),
        ('VOXlevel', c_int),
        ('VOXspeed', c_int),
        ('comfortnoise', c_int),
        ('noiselevel', c_int)
        ]

class hvdi_enc_state (Structure):
    """
    A structure representing the encoder state.
    Use hvdi.hvdi.NewEncState() function to get its properly initialized
    and usable instance, and hvdi.hvdi.DeleteEncState() to remove it from memory.
    It is used by the hvdi.hvdi.PacketEncode() function and changed
    via the hvdi.hvdi.EncStateSetCodec().
    There is generally no need for a developer to access its attributes directly.
    """
    __slots__ = [
        'codec',
        'sequence',
        'state',
        'vox'
        ]
    _fields_ = [
        ('codec', c_ubyte),
        ('sequence', c_ushort),
        ('state', POINTER(None)),
        ('vox', POINTER(hvdi_vox))
        ]

class hvdi_dec_state (Structure):
    """
    A structure representing the decoder state.
    Use hvdi.hvdi.NewDecState() function to get its properly initialized
    and usable instance, and hvdi.hvdi.DeleteDecState() to remove it from memory.
    It is used by the hvdi.hvdi.PacketDecode() function and its codec
    attribute can be checked via the hvdi.hvdi.DecStateGetCodec().
    There is generally no need for a developer to access its attributes directly.
    """
    __slots__ = [
        'codec',
        'sequence',
        'state'
        ]
    _fields_ = [
        ('codec', c_ubyte),
        ('sequence', c_ushort),
        ('state', POINTER(None))
        ]

class hvdi_agc (Structure):
    """
    A structure used to hold AGC information.
    Use hvdi.hvdi.NewAGC() function to get its properly initialized
    and usable instance, and hvdi.hvdi.DeleteAGC() to remove it from memory.
    It is used by the hvdi.hvdi.AGC() function and
    there is generally no need for a developer to access
    any of its attributes directly.
    """
    __slots__ = [
        'sample_max',
        'counter',
        'igain',
        'ipeak',
        'silence_counter'
        ]
    _fields_ = [
        ('sample_max', c_uint),
        ('counter', c_int),
        ('igain', c_long),
        ('ipeak', c_int),
        ('silence_counter', c_int),
        ]
# Structure from rate.c:
class hvdi_rate (Structure):
    """
    A structure used to hold rate information.
    Use hvdi.hvdi.NewRate() function to get its properly initialized
    and usable instance, and hvdi.hvdi.DeleteRate() to remove it from memory.
    It is used by the hvdi.hvdi.RateFlow() function and
    there is generally no need for a developer to access
    any of its attributes directly.
    """
    __slots__ = [
        'lcmrate',
        'inskip',
        'outskip',
        'total',
        'intot',
        'outtot',
        'lastsamp',
        ]
    _fields_ = [
        ('lcmrate', c_long),
        ('inskip', c_long),
        ('outskip', c_long),
        ('total', c_long),
        ('intot', c_long),
        ('outtot', c_long),
        ('lastsamp', c_long)
        ]

# Create __all__ list containing defined structures only:
__all__ = list(set(dir()).difference(s))
del s