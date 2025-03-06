from Crypto.Util.number import long_to_bytes
def add_PQ(P, Q, a, p):
  O = (0,0)
  if P == O:
    return Q
  if Q == O:
    return P
  x1, y1 = P[0], P[1]
  x2, y2 = Q[0], Q[1]

  if x1 == x2 and y1 == (p-y2) % p:
    return O

  if P != Q:
    s = ((y2-y1) * pow(x2-x1, -1, p)) % p
  else:
    s = ((3 * x1**2 + a)*pow(2*y1, -1, p)) % p
  x3 = (s**2 - x1 - x2) % p
  y3 = (s*(x1-x3) - y1) % p
  return x3,y3

def encontra_nP(k, P, a, p):
    result = (0, 0)
    addend = P
    while k > 0:
        if k % 2 == 1:
            result = add_PQ(result, addend, a, p)
        addend = add_PQ(addend, addend, a, p)
        k //= 2
    return result

# Chave Pública
# y^2 = x^3 +ax +b (mod p)
a = 15347898055371580590890576721314318823207531963035637503096292
b = 7444386449934505970367865204569124728350661870959593404279615

P = (1619092589586542907492569170434842128165755668543894279235270,
     3436949547626524920645513316569700140535482973634182925459687)
 
p = 17676318486848893030961583018778670610489016512983351739677143 

# Mensagem Encriptada
S = (334723336424414961000482608007001766504544326753246721049147, 12254736703215694149846183808068667208423268069978932609288223)

# Diffie-Helmann

Q_sam= (246061765250195212969506118903120091083185433952208069588975,9343754362889750569766954041373414358787687742337204027292453)

n_frodo = 233336110442550297617299

# Altere SOMENTE esse trecho abaixo para obter a mensagem decriptada
# Um exemplo seria: 3P = encontra_nP(3,P,a,p)
T = encontra_nP(n_frodo, Q_sam, a, p)

dec_x = (S[0] * pow(T[0], -1, p)) % p # xs * xt^-1 mod p
dec_y = (S[1] * pow(T[1], -1, p)) % p # ys * yt^-1 mod p
# Até aqui

# Essa função retorna a flag, basta alterar o trecho acima e você terá a resposta =)
print(long_to_bytes(int(str(dec_x)+""+str(dec_y))))