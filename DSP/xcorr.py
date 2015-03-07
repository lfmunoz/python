import numpy as np
import scipy
from scipy.signal import square, sawtooth, correlate
import pylab as plt


def xcorr(A,B):
    N = B.size
    C = np.array([])
    tmpA = np.concatenate([np.zeros(N-1), A])
    tmpB = np.concatenate([B,np.zeros(N-1)])
    for i in range(2*N-1):
        tmp0 = np.roll(tmpA,i+1)
        C = np.append(C,[sum(tmp0*tmpB)])
    return C


A = np.arange(5)
B = np.arange(5)

print xcorr(A,B)
