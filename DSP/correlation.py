import numpy as np
import scipy
from scipy.signal import square, sawtooth, correlate, triang
from numpy import pi, random
import pylab as plt


def xcorrFunc(A,B):
    N = B.size
    C = np.array([])
    tmpB = np.concatenate([np.zeros(N-1), B])
    tmpA = np.concatenate([A,np.zeros(N-1)])
    for i in range(2*N-1):
        tmp0 = np.roll(tmpA,i+1)
        C = np.append(C,[sum(tmp0*tmpB)])
    return C


t=range(7)
nsamples=7
x = triang(5)
y = np.roll(x,2)

plt.figure(0) 
plt.subplot(2,1,1)
plt.stem(x)
#plt.axis([0 22 -1 2])
plt.title('Input Sequence')

plt.subplot(2,1,2)
plt.stem(y)
#plt.axis([0 22 -1 2])
plt.title('Output Sequence')


xcorr = correlate(x, y)
xcorr0 = xcorrFunc(x, y)

print xcorr
print xcorr0

plt.figure(1) 
plt.stem(xcorr)




# The peak of the cross-correlation gives the shift between the two signals
# The xcorr array goes from -nsamples to nsamples
dt = np.linspace(-t[-1], t[-1], 2*nsamples-1)
recovered_time_shift = dt[xcorr.argmax()]

#print x
#print y

print "xcorr size %d" % xcorr.size
print "xcorr max indx %d" % xcorr.argmax()
print "recovered shift %d" % recovered_time_shift


plt.show();
