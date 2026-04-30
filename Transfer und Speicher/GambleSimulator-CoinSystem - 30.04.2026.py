
import tkinter as tk
import random 
from PIL import Image, ImageTk
#Muenzsystem und Quest
#Konto
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

Artefakte = [['Peperoni', 1 , 'bei Kauf für nächste 5 Spins ist die Wahrscheinlichkeit für die unwahrscheinlichsten Symbole erhöht'], 
             ['Rakete', 1 , 'Auszahlung/Gewinn für die nächsten 5 Spins verdoppelt'], 
             ['Gefängniszelle', 1 , 'das wahrscheinlichste symbol kommt nicht mehr'], 
             ['Krabbenschere', 1, '2 zusätzliche Spins für das gesamte game (deshalb teuer!)'], 
             ['Geldschein', 1, 'x zusätzliche Münzen (um Level zu schaffen)'], 
             ['Diamant', 1, 'Der Multiplikator für jedes Muster verdreifacht sich'], 
             ['Stern', 1, 'ein garantierter Jackpot in der nächsten Spin runde (1x nutzbar, teuer)'], 
             ['Zitrone', 1, ' wenn in der letzten Runde kein einziger Gewinn, dann wird die Auszahlung für die nächste runde verdoppelt'], 
             ['Herz', 1, 'Herz: wenn man kurz davor ist zu verlieren (keine tickets mehr für weitere spins), bekommt man 2 zusätzliche spins (nur 1x nutzbar)']] # ['Name', 'Preis', 'Nutzen']
ArtefakteInventory = []
class Artefakten ():
    def __init__(self, Artefakt1, Artefakt2, Artefakt3, TicketKonto = 0):
        self.__Artefakt1 = Artefakt1
        self.__Artefakt2 = Artefakt2
        self.__Artefakt3 = Artefakt3
        self.__TicketKonto = TicketKonto
    
    def RerollArtefakte(self):
        """
        Setzt Artefakte zufällig neu (ohne gleiche Artefakte asuzuwählen)
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

        tk.Canvas.create_text()

    def BuyArtefakt1(self):
        """
        Kauft das Artefakt an erster Stelle und prüft ob genug Tickets
        """
        if len(ArtefakteInventory) == 3:
            print('Dein Inventar ist voll du Lümmel')
        elif self.__Artefakt1[1] > self.__TicketKonto:
            print('Du hast nicht genug Tickets du KEK')
        else:
            ArtefakteInventory.append[self.__Artefakt1]
            self.__TicketKonto -= self.__Artefakt1[1]
            

    def BuyArtefakt2(self):
        """
        Kauft das Artefakt an erster Stelle und prüft ob genug Tickets
        """
        if len(ArtefakteInventory) == 3:
            print('Dein Inventar ist voll du Lümmel')
        elif self.__Artefakt2[1] > self.__TicketKonto:
            print('Du hast nicht genug Tickets du KEK')
        else:
            ArtefakteInventory.append[self.__Artefakt2]
            self.__TicketKonto -= self.__Artefakt2[1]
            

    def BuyArtefakt3(self):
        """
        Kauft das Artefakt an erster Stelle und prüft ob genug Tickets
        """
        if len(ArtefakteInventory) == 3:
            print('Dein Inventar ist voll du Lümmel')
        elif self.__Artefakt2[1] > self.__TicketKonto:
            print('Du hast nicht genug Tickets du KEK')
        else:
            ArtefakteInventory.append[self.__Artefakt2]
            self.__TicketKonto -= self.__Artefakt2[1]
            

BuyArtefakt1Button = tk.Button(text = 'Artefakt kaufen', font=('Arial', 20, 'bold'), command = Artefakten.BuyArtefakt1)
BuyArtefakt2Button = tk.Button(text = 'Artefakt kaufen', font=('Arial', 20, 'bold'), command = Artefakten.BuyArtefakt2)
BuyArtefakt3Button = tk.Button(text = 'Artefakt kaufen', font=('Arial', 20, 'bold'), command = Artefakten.BuyArtefakt3)

'Nächste Aufgabe: Wirkung Artefakte, Artefakte Symbole einfügen mit Erklärungstext'
'+ Kosten, Erklärung für Artefakte anpassen'

'+: Ultra gewinn'
'- direkt verloren'