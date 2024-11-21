
def print_with_delay(text, delay=0.05):
    """Skriver text med en kort fördröjning mellan varje tecken för dramatisk effekt."""
    import sys
    import time
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Ny rad efter texten


def game_intro():
    """Skriver ut backstory för spelet."""
    intro_text = """
    *** Welcome to President Evil ***

    The year is 2047. Science has reached unimaginable heights, but with great knowledge comes great risk.
    You are Dr. Arnold Schwarzenegger, a brilliant but daring scientist leading a top-secret experiment:
    "Project Helios". The purpose? Harnessing quantum energy to create an infinite energy source.
    
    But something goes terribly wrong.
    An unexpected energy surplus sends the laboratory into chaos. Light flashes. A high frequency 
    tone cuts through the air. Machines explode. Colleagues scream – and then... silence.

    When you wake up, the laboratory has changed. The walls pulsate faintly, as if the building 
    given life. The experimental equipment seems to have taken on a form of consciousness of its own. And worst of all:
    you are alone. 

    The doors are locked. Every attempt to contact the outside world is met with static silence. It is 
    now it's up to you to find a way out - before what's awakened in the laboratory finds you.

    Good luck, Dr. Schwarzenegger. The universe may not get a second chance.
    """
    print_with_delay(intro_text)

# Kör backstory-funktionen när spelet startar
game_intro()
 