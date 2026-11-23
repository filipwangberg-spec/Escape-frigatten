
import en_modul


#karaktärer


class Karaktar :
    def __init__(self,namn,hp, luck, styrka , xp):
        self.namn = namn
        self.hp = hp
        self.luck = luck
        self.styrka = styrka
        self.xp = xp
        self.inventory = []
        
    def print_character(self):
        en_modul.slow_type(f" {self.namn} hp: {self.hp} luck: {self.luck} styrka: {self.styrka} xp :{self.xp} ")



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
diddi = Fiende(" P-diddi" , 5 ,20)
på_körd = Fiende ("Jennifer" , 10 , 70)

fiender = [Numer1opp, shottas, Telefontillmammma, jul, epi, diddi , på_körd]        






def start_meny():
    en_modul.Rubrik()
    while True :
        start_svar = input("""
        Tryck 1 för att Starta Spel 
        Tryck 2 för att se Credits 
        Truck 3 för att Avsluta 
        """)
        try :
            start_svar = int(start_svar)
            break
        except :
            print("något gick fel")
            continue
    if start_svar == 1 :
        karaktar_val()
    elif start_svar == 2:
        en_modul.slow_type("här ska det stå credits och sedan fråga om den vill gå til start meny eller avsluta")
    elif start_svar == 3 :
        en_modul.slow_type("Du hoppade av taket och föll till döds😭😭😭")
        en_modul.konstpaus()
        en_modul.game_over()
    else :
        print ("Ditt tal är inte mellan 1-3")
        start_meny()
    
 
# skriver ut karaktärerna
        


def karaktar_val():
    en_modul.Karaktar_val_text()
    while True :
        for c in charachters :
            c.print_character()
            
    
        val = input()
        
        break
    
    
    if val == "Nazrull":
        return val
    elif val == "Liza":
        return val
    elif val == "Jeffi":
        return val
    else :
        print("hej")
        
def fight(spelare, fiende):
    while karaktar.hp >= 0 and fiende.hp >=0 :
        print("ludde lock in !!!!")
        break
        
 
start_meny()

# slayer.inventory.append()
# print(slayer.hp)
# slayer.hp -= 0.1
# print(slayer.hp)

