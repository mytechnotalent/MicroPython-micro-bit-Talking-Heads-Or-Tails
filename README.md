![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/MicroPython-micro-bit%20Talking%20Heads%20Or%20Tails.png?raw=true)

# MicroPython micro:bit
# Talking Heads Or Tails
This is a FUN talking Heads Or Tails game for the official BBC micro:bit V2 where you play with get to play with our little talking friend!

## Schematic
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/schematic.png?raw=true)

## Parts
[micro:bit](https://microbit.org/buy/?location=US&version=microbitV2)

## STEP 1: Download & Install Mu IDE
[Instructions](https://www.linkedin.com/pulse/python-kids-part-2-install-mu-ide-kevin-thomas/)<br>
*** PLEASE MAKE SURE YOU INSTALL THE ALPHA VERSION OF MU IN ORDER FOR THE MICRO:BIT V2 TO WORK PROPERLY ***

## STEP 2: Plug micro:bit Into Computer
***PLUG IN USB CABLE TO COMPUTER AND DEVICE***

## STEP 3: Open Mu IDE

## STEP 4: Type Code Into Mu IDE
```python
import gc
import time
from random import randint

from microbit import display, Image, button_a, button_b
from speech import say

# Customize bot speaking speed
SPEED = 95


def play_game():
    """Play game 
    
    Play game is a function that allows you
    play a fun heads or tails game as when you
    plug in the micro:bit the game will begin
    and our little friend will start speaking and
    after you play the game if you would like to
    play again press the reset button
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
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


play_game()
```

## STEP 5: Click Save - main.py

## STEP 6: Click Flash

## STEP 7: Click Reset Button (Back Side micro:bit)

## STEP 8: Play Heads Or Tails!
When you plug in the micro:bit our little friend will introduce the game and give you some basic instructions.  If you would like to guess heads press the A button and if you would like to guess tails press the B button.  Once you play and you would like to play again simply press the reset button on the back of the micro:bit.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
