import classes
import minimeny 
import gameintro

RED = "\033[31m"
ORANGE = "\033[38;2;255;165;0m"
RESET = "\033[0m"

#skapar en rå sträng som ignorerar "\"" som escape-sekvenser
project_helios_text= rf"""{ORANGE}
 ______   ______     ______       __     ______     ______     ______               __  __     ______     __         __     ______     ______    
/\  == \ /\  == \   /\  __ \     /\ \   /\  ___\   /\  ___\   /\__  _\             /\ \_\ \   /\  ___\   /\ \       /\ \   /\  __ \   /\  ___\   
\ \  _-/ \ \  __<   \ \ \/\ \   _\_\ \  \ \  __\   \ \ \____  \/_/\ \/             \ \  __ \  \ \  __\   \ \ \____  \ \ \  \ \ \/\ \  \ \___  \  
 \ \_\    \ \_\ \_\  \ \_____\ /\_____\  \ \_____\  \ \_____\    \ \_\              \ \_\ \_\  \ \_____\  \ \_____\  \ \_\  \ \_____\  \/\_____\ 
  \/_/     \/_/ /_/   \/_____/ \/_____/   \/_____/   \/_____/     \/_/               \/_/\/_/   \/_____/   \/_____/   \/_/   \/_____/   \/_____/ 
                                                                                                                                                 {RESET}"""


def get_user_input():
    while True:
        menytal = input(f"{project_helios_text}\n[1] START\n[2] INTRO\n[3] EXIT\n") 
        
        if menytal == "1": 
            print("PICK A CHARACTER")
            print("[1] Janitor \n[2] Chemist") 
            classes.my_character()
            minimeny.menu_choice() 
        elif menytal == "2":  
            #print(gameintro)
            gameintro.game_intro()
        elif menytal == "3": 
            print("Program Terminated")
            exit()
        else: 
            print("Choose a number; 1, 2 or 3!") 


get_user_input() 


