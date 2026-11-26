
import en_modul
import random as randint


#karaktärer


class Karaktar :
    def __init__(self,namn,hp, luck, styrka , xp ):
        self.namn = namn
        self.hp = hp
        self.luck = luck
        self.styrka = styrka
        self.xp = xp
        self.inventory = []
        self.hand = []
        
    def print_character(self):
        print(f"{self.namn} hp: {self.hp} luck: {self.luck} styrka: {self.styrka} xp :{self.xp} ")

    def show_inventory(self) -> Vapen:
        for vapen in self.inventory:
            print(f"du har {vapen.namn} sho")
    
    def Lägg_till_i_inventory(self,sak):
        self.inventory.append(sak)

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
    def __init__(self,namn,multiplyer,användningar) :
        self.namn = namn
        self.multiplyer = multiplyer
        self.användningar = användningar

kniv = Vapen("Köks kniv", 1.2 ,0 )
tofla = Vapen("Rutten tofla", 1.05,0)
#ska bara kunna användas 5 gånger
ak = Vapen("Ak47", 2.5,0)
# ska bara kunna användas 1 gång
granat = Vapen("Granat",5,0)

def kista():
    print("Du hittade en kista välj ett vapen")
    import random
    slumpat_vapen = random.choice(vapen_kista)
    print(f"Du har hittat en {slumpat_vapen.namn}")
    while True :
        try:
            ta_upp_vapen = int(input(f"""
            Vill du ta upp {slumpat_vapen.namn} som ökar din Damage med {slumpat_vapen.multiplyer} och lägga de i ditt inventory ? 
            tryck 1 för ja, tryck 2 för nej :"""))
        except :
            print("Du kan bara skriva med siffror")
            continue
        #Ja
        if ta_upp_vapen == 1 :
            charachter_vald[0].Lägg_till_i_inventory(slumpat_vapen)
            vapen_kista.remove(slumpat_vapen)
            en_modul.konstpaus()
            Karaktar.show_inventory
            break
        #Nej
        elif ta_upp_vapen == 2:
            print ("du lämnade vapent i kistan ? 🤌🤌")
            en_modul.konstpaus()
            Karaktar.show_inventory
            break
        else :
            print("ditt tal är utanför 1-2")
            continue




vapen_kista = [kniv,kniv,tofla,tofla,tofla,ak]


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
på_körd = Fiende ("Jennifer(fiat 500)" , 10 , 70)

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
        except :
            print("något gick fel")
            continue
        if start_svar == 1 :
            karaktar_val()
            en_modul.konstpaus
        elif start_svar == 2:
            en_modul.slow_type("här ska det stå credits och sedan fråga om den vill gå til start meny eller avsluta")
            en_modul.konstpaus
        elif start_svar == 3 :
            en_modul.slow_type("Du hoppade av taket och föll till döds😭😭😭")
            en_modul.konstpaus()
            en_modul.game_over()
            break
        else :
            print ("Ditt tal är inte mellan 1-3")
            continue
    
 
# skriver ut karaktärerna
        


def karaktar_val():
    en_modul.Karaktar_val_text()
    while True :
        for c in charachters :
            c.print_character()
           
        try:
            val = int(input("""
            Tryck 1 för att välja Nazrull 
            
            Tryck 2 för att välja Liza
            
            Tryck 3 För att välja Jeffi"""))
            
        except:
            print("skriv bara med bokstäver")
    
        
        if val == 1:
            charachter_vald.append(Lucky)
            print("Du har valt Nazrull")
            en_modul.konstpaus
            intro()
            break
        elif val == 2:
            charachter_vald.append(Surviver)
            print("Du har valt Liza")
            en_modul.konstpaus
            intro()
            break
            intro()
        elif val == 3:
            charachter_vald.append(Damage)
            print("Du har valt Jeffi")
            en_modul.konstpaus
            intro()
            break
        else :
            print("ditt tal är utanför 1-3")
            continue

  

def intro():
    en_modul.slow_type("Du har vaknat upp på taket av faliga hustak 3 i Fregatten, du minns inte hur du hamnade här")
    en_modul.konstpaus
    kista()
    door()


def door():
    print("Du uppnår tre dörrar")
    while True :
        try :
            val = input("Vilken dörr väljer du? Dörr 1, 2 eller 3?")
            print(f"Du går in i dörr nummer {val}.")
        except :
            print("hej")




def get_current_charachter() -> Karaktar:
    return charachter_vald[0]

def get_random_fiende ()-> Fiende :
    import random
    slumpad_fiende = random.choice(fiender)
    fiender.remove(slumpad_fiende)
    return slumpad_fiende



def fight():
    current_character = get_current_charachter()
    current_fiende = get_random_fiende()
    
    en_modul.slow_type(f"Du stöter på {current_fiende.namn}")
    
    while current_character.hp > 0 and current_fiende.hp > 0:
       
        print(f"{current_fiende.namn} har {current_character.hp} hp")
        print(f"Du har {current_character.hp} hp")
        print(f"Tryck 1 för att attackera och 2 för att fly.")
        try:
            val = int(input("Vad vill du göra"))
        except :
            print("Du kan bara svara med 1 eller 2")
        if val == 1:
            skada = current_character.styrka
            
            if len(current_character.hand) > 0:
                vapen = current_character.hand[0]
                skada = int(skada * vapen.multiplyer)
                print(f"Du attackerade med {vapen.namn}")

            
                
                
            
    

        
        
            
            
        
        
 
start_meny()




    

# slayer.inventory.append()
# print(slayer.hp)
# slayer.hp -= 0.1
# print(slayer.hp)









