import tkinter as tk
import random

fenster = tk.Tk()
fenster.title("Slot Machine")
fenster.resizable(False, False)

'''Klassenidee:
? Slot Maschine (benutzer?, Quests (rekursiv, nur Zahlen ändern sich), Zinsen, Wahrscheinlichkeitsshop, ...)
jedes Feld als eine Klasse (Koordinaten, Wahrscheinlichkeit, Wert, PNG, nebenliegende Felder)
jede Walze als Klasse mit Feld
Animationsidee: Walzen zusammenhängend machen, Walzen drehen lassen mit gleicher Animation aber unterschiedlichem Ergebnis
oder verschiebe PNG pro Sekunde ein Pixel down, bis Grenze(oben/unten), danach ZufallsPNG für bestimmte Dauer(Animation),
danach erscheinen ausgewählte PNGs
vielleicht einzelne Walzenanimationen tauschen (1-5)
+ walzen/letzte Symbole bevor nach unten verschwinden lassen
+ Endanimation'''

anzWalzen = 5
anzZeilen = 3

x = 1000
y = 500+anzZeilen * 125

points = [

(x/2 - 2*(0.5*x/5), y/2 - (0.5*y/3)),
(x/2 - 1*(0.5*x/5), y/2 - (0.5*y/3)),
(x/2,               y/2 - (0.5*y/3)),
(x/2 + 1*(0.5*x/5), y/2 - (0.5*y/3)),
(x/2 + 2*(0.5*x/5), y/2 - (0.5*y/3)),

(x/2 - 2*(0.5*x/5), y/2),
(x/2 - 1*(0.5*x/5), y/2),
(x/2,               y/2),
(x/2 + 1*(0.5*x/5), y/2),
(x/2 + 2*(0.5*x/5), y/2),

(x/2 - 2*(0.5*x/5), y/2 + (0.5*y/3)),
(x/2 - 1*(0.5*x/5), y/2 + (0.5*y/3)),
(x/2,               y/2 + (0.5*y/3)),
(x/2 + 1*(0.5*x/5), y/2 + (0.5*y/3)),
(x/2 + 2*(0.5*x/5), y/2 + (0.5*y/3))

]

WIDTH, HEIGHT = x, y
canvas = tk.Canvas(fenster, width=WIDTH, height=HEIGHT, bg="#222")
canvas.pack()

symbole = [("a", "red"), ("b", "green"), ("c", "blue"), ("d", "yellow"), ("e", "white")]
walzen = ["", "", "", "", ""]
maxSchritte = 10
drehen = True
drehSchritte = 0

class Walze():
    def __init__(self, spalte = 1, felder = []):
        """
        Konstruktoraufruf der Klasse  Walze
        """
        self.__spalte = spalte
        self.__felder = felder

    def felderAdden(self):
        """fügt 3 Felder zur Walze hinzu"""
        self.__felder.append(Feld(1, symbole[random.randint(0, anzWalzen-1)], 1, points[self.__spalte-1]))
        self.__felder.append(Feld(1, symbole[random.randint(0, anzWalzen-1)], 1, points[self.__spalte+4]))
        self.__felder.append(Feld(1, symbole[random.randint(0, anzWalzen-1)], 1, points[self.__spalte+9]))
    
    def malen(self):
        """malt alle Felder in Walze"""
        canvas.delete("walzen")
        for feld in self.__felder:
            feld.malen()
    
    def animation():
        global drehen, drehSchritte,zeit,message_id
        drehen = True
        zeit = 100
        if drehen == True:
            drehButton.place(x=WIDTH // 2 - 50, y=2*HEIGHT, width=100, height=40)
            canvas.itemconfig(message_id, text="Dreht...")
        if drehSchritte < maxSchritte:
            malens()
            drehSchritte += 1
            fenster.after(zeit, Walze.animation)
        else:
            drehen = False
            drehButton.place(x=WIDTH // 2 - 63, y=HEIGHT//3 + anzZeilen * 125, width=126, height=50)
            canvas.itemconfig(message_id, text="DREHEN drücken")
            drehSchritte = 0

class Feld(Walze):
    def __init__(self, zeile = 1, symbol = tuple, wahrscheinlichkeit = int, koordinaten = tuple):
        """
        Konstruktoraufruf der Klasse Feld, abgeleitet von Walze
        """
        self.__zeile = zeile
        self.__koordinaten = koordinaten            #vielleicht weglassen(durch zeile)
        self.__symbol = symbol
        self.__wahrscheinlichkeit = wahrscheinlichkeit
        super().__init__(spalte = 1)

    def malen(self):
        """malt das Feld"""
        name, farbe = self.__symbol
        x, y = self.__koordinaten
        rechteck = canvas.create_rectangle(x-40, y-40, x+40, y+40, fill=farbe, tags="walzen")

class Symbol():
    def __init__(self, symbol = "", wahrscheinlichkeit = int):
        self.__symbol = symbol
        self.__wahrscheinlichkeit = wahrscheinlichkeit

"""

def randomWalzen():
    """ #Setzt random Werte für die einzelnen Walzen 
"""
    global walzen
    for i in range(anzWalzen):
        walzen[i] = symbole[random.randint(0, anzWalzen-1)] #Walzen werden random Werte zugeordnet


def walzenMalen(walzen, zeile):
    """# Malt die vorbereiteten Walzen erstmalig
"""
    #walzen = drehVorbereitung()
    x = 67
    y = 100 + zeile * 125
    for i in range(anzWalzen):
        name, farbe = walzen[i]
        rechteck = canvas.create_rectangle(x, y, x+75, y+100, fill=farbe, tags="walzen")
        fenster.update()
        x += 100
        
def walzenKombi():
    if drehen:
        for i in range(anzZeilen):
            randomWalzen()
            walzenMalen(walzen, i)     #Hier Werte auswerten oder Feldkoordinaten implementieren
    else:
        return

def drehAnimation():
    global drehen, drehSchritte
    drehen = True
    if drehSchritte < maxSchritte:
        walzenKombi()
        drehSchritte += 1
        fenster.after(100, drehAnimation)
    else:
        drehen = False
        drehSchritte = 0
        
def Start():
    for j in range(anzZeilen):
        x = 67
        y = 100 + j * 125
        for i in range(anzWalzen):
            name, farbe = "a", "red"
            rechteck = canvas.create_rectangle(x, y, x+75, y+100, fill=farbe, tags="walzen")
            fenster.update()
            x += 100
    
Start()

drehButton = tk.Button(text = "Drehen", font=("Arial", 16, "bold"), command = drehAnimation)
drehButton.place(x=600 // 2 - 50, y=100 + anzZeilen * 125, width=100, height=40)

"""
#erstellt Label
message_id = canvas.create_text(
    WIDTH // 2, (1/6)*HEIGHT,
    text="DREHEN drücken",
    fill="white",
    font=("Arial", 20, "bold")
)

#erstellt Walzen und malt sie 
def malens():
    walzens = []
    for i in range(anzWalzen):
        walzens.append(Walze(i))
        walzens[i].felderAdden()
        walzens[i].malen()

#Button erstellen
drehButton = tk.Button(text = "Drehen", font=("Arial", 20, "bold"), command = Walze.animation)
drehButton.place(x=WIDTH // 2 - 63, y=HEIGHT//3 + anzZeilen * 125, width=126, height=50)

malens()
"""
felder = []
felder.append(Feld(1, symbole[2], 1, points[1]))
felder[0].malen()
feld2 = Feld(1, symbole[3], 1, points[2])
feld2.malen()
"""
#Start
fenster.mainloop()