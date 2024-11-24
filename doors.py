import classes 
import random 

door_alternatives = ["Trap", "Monster", "Chest" ] 
# chosen_alternative = random.choice(door_alternatives) 



def door_choice(): 
    global door_alternatives
    door = (input("You have come to 3 doors. You will now either get to open a chest, fight a monster or encounter a trap!\nChoose one of the 3 doors.\n[1]LEFT\n[2]FORWARD\n[3]RIGHT\n"))
    if door == "1" or door == "left" or door == "Left":  
        chosen_alternative = random.choice(door_alternatives) 
        print("You have now encountered a",chosen_alternative)
    elif door == "2" or door == "forward" or door == "Forward": 
        chosen_alternative = random.choice(door_alternatives) 
        print("You have now encountered a",chosen_alternative)
    elif door == "3" or door == "right" or door == "Right": 
        chosen_alternative = random.choice(door_alternatives) 
        print("You have now encountered a",chosen_alternative)
    else: 
        print("Invalid choice. You have to choose either 1,2 or 3!")

    if chosen_alternative == "Trap": 
        # Slumpa fram en skada mellan 5 och 20 HP
        damage = random.randint(5, 20)
        classes.selected_player.take_damage(damage)
    elif chosen_alternative == "Monster": 
        print("Prepare for battle!")
    elif chosen_alternative == "Chest": 
        print("Congratulations!") 
    



# def door_encounter():#skapar en funktion som bestämmer vad som händer när man möter trap, monster eller chest

 