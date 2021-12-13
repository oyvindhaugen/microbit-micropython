from microbit import *
import radio
import random
radio.config(group=2)
radio.on()
def LEDlights():
    while True:
        messageReceived = radio.receive()
        if button_a.was_pressed():
            pin0.write_digital(1)
            sleep(50)
            pin0.write_digital(0)
            sleep(50)
            pin0.write_digital(1)
            sleep(50)
            pin0.write_digital(0)
            sleep(50)
            pin0.write_digital(1)
            sleep(50)
            pin0.write_digital(0)
            sleep(50)
            radio.send('pp')
        elif messageReceived:
            pin0.write_digital(1)
            sleep(50)
            pin0.write_digital(0)
            sleep(50)
            pin0.write_digital(1)
            sleep(50)
            radio.send('pp')
            pin0.write_digital(0)
            sleep(50)
            pin0.write_digital(1)
            sleep(50)
            pin0.write_digital(0)
            sleep(50)
LEDlights()



def godzilla():
    def optionsForServo():
        while True:
            number = random.randint(1,5)
            time = random.randint(1,3000)
            if number == 1:
                pin0.write_analog(1)
                sleep(time)
                pin0.write_analog(90)
                sleep(time)
                pin0.write_analog(1)
                radio.send('pp')
            elif number == 2:
                pin0.write_analog(73)
                sleep(time)
                pin0.write_analog(42)
                sleep(time)
                pin0.write_analog(73)
                sleep(time)
                pin0.write_analog(1)
                radio.send('pp')
            elif number == 3:
                pin0.write_analog(80)
                sleep(time)
                pin0.write_analog(40)
                sleep(time)
                pin0.write_analog(80)
                sleep(time)
                pin0.write_analog(1)
                radio.send('pp')
            elif number == 4:
                pin0.write_analog(120)
                sleep(time)
                pin0.write_analog(75)
                sleep(time)
                pin0.write_analog(1)
                radio.send('pp')
            else:
                sleep(200)
                pin0.write_analog(35)
                sleep(time)
                pin0.write_analog(90)
                sleep(time)
                pin0.write_analog(1)
                radio.send('pp')
    def servo():
        while True:
            messageReceived = radio.receive('pp')
            if messageReceived:
                optionsForServo()
    servo()
godzilla()
