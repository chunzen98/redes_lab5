# --------- IMPORTACIONES ---------
import scipy.io

import numpy as np
import matplotlib.pyplot as plt


# ---------- BLOQUE FUNCIONES -------------


# bits= Arreglo de bits (Senal digital)
# a1 = 1 signal amplitude
# a0 = 0 signal amplitude
# bt = bit time
# fs = sample frequency

def OOK(bits, a1, bt, fs):

    tSignal = []
    signal = []

    a0 = 0
    a = 0
    for i in bits:

        t = np.linspace(a, a + bt, num=fs * bt * 100)

        if i == 1:
            carrier = a1 * np.cos(2 *np.pi * fs * t)
        else:
            carrier = a0 * np.cos(2 * np.pi * fs * t)

        a += bt

        signal = signal + carrier.tolist()
        tSignal = tSignal + t.tolist()



    plt.figure("Portadora OOK 1")
    plt.plot(tSignal, signal, "c")
    plt.xlabel("Tiempo(s)")
    plt.ylabel("Amplitud [dB]")
    plt.title("Portadora OOK")
    plt.show()


    return signal, tSignal


def demodOOK(signal, a1, bt, fs):

    t = np.linspace(0, bt, num=fs * bt * 100)
    a0 = 0

    bits = []

    carry1 = a1 * np.cos(2 * np.pi * fs * t)
    carry0 = a0 * np.cos(2 * np.pi * fs * t)
    yAux = []

    i = 0
    while i < len(signal):
        if i % (fs * bt * 100) == 0:
            #if(np.correlate(yAux,carry1)[0] == 0):
            if (signal[i] != 0):
                bits.append(1)
            #elif(np.correlate(yAux, carry0)[0] == 0):
            elif (signal[i] == 0):
                bits.append(0)
            yAux = []
        yAux.append(signal[i])
        i += 1

    return bits

# ---------- BLOQUE PRINCIPAL -------------

bits = [1, 0, 1, 0, 1, 1, 1]





signalOOK,tOOK = OOK(bits, 2, 1, 10)


bitsDemod = demodOOK(signalOOK, 2, 1, 10)

print(bitsDemod)

#print(np.correlate(np.array([123,1,1]), np.array([0,1,0])))