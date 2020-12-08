import random
class DHKE:
    def __init__(self,G,P):
        self.G_param = G
        self.P_param = P

    def generate_privatekey(self):
        self.pk = random.randrange(start = 1,stop = 100,step = 1)
        return 1

    def generate_publickey(self):
        self.pub_key = pow(self.G_param,self.pk) % self.P_param
        return 1

    def exchange_key(self,other_public):
        self.share_key = pow(other_public,self.pk) % self.P_param
        return 1


ali = DHKE(5, 23)
burak = DHKE(5,23)


ali.generate_privatekey()
burak.generate_privatekey()

print("Ali'ni Private Key'i: ' ",ali.pk,"\n")
print("Burak'ın private key'i:  ",burak.pk,"\n")
print("------------------------\n\n")

ali.generate_publickey()
burak.generate_publickey()

print("Ali'nin Public Key'i : ",ali.pub_key,"\n")
print("Burak'ın public key'i:  ",burak.pub_key,"\n")
print("------------------------\n\n")


ali.exchange_key(burak.pub_key)
burak.exchange_key(ali.pub_key)
print("Ali tarafından paulaşılan anahtar : ",ali.share_key,'\n')
print("Burak tarafından paylaşılan anahtar : ",burak.share_key,'\n')
print("-----------------------\n")










