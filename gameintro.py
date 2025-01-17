import random as rand
import sys
import time

#olika fräg koder som kan fräga texten efter prompten
FAT_STYLE = "\033[1m"
RESET = "\033[0m"
WHITE = "\033[47m"
YELLOW = "\033[33m"

def print_with_delay(text,delay):
    """Skriver text med en kort fördröjning mellan varje tecken för dramatisk effekt."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Ny rad efter texten

def clear_screen():
    sys.stdout.write("\033c")
    sys.stdout.flush()

def blink_logo(text, delay=0.8, times=5):
    for _ in range (times):
        print(text, end='', flush=True)
        time.sleep(delay)

        clear_screen()
        time.sleep(delay)
        

def game_intro():
    """Prints the backstory for the game."""
    intro_text = """
    *** Project Helios ***

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
    print_with_delay(intro_text,0.05)

# Kör backstory-funktionen när spelet startar
#game_intro()


def game_outro_escape(): 
    escaped_text_2 = rf"""{YELLOW}

 __  __     ______     __  __        ______     ______     ______     ______     ______   ______     _____    
/\ \_\ \   /\  __ \   /\ \/\ \      /\  ___\   /\  ___\   /\  ___\   /\  __ \   /\  == \ /\  ___\   /\  __-.  
\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \  __\   \ \___  \  \ \ \____  \ \  __ \  \ \  _-/ \ \  __\   \ \ \/\ \ 
 \/\_____\  \ \_____\  \ \_____\     \ \_____\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\    \ \_____\  \ \____- 
  \/_____/   \/_____/   \/_____/      \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/     \/_____/   \/____/ {RESET}"""
    outro_text_2= """                                                                      
\nYou espace the Entitys grasp, the horrors of Project Helios still remain. 
"Schwarzenegger, you've saved your self. But left the world in terrible danger..."
As rescue arrives, the Entity grows stronger, destroying everything in its path including the rescue team.
The Entity manages to escape causing a worldwide zombie apocalypse since YOU did not kill it!

The world is not safe... 

Game Complete (bad ending)!
Thank you for playing."""
    blink_logo(escaped_text_2, delay = 0.5, times = 3)
    print(escaped_text_2)
    print_with_delay(outro_text_2,0.05)
    exit()

def game_outro_kill(): 
    victory_text_1 = rf"""{YELLOW}

 __   __   __     ______     ______   ______     ______     __  __  
/\ \ / /  /\ \   /\  ___\   /\__  _\ /\  __ \   /\  == \   /\ \_\ \   
\ \ \' /  \ \ \  \ \ \____  \/_/\ \/ \ \ \/\ \  \ \  __<   \ \____ \  
 \ \__|    \ \_\  \ \_____\    \ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
  \/_/      \/_/   \/_____/     \/_/   \/_____/   \/_/ /_/   \/_____/ {RESET}"""
    outro_text_1= """                                                                      
\nYou escape the ruins, the horrors of Project Helios silenced. As rescue arrives, the President's message rings clear:
"Schwarzenegger, you saved us all. Rest now, but stay ready."

The world is safe... For now.

Game Complete (good ending)!
Thank you for playing."""
    blink_logo(victory_text_1, delay = 0.5, times = 3)
    print(victory_text_1)
    print_with_delay(outro_text_1,0.05)
    exit()
 

 