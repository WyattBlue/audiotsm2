A real-time audio time-scale modification library
=================================================

.. image:: https://readthedocs.org/projects/audiotsm/badge/?version=latest
    :target: http://audiotsm.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://travis-ci.org/Muges/audiotsm.svg?branch=master
    :target: https://travis-ci.org/Muges/audiotsm
    :alt: Build Status

Audiotsm2 is the light-weight version of the original.


Basic usage
-----------

Below is a basic example showing how to reduce the speed of a wav file by half
using the phase vocoder procedure::

    from audiotsm2 import phasevocoder
    from audiotsm2.io.wav import WavReader, WavWriter

    with WavReader(input_filename) as reader:
        with WavWriter(output_filename, reader.channels, reader.samplerate) as writer:
            phasevocoder(reader.channels, speed=0.5).run(reader, writer)
