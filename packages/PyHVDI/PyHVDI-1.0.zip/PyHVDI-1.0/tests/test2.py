from hvdi import hvdi
import wave, sunau, aifc
import os, sys

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

inpath = sys.argv[1] if len(sys.argv)>1 else "16bit.wav"
try:
    infile = aopen(inpath)
except Exception, e:
    print "Could not open input file"
    print e
    sys.exit(1)

codec = sys.argv[2].lower() if len(sys.argv)>2 else "GSM"
try:
    hvdi_codec = hvdi.codec(codec)
except KeyError:
    print "Wrong codec name!\nSupported codecs:\n"
    print "\n".join(sorted(hvdi.list_codecs()))
    sys.exit(1)

outpath = os.path.join(os.path.dirname(inpath), codec.upper()+"-"+os.path.basename(inpath))
try:
    outfile = aopen(outpath, "w")
except Exception, e:
    print "Could not open output file '%s'" % outpath
    print e
    sys.exit(1)

print "Transcoding '%s' to '%s' ..." % (inpath, outpath)
hvdi.Decode(hvdi.IterEncode(infile, codec), False, outfile)
print "Done!"

infile.close()
outfile.close()

raw_input()