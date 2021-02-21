![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/MicroPython-micro-bit%20Talking%20Heads%20Or%20Tails.png?raw=true)

# MicroPython micro:bit
# Talking Heads Or Tails
This is a FUN talking Heads Or Tails game for the official BBC micro:bit V2 where you play with get to play with our little talking friend!

## Schematic
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/schematic.png?raw=true)

## Parts
[micro:bit](https://microbit.org/buy/?location=US&version=microbitV2)

## STEP 1: Navigate To The FREE micro:bit Python Web Editor
[micro:bit Python Web Editor](https://python.microbit.org/v/beta)<br><br>
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%201.png?raw=true)

## STEP 2: Plug micro:bit V2 Into Computer
***PLUG IN USB CABLE TO COMPUTER AND DEVICE**

## STEP 3: Click CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%203.png?raw=true)

## STEP 4: Click "BBC micro:bit CMSIS-DAP" & CONNECT
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%204.png?raw=true)

## STEP 5: Highlight Sample Code - Select All
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%205.png?raw=true)

## STEP 6: Click Backspace On Keyboard To Delete Sample Code
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%206.png?raw=true)

## STEP 7: Copy Talking Heads Or Tails Python Code Template Into Python Web Editor
# CODE
```python
import gc
import time
from random import randint

from microbit import display, Image, button_a, button_b
from speech import say

# Customize bot speaking speed
SPEED = 95


gc.collect()
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
```

## STEP 8: Rename Script Name To talking_headsortails

## STEP 9: Click Save
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%209.png?raw=true)

## STEP 10: Click Download Python Script
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%2010.png?raw=true)

## STEP 11: Click Flash
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/STEP%2011.png?raw=true)

## STEP 12: Play Heads Or Tails!
When you plug in the micro:bit our little friend will introduce the game and give you some basic instructions.  If you would like to guess heads press the A button and if you would like to guess tails press the B button.  Once you play and you would like to play again simply press the reset button on the back of the micro:bit.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
