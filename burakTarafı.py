import DiffieHellman
import aliTarafı

burak = DiffieHellman.DHKE(5,23)



burak.generate_privatekey()
print("Burak'ın private key'i:  ",burak.pk,"\n")
print("------------------------\n\n")


burak.generate_publickey()
print("Burak'ın public key'i:  ",burak.pub_key,"\n")
print("------------------------\n\n")


burak.exchange_key(aliTarafı.pub_key)
print("Burak tarafından paylaşılan anahtar : ",burak.share_key,'\n')
print("-----------------------\n")
