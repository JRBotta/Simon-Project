# Simon-Project

In this repository, I'm going to be going over my process of trying to replicate the game Simon on a Raspberry Pi.  The result was mostly successful, with a little bit of jank.

The version I ended up with only uses two lights and buttons instead of the traditional four in order to keep things simple.  Just like the acutal game, one light will flash.  If the user presses the correct button, the same light will flash and then the sequence will be extended, either by the same light or by the other light at random.  This will continue until the user is incorrect and a score will be printed on the screen.

The required components are:

1. Raspberry Pi
2. Breadboard
3. Four male-to-male jumper cables
4. Five male-to-female jumper cables
5. Two LED lights of different colors
6. Two push button switches


Schematic:

<img width="793" height="534" alt="Screenshot 2025-12-04 183842" src="https://github.com/user-attachments/assets/c65db36e-df22-44ee-9dfc-f4f8532d4399" />

Step 1:

Begin by making sure the Raspberry Pi is powered off.  Connect the LEDs using resistors between them and the GPIO pins (the green to pin 2 and the red to pin 3) on the Raspberry Pi

Step 2:

We'll be using a centralized ground, so connect the LEDs to the same column on the breadboard as the diagram shows

Step 3:

Connect the buttons to the breadboard and wire those to GPIO pins (the top to pin 14 and the bottom to pin 16 if you want them to match up with the LEDs) as well

Step 4:

Connect those to the same ground column as the LEDs

Step 5:

Turn on the Raspberry Pi and run the code using the command 'run simon.py'

Completed product:

![20251202_120151](https://github.com/user-attachments/assets/82639fe6-0044-4e0e-bf9c-709b9c4620a9)
