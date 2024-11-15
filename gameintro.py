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
    *** Välkommen till Experimentets Fall ***

    Året är 2047. Vetenskapen har nått otänkbara höjder, men med stor kunskap följer stor risk.
    Du är Dr. Alva Nyström, en briljant men djärv forskare som leder ett topphemligt experiment:
    "Projekt Helios". Syftet? Att utnyttja kvantenergi för att skapa en oändlig energikälla.
    
    Men något går fruktansvärt fel.
    Ett oväntat energiöverskott skickar laboratoriet in i kaos. Ljus blixtrar. En hög frekvent 
    ton skär genom luften. Maskiner exploderar. Kollegor skriker – och sedan... tystnad.

    När du vaknar är laboratoriet förändrat. Väggarna pulserar svagt, som om byggnaden 
    fått liv. Experimentutrustningen verkar ha tagit en egen form av medvetande. Och värst av allt:
    du är ensam.

    Dörrarna är låsta. Varje försök att kontakta omvärlden möts av statisk tystnad. Det är 
    nu upp till dig att hitta en väg ut – innan det som väcks i laboratoriet hittar dig.

    Lycka till, Dr. Nyström. Universum kanske inte får en andra chans.
    """
    print_with_delay(intro_text)

# Kör backstory-funktionen när spelet startar
game_intro()
 