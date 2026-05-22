
import tkinter as tk
import random 
from PIL import Image, ImageTk
#Muenzsystem und Quest
#Konto
root = tk.Tk()
root.title("Artefakt Shop")
root.geometry("1000x600")
root.config(bg="black")

canvas = tk.Canvas(root, width=1000, height=600, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

Kombination = True
datentabelle = [[],
                [1, 75,   7,  3],
                [2, 200,  14, 6],
                [3, 666,  28, 20],
                [4, 2222, 42, 69],
                [5, 12500,56, 300],
                [6, 33333,140,1000],
                [7, 66666,168,2000]]

#Quest
class Quest():
    def __init__(self, debt = 75, deposited = int, deadline = 1, machinecost = 7, rerollcost = 3, spins = 7, rounds = 3, tickets = int):
        self.__debt = debt
        self.__deposited = deposited
        self.__deadline = deadline 
        self.__machinecost = machinecost
        self.__rerollcost = rerollcost
        self.__spins = spins
        self.__rounds = rounds
        self.__tickets = tickets
    
    def setMachinecost(self):
        """
        Setzt die Kosten für Spins nach jedem Level nach Datentabelle
        """
        self.__machinecost = datentabelle([self.deadline][3])
    
    def setRerollcost(self):
        """
        Setzt die Kosten für Artefakte Reroll nach jedem Level nach Datentabelle
        """
        self.__rerollcost = datentabelle([self.deadline][4])
    
    def setDebt(self):
        """
        Setzt die Schulden nach jedem Level nach Datentabelle
        """
        self.__debt = datentabelle([self.__deadline][2])

    # def setSpins(self):
        """
        Setzt die Spins nach jedem Level auf 7
        """
        #self.__spins = 7
    
    def setRounds(self):
        """
        Setzt die Runde nach jedem Level und erzeugt Button für Spins kaufen
        """
        self.__rounds = 3
        SpinBuyButton = tk.Button(text = '/ Spins + 1 Ticket (-7c)', font=('Arial', 20, 'bold'), command = Quest.BuySpins)
    
    def setDeposited(self):
        """
        - Setzt Eingezahltes und aktualisiert Schulden
        - falls Schulden fertig abgezahlt -> sorgt für Stopp bei 0
        """
        self.__deposited += Konto.__Kontostand
        self.__debt -= Konto.__Kontostand
        if self.__debt < 0:
            Konto.__Kontostand += self.__debt 
            self.__debt = 0
        Konto.setKontostand
    
    def getDeadline(self):
        return self.__deadline
    
    def CheckProgress(self):
        """
        Check den Prorgress nach jedem Spin (debt abgezahl?, spawnt Button für Nächstes Level)
        """
        if self.__debt == 0 and self.__spins == 0 and self.__rounds == 0:
            DeadlineButton = tk.Button(text = 'Nächstes Level', font=('Arial', 20, 'bold'), command = Quest.NextLevel)
        #if self.__spins == 0:
            #self.__rounds -= 1
    
    def BuySpins(self):
        """
        Kaufeh von Spins, Tickets, Aktualisierung von Kontostand
        """
        self.__spins = 7
        self.__tickets = 2
        Konto.__Kontostand -= self.__machinecost
    
    def Einzahlen(self):
        """
        Einzahlen auf Button Click
        """
        self.setDeposited(self)
        self.CheckProgress(self)
    
    def NextLevel(self):
        """
        Nächstes Level auf Button Click
        """
        self.__deadline += 1
        self.setMachinecost(self)
        self.setRerollcost(self)   
        self.setDebt(self)     
        self.__deposited = 0
        #self.setSpins(self)
        self.setRounds(self)
    
    def CheckWL(self):
        """
        Checkt bei Runde 0 ob noch möglich zu gewinnen oder nicht
        """
        if self.__debt > Konto.__Kontostand:
            print("Du hast verloren! (Imagine, so ein Bot)")
        else:
            print("Bezahle deine Schulden und gehe zum nächsten Level du Manyak")

    def NewRound(self):
        """
        Neue Runde + Spawnt SpinBuyButton
        """
        self.__rounds -= 1
        SpinBuyButton = tk.Button(text = '/ Spins + 1 Ticket (-7c)', font=('Arial', 20, 'bold'), command = Quest.BuySpins)
        if self.__round == 0:
            self.CheckWL(self)

class Konto(Quest):
    def __init__(self, Kontostand = 13, GV = int, Einzahlung = int):
        self.__Kontostand = Kontostand
        self.__GV = GV
        self.__Einzahlung = Einzahlung
    
    #def CheckEinzahlung():
        #for i in range(1,7):
            #if Quest.getDeadline() == i:
                #Einzahlung = Quest.getDeadline

    def CheckGV(self):
        """
        Prüft Gewinn / Loose
        """
        if Kombination.check:
            Kontostand =+ Kombination.wert
        elif not(Kombination.check):
            Kontostand =- self.__Einzahlung
    
    def getKontostand(self):
        return self.__Kontostand
    
    def setKontostand(self):
        self.__Kontostand == self.__Kontostand

EinzahlenButton = tk.Button(text = 'Einzahlen', font=('Arial', 20, 'bold'), command = Quest.Einzahlen)

'Nach Abschluss einer Runde werden die Artefakte reloaded und man bekommt Tickets'
'Start Programm: Setter Methoden Aufrufen'
"""
- Button 1: Einzahlen 
- Button 2: Spins Kaufen
- Button 3: Artfakte kaufen
- Button 4: Next Level Button

"""

Artefakte = [['Peperoni', 1 , 'bei Kauf für nächste 7 Spins ist die Wahrscheinlichkeit für die unwahrscheinlichsten Symbole erhöht', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\Peperoni.png"], 
             ['Rakete', 2 , 'Auszahlung/Gewinn für die nächsten 7 Spins verdoppelt', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\Rakete.png"], 
             ['Gefängniszelle', 1 , 'das wahrscheinlichste symbol kommt nicht mehr', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\Gefängnis.png"], 
             ['Krabbenschere', 1, '2 zusätzliche Spins für die Runde', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\Krabbe-1.png.png"], 
             ['Geldschein', 5, 'x zusätzliche Münzen (um Level zu schaffen)', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\Geld.png"], 
             ['Diamant', 3, 'Der Multiplikator für jedes Muster verdreifacht sich', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\diamant.png"], 
             ['Stern', 3, 'ein garantierter Jackpot in der nächsten Spin runde (1x nutzbar)', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\stern.png"], 
             ['Zitrone', 1, ' wenn in der letzten Runde kein einziger Gewinn, dann wird die Auszahlung für die nächste runde verdoppelt', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\zitrone.png"], 
             ['Herz', 2, 'Herz: wenn man kurz davor ist zu verlieren (keine tickets mehr für weitere spins), bekommt man 2 zusätzliche spins (nur 1x nutzbar)', "I:\Schule\LK Info\GambleSimulator\Artefakte\Symbole\herz.png"]] # ['Name', 'Preis', 'Nutzen', 'Bildpfad']
ArtefakteInventory = []
class Artefakten ():
    def __init__(self, Artefakt1 = None, Artefakt2 = None, Artefakt3 = None, TicketKonto = 0, gekauft1 = False, gekauft2 = False, gekauft3 = False, button1 = None, button2 = None, button3 = None):
        self.__Artefakt1 = Artefakt1
        self.__Artefakt2 = Artefakt2
        self.__Artefakt3 = Artefakt3
        self.__TicketKonto = TicketKonto
        self.__gekauft1 = gekauft1
        self.__gekauft2 = gekauft2
        self.__gekauft3 = gekauft3
        self.__button1 = button1
        self.__button2 = button2
        self.__button3 = button3

        self.images = []
    
    def RerollArtefakte(self):
        """
        Setzt Artefakte zufällig neu (ohne gleiche Artefakte asuzuwählen)
        """
        """
        zahl1 = random.randint(0,8)
        zahl2 = random.randint(0,8)
        zahl3 = random.randint(0,8)

        while zahl1 == zahl2 or zahl1 == zahl3 or zahl2 == zahl3:
            zahl2 = random.randint(0,8)
            zahl3 = random.randint(0,8)
        

        self.__Artefakt1 = Artefakte[zahl1]
        self.__Artefakt2 = Artefakte[zahl2]
        self.__Artefakt3 = Artefakte[zahl3]
        """

        zufall = random.sample(Artefakte, 3)

        self.__Artefakt1 = zufall[0]
        self.__Artefakt2 = zufall[1]
        self.__Artefakt3 = zufall[2]

        self.__gekauft1 = False
        self.__gekauft2 = False
        self.__gekauft3 = False

        self.createArtefakte()

    def createArtefakte(self):

        canvas.delete("artefakt")

        artefakte = [self.__Artefakt1, self.__Artefakt2, self.__Artefakt3]

        gekauft_status = [self.__gekauft1, self.__gekauft2, self.__gekauft3]

        self.images.clear()

        x_position = 70

        for index, artefakt in enumerate(artefakte):

            name = artefakt[0]
            preis = artefakt[1]
            beschreibung = artefakt[2]
            bildpfad = artefakt[3]

            # Bild laden

            img = Image.open(bildpfad)

            img = img.resize((100, 100))

            tk_image = ImageTk.PhotoImage(img)

            self.images.append(tk_image)

            # Hintergrund Box

            canvas.create_rectangle(
                x_position - 20,
                40,
                x_position + 180,
                320,
                fill="#1e1e1e",
                outline="white",
                width=2,
                tags="artefakt"
            )

            # Bild

            canvas.create_image(
                x_position + 40,
                60,
                image=tk_image,
                anchor="nw",
                tags="artefakt"
            )

            # Name

            canvas.create_text(
                x_position + 90,
                180,
                text=name,
                fill="white",
                font=("Arial", 16, "bold"),
                tags="artefakt"
            )

            # Preis

            canvas.create_text(
                x_position + 90,
                210,
                text=f"Preis: {preis}",
                fill="gold",
                font=("Arial", 13, "bold"),
                tags="artefakt"
            )

            # Beschreibung

            canvas.create_text(
                x_position + 90,
                260,
                text=beschreibung,
                fill="white",
                width=170,
                font=("Arial", 10),
                tags="artefakt"
            )

            # Gekauft Anzeige

            if gekauft_status[index]:

                canvas.create_text(
                    x_position + 90,
                    340,
                    text="GEKAUFT",
                    fill="lime",
                    font=("Arial", 14, "bold"),
                    tags="artefakt"
                )

            x_position += 300

        # Ticketanzeige

        canvas.create_text(
            850,
            40,
            text=f"Tickets: {self.__TicketKonto}",
            fill="lime",
            font=("Arial", 18, "bold"),
            tags="artefakt"
        )

        self.updateButtons()

    def updateButtons(self):

         # Artefakt 1

        if (
            self.__gekauft1
            or len(ArtefakteInventory) >= 3
            or self.__Artefakt1[1] > self.__TicketKonto
        ):

            self.__button1.config(state="disabled")

        else:

            self.__button1.config(state="normal")

        # Artefakt 2

        if (
            self.__gekauft2
            or len(ArtefakteInventory) >= 3
            or self.__Artefakt2[1] > self.__TicketKonto
        ):

            self.__button2.config(state="disabled")

        else:

            self.__button2.config(state="normal")

        # Artefakt 3

        if (
            self.__gekauft3
            or len(ArtefakteInventory) >= 3
            or self.__Artefakt3[1] > self.__TicketKonto
        ):

            self.__button3.config(state="disabled")

        else:

            self.__button3.config(state="normal")

    def BuyArtefakt1(self):
        """
        Kauft das Artefakt an erster Stelle und prüft ob genug Tickets
        """
        """
        if len(ArtefakteInventory) == 3:
            print('Dein Inventar ist voll du Lümmel')
        elif self.__Artefakt1[1] > self.__TicketKonto:
            print('Du hast nicht genug Tickets du KEK')
        else:
            ArtefakteInventory.append(self.__Artefakt1)
            self.__TicketKonto -= self.__Artefakt1[1]
            
        """

        if self.__gekauft1:
            return

        ArtefakteInventory.append(self.__Artefakt1)

        self.__TicketKonto -= self.__Artefakt1[1]

        self.__gekauft1 = True

        self.createArtefakte()
    def BuyArtefakt2(self):
        """
        Kauft das Artefakt an erster Stelle und prüft ob genug Tickets
        """
        """"
        if len(ArtefakteInventory) == 3:
            print('Dein Inventar ist voll du Lümmel')
        elif self.__Artefakt2[1] > self.__TicketKonto:
            print('Du hast nicht genug Tickets du KEK')
        else:
            ArtefakteInventory.append(self.__Artefakt2)
            self.__TicketKonto -= self.__Artefakt2[1]

        def BuyArtefakt1(self):
        """
        if self.__gekauft2:
            return

        ArtefakteInventory.append(self.__Artefakt2)

        self.__TicketKonto -= self.__Artefakt2[1]

        self.__gekauft2 = True

        self.createArtefakte() 

    def BuyArtefakt3(self):
        """
        Kauft das Artefakt an erster Stelle und prüft ob genug Tickets
        """
        """
        if len(ArtefakteInventory) == 3:
            print('Dein Inventar ist voll du Lümmel')
        elif self.__Artefakt3[1] > self.__TicketKonto:
            print('Du hast nicht genug Tickets du KEK')
        else:
            ArtefakteInventory.append(self.__Artefakt3)
            self.__TicketKonto -= self.__Artefakt3[1]
        
        def BuyArtefakt1(self):
        """
        if self.__gekauft3:
            return

        ArtefakteInventory.append(self.__Artefakt3)

        self.__TicketKonto -= self.__Artefakt3[1]

        self.__gekauft3 = True

        self.createArtefakte()
    
shop = Artefakten(TicketKonto=10)

# Buttons

BuyArtefakt1Button = tk.Button(
    root,
    text="Kaufen",
    font=("Arial", 12, "bold"),
    command=shop.BuyArtefakt1
)

BuyArtefakt1Button.place(
    x=110,
    y=370,
    width=120,
    height=40
)


BuyArtefakt2Button = tk.Button(
    root,
    text="Kaufen",
    font=("Arial", 12, "bold"),
    command=shop.BuyArtefakt2
)

BuyArtefakt2Button.place(
    x=410,
    y=370,
    width=120,
    height=40
)


BuyArtefakt3Button = tk.Button(
    root,
    text="Kaufen",
    font=("Arial", 12, "bold"),
    command=shop.BuyArtefakt3
)

BuyArtefakt3Button.place(
    x=710,
    y=370,
    width=120,
    height=40
)

# Buttons im Objekt speichern

shop.__button1 = BuyArtefakt1Button
shop.__button2 = BuyArtefakt2Button
shop.__button3 = BuyArtefakt3Button

shop.RerollArtefakte()

shop.updateButtons()

# Reroll Button

RerollArtefakteButton = tk.Button(
    root,
    text="Reroll",
    font=("Arial", 14, "bold"),
    bg="orange",
    command=shop.RerollArtefakte
)

RerollArtefakteButton.place(
    x=420,
    y=470,
    width=160,
    height=50
)

root.mainloop()
BuyArtefakt1Button = tk.Button(text = 'Artefakt kaufen', font=('Arial', 20, 'bold'), command = Artefakten.BuyArtefakt1)
BuyArtefakt2Button = tk.Button(text = 'Artefakt kaufen', font=('Arial', 20, 'bold'), command = Artefakten.BuyArtefakt2)
BuyArtefakt3Button = tk.Button(text = 'Artefakt kaufen', font=('Arial', 20, 'bold'), command = Artefakten.BuyArtefakt3)
RerollArtefakteButton = tk.Button(text = 'Reroll', font=('Arial', 20, 'bold'), command = Artefakten.RerollArtefakte)
RerollArtefakteButton.place(40,40, width=40, height=40)


'Nächste Aufgabe: Wirkung Artefakte, Artefakte Symbole einfügen mit Erklärungstext'
'+ Kosten, Erklärung für Artefakte anpassen'

'+: Ultra gewinn'
'- direkt verloren'