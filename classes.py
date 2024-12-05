
# Färger som används
RED = "\033[31m"
dark_red = "\033[38;2;139;0;0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
light_blue = "\033[38;2;173;216;230m"
RESET = "\033[0m"
# ascii text som visas när spelaren förlorar
game_over = rf"""{RED}
 ______     ______     __    __     ______        ______     __   __   ______     ______    
/\  ___\   /\  __ \   /\ "-./  \   /\  ___\      /\  __ \   /\ \ / /  /\  ___\   /\  == \   
\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __<   
 \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_/      \/_____/   \/_/ /_/ 
                                                                                            {RESET}"""

# klassen player som bestämmer spelarens egenskaper
class player: 
    def __init__(self, name, HP, STR, LVL):
        self.name = name
        self.HP = HP
        self.STR = STR
        self.LVL = LVL
#self refererar till det aktuella objektet/ playern som skapas eller används, där self gör att man kan ha flera med samma atributer (HP, STR).
     
    def take_damage(self, damage): # funktion som hanterar skadan spelaren tar från traps eller monster. Anropas i filen "doors"
        self.HP -= damage
        if self.HP <= 0:  # Säkerställer att HP inte går under 0
            #self.HP = 0
            self.death() #<-- här aktiveras funktionen "death" i funktionen "take damage". 
        print(f"{self.name} took {damage} damage! Current HP: {self.HP}") 
    
    def death(self):
        print(f"{RED}You died{RESET}\n",game_over) 
        exit()   #<-- denna funktion gör så att spelet avslutas genom "exit()". Anropas i take_damage

    # funktion som avslutar spelet när spelarens level blir 10
    def game_ending(self):
        if self.LVL == 10:
            import gameintro
            gameintro.game_outro()
            exit()

p1 = player("Janitor", 150, 15, 1)
p2 = player("Chemist", 100, 25 ,1) 
selected_player = None
# skapar två olika spelare (spelarklassen) med olika atributer

# skapar en klass för egenskaperna föremålen ska ha
class item:
    def __init__ (self, name, STR, HP):  
        self.name = name
        self.STR = STR
        self.HP = HP
# funktion som används för att returnera en sträng för objektet
    def __str__(self): 
        item_print = f"""
**{YELLOW}{self.name}{RESET}**
{RED}STR: {self.STR}{RESET}
{GREEN}HP: {self.HP}{RESET}"""
        return item_print




def print_stats():
    if selected_player: 
        print(f"**{light_blue}{selected_player.name}{RESET}**\n{GREEN}HP: {selected_player.HP}{RESET}\n{RED}STR: {selected_player.STR}{RESET}\n{BLUE}LVL: {selected_player.LVL}{RESET}")
    else: 
        print("No player selected.")

# funktionen som hanterar vilken spelare som väljs. Anropas i filen "huvudmeny"
def my_character():
    global selected_player
    while True:
        try: 
            character = int(input("---> "))
            if character == 1: 
                print(f"\n*{light_blue}{p1.name}{RESET}*\n{GREEN}HP: {p1.HP}{RESET}\n{RED}STRENGTH: {p1.STR}{RESET}\n{BLUE}LVL: {p1.LVL}{RESET} ")
                selected_player = p1
                break
            elif character == 2:  
                print(f"\n*{light_blue}{p2.name}{RESET}*\n{GREEN}HP: {p2.HP}{RESET}\n{RED}STRENGTH: {p2.STR}{RESET}\n{BLUE}LVL: {p2.LVL}{RESET} ")
                selected_player = p2
                break
            else: 
                print("\nInvalid choice! Please choose; 1 or 2\n")
        except ValueError:
            print("\nInvalid input! Please choose; 1 or 2\n") 
#global gör så att den inte skapar en ny variabel med samma namn utan kan då byta dess värde genom flera funktioner

# klassen för monsters egenskaper
class enemy: 
    def __init__(self, name, HP, STR):
        self.name = name
        self.HP = HP
        self.STR = STR

    def __str__(self): 
        enemy_print = f"""
**{dark_red}{self.name}{RESET}**
{RED}STR : {self.STR}{RESET}
{GREEN}HP : {self.HP}{RESET}"""
        return enemy_print
