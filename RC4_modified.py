#%%
import numpy as np

key = 'dfdrefdfdf'
plaintext = 'I want to learn about this'
plaintextArray = np.array([ord(i) for i in plaintext])
keyArray = [ord(i) for i in key]
S = [x for x in range(256)]
GenerateOutput = [i for i in plaintext]


def KSA (key):
    j = 0
    for i in range(256):
        S[i] = i
    for i in range(256):
        j = ( j + S[i] + key[i % len(key)] ) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        
    return S
#%%
def PRNG(S , GenerateOutput):
    h = 0
    j = 0
    key = []
    while GenerateOutput == True:
        i = i + 1 %256
        j = (j + S[i]) %256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        R = S[ (S[i] + s[j]) %256 ]
        key.append(R)
        
    return key

key = keyArray
S = KSA(key)
keyStream = np.array(PRNG(S, len(plaintext)))
cipher = keyStream ^ plaintextArray

print(cipher)





# %%
