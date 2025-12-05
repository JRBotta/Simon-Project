from gpiozero import Button, LED
from time import sleep
import random
import RPi.GPIO as GPIO

round = []
greenLight = LED(2)

redLight = LED(3)



arr = [greenLight,redLight]

def cb(e):
round.append(e)
print('test')

for light in arr:
light.off()


for light in arr:
light.on()

sleep(1)

for light in arr:
light.off()
sleep(1)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(14, GPIO.RISING, callback=lambda x: cb(greenLight), bouncetime=200)
GPIO.add_event_detect(15, GPIO.RISING, callback=lambda x: cb(redLight), bouncetime=200)





seq = []
playing = True
score = 0
while playing:
seq.append(random.choice(arr))

print(seq)
for light in seq:
light.on()
sleep(1)
light.off()
sleep(1)
while True:
if(len(round)>len(seq)):
playing = False
break
if(round == seq):
score += 1
round = []
sleep(1)
break

print("Score: " + str(score))
