import sys
import numpy as np
from scipy.signal import triang 
from scipy.fftpack import fft
import pylab as plt

# bit resolution
r = 16 
# sample rate
fs = 368.64 *10**6
fs = 368.64 

# load samples
x = np.genfromtxt("./adc0.txt", dtype=None);
# normalize the signal
x  = x / 2.0**(r-1)

N = x.size
#fftbuffer = np.roll(fftbuffer, -(fftbuffer.size/2))

X = fft(x)
mx = 20*np.log10(2.0  * 1/ N * abs(X))
pX = np.angle(X)

plt.subplot(2,1,1)
plt.plot(x[:256])
plt.title('Waveform Analysis')
plt.ylabel('Time Domain')

plt.subplot(2,1,2)
xaxis= np.arange(N/2-1) * fs/N
plt.plot(xaxis, mx[:N/2-1])
plt.ylabel('Frequency Domain')
plt.xlabel('MHz')

plt.show()



