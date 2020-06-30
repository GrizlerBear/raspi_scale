import guizero
from time import sleep

def set_seven_segment(waffle):
    for i in range(1, 12):
        if i == 1 or i == 2 or i == 5 or i == 6 or i == 9 or i == 10:
            for j in range(1, 7):
                if j == 1 or j == 2 or j == 4 or j == 5:
                    waffle.set_pixel(i, j, "black")

def counter():
    for pixel in range(0, waffle.height - 1):
        if waffle.get_pixel(0, pixel) == "white":
            waffle.set_pixel(0, pixel, "gray")
            waffle.set_pixel(0, pixel + 1, "white")
            return
        elif waffle.get_pixel(0, waffle.height-1) == "white":
            waffle.set_pixel(0, waffle.height-1, "gray")
            return
    waffle.set_pixel(0,0, "white")
    return
   
app = guizero.App(title="GUI app", width=350, height=225, layout="grid")

columns = range(1, 13)
rows = range(1, 8)
for i in columns:
    box = guizero.Box(app, width=20, height=20, align="bottom", grid=[i,0], border=True)
    column = guizero.Text(box, text=i, align="bottom")

for i in rows:
    box = guizero.Box(app, width=20, height=20, align="right", grid=[0,i], border=True)
    row = guizero.Text(box, text=i, align="bottom")

waffle = guizero.Waffle(app, align="top", grid=[1,1,12,7], width=12, height=7, pad=5, color="gray")
set_seven_segment(waffle)

waffle.repeat(1000, counter)

app.display()

