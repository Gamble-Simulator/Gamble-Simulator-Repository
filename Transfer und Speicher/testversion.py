import tkinter as tk

def on_click(event):
    # Klickbereich definieren (x1, y1, x2, y2)
    if 50 < event.x < 200 and 50 < event.y < 150:
        print("Button-Bereich geklickt!")
    else:
        print("Außerhalb geklickt")

root = tk.Tk()
root.title("Canvas Test")

# Bild laden
img = tk.PhotoImage(file="bild.png")

# Canvas erstellen (Größe = Bildgröße)
canvas = tk.Canvas(root, width=img.width(), height=img.height())
canvas.pack()

# Bild anzeigen
canvas.create_image(0, 0, anchor="nw", image=img)

# Unsichtbaren klickbaren Bereich definieren
# (zum Debuggen kannst du outline="red" setzen)
click_area = canvas.create_rectangle(
    50, 50, 200, 150,
    outline="", fill=""
)

# Klick-Event nur für diesen Bereich
canvas.tag_bind(click_area, "<Button-1>", on_click)

root.mainloop()

