import numpy as np

def fft(data,time_data):
    n=len(data)
    k=np.arange(n)
    T=abs(time_data[0]-time_data[-1])
    freq=k/T
    freq=freq[range(int(n/2))]
    Y=np.fft.fft(data)/n
    Y=Y[range(int(n/2))]
    
    return Y,freq
