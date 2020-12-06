import numpy as np


def key_State(key):
    key_lenght = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_lenght]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp

def pRBG(S, GenerateOutput):
    i = 0
    j = 0
    while GenerateOutput ==True:
        i = i + 1 %256
        j = j + S[i] %256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        R = S[ S[i] + S[j] %256]
        print(R)

key = 'ENDEAVOUR'
plaintext = 'I only study to understand'

def prepareKeyArray(s):
    return[ord(c) for c in s]

key = prepareKeyArray(key)


S = key_State(key)

keyStream = np.array(pRBG(S , len(plaintext)))
print(keyStream)

plaintext = np.array([ord(i) for i in plaintext])
cipher = np.bitwise_xor([]keyStream ^ plaintext

print(cipher.astype(np.uint8).data.hex())
print([chr[c] for c in cipher])




