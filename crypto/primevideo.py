import hashlib
from Crypto.Util.number import long_to_bytes
def sha1(mensagem):
  m = hashlib.sha1()
  m.update(mensagem.encode('utf-8'))
  return m.hexdigest()

# módulo n (equvalente ao |E| descrito nas anotações da GET)
n = 656563738156183614196284144218755562218717754449979872699851236361364842254951562533589572185811735734269627798779142529399297211938766368323781389974849197211221357383295846145542699614912769848476126126824744284474444862644897675458539907

# Assinatura Digital 1 (Perceba que r é igual para as duas assinaturas)
r=95607856998428856962864667427230197797741826906987352066517618702726741034205788706243608221638336439218766183440425733114479831314017676199460278142286425537126711154511562912579612912784188540749745708743557963162626080980370058843390766
s1=221531213777841923648016978735137443328287049470572243281503729853749410439027043274206080010606200779066290864940142109323376613921602339131638767599272873444533706824739127385141559710420880102408860390182658578090121336115350942635014137
mensagem1 = "There's the pangs of time, there's the undiscover'd country from whose bourn no traveller returns, puzzles the native hue of resolution devoutly to be: that the unworthy takes, when he himself might his quietus make with and the respect that flesh is heir to, 'tis a consience of outrageous fortune, or not to be wish'd. To die: to sleep to sleep to sleep; to suffer the spurns that makes calamity of something after death, the rub; for in that sleep; to sleep to sleep; to sleep; to sleep; to sleep to suf"

# Assinatura Digital 2
r=95607856998428856962864667427230197797741826906987352066517618702726741034205788706243608221638336439218766183440425733114479831314017676199460278142286425537126711154511562912579612912784188540749745708743557963162626080980370058843390766
s2=55067590702777343534073294382670650356610198385801873654338933710289804624249903578690473638691031177408887487137275692190721991601026665566663726842114259490806349503408033328297681194917703223024735759356440903287908550041401014196411193
mensagem2 = "What down at the name of Sanders. (What down at the forest all by himself. It went like that, just buzzing, he climb the tree, there came to an open place was a large oak-tree, and as he had the forest, and in the middle of Sanders. (What does under it. So he began to climbed, and began to think. First of the tree, and lived under the top of there came to an open place in the only reason for making a bee. Then he thought another long time, and buzzing and as he climbed and he sang a buzzing-noise"

z1,z2 = int(sha1(mensagem1), 16), int(sha1(mensagem2), 16)
# Desafio Começa aqui :

k = ((z1 - z2) * pow(s1 - s2, -1, n)) % n

dA = ((s1 * k  - z1) * pow(r, -1, n)) % n

# Desafio acaba aqui! =)
print(long_to_bytes(dA))