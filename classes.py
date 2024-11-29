import random

class player: 
    def __init__(self, name, HP, STR):
        self.name = name
        self.HP = HP
        self.STR = STR
        self.inventory = []

     
    def take_damage(self, damage):
        self.HP -= damage
        if self.HP < 0:  # Säkerställ att HP inte går under 0
            self.HP = 0
        print(f"{self.name} took {damage} damage! Current HP: {self.HP}") 
    
while True:
    def death(self): 
        if self.HP < 0: 
            self.HP = 0 
            print("YOU DIED") 
    break
    
    
    
class item:
    def __init__ (self, name, STR, HP):  
        self.name = name
        self.STR = STR
        self.HP = HP
    
    def __str__(self): 
        item_print = f"""
name : {self.name}
STR : {self.STR}
HP : {self.HP}"""
        return item_print


p1 = player("Janitor", 150, 15)
p2 = player("Chemist", 100, 25) 
selected_player = None

def print_stats():
    if selected_player: 
        print("**",selected_player.name,"**\n""HP:", selected_player.HP,"\nSTR:" ,selected_player.STR) 
    else: 
        print("No player selected.")


def my_character():
    global selected_player
    while True:
        try: 
            character = int(input("---> "))
            if character == 1: 
                print("\n*", p1.name, "*", "\nHP:", p1.HP, "\nSTRENGTH:", p1.STR)
                selected_player = p1
                break
            elif character == 2:  
                print("\n*", p2.name, "*", "\nHP:", p2.HP, "\nSTRENGTH:", p2.STR)
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
name : {self.name}
STR : {self.STR}
HP : {self.HP}"""
        return enemy_print


# def rand_enemy ():
#     global selected_enemy
#     while True:
#         list = [1,2,3]
           
#         if list == 1:
#             print(e1.name)
#         elif list == 2:
#             print(e2.name)
#         elif list == 3:
#             print(e3.name)