![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/MPMBTHOT.png?raw=true)

# MicroPython micro:bit
# Talking Heads Or Tails
This is a FUN talking Heads Or Tails game for the official BBC micro:bit V2 where you play with get to play with our little talking friend!

## Schematic
![image](https://github.com/mytechnotalent/MicroPython-micro-bit_Talking_Heads_Or_Tails/blob/main/schematic.png?raw=true)

## Parts
[micro:bit](COMING NOVEMBER 2020)

## STEP 1: Download & Install Mu IDE
[Instructions](https://www.linkedin.com/pulse/python-kids-part-2-install-mu-ide-kevin-thomas/)
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
    say('Let us play heads or tails.')
    say('Press button A if you want to guess heads.')
    say('Press button B if you want to guess tails.')
    while True:
        if button_a.is_pressed():
            if result == 0:
                display.show(Image.HAPPY)
                say('Hooray!')
                say('You guessed heads and you were right.')
                say('You won!')
                say('Press the RESET button to play again!')
                break
            else:
                display.show(Image.SAD)
                say('Sorry!')
                say('When I flipped my little coin it came up tails.')
                say('Better luck next time!')
                say('Press the RESET button to play again!')
                break
        if button_b.is_pressed():
            if result == 1:
                display.show(Image.HAPPY)
                say('Hooray!')
                say('You guessed tails and you were right.')
                say('You won!')
                say('Press the RESET button to play again!')
                break
            else:
                display.show(Image.SAD)
                say('Sorry!')
                say('When I flipped my little coin it came up heads.')
                say('Better luck next time!')
                say('Press the RESET button to play again!')
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
