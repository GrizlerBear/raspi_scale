from gpiozero import Button, LED
from time import sleep

leds = [LED(2), LED(3), LED(4), LED(5), LED(6), LED(7), LED(8), LED(9), LED(10),
        LED(11), LED(12), LED(13)]
rows = [LED(14), LED(15), LED(16), LED(17), LED(18), LED(19), LED(20)]
    
for i in range(0, len(leds)):
    leds[i].on()
    for j in range(0, len(rows)):
        print("col {}, row {}".format(i, j))
        rows[j].on()
        sleep(.1)
        rows[j].off()
    leds[i].off()
