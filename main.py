import gc
import time
from random import randint

from microbit import display, Image, button_a, button_b
from speech import say

SPEED = 95

result = randint(0, 1)

display.show(Image.MEH)
say('Let us play heads or tails.', speed=SPEED)
time.sleep(1)
say('Press button Ayy if you want to guess heads.', speed=SPEED)
time.sleep(1)
say('Press button B if you want to guess tails.', speed=SPEED)

while True:
    if button_a.is_pressed():
        if result == 0:
            display.show(Image.HAPPY)
            say('Hooray!', speed=SPEED)
            say('You guessed heads and you were right.', speed=SPEED)
            say('You won!', speed=SPEED)
            say('Press the RESET button to play again!', speed=SPEED)
            break
        else:
            display.show(Image.SAD)
            say('Sorry!', speed=SPEED)
            say('When I flipped my little coin it came up tails.', speed=SPEED)
            say('Better luck next time!', speed=SPEED)
            say('Press the RESET button to play again!', speed=SPEED)
            break
    if button_b.is_pressed():
        if result == 1:
            display.show(Image.HAPPY)
            say('Hooray!', speed=SPEED)
            say('You guessed tails and you were right.', speed=SPEED)
            say('You won!', speed=SPEED)
            say('Press the RESET button to play again!', speed=SPEED)
            break
        else:
            display.show(Image.SAD)
            say('Sorry!', speed=SPEED)
            say('When I flipped my little coin it came up heads.', speed=SPEED)
            say('Better luck next time!', speed=SPEED)
            say('Press the RESET button to play again!', speed=SPEED)
            break
