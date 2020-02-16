#!/usr/bin/env pybricks-micropython

#I had to use separate functions because apparently, when you set up a Python with EV3 Project, only main.py will be run when you download the code to your EV3 Brick. So, if you would like to run a program from a function here, enter the function name at the bottom under the designated comment. Thanks!

#This line imports time (get the rhyme?)
import time

#This is just a bunch of stuff that you have to import in order to make sure that the code works
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# These are the programs I have created. If you would like to add more, feel free to download this and add on! I may also be accepting pull requests.
def beepMotor():
    #Makes a beep sound
    brick.sound.beep()
    #Initializes a motor at port B
    test_motor = Motor(Port.B)
    #Run the motor up to 500 degrees per second. To a target angle of 90 degrees
    test_motor.run_target(500, 90)
    #Makes a beep sound, but with two new customizable parameters: the frequency and duration. 1000 is the frequency (default unit is hertz), and 500 ms is the duration (default unit is milliseconds)
    brick.sound.beep(1000, 500)
def buttons():
    #Waits for a button to be pressed
    while not any(brick.buttons()):
        #I have no idea what this does
        wait(10)
    #Once the while loop exits because a button was pressed, the if statement checks to see if that button was the left button
    if Button.LEFT in brick.buttons():
        print("The left button is pressed.")
def light():
    #Changes the status light to red
    brick.light(Color.RED)
    #Prints red to the CONSOLE (on wherever you are coding), NOT the brick
    print("Red")
    #Sleeps for 10 seconds, which allows you to see the red status light for 10 seconds
    time.sleep(10)
    #Turns off the status light
    brick.light(None)
def sound():
    brick.sound.beep(1500, 1000)
    #Plays simple beeps by taking the number of beeps as a parameter
    brick.sound.beeps(5)
    #Plays a pre-downloaded Lego Sound File called "HELLO" (i guess...?)
    brick.sound.file(SoundFile.HELLO)
def display():
    #Clears the display on the brick
    brick.display.clear()
    #Displays, "Hello", at the center of the screen
    brick.display.text("Hello", (60, 50))
    #Waits for 1 second, so that you can see the word, "Hello", being displayed
    time.sleep(1)
    #Displays, "World", just below, "Hello"
    brick.display.text("World")
    time.sleep(1)
    brick.display.clear()
    #Displays a built-in image of two eyes looking up
    brick.display.image("ImageFile.UP")
    time.sleep(10)
def battery():
    #Prints the current of the brick battery to the console
    print("Current =", str(brick.battery.current()) + " mA")
    #Prints the voltage of the brick battery to the console
    print("Voltage =", str(brick.battery.voltage()) + " mV")
def motors():
    #Still working on this
    example_motor = Motor(Port.A, Direction.CLOCKWISE)
    example_motor.run_target
#Want to run one of the above programs, or one you created yourself? Just call the function here!
