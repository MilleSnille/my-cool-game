import random as rand

FAT_STYLE = "\033[1m"
RESET = "\033[0m"
VIT = "\033[47m"

def print_with_delay(text):
    """Skriver text med en kort fördröjning mellan varje tecken för dramatisk effekt."""
    import sys
    import time
    for char in text:
        delay = rand.uniform(0.01, 0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Ny rad efter texten


def game_intro():
    """Prints the backstory for the game."""
    intro_text = """
    *** President Evil ***

    The year is 1984. Science has reached unimaginable heights, but with great knowledge comes great risk.
    You're name is Arnold Schwarzenegger, a new employee at a top secret russian facility where 
    they are working on a dangerous experiment: "Project Helios". The purpose? 
    Harnessing quantum energy to create a virus that could take down the Americans.
    
    But suddenly something goes terribly wrong.
    An unexpected energy surplus sends the laboratory into chaos. Light flashes. A high frequency 
    tone cuts through the air. Machines explode. Colleagues scream – and then... silence.

    When you wake up, the laboratory has changed. The walls pulsate faintly, as if the building 
    given life. The scientist seem to have taken on a form that dosn't look human. And worst of all:
    you are alone.

    The air is stagnant and every attempt to contact the outside world is met with static silence. It is 
    now up to you to find a way out - before what's awakened in the laboratory finds you.

    Good luck, Schwarzenegger. Earth is counting on you to save it... 
    """
    print_with_delay(intro_text)

# Kör backstory-funktionen när spelet startar
#game_intro()

def game_outro():
    outro_text = """Victory Achieved
You escape the ruins, the horrors of Project Helios silenced. As rescue arrives, the President's message rings clear:
"Schwarzenegger, you saved us all. Rest now, but stay ready."

The world is safe... For now.

Game Complete!
Thank you for playing."""
    print_with_delay(outro_text)
 