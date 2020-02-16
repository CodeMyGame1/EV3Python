#!/usr/bin/env pybricks-micropython

#imports time
import time

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your programs here
def beepMotor():
    #Makes a beep sound
    brick.sound.beep()
    #Initializes a motor at port B
    test_motor = Motor(Port.B)
    test_motor.run_target(500, 90)
    brick.sound.beep(1000, 500)
def buttons():
    while not any(brick.buttons()):
        wait(10)
    if Button.LEFT in brick.buttons():
        print("The left button is pressed.")
def light():
    brick.light(Color.RED)
    print("Red")
    time.sleep(10)
    brick.light(None)
def sound():
    brick.sound.beep(1500, 1000)
    brick.sound.beeps(5)
    brick.sound.file(SoundFile.HELLO)
def display():
    brick.display.clear()
    brick.display.text("Hello", (60, 50))
    time.sleep(1)
    brick.display.text("World")
    time.sleep(1)
    brick.display.clear()
    brick.display.image("ProfilePhotoACSEF.jpg")
    time.sleep(10)
def battery():
    print("Current =", str(brick.battery.current()) + " mA")
    print("Voltage =", str(brick.battery.voltage()) + " mV")
def motors():
    example_motor = Motor(Port.A, Direction.CLOCKWISE)
    example_motor.run_target
#Run those programs here
battery()