# Translation of the packet test program for
# the HawkVoiceDI cross platform network library
# (test.c) by Phil Frisbie, Jr. from C into
# Python programming language.
# Copyright (C) test.py 2018 by Dalen Bernaca

from array import array
from hvdi.constants import *
import hvdi.hvdi as hvdi
import hvdi.crypt as hcrypt

import os, sys
import wave, aifc, sunau
import ctypes as C

# this is the LCM of 160, 180, 240, 320, 360, and 480 to simplify the code
NUM_SAMPLES = 2880

def aopen (path, mode="r", sw=2, nc=1, fr=8000):
    """
    Opens an audio file reader/writer depending on
    the given mode.
    The file format is chosen based on the file's extension in the path.
    """
    ext = os.path.splitext(path)[1].lower()
    if ext in (".wav", ".wave"):
        f = wave.open(path, mode)
    elif ext in (".aif", ".aifc", ".aiff"):
        f = aifc.open(path, mode)
    elif ext==".au":
        f = sunau.open(path, mode)
    else:
        raise ValueError, "Unrecognized format!"
    if mode=="w":
        f.setsampwidth(sw)
        f.setnchannels(nc)
        f.setframerate(fr)
    return f

# the salt would need to be passed from the other clients
salt = hcrypt.NewSalt()
key  = hcrypt.NewKey("HawkVoiceDi definitely rocks!!!", salt)

inpath = sys.argv[1] if len(sys.argv)>1 else "16bit.wav"
try:
    infile = aopen(inpath)
except Exception, e:
    print "Could not open input file"
    print e
    sys.exit(1)

# set the encoding preferences
hvdi.Hint(hvdi.NORMAL, 0)

# This block of code is not from original test.c
# It is added by Dalen to support more statistics
# And codec choosing
if len(sys.argv)>2:
    codec = sys.argv[2].lower()
    try:
        hvdi_codec = hvdi.codec(codec)
    except KeyError:
        print "Wrong codec name!\nSupported codecs:\n"
        print "\n".join(sorted(hvdi.list_codecs()))
        sys.exit(1)
    outpath = os.path.splitext(inpath)[0]+os.extsep+codec
    transfile = aopen(os.path.join(os.path.dirname(inpath), codec.upper()+"X"+os.extsep+"wav"), "w")
    outfile = open(outpath, "wb")
    enc = hvdi.NewEncState()
    dec = hvdi.NewDecState()
    hvdi.EncStateSetCodec(enc, hvdi_codec)

    agc = hvdi.NewAGC(0.6)
    vox = hvdi.NewVOX(hvdi.VOX_FAST, 300)

    # hints go here
    hvdi.Hint(hvdi.NORMAL, 0)
    hvdi.Hint(hvdi.SEQUENCE, 1)
    hvdi.Hint(hvdi.AUTO_VOX, 1)
    hvdi.Hint(hvdi.VOX_LEVEL, 300)
    #hvdi.Hint(hvdi.COMFORT_NOISE, 1)
    #hvdi.Hint(hvdi.NOISE_LEVEL, 10)

    # Statistics
    import time
    passed = 0
    nopass = 0
    infilesize = 0
    packetlens = []
    enctimes = []
    dectimes = []

    # Transcoding:
    chunk = infile.readframes(NUM_SAMPLES)
    while chunk:
        infilesize += len(chunk) # Statistics only

        chunk = array("h", chunk) # Get 16bit data
        samples = (C.c_short*len(chunk))(*chunk) # Declare and fill the C array
        buflen  = len(samples)

        decoded = (C.c_short*(NUM_SAMPLES*2))()
        packet = (C.c_ubyte*NL_MAX_PACKET_LENGTH)()
        paclen = NL_MAX_PACKET_LENGTH

        # exercise the AGC and VOX first
        hvdi.AGC(agc, samples, buflen)
        if hvdi.VOX(vox, samples, buflen):
            passed += 1
        else:
            nopass += 1

        t1 = time.time()
        enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, enc)
        t2 = time.time()
        outfile.write(array("B", packet[:enclen]).tostring())
        packetlens.append(enclen)
        #valid = hvdi.PacketIsVoice(packet, enclen)
        t3 = time.time()
        declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, dec)
        t4 = time.time()
        transfile.writeframes(array("h", decoded[:declen]).tostring())

        dectimes.append(t4-t3)
        enctimes.append(t2-t1)

        chunk = infile.readframes(NUM_SAMPLES)

    print "%d samples passed the VOX, and %d did not pass" % (passed, nopass)
    print "The "+codec.upper()+" compression ratio is %.3f" % ((outfile.tell()/float(infilesize)))
    print "Output file is %.4f KB smaller than the input file." % ((infilesize-outfile.tell())/1024.0)
    print "Average size of encoded packet is %i bytes," % (sum(packetlens)/len(packetlens))
    print "the smallest had %i bytes and the biggest %i bytes" % (min(packetlens), max(packetlens))
    print "using %i bytes long input chunk." % NUM_SAMPLES
    print "Average encoding time is %f sec" % (1.0*sum(enctimes)/len(enctimes))
    print "Average decoding time is %f sec" % (1.0*sum(dectimes)/len(dectimes))

    hvdi.DeleteAGC(agc)
    hvdi.DeleteVOX(vox)

    hvdi.DeleteEncState(enc)
    hvdi.DeleteDecState(dec)

    hcrypt.DeleteKey(key)
    hcrypt.DeleteSalt(salt)

    infile.close()
    outfile.close()
    transfile.close()
    sys.exit(0)

#---------------------------------------

# open the output files and create state objects
ulawfile = aopen("ulawx.wav", "w")
ulawenc = hvdi.NewEncState()
ulawdec = hvdi.NewDecState()
hvdi.EncStateSetCodec(ulawenc, ULAW_CODEC)

adpcmfile = aopen("adpcmx.wav", "w")
adpcmenc = hvdi.NewEncState()
adpcmdec = hvdi.NewDecState()
hvdi.EncStateSetCodec(adpcmenc, ADPCM_32_CODEC)

gsmfile = aopen("gsmx.wav", "w")
gsmenc = hvdi.NewEncState()
gsmdec = hvdi.NewDecState()
hvdi.EncStateSetCodec(gsmenc, GSM_CODEC)

lpcfile = aopen("lpcx.wav", "w")
lpcenc = hvdi.NewEncState()
lpcdec = hvdi.NewDecState()
hvdi.EncStateSetCodec(lpcenc, LPC_CODEC)

lpc10file = aopen("lpc10x.wav", "w")
lpc10enc = hvdi.NewEncState()
lpc10dec = hvdi.NewDecState()
hvdi.EncStateSetCodec(lpc10enc, LPC10_CODEC)

lpc14file = aopen("lpc14x.wav", "w")
lpc14enc = hvdi.NewEncState()
lpc14dec = hvdi.NewDecState()
hvdi.EncStateSetCodec(lpc14enc, LPC_1_4_CODEC)

lpc18file = aopen("lpc18x.wav", "w")
lpc18enc = hvdi.NewEncState()
lpc18dec = hvdi.NewDecState()
hvdi.EncStateSetCodec(lpc18enc, LPC_1_8_CODEC)

celp45file = aopen("celp45x.wav", "w")
celp45enc = hvdi.NewEncState()
celp45dec = hvdi.NewDecState()
hvdi.EncStateSetCodec(celp45enc, CELP_4_5_CODEC)

celp30file = aopen("celp30x.wav", "w")
celp30enc = hvdi.NewEncState()
celp30dec = hvdi.NewDecState()
hvdi.EncStateSetCodec(celp30enc, CELP_3_0_CODEC)

celp23file = aopen("celp23x.wav", "w")
celp23enc = hvdi.NewEncState()
celp23dec = hvdi.NewDecState()
hvdi.EncStateSetCodec(celp23enc, CELP_2_3_CODEC)

vbrlpc10file = aopen("vbrlpc10x.wav", "w")
vbrlpc10enc = hvdi.NewEncState()
vbrlpc10dec = hvdi.NewDecState()
hvdi.EncStateSetCodec(vbrlpc10enc, VBR_LPC10_CODEC)

agc = hvdi.NewAGC(0.6)
vox = hvdi.NewVOX(hvdi.VOX_FAST, 300)

# hints go here
hvdi.Hint(hvdi.NORMAL, 0)
hvdi.Hint(hvdi.SEQUENCE, 1)
#hvdi.Hint(hvdi.AUTO_VOX, 1)
#hvdi.Hint(hvdi.VOX_LEVEL, 300)
#hvdi.Hint(hvdi.COMFORT_NOISE, 1)
#hvdi.Hint(hvdi.NOISE_LEVEL, 10)

passed = 0
nopass = 0

chunk = infile.readframes(NUM_SAMPLES)
while chunk:
    chunk = array("h", chunk) # Get 16bit data
    samples = (C.c_short*len(chunk))(*chunk) # Declare and fill the C array
    buflen  = len(samples)

    decoded = (C.c_short*(NUM_SAMPLES*2))()
    packet = (C.c_ubyte*NL_MAX_PACKET_LENGTH)()
    paclen = NL_MAX_PACKET_LENGTH

    # exercise the AGC and VOX first
    hvdi.AGC(agc, samples, buflen)
    if hvdi.VOX(vox, samples, buflen):
        passed += 1
    else:
        nopass += 1

    # u-law
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, ulawenc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, ulawdec)
    ulawfile.writeframes(array("h", decoded[:declen]).tostring())

    # ADPCM *
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, adpcmenc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, adpcmdec)
    adpcmfile.writeframes(array("h", decoded[:declen]).tostring())

    # GSM
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, gsmenc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, gsmdec)
    gsmfile.writeframes(array("h", decoded[:declen]).tostring())

    # LPC
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, lpcenc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, lpcdec)
    lpcfile.writeframes(array("h", decoded[:declen]).tostring())

    # LPC-10
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, lpc10enc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, lpc10dec)
    lpc10file.writeframes(array("h", decoded[:declen]).tostring())

    # OpenLPC 1.4K
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, lpc14enc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, lpc14dec)
    lpc14file.writeframes(array("h", decoded[:declen]).tostring())

    # OpenLPC 1.8K
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, lpc18enc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, lpc18dec)
    lpc18file.writeframes(array("h", decoded[:declen]).tostring())

    # CELP 4.5K
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, celp45enc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, celp45dec)
    celp45file.writeframes(array("h", decoded[:declen]).tostring())

    # CELP 3.0K
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, celp30enc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, celp30dec)
    celp30file.writeframes(array("h", decoded[:declen]).tostring())

    # CELP 2.3K
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, celp23enc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, celp23dec)
    celp23file.writeframes(array("h", decoded[:declen]).tostring())

    # VBR-LPC-10
    enclen = hvdi.PacketEncode(packet, buflen, samples, paclen, key, vbrlpc10enc)
    valid = hvdi.PacketIsVoice(packet, enclen)
    declen = hvdi.PacketDecode(packet, enclen, decoded, NUM_SAMPLES * 2, key, vbrlpc10dec)
    vbrlpc10file.writeframes(array("h", decoded[:declen]).tostring())

    # read next chunk of audio
    chunk = infile.readframes(NUM_SAMPLES)

print "%d samples passed the VOX, and %d did not pass" % (passed, nopass)

hvdi.DeleteEncState(ulawenc)
hvdi.DeleteDecState(ulawdec)
hvdi.DeleteEncState(adpcmenc)
hvdi.DeleteDecState(adpcmdec)
hvdi.DeleteEncState(gsmenc)
hvdi.DeleteDecState(gsmdec)
hvdi.DeleteEncState(lpcenc)
hvdi.DeleteDecState(lpcdec)
hvdi.DeleteEncState(lpc10enc)
hvdi.DeleteDecState(lpc10dec)
hvdi.DeleteEncState(lpc14enc)
hvdi.DeleteDecState(lpc14dec)
hvdi.DeleteEncState(lpc18enc)
hvdi.DeleteDecState(lpc18dec)
hvdi.DeleteEncState(celp45enc)
hvdi.DeleteDecState(celp45dec)
hvdi.DeleteEncState(celp30enc)
hvdi.DeleteDecState(celp30dec)
hvdi.DeleteEncState(celp23enc)
hvdi.DeleteDecState(celp23dec)
hvdi.DeleteEncState(vbrlpc10enc)
hvdi.DeleteDecState(vbrlpc10dec)

hcrypt.DeleteKey(key)
hcrypt.DeleteSalt(salt)
hvdi.DeleteAGC(agc)
hvdi.DeleteVOX(vox)

lpc10file.close()
lpc14file.close()
lpc18file.close()
lpcfile.close()
gsmfile.close()
adpcmfile.close()
ulawfile.close()
celp45file.close()
celp30file.close()
celp23file.close()
vbrlpc10file.close()
infile.close()
raw_input()