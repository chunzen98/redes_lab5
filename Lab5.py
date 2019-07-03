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

def ASK(bits, a1, a0, bt, fs):

    tSignal = []
    signal = []


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



    plt.figure("Portadora ASK 1")
    plt.plot(tSignal, signal, "c")
    plt.xlabel("Tiempo(s)")
    plt.ylabel("Amplitud [dB]")
    plt.title("Portadora ASK")
    plt.show()

    return signal, tSignal

# ---------- BLOQUE PRINCIPAL -------------

bits = [0, 1, 0, 1, 1]

signalASK,tASK = ASK(bits, 2, 1, 1, 2)

