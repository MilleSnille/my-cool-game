
class player: 
    def __init__(self, name, HP, STR, LVL):
        self.name = name
        self.HP = HP
        self.STR = STR
        self.inventory = []
        self.LVL = LVL

     
    def take_damage(self, damage):
        self.HP -= damage
        if self.HP < 0:  # Säkerställer att HP inte går under 0
            self.HP = 0
            self.death() #<-- här aktiveras funktionen "death" i funktionen "take damage". 
        print(f"{self.name} took {damage} damage! Current HP: {self.HP}") 
    
    def death(self): 
        print("YOU DIED! GAME OVER...") 
        exit()   #<-- denna funktion gör så att när HP blir 0>= så kommer spelet att avslutas genom "exit()"

    def game_ending(self):
        if self.LVL == 10:
            import gameintro
            gameintro.game_outro()
            exit()
        

    
    
class item:
    def __init__ (self, name, STR, HP):  
        self.name = name
        self.STR = STR
        self.HP = HP
    
    def __str__(self): 
        item_print = f"""
**{self.name}**
STR : {self.STR}
HP : {self.HP}"""
        return item_print


p1 = player("Janitor", 150, 15, 1)
p2 = player("Chemist", 100, 25 ,1) 
selected_player = None

def print_stats():
    if selected_player: 
        print("**",selected_player.name,"**\n""HP:", selected_player.HP,"\nSTR:" ,selected_player.STR, "\nLVL:", selected_player.LVL) 
    else: 
        print("No player selected.")


def my_character():
    global selected_player
    while True:
        try: 
            character = int(input("---> "))
            if character == 1: 
                print("\n*", p1.name, "*", "\nHP:", p1.HP, "\nSTRENGTH:", p1.STR, "\nLVL:", p1.LVL)
                selected_player = p1
                break
            elif character == 2:  
                print("\n*", p2.name, "*", "\nHP:", p2.HP, "\nSTRENGTH:", p2.STR, "\nLVL:", p2.LVL)
                selected_player = p2
                break
            else: 
                print("Invalid choice! Please choose; 1 or 2\n")
        except ValueError:
            print("Invalid input! Please choose; 1 or 2\n") 


class enemy: 
    def __init__(self, name, HP, STR):
        self.name = name
        self.HP = HP
        self.STR = STR

    def __str__(self): 
        enemy_print = f"""
**{self.name}**
STR : {self.STR}
HP : {self.HP}"""
        return enemy_print
