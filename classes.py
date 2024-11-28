import random as rand

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


# i1 = item("Sword", 30)
# i2 = item("Acid bottle", 20)
# i3 = item("Mop", 10)
# i4 = item("Glass Shard", 15)
# i5 = item("Energy Sword", 40)
# i6 = item("Fire Flower", 45)


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

# my_character()
# print_stats() 


class enemy: 
    def __init__(self, name, HP, STR):
        self.name = name
        self.HP = HP
        self.STR = STR

e1 = enemy("ZOMBIE", 100, 5)
e2 = enemy("SCOBBY DOO", 55, 20)
e3 = enemy("DIDDY", 150, 10)
selected_enemy = None

def rand_enemy ():
    global selected_enemy
    while True:
        list = [1,2,3]
           
        if list == 1:
            print(e1.name)
        elif list == 2:
            print(e2.name)
        elif list == 3:
            print(e3.name)