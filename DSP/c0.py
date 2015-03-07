
import numpy as np
import scipy
from scipy.signal import square, sawtooth, correlate
import pylab as plt
import logging

logging.basicConfig(format='[%(levelname)-8s] %(message)s', level=logging.DEBUG)

A = 0.8
f = 1
phi = 0
fs = 20
t = np.arange(-1, 1, 1.0/fs)
N = t.size
logging.debug("N : %d" % N) 
x0 = A*np.sin(2*np.pi*f*t + phi)

plt.figure(0)
plt.title("Waveform 0")
plt.plot(t,x0)

A = 0.8
f = 1
phi = np.pi 
fs = 20
t = np.arange(-1, 1, 1.0/fs)
N = t.size
logging.debug("N : %d" % N) 
x1 = A*np.sin(2*np.pi*f*t + phi)

plt.figure(1)
plt.title("Waveform 1")
plt.plot(t,x1)


#find cross_correlation
xcorr = correlate(x0, x1)
#delta time array to match xcorr
dt = np.arange(1-N, N)
recovered_time_shift = dt[xcorr.argmax()]

logging.debug("time shift : %f" % recovered_time_shift ) 

plt.figure(2)
plt.xcorr(x0,x1)

plt.show()





