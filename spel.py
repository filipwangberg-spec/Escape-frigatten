
#karaktärer
class Karaktar :
    def __init__(self,namn,hp, luck,styrka , xp):
        self.namn = namn
        self.hp = hp
        self.luck = luck
        self.styrka = styrka
        self.xp = xp
        self.inventory = []

def xp_ett (Karaktar):
    Karaktar.xp += 1
    print("du fick ett xp !!!")
    


Lucky = Karaktar("Nazrull", 100 , 0.7 , 10 , 0)
Surviver = Karaktar("Liza", 120 , 0.5 , 10 , 0)
Damage = Karaktar ("Jeffi", 100 , 0.5 , 14 , 0)

class Vapen :
    def __init__(self,namn,multiplyer) :
        self.namn = namn
        self.multiplyer = multiplyer



kniv = Vapen("Köks kniv", 1.2 )
tofla = Vapen("Rutten tofla", 1.05)


class Fiende :
    def _init__(self, namn , hp , styrka):
        self.namn = namn
        self.hp = hp
        self.styrka = styrka

Numer1opp =  Fiende("Abdulahlrazim" , 28 , 3)
shottas = Fiende("Jordgubben" , 20 , 10)
Telefontillmammma = Fiende("Gunilla", 50 , 2)
        








def start_meny():
    while True:
        print("~~~~Escape Fregatten~~~~")
        print("1. Starta Spel")
        print("2. Credits")
        print("3. Avsluta")




# slayer.inventory.append()
# print(slayer.hp)
# slayer.hp -= 0.1
# print(slayer.hp)
