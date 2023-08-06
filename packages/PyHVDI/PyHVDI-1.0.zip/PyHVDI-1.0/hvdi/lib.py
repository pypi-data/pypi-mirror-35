from tweaks import *
from structures import *

import help_support
del help_support

# To construct the __all__ list for
# "from lib import *" importing form

s = set(dir())
s.add("s")

libpath = os.path.dirname(os.path.abspath(__file__))
if sys.platform.startswith("win"):
    # Py2Exe support:
    if os.path.isfile(libpath):
        libpath = os.path.dirname(libpath)
    libpath = os.path.join(libpath, "_hvdi.dll")
    _lib = ctypes.windll.LoadLibrary(libpath)
elif sys.platform.startswith("cygwin"):
    libpath = os.path.join(libpath, "_cyghvdi.dll")
    _lib = ctypes.cdll.LoadLibrary(libpath)
elif sys.platform.startswith("linux"):
    import platform
    if "arm" in platform.machine():
        libpath = os.path.join(libpath, "_rpihvdi.so")
    else:
        libpath = os.path.join(libpath, "_hvdi.so")
    _lib = ctypes.cdll.LoadLibrary(libpath)
    del platform
else:
    raise OSError, "Platform not supported!"

# hcrypt.h:
hcrypt_funcs = [] # List of functions belonging to hcrypt.h
h = set(dir())
h.add("h")

NewSalt = _lib.hcryptNewSalt
NewSalt.argtypes = []
NewSalt.restype  = POINTER(hcrypt_salt)
NewSalt.__doc__  = """
hcrypt_salt* NewSalt(void)
  Creates a salt value (or salt for short) that can be used with NewKey()
  to create hacker resistant keys. The hcrypt_salt is an array of 16 unsigned
  bytes (128 bits). The creator of the salt must send it to the other clients
  so that they may use it along with the password to create the key.
"""

DeleteKey = _lib.hcryptDeleteKey
DeleteKey.argtypes = [POINTER(hcrypt_key)]
DeleteKey.argnames = ["key"]
DeleteKey.restype  = None
DeleteKey.__doc__  = """
void DeleteKey(hcrypt_key *key)
  Deletes the key.
"""

NewKey = _lib.hcryptNewKey
NewKey.argtypes = [String, POINTER(hcrypt_salt)]
NewKey.argnames = ["password", "salt"]
NewKey.restype  = POINTER(hcrypt_key)
NewKey.__doc__  = """
hcrypt_key* NewKey(const char *password, const hcrypt_salt* salt)
  Creates an encryption key from a password and an optional salt. Both the
  sender and receiver must use the same password and optional salt to create
  the key. The salt is created by hcryptNewSalt and sent to each
  client. If salt is None then only the password will be used to create the key,
  and it will be easier for a hacker to use a dictionary attack.
"""

DeleteSalt = _lib.hcryptDeleteSalt
DeleteSalt.argtypes = [POINTER(hcrypt_salt)]
DeleteSalt.argnames = ["salt"]
DeleteSalt.restype  = None
DeleteSalt.__doc__  = """
void DeleteSalt(hcrypt_salt *salt)
  Deletes the salt.
"""

EncryptPacket = _lib.hcryptEncryptPacket
EncryptPacket.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(hcrypt_key)]
EncryptPacket.argnames = ["_in", "out", "buflen", "key"]
EncryptPacket.restype  = None
EncryptPacket.__doc__  = """
void EncryptPacket(unsigned char *in, unsigned char *out, int buflen,
                         hcrypt_key *key)
  Encrypts a packet from in to out. buflen is the number of bytes to encrypt.
  in and out may be the same buffer.
"""

EncryptStream = _lib.hcryptEncryptStream
EncryptStream.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(hcrypt_key)]
EncryptStream.argnames = ["_in", "out", "buflen", "key"]
EncryptStream.restype  = None
EncryptStream.__doc__  = """
void EncryptStream(unsigned char *in, unsigned char *out, int buflen,
                         hcrypt_key *key)
  Encrypts a byte stream from in to out. buflen is the number of bytes to encrypt.
  This should only be used for files, TCP streams, or other reliable streams.
  in and out may be the same buffer.
"""

DecryptPacket = _lib.hcryptDecryptPacket
DecryptPacket.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(hcrypt_key)]
DecryptPacket.argnames = ["_in", "out", "buflen", "key"]
DecryptPacket.restype  = None
DecryptPacket.__doc__  = """
void DecryptPacket(unsigned char *in, unsigned char *out, int buflen,
                         hcrypt_key *key)
  Decrypts a packet from in to out. buflen is the number of bytes to decrypt.
  in and out may be the same buffer.
"""

DecryptStream = _lib.hcryptDecryptStream
DecryptStream.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(hcrypt_key)]
DecryptStream.argnames = ["_in", "out", "buflen", "key"]
DecryptStream.restype  = None
DecryptStream.__doc__  = """
void DecryptStream(unsigned char *in, unsigned char *out, int buflen,
                         hcrypt_key *key)
  Decrypts a byte stream from in to out. buflen is the number of bytes to decrypt.
  This should only be used for files, TCP streams, or other reliable streams. 
  in and out may be the same buffer.
"""

SignPacket = _lib.hcryptSignPacket
SignPacket.argtypes = [POINTER(c_ubyte), c_int, POINTER(hcrypt_key)]
SignPacket.argnames = ["_in", "buflen", "key"]
SignPacket.restype  = None
SignPacket.__doc__  = """
void SignPacket(unsigned char *in, int buflen, hcrypt_key *key)
  Using key, appends a 4 byte MD5 hash to the end of in. You MUST make sure
  that it is long enough to store 4 more bytes, and make sure you add 4 bytes
  to buflen after the call!
"""

AuthenticatePacket = _lib.hcryptAuthenticatePacket
AuthenticatePacket.argtypes = [POINTER(c_ubyte), c_int, POINTER(hcrypt_key)]
AuthenticatePacket.argnames = ["_in", "buflen", "key"]
AuthenticatePacket.restype  = c_int
AuthenticatePacket.__doc__  = """
int AuthenticatePacket(unsigned char *in, int buflen, hcrypt_key *key)
  Using key, compares the MD5 hash with the last 4 bytes of in. If they match it
  returns 1, otherwise it returns 0. Make sure you either discard or do not use
  the last 4 bytes of the packet since they were added by SignPacket.
"""

# Add hcrypt.h functions to its list
hcrypt_funcs.extend(set(dir()).difference(h))

# hvdi.h:
hvdi_funcs = [] # A list of functions belonging to hvdi.h
h = set(dir())
h.add("h")

NewEncState = _lib.hvdiNewEncState
NewEncState.argtypes = []
NewEncState.restype  = POINTER(hvdi_enc_state)
NewEncState.__doc__  = """
hvdi_enc_state* NewEncState(void)
  Creates an encoder state. You must create one encoder state to encode your
  out going voice stream. For each encoder state you MUST set the codec with
  EncStateSetCodec().
"""

NewDecState = _lib.hvdiNewDecState
NewDecState.argtypes = []
NewDecState.restype  = POINTER(hvdi_dec_state)
NewDecState.__doc__  = """
hvdi_dec_state* NewDecState(void)
  Creates a decoder state. You must create a decoder state for each incoming
  voice stream.
"""

DeleteEncState = _lib.hvdiDeleteEncState
DeleteEncState.argtypes = [POINTER(hvdi_enc_state)]
DeleteEncState.argnames = ["state"]
DeleteEncState.restype  = None
DeleteEncState.__doc__  = """
void DeleteEncState(hvdi_enc_state *state)
  Frees an encoder state.
"""

DeleteDecState = _lib.hvdiDeleteDecState
DeleteDecState.argtypes = [POINTER(hvdi_dec_state)]
DeleteDecState.argnames = ["state"]
DeleteDecState.restype  = None
DeleteDecState.__doc__  = """
void DeleteDecState(hvdi_dec_state *state)
  Frees a decoder state.
"""

EncStateSetCodec = _lib.hvdiEncStateSetCodec
EncStateSetCodec.argtypes = [POINTER(hvdi_enc_state), c_ubyte]
EncStateSetCodec.argnames = ["state", "codec"]
EncStateSetCodec.restype  = c_int
EncStateSetCodec.__doc__  = """
int EncStateSetCodec(hvdi_enc_state *state, unsigned char codec)
  Sets the codec for the encoder state. You must call this before you attempt
  to encode a voice packet. You can call this at ANY time to change your
  encoder codec. It returns either the buffer frame size the codec requires,
  or NL_INVALID if an error occurred. The buffer can be a multiple of the
  frame size and a frame size of '0' means any EVEN buffer size can be used.
  For example, the GSM codec will return a frame size of 160, so a buffer of
  800 samples would be valid and encode 1/10 of a second of sound.
"""

DecStateGetCodec = _lib.hvdiDecStateGetCodec
DecStateGetCodec.argtypes = [POINTER(hvdi_dec_state)]
DecStateGetCodec.argnames = ["state"]
DecStateGetCodec.restype  = c_ubyte
DecStateGetCodec.__doc__  = """
unsigned char DecStateGetCodec(hvdi_dec_state *state)
  Get the codec that is being used for decoding.
"""

PacketIsVoice = _lib.hvdiPacketIsVoice
PacketIsVoice.argtypes = [POINTER(c_ubyte), c_int]
PacketIsVoice.argnames = ["packet", "length"]
PacketIsVoice.restype  = c_int
PacketIsVoice.__doc__  = """
int PacketIsVoice(unsigned char *packet, int length)
  Checks for a valid voice packet. Returns NL_TRUE is packet is valid, otherwise
  returns NL_FALSE.
"""

PacketDecode = _lib.hvdiPacketDecode
PacketDecode.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_short), c_int, POINTER(hcrypt_key), POINTER(hvdi_dec_state)]
PacketDecode.argnames = ["packet", "packlen", "buffer", "buflen", "key", "state"]
PacketDecode.restype  = c_int
PacketDecode.__doc__  = """
int PacketDecode(unsigned char *packet, int paclen, short *buffer,
                       int buflen, hcrypt_key *key, hvdi_dec_state *state)
  Decrypts and decodes a voice packet into buffer. It returns the number of
  samples in buffer, or NL_FALSE if an error occured. buflen is the number of
  decoded short voice samples that can be written to buffer, it is NOT the
  length in bytes. Note that it will drop UDP packets that are out of order.
  If key is not None, it will be used to decrypt and validate the packet.
"""

PacketEncode = _lib.hvdiPacketEncode
PacketEncode.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_short), c_int, POINTER(hcrypt_key), POINTER(hvdi_enc_state)]
PacketEncode.argnames = ["packet", "packlen", "buffer", "buflen", "key", "state"]
PacketEncode.restype  = c_int
PacketEncode.__doc__  = """
int hvdiPacketEncode(unsigned char *packet, int paclen, short *buffer,
                       int buflen, hcrypt_key *key, hvdi_enc_state *state)
  Encodes and encrypts buffer into a voice packet. Buflen is the number of
  voice samples in buffer. It returns the size of the encoded packet in bytes.
  If key is not None, it will be used to encrypt and validate the packet.
"""

NewVOX = _lib.hvdiNewVOX
NewVOX.argtypes = [c_int, c_int]
NewVOX.argnames = ["voxspeed", "noisethreshold"]
NewVOX.restype  = POINTER(hvdi_vox)
NewVOX.__doc__  = """
hvdi_vox* NewVOX(int voxspeed, int noisethreshold)
  Create a new hvdi_vox object. voxspeed is the number of samples of silence
  before hvdiVOX returns 0(false), and noisethreshold is an int between
  0(always pass) to 1000(never pass). 300 is a good starting point.
"""

VOX = _lib.hvdiVOX
VOX.argtypes = [POINTER(hvdi_vox), POINTER(c_short), c_int]
VOX.argnames = ["vox", "buffer", "buflen"]
VOX.restype = c_int
VOX.__doc__ = """
int VOX(hvdi_vox *vox, short *buffer, int buflen)
  Process a voice buffer with VOX, or voice activated transmission. It
  returns 1 if the buffer should be sent, or 0 if it is silent (or at least
  unvoiced).
"""

DeleteVOX = _lib.hvdiDeleteVOX
DeleteVOX.argtypes = [POINTER(hvdi_vox)]
DeleteVOX.argnames = ["vox"]
DeleteVOX.restype  = None
DeleteVOX.__doc__  = """
void DeleteVOX(hvdi_vox *vox)
  Delete the hvdi_vox object.
"""

# Some functions from rate.c, but they are included in hvdi.c, so let them be here.
NewRate = _lib.hvdiNewRate
NewRate.argtypes = [c_int, c_int]
NewRate.argnames = ["inrate", "outrate"]
NewRate.restype  = POINTER(hvdi_rate)
NewRate.__doc__  = """
hvdi_rate* NewRate(int inrate, int outrate)
  Create a hvdi_rate object for the sample rates supplied. Sample rates
  are in samples per second.
"""

RateFlow = _lib.hvdiRateFlow
RateFlow.argtypes = [POINTER(hvdi_rate), POINTER(c_short), POINTER(c_short), POINTER(c_int), POINTER(c_int)]
RateFlow.argnames = ["rate", "inbuf", "outbuf", "inlen", "outlen"]
RateFlow.restype  = None
RateFlow.__doc__  = """
void RateFlow(hvdi_rate *rate, short *inbuf, short *outbuf, int *inlen,
					int *outlen)
  Resamples inbuf to outbuf. inlen and outlen are updated with the actual
  number of samples processed. Note that inlen may return less than the
  length of inbuf, so you may need to save several samples to add to the
  beginning of the next buffer.
"""

DeleteRate = _lib.hvdiDeleteRate
DeleteRate.argtypes = [POINTER(hvdi_rate)]
DeleteRate.argnames = ["rate"]
DeleteRate.restype  = None
DeleteRate.__doc__  = """
void DeleteRate(hvdi_rate *rate)
  Delete the hvdi_rate object.
"""

NewAGC = _lib.hvdiNewAGC
NewAGC.argtypes = [c_float]
NewAGC.argnames = ["level"]
NewAGC.restype  = POINTER(hvdi_agc)
NewAGC.__doc__  = """
hvdi_agc* NewAGC(float level)
  Create a new hvdi_agc object. level is the percent of max volume for the
  sound buffer. The valid range is 0.5f to 1.0f, but the recomended
  range is 0.8f to 0.95f. At 1.0f, some clipping might be experienced.
"""

AGC = _lib.hvdiAGC
AGC.argtypes = [POINTER(hvdi_agc), POINTER(c_short), c_int]
AGC.argnames = ["agc", "buffer", "len"]
AGC.restype  = None
AGC.__doc__  = """
void AGC(hvdi_agc *agc, short *buffer, int len)
  Performs the AGC function on buffer. AGC is adjusted 10 times per second.
"""

DeleteAGC = _lib.hvdiDeleteAGC
DeleteAGC.argtypes = [POINTER(hvdi_agc)]
DeleteAGC.argnames = ["agc"]
DeleteAGC.restype  = None
DeleteAGC.__doc__  = """
void DeleteAGC(hvdi_agc *agc)
  Delete the hvdi_agc object.
"""

Mix = _lib.hvdiMix
Mix.argtypes = [POINTER(c_short), POINTER(POINTER(c_short)), c_int, c_int]
Mix.argnames = ["outbuf", "inbuf", "number", "inlen"]
Mix.restype  = None
Mix.__doc__  = """
void Mix(short *outbuf, short **inbuf, int number, int inlen)
  Mixes two or more buffers into outbuf. inbuf is an array of pointers to
  the inbuf buffers, number is the number of inbuf buffers, and inlen is
  the number of samples in each inbuf buffer.
"""

Hint = _lib.hvdiHint
Hint.argtypes = [c_int, c_int]
Hint.argnames = ["name", "arg"]
Hint.restype  = None
Hint.__doc__  = """
void Hint(int name, int arg)
  The first three change the encoding performance/quality of some codecs.

             codec |      GSM LPT_CUT     CELP_CODEBOOK_LEN   CELP_FAST_GAIN
-----------------------------------------------------------------------------
  option           |
--------------------
NORMAL        |          No               256                 No

FAST          |         Yes               128                Yes

FASTEST       |         Yes                32                Yes



  CELP_CODEBOOK directly sets the CELP codebook length from 32 to 256.

  SEQUENCE enables/disables sequence numbers added to packets. To disable,
  arg = 0, to enable (default), arg != 0. The sequence adds 2 bytes to each packet.

  AUTO_VOX enables/disables automatic VOX processing inside PacketEncode().
  To disable (default), arg = 0, to enable, arg != 0. If COMFORT_NOISE is
  enabled then PacketEncode() will create silence packets when the VOX does not
  pass, otherwise PacketEncode() will return 0.

  VOX_LEVEL sets the VOX level when AUTO_VOX is enabled. Valid range is
  0 to 1000, and the default 300.

  VOX_SPEED sets the VOX speed when AUTO_VOX is enabled. Default VOX_FAST.

  COMFORT_NOISE enables/disables silence packets when AUTO_VOX is enabled
  when encoding, and enables/disables comfort noise when decoding.

  NOISE_LEVEL sets the comfort noise level when COMFORT_NOISE is enabled.
  Valid range 0 to 1000, default 100.
"""

hvdi_funcs.extend(set(dir()).difference(h))
del h

__all__ = list(set(dir()).difference(s))
del s