from audiotsm2 import phasevocoder, soundstretch

phasevocoder('sine.wav', 'out.wav', speed=3)

soundstretch('sine.wav', 'out2.wav', speed=3)