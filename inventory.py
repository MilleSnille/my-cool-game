import time

inv = []

def inventory(): 
    global inv
    if len(inv) < 1: 
        print("\nYour inventory is empty! Choose a door to have a chance of receiving items!") 
    elif len(inv) > 0:
        print("\nYOUR INVENTORY:")
        for item in inv: 
            print(item)
            time.sleep(0.8) # printar alla föremål i inventoryt med en delay mellan 
    
        


 
