from math import sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np

rows = 4
cols = 1

# T = 10s
T = 2
fp = 1000
N = T * fp
dt = 1.0/fp

#generate time
t = np.linspace(0, T, N, endpoint=False)

plt.subplot(rows, cols, 1)
#my 1. sin wave
A1 = 1
f1 = 3
ph1 = 0
off1 = 0
y1 = []
for n in t:
    y1.append(A1 * sin(n * f1 * (2 * pi) + ph1) + off1)
plt.plot(t, y1, 'b')

plt.subplot(rows, cols, 2)
#my 2. sin wave
A2 = 1
f2 = 1/2.0
ph2 = 0
off2 = 0
y2 = []
for n in t:
    y2.append(A2 * sin(n * f2 * (2 *pi) + ph2) + off2)
plt.plot(t, y2, 'g')

#plot y1+y2
plt.subplot(rows, cols, 3)
y3 = []
for n, m in zip(y1, y2):
    y3.append(n+m)
plt.plot(t, y3)


plt.subplot(rows, cols, 4)
#fourier
ft = np.fft.fft(y1)
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, abs(ft))

#jedynka tryg.
#plt.subplot()
# s = []
# for n, m in zip(y1, y2):
#     s.append(n**2+m**2)
# plt.plot(t, s)

plt.show()

