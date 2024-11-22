import classes
import minimeny 


def get_user_input():
    while True:
        menytal = input("*** President Evil ***\n[1] START\n[2] INTRO\n[3] EXIT\n") 
        
        if menytal == "1": 
            print("PICK A CHARACTER")
            print("[1] Janitor \n[2] Chemist") 
            classes.my_character()
            minimeny.menu_choice() 
            
            
        elif menytal == "2":  
            import gameintro
            print(gameintro)

        elif menytal == "3": 
            print("Program Terminated")
            break

        else: 
            print("Choose a number; 1, 2 or 3!") 


get_user_input() 

