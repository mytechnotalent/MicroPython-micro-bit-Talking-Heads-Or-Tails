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
