import guizero
import gpiozero as gpio
from time import sleep


def check_active_column(column, number):
    if column.is_active:
        print("col {}\tis live".format(number))
    else:
        print("col {}\tis dead".format(number))


def check_active_row(row, number):
    if row.is_active:
        print("row {}\tis live".format(number))
    else:
        print("row {}\tis dead".format(number))


def initialize_seven_segment(waffle):
    for i in range(1, 12):
        if i == 1 or i == 2 or i == 5 or i == 6 or i == 9 or i == 10:
            for j in range(1, 7):
                if j == 1 or j == 2 or j == 4 or j == 5:
                    waffle.set_pixel(i, j, "black")


columns = [gpio.InputDevice(2, pull_up=True),
           gpio.InputDevice(3, pull_up=True),
           gpio.InputDevice(4),
           gpio.InputDevice(5),
           gpio.InputDevice(6),
           gpio.InputDevice(7),
           gpio.InputDevice(8),
           gpio.InputDevice(9),
           gpio.InputDevice(10),
           gpio.InputDevice(11),
           gpio.InputDevice(12),
           gpio.InputDevice(13)]

rows = [gpio.InputDevice(14),
        gpio.InputDevice(15),
        gpio.InputDevice(16),
        gpio.InputDevice(17),
        gpio.InputDevice(18),
        gpio.InputDevice(19),
        gpio.InputDevice(20)]

while True:
    for i in range(0, len(columns)):
        check_active_column(columns[i], i)
    print("")
    for i in range(0, len(rows)):
        check_active_row(rows[i], i)

    sleep(2)
    print("\nnew cycle:")
