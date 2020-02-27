'''
Here art'h dow focused my taughts that lay beneath.

Regarding SU approach vs full evolution (delta N -> Transport -> PyCool (covers everything statitically!)). 
Super or sub horizon which is more dominant? Which is more testable? which is more tellin and which is more interesting?

Tel this story. The struggle to understand the mapping of physics to observation in the universe. The increasing levels of complexity to which we may describe it. That which we seak to understand. Focus on and must persist. Where religion has acted in the past so much science now. The needs of the individual require an understanding, an answer readily available and in line with reality and expectation.. Under those two conditions we create an idea a worlf that one may construct. 
Under only that regieme may we follow, only one, no matter what. 
This is the way towards history. Because oterwise there is nothing else.
It's survival.
'''

import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 20  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 
