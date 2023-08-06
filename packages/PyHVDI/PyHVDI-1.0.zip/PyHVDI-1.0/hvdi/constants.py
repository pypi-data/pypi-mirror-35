# HawkVoiceDI constants from hvdi.h and hcrypt.h

NL_INVALID = -1
NL_FALSE   = 0
NL_TRUE    = 1
NL_MAX_PACKET_LENGTH = 16384

CODECS = {}
s = set(dir())
s.add("s") # Include s in the dir() variable list set

HV_2_4K_CODEC = 1
HV_4_8K_CODEC = 2
HV_13_2K_CODEC = 3
HV_32K_CODEC = 4
HV_64K_CODEC = 5
HV_1_4K_CODEC = 6
HV_1_8K_CODEC = 7
HV_4_5K_CODEC = 8
HV_3_0K_CODEC = 9
HV_2_3K_CODEC = 10
HV_VBR_2_4K_CODEC = 11
HV_SILENCE_CODEC = 31

LPC10_CODEC = HV_2_4K_CODEC
LPC_CODEC = HV_4_8K_CODEC
GSM_CODEC = HV_13_2K_CODEC
ADPCM_32_CODEC = HV_32K_CODEC
PCM_64_CODEC = HV_64K_CODEC
G_711_CODEC = HV_64K_CODEC
ULAW_CODEC = HV_64K_CODEC
LPC_1_4_CODEC = HV_1_4K_CODEC
LPC_1_8_CODEC = HV_1_8K_CODEC
CELP_4_5_CODEC = HV_4_5K_CODEC
CELP_3_0_CODEC = HV_3_0K_CODEC
CELP_2_3_CODEC = HV_2_3K_CODEC
VBR_LPC10_CODEC = HV_VBR_2_4K_CODEC

# Add all codecs to a dictionary CODECS:
for codec in set(dir()).difference(s):
    value = globals()[codec]
    CODECS[codec] = value
    CODECS[codec[:-6]] = value
    if codec.startswith("HV_"):
        CODECS[codec[3:]] = value
        CODECS[codec[3:-6]] = value

del value, s

def codec (c):
    """
    Simplifies usage of the codec constants.
    c may be a constant number of the codec or the codec's name as returned by list_codecs() function
    or any of longer versions from CODECS dictionary.
    The function is case insensitive.
    The returned value is the constant and the existance
    of the codec is always checked.
    Raises the KeyError() if the codec does not exist.
    """
    if isinstance(c, (int, long)):
        if c in CODECS.values():
            return int(c)
    elif isinstance(c, basestring):
        return CODECS["_".join(c.upper().replace("-", " ").replace("_", " ").split())]
    raise KeyError, "No such codec!"

list_codecs = lambda: [codec for codec in CODECS
                       if (not codec.startswith("HV_") and not codec.endswith("_CODEC"))]
list_codecs.__doc__ = "Lists all possible shortened codec names."

VOX_FAST = 4000
VOX_MEDIUM = 8000
VOX_SLOW = 12000

NORMAL = 1
FAST = 2
FASTEST = 3
CELP_CODEBOOK = 4
SEQUENCE = 5
AUTO_VOX = 6
VOX_LEVEL = 7
VOX_SPEED = 8
COMFORT_NOISE = 9
NOISE_LEVEL = 10
