import classes 
import inventory
import doors


def menu_choice(): 
    
    while True: 
        try: 
            choice =int(input("\nChoose one of the 3 below\n[1] STATISTICS\n[2] LOOK AT YOUR INVENTORY\n[3] PICK A DOOR\n")) 
            if choice == 1: 
                classes.print_stats()
            elif choice == 2: 
                inventory.inventory()
            elif choice == 3:
                doors.door_choice() 
            else: 
                print("Invalid choice, please choose number 1, 2 or 3") 
        except ValueError: 
            print("Invalid choice, please choose number 1, 2 or 3")




            
    