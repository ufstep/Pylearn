import numpy as np
import matplotlib.pyplot as plt

bit = 14 # RX ADC 
Fs = 122.88 # RX ADC: FS=122.88 MSPS
BW = 15.36 # BandWidth = 153600000/1000000 = 15.36M

#Read IQ data files
IData = np.genfromtxt('I.csv',delimiter=",")
QData = np.genfromtxt('Q.csv',delimiter=",")

#Combine IQ data to complex (x +jy) number.
C = np.vectorize(complex)(IData,QData)

# FFT Conversion 
xf = np.fft.fft(C)

# Image Abs
D = 20*np.log10(np.absolute(xf))

#calculate sampling point
S = np.count_nonzero(D)
print S

#swap array data
temp1 = D[0:(S/2)]
temp2 = D[(S/2):S]
D = np.concatenate((temp2,temp1), axis=0)

PdBFs = D-(6.02*bit)-(10*np.log10(Fs/(2*BW)))-20*np.log10(S)

Pw = 10**(PdBFs/10)

#plot FFT spectrum
plt.xlabel("Frequency bin")
plt.ylabel("Power(dB)")
plt.grid(b=True, which='both', color='0.45',linestyle='--')
plt.plot(PdBFs)
plt.show()

