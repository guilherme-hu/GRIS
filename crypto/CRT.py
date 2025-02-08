import math
from Crypto.Util.number import long_to_bytes
# Altere somente as linhas com ??
def CRT(sistema):
    N = 1
    for ai, ni in sistema:
        N *= ni

    X = 0
    for ai, ni in sistema:
        Ni = N//ni
        xi = pow(Ni, -1, ni) # xi * Ni ≡ 1 (mod ni)
        X += Ni * xi * ai

    return pow(X,1,N)

e = 7
n1 = 12836199686973860671317829319572068536675366202551
n2 = 9207164809729988062334325079856956174096146645421
n3 = 13622149579754221729460065730654953951867472393417

a1 = 3813911391918830343786624637400279512933046231999
a2 = 2068264257340920848271568225822036140145353768448
a3 = 5020458554640173667230974368342025301857250930440

sistema = [(a1, n1),
           (a2, n2), 
           (a3, n3)]  # X ≡ a1 (mod n1), X ≡ a2 (mod n2), X ≡ a3 (mod n3)
 
X = math.ceil(CRT(sistema)**(1/e))      # X ≡ (msg**7)**(1/7) (mod N)

print(f"CTF-BR{{{long_to_bytes(X).decode()}}}") 