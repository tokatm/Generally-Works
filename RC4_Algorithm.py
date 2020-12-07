def key_State(key):
    key_lenght = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_lenght]) % 256
        S[i] , S[j] = S[j] , S[i]
    return S

def pRBG(S, n):
    i = 0
    j = 0
    key = []
    while n>0:
        n = n -1 
        i = (i + 1) %256
        j = (j + S[i]) %256
        S[i] , S[j] = S[j] , S[i]
        K = S[(S[i] + S[j])% 256]
        key.append(K)
    return key


key = 'CRYPTO'
plaintext = 'Mustafa'

def prepareKeyArray(s):
    return[ord(c) for c in s]

key = prepareKeyArray(key)

import numpy as np
S = key_State(key)

keyStream = np.array(pRBG(S , len(plaintext)))
print(keyStream)

plaintext = np.array([ord(i) for i in plaintext])
cipher = keyStream ^ plaintext

print(cipher.astype(np.uint8).data.hex())
print([chr(c) for c in cipher])




