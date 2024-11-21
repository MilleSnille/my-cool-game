
class player: 
    def __init__(self, name, HP, STR):
        self.name = name
        self.HP = HP
        self.STR = STR

p1 = player("Janitor", 150, 15)
p2 = player("Chemist", 100, 25) 


while True:
    try:
        karaktär = int(input("--->")) 
        if karaktär == 1: 
            print("*", p1.name, "*", "\nHP:", p1.HP, "\nSTRENGTH:", p1.STR)
            break
        elif karaktär == 2:  
            print("*", p2.name, "*", "\nHP:", p2.HP, "\nSTRENGTH:", p2.STR)
            break
        else: 
            print("Invalid choice! Please choose 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).") 
    
 
