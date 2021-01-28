from audiotsm2 import phasevocoder, WavReader, WavWriter

with WavReader('sine.wav') as reader:
    with WavWriter('out.wav', reader.channels, reader.samplerate) as writer:
        phasevocoder(reader.channels, reader, writer, speed=0.5)