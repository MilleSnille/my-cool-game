import classes 
import random as rand
import inventory

# skapar textfärger (ANSI)
BLINK = "\033[5m"
RED = "\033[31m"
dark_red = "\033[38;2;139;0;0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
# Olika färger man kan ha på text i terminalen

# alternativ som kan väljas när spelaren öppnar en dörr
door_alternatives = ["infested room", "burning room", "Monster", "Chest" ] 
 

def get_random_enemy(): #returnerar ett slumpmässigt monster från en lista
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
    

def enemy_encounter():  #skapar en funktion som bestämmer vad som händer när man möter ett monster
    global random_enemy
    print(f"You encounter {get_random_enemy()}")
    while True:
        flee_or_fight = input(f"\nYou've still got time to flee! But remember, if you don't fight {random_enemy.name}, you might not get out of here!\n[1]Fight\n[2]Flee\n[3]Statistics\n") 
        if flee_or_fight == "1" or flee_or_fight.lower() == "fight": 
            enemy_damage = rand.randint(10,20)
            # jämför spelarens styrka och HP mot monstrets
            if classes.selected_player.HP / random_enemy.STR < random_enemy.HP / classes.selected_player.STR: 
                print(f"{dark_red}{random_enemy.name}{RESET} was stronger than you! You lost {enemy_damage} HP.")
                classes.selected_player.take_damage(enemy_damage)
                break
            elif classes.selected_player.HP / random_enemy.STR > random_enemy.HP / classes.selected_player.STR: 
                print(f"Congratulations! You were stronger than {dark_red}{random_enemy.name}{RESET}")
                # öka spelarens level vid vinst
                classes.p1.LVL += 1
                classes.p2.LVL += 1
                print(f"You defeated the monster and leveled up to {BLUE}LVL:{classes.selected_player.LVL}{RESET}")
                classes.selected_player.game_ending()
                break
            else: 
                print(f"You and {dark_red}{random_enemy.name}{RESET} were evenly strong. {dark_red}{random_enemy.name}{RESET} fled!")
                break
        elif flee_or_fight == "2" or flee_or_fight.lower() == "flee": 
            # om spelaren flyr avslutas striden
            print(f"You escaped {dark_red}{random_enemy.name}{RESET}")
            break
        elif flee_or_fight == "3" or flee_or_fight.lower() == "stats":
            classes.print_stats()
            continue # startar om loopen för att visa alternativen igen
        else: 
            # felhantering vid fel inmatning
            print("Invalid choice. you have to choose 1, 2 or 3!")
            continue
#continue gör så att den går tillbaks och kör funktionen igen, så man får välja en gång till 
            
 

def get_random_chest_item(): # returnerar ett slumpmässigt item från en lista 
    global random_item
    chest_items = [
        classes.item("Dissecting Set", 10, 0),
        classes.item("Acid bottle", 15, 0),
        classes.item("Mop", 8, 0),
        classes.item("Glass Shard", 12, 0),
        classes.item("Energy Sword", 25, 0),
        classes.item("Flame Thrower", 20, 0),
        classes.item("Estus Flask", 0, 50)
    ]
    #lista med items man kan få ur en chest
    random_item = rand.choice(chest_items)
    return random_item
    #som sedan returneras så att random_item får ett nytt temporärt värde
    #snarlikt till enemy listan

def add_random_item(): # bestämmer vad som händer när spelaren hittar ett föremål i en kista
    global random_item
    while True:
        if random_item.name == "Estus Flask": 
            # vad som specifikt händer om föremålet är Estus Flask
            while True:
                answer = input(f"Do you want to consume the {YELLOW}Estus Flask{RESET}? [Y] to consume or [N] to leave it behind\n")
                if answer.lower() in ["n", "no"]:
                    print("You left the Estus Flask behind...\n")
                    return        # avslutar funktionen 
                elif answer.lower() in ["y", "yes"]:
                    print(f"You slurped up all the {YELLOW}Estus Juice{RESET}, then threw it away!")
                    # lägger till HP till spelaren
                    classes.p1.HP += random_item.HP
                    classes.p2.HP += random_item.HP
                    return  
                else:
                    print("Invalid choice. Please enter [Y] or [N].")
        if len(inventory.inv) >= 5: # kontrollerar om listan inv innehåller 5 items  
            print("\nYour inventory is full. You must replace an item to equip this one.")
            print("Current inventory:")
                
            index = 1 
            for item in inventory.inv:
                print(f"{index}. {YELLOW}{item.name}{RESET} ({RED}STR: {item.STR}{RESET}, {GREEN}HP:{item.HP}{RESET})") 
                index += 1
            print(f"\nThe chest contains: {YELLOW}{random_item.name}{RESET} ({RED}STR: {random_item.STR}{RESET}, {GREEN}HP: {random_item.HP}{RESET}")
            
            while True: 
                # låter spelaren byta ut ett föremål i listan inv
                choice = input("\nDo you want to replace an item? Enter the number of the item you want to replace, or press [N] to leave the item.\n")
                if choice.lower() == "n": 
                    print("You left the item behind.")
                    return
                else: 
                    try: 
                        choice = int(choice) -1 
                        if choice >= 0 and choice <= 5: 
                            print(f"You replaced {YELLOW}{inventory.inv[choice].name}{RESET} with {YELLOW}{random_item.name}{RESET}") 
                            classes.p1.STR -= inventory.inv[choice].STR
                            classes.p2.STR -= inventory.inv[choice].STR # Tar bort STR värden från det borttagna från spelaren 
                            inventory.inv[choice] = random_item # byter ut det item du har valt till chest item
                            classes.p1.STR += random_item.STR
                            classes.p2.STR += random_item.STR
                            #Lägger till den styrka som ett item har till spelarens totala, och funktionen take_damage är här så att man kan dö om man tar bort estus_flask och hamnar under 0 HP .
                            return
                        else: 
                            print("Invalid input. You have to choose a number within your inventory, [1] - [5]")
                            continue
                    except ValueError:
                        print("Invalid input. You have to choose a number within your inventory, [1] - [5]")
        else: 
            #Om inventoryt inte är fullt kan föremålet läggas till direkt
            C = input("Do you want to take this item with you? [Y] or [N]\n")
            if C.lower() == "y": 
                    print("You picked up the item!")
                    inventory.inv.append(random_item)
                    classes.p1.STR += random_item.STR
                    classes.p2.STR += random_item.STR
                    break
            elif C.lower() == "n": 
                print("You leave the item behind and journey forth")
                break
            else: 
                print("You have to pick; [Y] or [N]!") 
                continue


def door_choice(): # låter spelaren välja en dörr och bestämmer vad som finns bakom den
    global door_alternatives
    chosen_alternative = None #<-- detta ger den ett standardvärde vilket gör så att även om spelaren skriver in annat än "1, 2 eller 3" så kraschar inte spelet.

    door = (input("\nYou have come 3 doors. You may proceed into the unknown... \n(Enter one of the 3 doors.)\n[1]LEFT\n[2]FORWARD\n[3]RIGHT\n"))
    if door == "1" or door == "left" or door == "Left":  
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    elif door == "2" or door.lower() == "forward": 
        chosen_alternative = rand.choice(door_alternatives) 
        print("You have now encountered a", chosen_alternative)
    elif door == "3" or door.lower() == "right": 
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
        print("Round One Fight!")
        enemy_encounter() 
    elif chosen_alternative == "Chest":    
        print(f"It contains a {get_random_chest_item()}") 
        add_random_item()

    # def door_encounter():#skapar en funktion som bestämmer vad som händer när man möter trap, monster eller chest
