def menu_choice(): 
    
    while True: 
        try: 
            val=int(input("Choose one of the 3 below\n\n[1] STATISTICS\n[2] LOOK AT YOUR INVENTORY\n[3] PICK A DOOR")) 
            if val == 1: 
                import classes 
                print(classes)
            elif val == 2: 
                import inventory
                print(inventory)
            elif val == 3:
                import doors
                print(doors)
            else: 
                print("Invalid choice, please choose number 1, 2 or 3") 
        except ValueError: 
            print("Invalid choice, please choose number 1, 2 or 3")

menu_choice()


            
    
