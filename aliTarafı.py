import DiffieHellman
import burakTarafı

ali = DiffieHellman.DHKE(5, 23)


ali.generate_privatekey()
print("Ali'ni Private Key'i: ' ",ali.pk,"\n")
print("------------------------\n\n")


ali.generate_publickey()
print("Ali'nin Public Key'i : ",ali.pub_key,"\n")
print("------------------------\n\n")



ali.exchange_key(burakTarafı.pub_key)
print("Ali tarafından paulaşılan anahtar : ",ali.share_key,'\n')
print("------------------------------\n")
