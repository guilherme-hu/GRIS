from Crypto.Util.number import long_to_bytes
FLAG = 31629006585085327409812507270875453196064125651594425718867181172787427788449 # mensagem cifrada = c
e = 65537                                                                            # expoente publico

p = 2
n = 174273493446054651350782275296370226885594728696881571385688057497125122365534 
q = n//2 # q = n/2 -> n = p.q, logo q = n/p = n/2
phi = q-1 # phi = (p-1)(q-1), p = 2
d = pow(e,-1,phi)
print(long_to_bytes(pow(FLAG, d, n)))