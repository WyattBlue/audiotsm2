<h1 style="center">AudioTSM 2</h1>
<h2 style="center">An ultrafast audio time-scale modification library</h2>

```terminal
pip install audiotsm2
```

### Basic usage
AudioTSM 2 is a light weight audio speed modification library. Below is a basic example showing how to reduce the speed of a wav file by half using the phase vocoder procedure.

```python

from audiotsm2 import phasevocoder
from audiotsm2.io.wav import WavReader, WavWriter

with WavReader(input_filename) as reader:
    with WavWriter(output_filename, reader.channels, reader.samplerate) as writer:
        phasevocoder(reader.channels, speed=0.5).run(reader, writer)
```