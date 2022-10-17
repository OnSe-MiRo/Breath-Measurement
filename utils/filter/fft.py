import numpy as np

def fft(data):
    n=len(data)
    k=np.arange(n)
    Fs=60
    T=n/Fs
    freq=k/T
    freq=freq[range(int(n/2))]
    Y=np.fft.fft(data)/n
    print(data)
    Y=Y[range(int(n/2))]
    return Y,freq