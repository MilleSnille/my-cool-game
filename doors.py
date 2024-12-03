import classes 
import random as rand
import inventory

RED = "\033[31m"
dark_red = "\033[38;2;139;0;0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
# Olika färger man kan ha på text i terminalen

door_alternatives = ["infested room", "burning room", "Monster", "Chest" ] 
# chosen_alternative = random.choice(door_alternatives) 

def get_random_enemy(): 
    global random_enemy
    enemy_types = [
        classes.enemy("ZOMBIE", 100, 5),
        classes.enemy("SCOBBY DOO", 55, 20),
        classes.enemy("DIDDY", 125, 50),
        classes.enemy("The Terminator", 150, 75),
        classes.enemy("Shrek", 120, 10),
        classes.enemy("Leon S Kennedy", 75, 20),
        classes.enemy("Boris Golitsyn", 60, 40)
    ]
    random_enemy = rand.choice(enemy_types)
    return random_enemy
    

def enemy_encounter(): 
    global random_enemy
    print(f"You encounter {get_random_enemy()}")
    while True:
        flee_or_fight = input(f"\nYou've still got time to Flee! But remember, if you don't fight {random_enemy.name}, you might not get out of here!\n[1]Fight\n[2]Flee\n[3]Statistics\n") 
        if flee_or_fight == "1" or flee_or_fight == "Fight" or flee_or_fight == "fight": 
            enemy_hp_damage = rand.randint(10,20)
            if classes.selected_player.HP / random_enemy.STR < random_enemy.HP / classes.selected_player.STR: 
                # classes.p1.HP -= enemy_hp_damage
                # classes.p2.HP -= enemy_hp_damage
                classes.selected_player.take_damage(enemy_hp_damage)
                print(f"{dark_red}{random_enemy.name}{RESET} was stronger than you! You lost {enemy_hp_damage} HP.")
                break
            elif classes.selected_player.HP / random_enemy.STR > random_enemy.HP / classes.selected_player.STR: 
                print(f"Congratulations! You were stronger than {dark_red}{random_enemy.name}{RESET}")
                classes.p1.LVL += 1
                classes.p2.LVL += 1
                print(f"You defeated the monster and leveled up to {BLUE}LVL:{classes.selected_player.LVL}{RESET}")
                classes.selected_player.game_ending()
                break
            else: 
                print(f"You and {dark_red}{random_enemy.name}{RESET} were evenly strong. {dark_red}{random_enemy.name}{RESET} fled!")
                break
        elif flee_or_fight == "2" or flee_or_fight =="Flee" or flee_or_fight == "flee":  
            print(f"You escaped {dark_red}{random_enemy.name}{RESET}")
            break
        elif flee_or_fight == "3" or flee_or_fight == "stats" or flee_or_fight == "s":
            classes.print_stats()
            continue
            



def get_random_chest_item():
    global random_item
    chest_items = [
        classes.item("Dissecting Set", 10, 0),
        classes.item("Acid bottle", 15, 0),
        classes.item("Mop", 8, 0),
        classes.item("Glass Shard", 12, 0),
        classes.item("Energy Sword", 25, 0),
        classes.item("Flame Thrower", 20, 0),
        classes.item("Estus Flask", 0, 100)
    ]
    random_item = rand.choice(chest_items)
    return random_item

def add_random_item(): 
    global random_item
    while True:
        if len(inventory.inv) >= 5: 
            print("\nYour inventory is full. You must replace an item to equip this one.")
            print("Current inventory:")
                
            index = 1 
            for item in inventory.inv:
                print(f"{index}. {YELLOW}{item.name}{RESET} ({RED}STR: {item.STR}{RESET}, {GREEN}HP:{item.HP}{RESET})")
                index += 1
            print(f"\nThe chest contains: {random_item.name} (STR: {random_item.STR}, HP: {random_item.HP} ")

            while True: 
                choice = input("\nDo you want to replace an item? Enter the number of the item you want to replace, or press [N] to leave the item.")
                if choice.lower() == "n": 
                    print("\nYou left the item behind.")
                    return
                else: 
                    choice = int(choice) -1 
                    if choice >= 0 and choice <= 5: 
                        print(f"You replaced {inventory.inv[choice].name} with {random_item.name}")
                        inventory.inv[choice] = random_item
                        classes.p1.STR += random_item.STR
                        classes.p2.STR += random_item.STR
                        classes.p1.HP += random_item.HP
                        classes.p2.HP += random_item.HP
                        return
                    else: 
                        print("Invalid input. You have to choose a number within your inventory, [1] - [5]")
                        continue
        else: 
            C = input("Do you want to take this item with you? [Y] or [N]\n")
            if C == "Y" or C == "y": 
                print("You picked up the item!")
                inventory.inv.append(random_item)
                classes.p1.STR += random_item.STR
                classes.p2.STR += random_item.STR
                classes.p1.HP += random_item.HP
                classes.p2.HP += random_item.HP
                # classes.p1.LVL += 1 
                # classes.p2.LVL += 1
                print(f"You leveled up to{BLUE} LVL:{classes.selected_player.LVL}{RESET}")
                classes.selected_player.game_ending() 
                break
            elif C == "N" or C == "n": 
                print("You leave the item behind and journey forth")
                break
            else: 
                print("You have to pick; [Y] or [N]!") 
                continue


def door_choice(): 
    global door_alternatives
    chosen_alternative = None #<-- detta ger den ett standardvärde vilket gör så att även om spelaren skriver in annat än "1, 2 eller 3" så kraschar inte spelet.

    door = (input("\nYou have come 3 doors. You may proceed into the unknown... \n(Enter one of the 3 doors.)\n[1]LEFT\n[2]FORWARD\n[3]RIGHT\n"))
    if door == "1" or door == "left" or door == "Left":  
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    elif door == "2" or door == "forward" or door == "Forward": 
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    elif door == "3" or door == "right" or door == "Right": 
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    else: 
        print("There are only three doors, choose either [1], [2] or [3]!")

    if chosen_alternative == "burning room": 
        # Slumpa fram en skada mellan 5 och 15 HP
        damage = rand.randint(4, 15)
        classes.selected_player.take_damage(damage)
    elif chosen_alternative == "infested room":
        # Slumpa fram mellan 2 och 10 HP, som den andra fällan fast mindre skada
        damage = rand.randint(2, 10)
        classes.selected_player.take_damage(damage)
    elif chosen_alternative == "Monster": 
        print("Try and Survive!")
        enemy_encounter() 
    elif chosen_alternative == "Chest":    
        print("Congratulations!") 
        print(f"It contains a {get_random_chest_item()}") 
        add_random_item()

    # def door_encounter():#skapar en funktion som bestämmer vad som händer när man möter trap, monster eller chest

