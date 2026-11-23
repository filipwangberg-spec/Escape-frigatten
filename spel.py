
import en_modul
import random as randint


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
        en_modul.slow_type(f"{self.namn} hp: {self.hp} luck: {self.luck} styrka: {self.styrka} xp :{self.xp} ")

    def showinventory():
        for i in self.inventory:
            print(i)


def xp_ett (Karaktar):
    Karaktar.xp += 1
    print("du fick ett xp !!!")


    



Lucky = Karaktar("Nazrull", 100 , 0.7 , 10 , 0)
Surviver = Karaktar("Liza", 120 , 0.5 , 10 , 0)
Damage = Karaktar ("Jeffi", 100 , 0.5 , 14 , 0)
#lista med karaktärerna för att kunna printa ut dem i starten
charachters = [Lucky, Surviver, Damage]
charachter_vald = []



class Vapen :
    def __init__(self,namn,multiplyer) :
        self.namn = namn
        self.multiplyer = multiplyer

def kista():
    print("Du hittade en kista")
    foremal = vapen(randint(0,6))

kniv = Vapen("Köks kniv", 1.2 )
tofla = Vapen("Rutten tofla", 1.05)
ak = Vapen("Ak47", 40)

vapen = [kniv,kniv,tofla,tofla,tofla,ak]


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
            if c == Lucky :
                print("Tryck 1 för att välja Nazrull")
            elif c == Surviver :
                print("Tryck 2 för att välja Liza")
            elif c == Damage :
                print("Tryck 3 för att välja Jeffi")
            
        try:
            val = int(input())
            break
        except:
            print("skriv bara med bokstäver")
    
    
    if val == 1:
        charachter_vald.append(Lucky)
        print("Du har valt Nazrull")
        en_modul.konstpaus

        intro()
    elif val == 2:
        charachter_vald.append(Surviver)
        print("Du har valt Liza")
        en_modul.konstpaus
        intro()
    elif val == 3:
        charachter_vald.append(Damage)
        print("Du har valt Jeffi")
        en_modul.konstpaus

        intro()
    else :
        print(f"ditt tal är utanför 1-3{karaktar_val}")

def intro():
    en_modul.slow_type("Du har vaknat upp på taket av faliga hustak 3 i Fregatten, du minns inte hur du hamnade här")

        
def fight(spelare, fiende):
    print(" Ludde fråga martin")
        
 
start_meny()




    

# slayer.inventory.append()
# print(slayer.hp)
# slayer.hp -= 0.1
# print(slayer.hp)

