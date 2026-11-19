
import en_modul

#karaktärer


class Karaktar :
    def __init__(self,namn,hp, luck,styrka , xp):
        self.namn = namn
        self.hp = hp
        self.luck = luck
        self.styrka = styrka
        self.xp = xp
        self.inventory = []

        
    def print_character(self):
        print(f" {self.namn} hp: {self.hp} luck: {self.luck} styrka: {self.styrka} xp :{self.xp} ")



def xp_ett (Karaktar):
    Karaktar.xp += 1
    print("du fick ett xp !!!")



Lucky = Karaktar("Nazrull", 100 , 0.7 , 10 , 0)
Surviver = Karaktar("Liza", 120 , 0.5 , 10 , 0)
Damage = Karaktar ("Jeffi", 100 , 0.5 , 14 , 0)
#lista med karaktärerna för att kunna printa ut dem i starten
charachters = [Lucky, Surviver, Damage]



class Vapen :
    def __init__(self,namn,multiplyer) :
        self.namn = namn
        self.multiplyer = multiplyer



kniv = Vapen("Köks kniv", 1.2 )
tofla = Vapen("Rutten tofla", 1.05)


class Fiende :
    def __init__(self, namn , hp , styrka):
        self.namn = namn
        self.hp = hp
        self.styrka = styrka

Numer1opp = Fiende( "Abdulahlrazim" , 28 , 3)
shottas = Fiende("Jordgubben" , 20 , 10)
Telefontillmammma = Fiende("Gunilla", 50 , 2)
jul = Fiende("Jultomten", 67 , 1)
epi = Fiende("Epstain" , 30 , 10)
        






def start_meny():
    en_modul.Rubrik()
    while True :
        start_svar = input("""Tryck 1 för att Starta Spel 
        Tryck 2 för att se Credits 
        Truck 3 för att Avsluta """)
        try :
            int(start_svar)
            break
        except :
            print("något gick fel")
            continue
        # skriver ut karaktärerna
        


def karaktar_val():
    for c in charachters:
            c.print_character()
    try :
        karaktar_vald = input("V")

    except :
        d
 
start_meny()

# slayer.inventory.append()
# print(slayer.hp)
# slayer.hp -= 0.1
# print(slayer.hp)

