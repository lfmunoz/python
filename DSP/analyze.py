import sys
import numpy as np
from scipy.signal import triang 
from scipy.fftpack import fft
import pylab as plt

# data format, binary offset
binary_offset = True # False = two's complement 
# bit resolution
r = 8
# sample rate in MHz
fs = 1250

# load samples
x = np.genfromtxt("./data/adc0_fmc126.txt", dtype=None);
N = x.size

if binary_offset == True:
	for num in range(N):
		if x[num] < 0:
			x[num] = x[num] + 2**r
		else:
			x[num] = abs(x[num])
	# normalize the signal
	x  = x / 2.0**(r)
else:
	# subtract one because MSB is sign bit and already represented with sign
	x  = x / 2.0**(r-1)
		
# generate window function
#window = np.blackman(N)
#window = np.hamming(N)
window = np.hanning(N)
#window = np.bartlett(N)
#window = np.ones(N)

# roll the waveform to get correct phase
#fftbuffer = np.roll(fftbuffer, -(fftbuffer.size/2))

# perform the FFT
X = fft(x*window)
mx = 20*np.log10(2.0  * 1/ N * abs(X))
pX = np.angle(X)

# plot time domain
plt.subplot(2,1,1)
plt.plot(np.arange(256), x[:256])
plt.title('Waveform Analysis')
plt.ylabel('Time Domain')

# plot frequency domain
plt.subplot(2,1,2)
xaxis= np.arange(N/2-1) * fs/N
plt.plot(xaxis, mx[:N/2-1])
plt.ylabel('Frequency Domain')
plt.xlabel('MHz')

plt.show()



