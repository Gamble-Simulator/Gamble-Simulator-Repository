import tkinter as tk
import random
from PIL import Image, ImageTk

fenster = tk.Tk()
fenster.title("Slot Machine")
fenster.resizable(False, False)

'''
'''

anzWalzen = 5
anzZeilen = 3

x = 1500
y = 500+anzZeilen * 125

points = [

(x/2 - 1.5*(x/10), y/2 - (15*y/64)),
(x/2 - 0.5*(x/10), y/2 - (15*y/64)),
(x/2 + 0.5*(x/10), y/2 - (15*y/64)),
(x/2 + 1.5*(x/10), y/2 - (15*y/64)),
(x/2 + 2.5*(x/10), y/2 - (15*y/64)),

(x/2 - 1.5*(x/10), y/2 - (5.5*y/64)),
(x/2 - 0.5*(x/10), y/2 - (5.5*y/64)),
(x/2 + 0.5*(x/10), y/2 - (5.5*y/64)),
(x/2 + 1.5*(x/10), y/2 - (5.5*y/64)),
(x/2 + 2.5*(x/10), y/2 - (5.5*y/64)),

(x/2 - 1.5*(x/10), y/2 + (4*y/64)),
(x/2 - 0.5*(x/10), y/2 + (4*y/64)),
(x/2 + 0.5*(x/10), y/2 + (4*y/64)),
(x/2 + 1.5*(x/10), y/2 + (4*y/64)),
(x/2 + 2.5*(x/10), y/2 + (4*y/64))

]

WIDTH, HEIGHT = x, y
canvas = tk.Canvas(fenster, width=WIDTH, height=HEIGHT, bg="#222")
canvas.pack()

symbole = [(0, "Apfel"), (1, "Amogus"), (2, "Sieben"), (3, "Kleeblatt"), (4, "Kirsche"), (5, "Flamme"), (6, "Melone")]
wahrscheinlichkeiten = [194, 119, 76, 149, 194, 194, 119] #gesamt = 1000
anzSymbole = 7
walzen = ["", "", "", "", ""]
maxSchritte = 5
drehen = True
drehSchritte = 0

TagBild = "bild"

#Hintergrundbild einfügen
bg_img = Image.open(r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Hintergrund.png').resize((WIDTH, HEIGHT))
bg_tk = ImageTk.PhotoImage(bg_img)
bg_id = canvas.create_image(0, 0, image=bg_tk, anchor="nw")
            
class Walze():
    def __init__(self, spalte = 1, felder = None):
        """
        Konstruktoraufruf der Klasse  Walze
        """
        self.__spalte = spalte
        self.__felder = [] if felder is None else felder

    def felderAdden(self):
        """fügt 3 Felder zur Walze hinzu"""
        self.__felder.append(Feld(1, random.choices(symbole, weights=wahrscheinlichkeiten)[0], 1, points[self.__spalte-1]))
        self.__felder.append(Feld(2, random.choices(symbole, weights=wahrscheinlichkeiten)[0], 1, points[self.__spalte+4]))
        self.__felder.append(Feld(3, random.choices(symbole, weights=wahrscheinlichkeiten)[0], 1, points[self.__spalte+9]))
    
    def malen(self):
        """malt alle Felder in Walze"""
        #canvas.delete("walzen")
        feldBild = []
        for feld in self.__felder:
            feldBild.append(feld.malen())
        return feldBild

    def bilderAendern(self):
        """malt alle Felder in Walze"""
        #canvas.delete("walzen")
        for feld in self.__felder:
            feld.bildaendern()
    
    def animation():
        """führt Animation beim Spin durch"""
        global drehen, drehSchritte,zeit,message_id
        drehen = True
        zeit = 100
        if drehen == True:
            canvas.coords(hitboxDrehButton, 2*WIDTH, 2*HEIGHT, 2*WIDTH, 2*HEIGHT)   #Hitbox verschwinden lassen
            canvas.itemconfig(message_id, text="Dreht...")
        if drehSchritte < maxSchritte:
            #canvas.delete()
            aendern()
            drehSchritte += 1
            fenster.after(zeit, Walze.animation)
        else:
            drehen = False
            canvas.coords(hitboxDrehButton, 15*WIDTH // 64 + WIDTH//175,     #obere linke x
            5*HEIGHT//6 + HEIGHT//45,       #obere linke y
            15*WIDTH // 64 + WIDTH//175 + WIDTH//15, #untere rechte x
            5*HEIGHT//6 + HEIGHT//45 + HEIGHT//10)

            pruefer = GewinnPruefer(all)
            if pruefer.pruefen1() > 0:
                if pruefer.pruefen1() == 1:
                    canvas.itemconfig(message_id, text="Kleiner Gewinn!")
                elif pruefer.pruefen1() <= 3:
                    canvas.itemconfig(message_id, text="Mittlerer Gewinn!")
                elif pruefer.pruefen1() <= 9:
                    canvas.itemconfig(message_id, text="GROßER GEWINN!")
                elif pruefer.pruefen1() == 10:
                    canvas.itemconfig(message_id, text="JACKPOT!!!")
            else:
                canvas.itemconfig(message_id, text="Verloren")
            drehSchritte = 0

    def getFelder(self, index = -1):
        if index > -1:
            return self.__felder[index]
        else:
            return self.__felder

class Feld(Walze):
    def __init__(self, zeile = 1, symbol = tuple, wahrscheinlichkeit = int, koordinaten = tuple):
        """
        Konstruktoraufruf der Klasse Feld, abgeleitet von Walze
        """
        self.__zeile = zeile
        self.__koordinaten = koordinaten            #vielleicht weglassen(durch zeile)
        self.__symbol = symbol
        self.__wahrscheinlichkeit = wahrscheinlichkeit
        self.bild_id = None
        super().__init__(spalte = 1)

    def malen(self):
        """malt das Feld"""
        name, farbe = self.__symbol
        x, y = self.__koordinaten

        img = Image.open(Symbol.zuordnung(name)).resize((80, 80), Image.Resampling.NEAREST)  #Verknüpft Symbol mit Bildern
        self.tk_image = ImageTk.PhotoImage(img)
        
        self.bild_id = canvas.create_image(x-40, y-40, image = self.tk_image, anchor="nw")
        #rechteck = canvas.create_rectangle(x-40, y-40, x+40, y+40, fill=farbe, tags="walzen")

    def bildaendern(self):
        """ändert das Bild des Feldes"""
        name, farbe = self.__symbol
        x, y = self.__koordinaten

        img = Image.open(Symbol.zuordnung(name)).resize((80, 80), Image.Resampling.NEAREST)  #Verknüpft Symbol mit Bildern
        self.tk_image = ImageTk.PhotoImage(img)

        canvas.itemconfig(self.bild_id, image = self.tk_image)
        #rechteck = canvas.create_rectangle(x-40, y-40, x+40, y+40, fill=farbe, tags="walzen")

    def neues_symbol(self):
        self.__symbol = random.choices(symbole, weights=wahrscheinlichkeiten)[0]

    def getSymbol(self):
        return self.__symbol[0]   # nur die Zahl

class Symbol():
    def __init__(self, symbol = "", wahrscheinlichkeit = int):
        self.__symbol = symbol
        self.__wahrscheinlichkeit = wahrscheinlichkeit

    def zuordnung(i):
        """ordnet einer Zahl ein Bild zu"""
        if i == 0:
            return r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Apfel.png'
        elif i == 1:
            return r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Amogus.png'
        elif i == 2:
            return r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Sieben.png'
        elif i == 3:
            return r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Kleeblatt.png'
        elif i == 4:
            return r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Kirschen.png'
        elif i == 5:
            return r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Flamme.png'
        elif i == 6:
            return r'i:\Unterricht\Neuer Ordner\Projekt Gamblesimulator\Melone.png'
        
class GewinnPruefer:
    def __init__(self, walzen):
        """Konstruktoraufruf der Klasse GewinnPruefer"""
        self.__walzen = walzen

    def matrix(self):
        matrix = []
        for z in range(3):
            row = []
            for w in self.__walzen:
                row.append(w.getFelder(z).getSymbol())
            matrix.append(row)
        return matrix

    def pruefe_horizontal1(self):
        for row in self.matrix():
            count = 1
            for i in range(1, len(row)):
                if row[i] == row[i-1]:
                    count += 1
                    if count >= 3:
                        return True
                else:
                    count = 1
    
        return False
    
    def pruefe_horizontal2(self):
        for row in self.matrix():
            count = 1
            for i in range(1, len(row)):
                if row[i] == row[i-1]:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 1
    
        return False
    
    def pruefe_horizontal3(self):
        for row in self.matrix():
            count = 1
            for i in range(1, len(row)):
                if row[i] == row[i-1]:
                    count += 1
                    if count >= 5:
                        return True
                else:
                    count = 1
    
        return False
    
    def pruefe_vertikal(self):
        for walze in self.__walzen:
            f0 = walze.getFelder(0).getSymbol()
            f1 = walze.getFelder(1).getSymbol()
            f2 = walze.getFelder(2).getSymbol()

            if f0 == f1 == f2:
                return True

        return False

    def pruefe_diagonal(self):
        m = self.matrix()

        # ↘ Richtung
        for start in range(3):  # 0,1,2
            if m[0][start] == m[1][start+1] == m[2][start+2]:
                return True

        # ↗ Richtung
        for start in range(3):  # 0,1,2
            if m[2][start] == m[1][start+1] == m[0][start+2]:
                return True

        return False

    def pruefe_v_form(self):
        m = self.matrix()
        # V (Spitze unten)
        if m[0][0] == m[1][1] == m[2][2] == m[1][3] == m[0][4]:
            return True
        # ∧ (Spitze oben)
        if m[2][0] == m[1][1] == m[0][2] == m[1][3] == m[2][4]:
            return True
        return False
    
    def pruefe_jackpot(self):
        m = self.matrix()
        
        erstes = m[0][0]

        for row in m:
            for feld in row:
                if feld != erstes:
                    return False
                
        return True

    def pruefen1(self):
        if self.pruefe_jackpot():
            return 10
        if self.pruefe_v_form():
            return 5
        if self.pruefe_horizontal3():
            return 4
        if self.pruefe_horizontal2():
            return 3  
        if self.pruefe_horizontal1():
            return 1
        if self.pruefe_vertikal():
            return 1
        if self.pruefe_diagonal():
            return 1     
        return -1
        

#erstellt Label
message_id = canvas.create_text(
    5*WIDTH // 8 - WIDTH // 200, (5/6)*HEIGHT + HEIGHT//15,
    text="SPIN drücken",
    fill="#FFB000",     #oder "white",
    font=("Arial", 20, "bold")
)

all = []
#erstellt Walzen und malt sie 
def malens():
    global all
    for i in range(anzWalzen):
        walz = Walze(i+1)
        walz.felderAdden()
        walz.malen()
        all.append(walz)

#ändert Walzen und malt sie 
def aendern():
    for walze in all:
        for feld in walze.getFelder():
            feld.neues_symbol()
            feld.bildaendern()

#Button erstellen
hitboxDrehButton = canvas.create_rectangle(
    15*WIDTH // 64 + WIDTH//175,     #obere linke x
    5*HEIGHT//6 + HEIGHT//45,       #obere linke y
    15*WIDTH // 64 + WIDTH//175 + WIDTH//15, #untere rechte x
    5*HEIGHT//6 + HEIGHT//45 + HEIGHT//10,  #untere rechte y
    fill="",
    outline=""
)

canvas.tag_bind(hitboxDrehButton, "<Button-1>", lambda e: Walze.animation())

malens()

#Start
fenster.mainloop()