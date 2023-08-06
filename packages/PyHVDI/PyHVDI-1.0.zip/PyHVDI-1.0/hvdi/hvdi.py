"""
HawkVoiceDI API Python bindings by Dalen Bernaca

hvdi.c  Version: 0.91 beta
hvdi.py Version: 1.0  beta

* For encryption functions and classes see:
  >>> import hvdi.crypt as hcrypt
  >>> help(hcrypt)
  >>>

* Higher level encoding and decoding classes are added by Dalen
  to simplify use of the encryption/decryption and
  provide more Pythonic interface.

General notes for low-level part by Phil Frisbie:

This is a no nonsense API that wraps all codec and encryption details for
the developer.

There is a lot of error detection, but I have not decided how to report the
errors yet. I will either define multiple return codes, or add a 'getError'
type function.

Note that ALL codecs except ADPCM and U-Law require 8 KHz sample rate, and ALL require
16 bit (short) samples.

Be careful of encoding voice buffer sizes. If you ignore the frame size from
EncStateSetCodec(), your buffer may be truncated, and you will have breaks of
silence between your voice packets.

I recommend the following codecs: On a LAN, use u-law or ADPCM for best quality
(they even do very well with music and multiple voices). On the open 'net, use
GSM if you have the extra 13.2 K of bandwidth, CELP, or LPC-10. Use LPC only if you
don't have enough bandwidth for GSM, and you don't have the CPU cycles for
CELP or LPC-10. The quality of LPC is MUCH worse than CELP or LPC-10.

For Windows CE and other platforms that do not have hardware floating point
instructions you should only use the u-law, ADPCM, or GSM codecs. The other codecs
will not run in real-time even on a 400 MHz StongArm PocketPC.
"""

from constants import *
import lib
import structures

for struct in structures.__all__:
    if not struct.startswith("hvdi_"): continue
    globals()[struct] = getattr(structures, struct)
del struct

for func in lib.hvdi_funcs:
    globals()[func] = getattr(lib, func)
del func

class Encoder:
    """
    High level encoder class.
    """
    from ctypes import c_short, c_ubyte
    from array  import array
    from crypt  import Key
    _codec = staticmethod(codec)
    def __init__ (self, codec="GSM", key=None, password=None, salt=None):
        """
        codec --> Default codec of the encoder
        key   --> hvdi.crypt.Key() object to use as default key in encryption
                  If None, password and salt are used to construct the key.
                  If 0 or False, the encryption will not be used at all.
        """
        self.codec = self._codec(codec)
        self.state = NewEncState()
        self.framesize = EncStateSetCodec(self.state, self.codec)
        self.framesize = 160 if self.framesize==0 else self.framesize
        if   key==None:
            self.key = self.Key(password, salt)
        elif not key:
            class fake:
                key = None
            self.key = fake()
        elif isinstance(key, self.Key):
            self.key = key
        else:
            raise TypeError, "key must be hvdi.crypt.Key(), None, 0 or False, %s given." % str(type(key))
        self.agc = None
        self.vox = None

    def __del__ (self):
        try:
            DeleteEncState(self.state)
            del self.state
        except: pass
        try:
            DeleteAGC(self.agc)
            del self.agc
        except: pass
        try:
            DeleteVOX(self.vox)
            del self.vox
        except: pass
        try: del self.key
        except: pass

    def encode (self, data):
        """
        Encodes the data into a packet.
        The data must be at least Encoder().framesize samples long.
        Otherwise, the result is unpredictable.
        The samples must be 16bit, 8000 Hz, mono linear PCM encoded audio bytes in a string or an iterable
        containing the signed short integers (Python ints from -2**15 to 2**15).
        Returns a string containing the packet.
        """
        if not data: return ""
        data   = self.array("h", data)
        buflen = len(data)
        data   = (self.c_short*buflen)(*data)
        if self.agc:
            AGC(self.agc, data, buflen)
        packet = (self.c_ubyte*NL_MAX_PACKET_LENGTH)()
        paclen = NL_MAX_PACKET_LENGTH
        enclen = PacketEncode(packet, buflen, data, paclen, self.key.key, self.state)
        return self.array("B", packet[:enclen]).tostring()

    def iterenc (self, bufs):
        """
        Encodes an iterable of audio chunks.
        Each chunk must be at least Encoder().framesize samples long.
        Otherwise, the results are unpredictable.
        Returns a generator object that has to be iterated over.
        """
        for buf in bufs:
            yield self.encode(buf)

    def setcodec (self, codec="GSM"):
        """
        Sets a currently used codec.
        """
        self.codec     = self._codec(codec)
        self.framesize = EncStateSetCodec(self.state, self.codec)
        self.framesize = 160 if self.framesize==0 else self.framesize

    def setagc (self, value=0.6):
        """
        Sets an auto gain control.
        value --> A float between 0.5 and 1.0.
                  Recommended values range from 0.8 to 0.95.
                  At 1.0 some clipping might be experienced.
        If value is 0, AGC will be turned off as on Encoder()'s initialization.
        If AGC is set, it will be performed on the input data before each encoding.
        """
        if self.agc:
            DeleteAGC(self.agc)
        if not value:
            self.agc = None
            return
        self.agc = NewAGC(value)

    def setvox (self, speed=VOX_FAST, noisethreshold=300, autovox=None, comfortnoise=None):
        """
        Sets the VOX to be used with isvoiced() method.
        Also, turns automatic VOX on or off and sets the comfort noise.
        If you want different values for autovox and manual VOX for isvoiced(),
        then you set the autovox first, and then call setvox() again with autovox=None and comfortnoise=None (defaults).
        speed          --> The VOX and/or autovox speed.
                           It is number of samples of silence before isvoiced() returns True.
                           Or autovox ignores the encoding or generates a silent packet (depends on comfortnoise being set).
                           There are 3 preset constants to help you:
                           VOX_FAST   = 4000 (default),
                           VOX_MEDIUM = 8000 and
                           VOX_SLOW   = 12000.
        noisethreshold --> An integer between 0 and 1000. 
                           0 - always pass, 1000 never pass. 300 is a good starting point (default).
        autovox        --> Turns automatic VOX upon encoding on or off.
                           If None (default) setting it is ignored, if a boolean the switching action is taken.
                           1/True - On, 0/False - off.
        comfortnoise   --> Turns silent packets upon encoding on or off.
                           If None (default), setting it is ignored, if an integer, it is a comfort noise level.
                           If 0/False, the silent packets are turned off.
                           If autovox is set, and comfort noise is off, the encode() method
                           will return an empty string when automatic VOX is triggered with a silence.
                           If autovox is on, and comfort noise set, an empty packet will be generated.
        """
        if noisethreshold<0 or noisethreshold>1000:
            raise ValueError, "Noise threshold out of range >= 0 and <= 1000"
        if self.vox:
            DeleteVOX(self.vox)
        self.vox = NewVOX(speed, noisethreshold)
        if autovox!=None:
            Hint(AUTO_VOX,      bool(autovox))
        if comfortnoise!=None:
            Hint(COMFORT_NOISE, bool(comfortnoise))
        if not autovox: return
        Hint(VOX_SPEED, speed)
        Hint(VOX_LEVEL, noisethreshold)
        if comfortnoise:
            Hint(NOISE_LEVEL, comfortnoise)

    def setsequence (self, onoff=1):
        """
        Turns packet sequencing on or off.
        1 for on, 0 for off (1 default).
        If it is on, each packet returned by the encode() method will have its ordinal number attached.
        If a packet that came out of order is encountered while decoding, it will be ignored.
        """
        Hint(SEQUENCE, onoff)

    def isvoiced (self, buffer):
        """
        Checks whether audio data in buffer is voiced or not.
        Uses the default VOX set by the setvox() method.
        If VOX is not set, it will be set with defaults of the setvox() method.
        Returns True if the buffer contains voiced audio, False otherwise.
        If True, the segment should be encoded and sent, and it should be ignored if isvoiced() is False.
        Note that voice activated transmission, when autovox is enabled uses the hvdi.hvdi.VOX()
        function, as does the isvoiced() method, which returns 0 when audio shouldn't be sent and 1 if it should.
        Do not accidentally mix up the results of two different outputs if you ever use both low-level
        function VOX() and the isvoiced() method as they are complementary.
        """
        if not self.vox: self.setvox()
        buffer = self.array("h", buffer)
        buflen = len(buffer)
        buffer = (self.c_short*buflen)(*buffer)
        return VOX(self.vox, buffer, buflen)==0

class Decoder:
    """
    High level decoder class.
    """
    from ctypes import c_short, c_ubyte
    from array  import array
    from crypt  import Key
    _codec = staticmethod(codec)
    def __init__ (self, key=None, password=None, salt=None):
        """
        key --> hvdi.crypt.Key() object to use as default key in packet decryption
                If None, password and salt are used to construct the key.
                If 0 or False, the decryption will not be used at all.
        """
        self.state = NewDecState()
        if   key==None:
            self.key = self.Key(password, salt)
        elif not key:
            class fake:
                key = None
            self.key = fake()
        elif isinstance(key, self.Key):
            self.key = key
        else:
            raise TypeError, "key must be hvdi.crypt.Key(), None, 0 or False, %s given." % str(type(key))
        self.buffer = (self.c_short*(NL_MAX_PACKET_LENGTH*600))()

    def __del__ (self):
        try:
            DeleteDecState(self.state)
            del self.state
        except: pass
        try: del self.key
        except: pass
        try: del self.buffer
        except: pass

    def decode (self, packet):
        """
        Decodes a compressed audio packet.
        Returns 16bit, 8000 Hz, mono, linear PCM audio samples as bytes in a string.
        """
        paclen = len(packet)
        packet = (self.c_ubyte*paclen)(*self.array("B", packet))
        paclen = paclen if paclen<NL_MAX_PACKET_LENGTH else NL_MAX_PACKET_LENGTH
        buffer = self.buffer
        declen = PacketDecode(packet, paclen, buffer, len(buffer), self.key.key, self.state)
        return self.array("h", buffer[:declen]).tostring()

    def iterdec (self, packs):
        """
        Decodes an iterable of audio packets.
        Returns a generator object that has to be iterated over.
        """
        for pack in packs:
            yield self.decode(pack)

    def setcomfortnoise (self, onoff=1):
        """
        Turns comfort noise on or off for silent packets.
        1 is on, 0 is off (1 default).
        """
        Hint(COMFORT_NOISE, onoff)

    def isvoiced (self, packet):
        """
        Checks whether an audio packet is voiced or not.
        Returns True if it is, False otherwise.
        """
        return PacketIsVoice(packet, len(packet))==NL_TRUE

    def getcodec (self):
        """
        Returns the audio codec that was used to decode the last packet.
        The returned value is the codec's human-readable name.
        """
        codec = DecStateGetCodec(self.state)
        if not codec: return
        codecs = []
        for k, v in CODECS.iteritems():
            if v==codec: codecs.append(k)
        if not codecs: return
        codecs.sort(key=lambda x: x.count("_"))
        if "_" not in codecs[0]:
            codecs = [x for x in codecs if "_" not in x]
        codecs.sort(key=lambda x: len(x))
        return codecs[0]

def Decode (instream, key=False, outstream=None):
    """
    Decodes packets from instream object and writes them into the outstream object using the crypt.Key() object from key argument for decryption.
    If key is 0/False (default), no decryption will be performed.

    The instream object must have one of following methods:
        readframes(), read(), recv() or get(), or be an iterable/generator object or a string.
    One of above mentioned methods will be called per iteration (without arguments) and must return a string with encoded packet.
    The decoding will stop when used method returns an empty string, or the iterable is at an end.
    If instream is a string, whole string will be considered one packet. Same will happen with the regular file.

    If outstream is None (default) the output will be a list of decoded packets.
    The outstream object must have one of following methods:
        writeframes(), write(), append(), push() or send(), or be a str(), buffer() or bytes object.
    Therefore you can use writers from wave, aifc and sunau modules, opened regular files in write mode, sockets or lists, queues and strings
    or any object supporting one of above mentioned object's protocols i.e. storing/sending methods.

    Decode() returns a reference to the outstream object
    so that you can access the returned list or string or use it in chained operations.
    """
    dec = Decoder(key)
    if outstream==None: outstream = []
    try:    _str = (str, bytes, buffer)
    except: _str = (str, buffer)
    if   hasattr(outstream, "writeframes"):
        write = outstream.writeframes
    elif hasattr(outstream, "write"):
        write = outstream.write
    elif hasattr(outstream, "append"):
        write = outstream.append
    elif hasattr(outstream, "send"):
        write = outstream.send
    elif hasattr(outstream, "push"):
        write = outstream.push
    elif isinstance(outstream, _str):
        def write (chunk):
            global outstream
            outstream += chunk
    else:
        raise AttributeError, "Output stream does not have supported write method."
    if isinstance(instream, _str):
        mark = 0
        def read ():
            global mark
            if mark: return ""
            mark = 1
            return instream
    elif hasattr(instream, "readframes"):
        read = instream.readframes
    elif hasattr(instream, "read"):
        read = instream.read
    elif hasattr(instream, "recv"):
        read = instream.recv
    elif hasattr(instream, "get"):
        read = instream.get
    else:
        try:
            g = iter(instream)
            def read ():
                try: return g.next()
                except: return ""
        except:
            raise AttributeError, "Input stream does not have supported read method."
    packet = read()
    while packet:
        write(dec.decode(packet))
        packet = read()
    return outstream

def Encode (instream, codec="GSM", key=False, chunksize=None, outstream=None):
    """
    Encodes chunks of linear PCM audio, 16bit, 8000 Hz, mono samples in bytes read from instream object
    into packets written to the outstream object using the specified codec and
    crypt.Key() object from key argument for encryption.

    codec can be a human-readable string name of a codec as returned by the
    hvdi.constants.list_codecs() function, or a HVDI numeric constant itself.

    If key argument is 0/False (default), no encryption will be applied.

    chunksize is a number of *samples* that will be read from the instream object.
    If it is None (default), the minimal required number of *samples* for the used codec will be chosen automatically.
    If instream is an iterable/generator object, then chunksize will be ignored and each item taken as an input chunk.
    The instream object must have one of following methods:
        readframes(), read(), recv() or get(), or be an iterable/generator object or a string.
    One of above mentioned methods will be called per iteration (with chunksize or number of bytes as an argument) and must return a string with
    linear PCM 16bit, 8000 Hz, mono audio samples.
    The encoding will stop when used method returns an empty string, or the iterable is at an end.
    If instream is a string it will be wrapped locally into the StringIO() object.
    Any supported method of the instream object, except writeframes(), will be used to extract chunksize 16bit *samples* per iteration.
    That means chunksize*2 bytes, but writeframes() is expected to return chunksize*2 bytes for chunksize as the argument.
    You can use one of readers from wave, aifc and sunau modules from Python stdlib for the instream object.

    If outstream is None (default) the output will be a list of encoded packets.
    The outstream object must have one of following methods:
        writeframes(), write(), append(), push() or send(), or be a str(), buffer() or bytes object.
    Therefore you can use sockets, lists, arrays, queues and strings
    or any object supporting one of above mentioned object's protocols i.e. storing/sending methods.
    The output packets will not be of the same length, so storing them using
    some of built-in storage objects like files, StringIO() or a string object, although possible,
    is practically useless.

    Encode() returns a reference to the outstream object
    so that you can access the returned list or string or use it in chained operations.
    """
    enc = Encoder(codec, key)
    if outstream==None: outstream = []
    try:    _str = (str, bytes, buffer)
    except: _str = (str, buffer)
    if   hasattr(outstream, "writeframes"):
        write = outstream.writeframes
    elif hasattr(outstream, "write"):
        write = outstream.write
    elif hasattr(outstream, "append"):
        write = outstream.append
    elif hasattr(outstream, "send"):
        write = outstream.send
    elif hasattr(outstream, "push"):
        write = outstream.push
    elif isinstance(outstream, _str):
        def write (pack):
            global outstream
            outstream += pack
    else:
        raise AttributeError, "Output stream does not have supported write method."
    if isinstance(instream, _str):
        import cStringIO
        instream = cStringIO.StringIO(instream)
    if hasattr(instream, "readframes"):
        read = instream.readframes
    elif hasattr(instream, "read"):
        read = lambda n: instream.read(n*2)
    elif hasattr(instream, "recv"):
        read = lambda n: instream.recv(n*2)
    else:
        try:
            g = iter(instream)
            def read (n):
                try: return g.next()
                except: return ""
        except:
            raise AttributeError, "Input stream does not have supported read method."
    chunksize  = chunksize if chunksize else enc.framesize
    chunksized = 2*chunksize
    chunk = read(chunksize)
    while chunk:
        l = len(chunk)
        if l<chunksized:
            chunk += (chunksized-l)*"\x00"
        write(enc.encode(chunk))
        chunk = read(chunksize)
    return outstream

def IterEncode (instream, codec="GSM", key=False, chunksize=None):
    """
    Same as Encode() but it returns a generator object instead of using the outstream object.
    Handy in loops.
    """
    enc = Encoder(codec, key)
    try:    _str = (str, bytes, buffer)
    except: _str = (str, buffer)
    if isinstance(instream, _str):
        import cStringIO
        instream = cStringIO.StringIO(instream)
    if hasattr(instream, "readframes"):
        read = instream.readframes
    elif hasattr(instream, "read"):
        read = lambda n: instream.read(n*2)
    elif hasattr(instream, "recv"):
        read = lambda n: instream.recv(n*2)
    else:
        try:
            g = iter(instream)
            def read (n):
                try: return g.next()
                except: return ""
        except:
            raise AttributeError, "Input stream does not have supported read method."
    chunksize = chunksize if chunksize else enc.framesize
    chunksize = chunksize if chunksize else 160
    chunk = read(chunksize)
    while chunk:
        l = len(chunk)
        if l<chunksize:
            chunk += (chunksize-l)*"\x00"
        yield enc.encode(chunk)
        chunk = read(chunksize)

def IterDecode (instream, key=False):
    """
    Same as Decode() but it returns a generator object instead of using the outstream object.
    Handy in loops.
    """
    dec = Decoder(key)
    try:    _str = (str, bytes, buffer)
    except: _str = (str, buffer)
    if isinstance(instream, _str):
        mark = 0
        def read ():
            global mark
            if mark: return ""
            mark = 1
            return instream
    elif hasattr(instream, "readframes"):
        read = instream.readframes
    elif hasattr(instream, "read"):
        read = instream.read
    elif hasattr(instream, "recv"):
        read = instream.recv
    elif hasattr(instream, "get"):
        read = instream.get
    else:
        try:
            g = iter(instream)
            def read ():
                try: return g.next()
                except: return ""
        except:
            raise AttributeError, "Input stream does not have supported read method."
    packet = read()
    while packet:
        yield dec.decode(packet)
        packet = read()

class Mixer:
    """
    High level mixer class.
    """
    from ctypes import c_short, c_ubyte, c_int, pointer, POINTER
    from array  import array
    from math import sin, cos, radians, sqrt
    sqrt22 = sqrt(2)/2
    def mix (self, *args):
        """
        Mixes all given audio sources into a single source.
        The audio samples in each of the input buffers must be 16bit, mono linear PCM encoded audio bytes in a string or an iterable
        containing signed short integers (Python ints from -2**15 to 2**15).
        The sample rate does not matter.
        Returns the mix of all input buffers as a 16bit, mono linear PCM audio samples as bytes in a string.
        """
        if len(args)<2:
            raise TypeError, "Not enough buffers to mix. At least 2 required!"
        buflen = len(max(args, key=lambda x: len(x)))
        if not buflen:
            raise TypeError, "At least one buffer must contain data!"
        args   = (y+((buflen-len(y))*"\x00") for y in args if y)
        buflen /= 2
        args   = [(self.c_short*buflen)(
            *self.array("h", x))
            for x in args]
        number = len(args)
        inbuf  = (self.POINTER(self.c_short*buflen)*number)(*[self.pointer(x) for x in args])
        outbuf = (self.c_short*buflen)()
        Mix(outbuf, inbuf, number, buflen)
        return self.array("h", outbuf).tostring()

    def resample (self, inbuf, inrate=22050, outrate=8000):
        """
        Resamples the audio source from inbuf sampled at inrate
        to the new sample rate set by outrate.
        inbuf   --> 16bit, 8000 Hz,mono audio samples in a string or iterable
                    The samples must be 16bit, 8000 Hz, mono, linear PCM encoded audio bytes in a string or an iterable
                    containing signed short integers (Python ints from -2**15 to 2**15).
        inrate  --> The original sample rate in Hz (22050 default)
        outrate --> The desired sample rate in Hz (8000 default)
        Returns the resampled version of the input buffer as a 16bit, outrate Hz, mono, linear PCM audio samples as bytes in a string.
        """
        if inrate==outrate:
            return inbuf
        rate    = NewRate(inrate, outrate)
        inlen   = len(inbuf)/2
        inbuf   = (self.c_short*inlen)(*self.array("h", inbuf))
        outlen  = int(round((float(inlen)/inrate)*outrate))
        outbuf  = (self.c_short*outlen)()
        ninlen  = self.c_int(inlen)
        noutlen = self.c_int(outlen)
        RateFlow(rate, inbuf, outbuf, self.pointer(ninlen), self.pointer(noutlen))
        DeleteRate(rate)
        s = self.array("h", outbuf[:noutlen.value+1]).tostring()
        if ninlen.value<inlen:
            s += self.resample(inbuf[ninlen.value:inlen], inrate, outrate)
        return s

    def agc (self, buffer, level=0.6):
        """
        Applies the automatic gain control to audio source in the input buffer.
        buffer --> 16bit, 8000 Hz,mono audio samples in a string or iterable
                   The samples must be 16bit, 8000 Hz, mono, linear PCM encoded audio bytes in a string or an iterable
                   containing signed short integers (Python ints from -2**15 to 2**15).
        level  --> The AGC level as a float between 0.5 and 1.0
                   Recommended values range from 0.8 to 0.95.
                   At 1.0 some clipping might be experienced.
        Returns the AGCed version of the input buffer as a 16bit, 8000 Hz, mono, linear PCM audio samples as bytes in a string.
        """
        buffer = self.array("h", buffer)
        buflen = len(buffer)
        buffer = (self.c_short*buflen)(*buffer)
        a = NewAGC(level)
        AGC(a, buffer, buflen)
        DeleteAGC(a)
        return self.array("h", buffer).tostring()

    def uninterleave (self, buffer):
        """
        Uninterleaves a single stereo audio channel into two separate mono channels.
        buffer --> 16bit, stereo audio samples in a string or iterable
                   The samples must be 16bit, stereo linear PCM encoded audio bytes in a string or an iterable
                   containing signed short integers (Python ints from -2**15 to 2**15).
                   The sample rate does not matter.
        Returns a tuple with two audio channels (left, right) of which each is 16bit, mono, PCM linear audio samples as bytes in a string.
        """
        buffer = self.array("h", buffer)
        return buffer[0::2].tostring(), buffer[1::2].tostring()

    def interleave (self, left, right):
        """
        Interleaves two mono audio channels into single stereo channel.
        left  --> Audio samples for the left channel
        right --> Audio samples for the right channel
        The samples must be 16bit, mono linear PCM encoded audio bytes in a string or an iterable
        containing signed short integers (Python ints from -2**15 to 2**15).
        The sample rate does not matter.
        Returns a string of bytes containing 16bit, stereo, PCM linear audio samples.
        """
        left  = self.array("h", left)
        right = self.array("h", right)
        out = self.array("h")
        for x in xrange(len(left)):
            out.append(left[x])
            out.append(right[x])
        return out.tostring()

    def pan (self, buffer, angle):
        """
        Pans a 16bit mono audio buffer into two channels.
        The algorithm derives from:
            https://dsp.stackexchange.com/questions/21691/algorithm-to-pan-audio
        buffer --> Audio data as iterable of signed short samples or an 16bit audio stream as bytes in a string
                   The samples must be 16bit, mono linear PCM encoded audio bytes in a string or an iterable
                   containing signed short integers (Python ints from -2**15 to 2**15).
                   The sample rate does not matter.
        angle  --> The angle in degrees
                   At which angle to pan the mono audio source in the stereo output.
                   At 0 and 180 degrees the left channel equals the right.
                   Audible inclination to the right starts around 25 degrees.
        Returns a tuple with two audio channels (left, right) of which each is 16bit, mono, PCM linear audio samples as bytes in a string.
        """
        buffer = self.array("h", buffer)
        angle  = self.radians(angle)
        c = self.cos(angle)
        s = self.sin(angle)
        lfact = self.sqrt22*(c-s)
        rfact = self.sqrt22*(c+s)
        l = self.array("h", (int(lfact*x) for x in buffer))
        r = self.array("h", (int(rfact*x) for x in buffer))
        return l.tostring(), r.tostring()
