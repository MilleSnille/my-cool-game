import classes 
import inventory
import doors


def menu_choice(): 
    
    while True: 
        try: 
            choice =int(input("\nChoose one of the 3 below\n[1] STATISTICS\n[2] LOOK AT YOUR INVENTORY\n[3] PICK A DOOR\n[4] EXIT GAME\n")) 
            if choice == 1: 
                classes.print_stats()
            elif choice == 2: 
                inventory.inventory()
            elif choice == 3:
                doors.door_choice() 
            elif choice == 4: 
                print("PROGRAM TERMINATED")
                exit()  #<-- denna funktion gör så att spelet avslutas genom "exit()"
            else: 
                print("Invalid choice, please choose number 1, 2, 3 or 4") 
        except ValueError: 
            print("Invalid choice, please choose number 1, 2, 3 or 4")




            
    
