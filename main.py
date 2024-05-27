from gpiozero import Button, LEDBoard
from signal import pause
from time import sleep

leds = LEDBoard(2, 3, 4, 17, 27, 22, 10, 9) 
# 1, 2, 4, 8, 16, 32, 64, 128, 256

number = 0

def Increase():
    global number
    number += 1
    print("Increasing " + str(number))
    UpdateLights()

def Decrease():
    global number
    number -= 1
    print("Decreasing " + str(number))
    UpdateLights()

def Cycle():
    for number in range(1, 257):
        for led in leds:
            led.value = number % 2
            number = int(number/2)
        sleep(0.05)

    for i in range(4):
        leds.on()
        sleep(0.25)
        leds.off()
        sleep(0.25)

incButton = Button(6)
decButton = Button(13)

incButton.when_pressed = Increase
decButton.when_pressed = Decrease

cycleButton = Button(5)
cycleButton.when_pressed = Cycle

def UpdateLights():
    temp = number

    for led in leds:
        led.value = temp % 2
        temp = int(temp/2)

pause()

