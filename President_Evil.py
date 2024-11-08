
lista = []

while True:
    print("1. Titta på listan.")
    print("2. Titta på en specifik listposotion.")
    print("3. Lägg till ett värde i listan.")
    print("4. Ta bort ett värde i listan.")
    print("5. Sortera listan.")
    print("6. Beräkna listan medelvärde.")
    print("7. Avsluta.")
    menytal = int(input("vad vill du göra? -->"))

    if menytal == 7:
        break
    elif menytal == 1:
        print("listan:", lista)
        if len(lista) == 0:
            print("listan är tom")
    
    if menytal == 2:
        index = int(input("vilken position vill du se? -->"))
        if index < len(lista):
            print(lista[index])
        else:
            print("ogiltlig position")
    
    if menytal == 3:
        tal = int(input("vilket tal vill du lägga till? -->"))
        lista.append(tal)
        print(" Nu har du lagt till ett tal i listan")       
    if menytal == 4:
        index = int(input("vilket plats vill du ta bort? -->"))
        lista.pop(index)
        if len(lista) == 0:
            print("din lista är tom")
    
    if menytal == 5:
        lista.sort()
        print("listan är sorterad")
        if len(lista) == 0:
            print("listan är tom")
    if menytal == 6:
        medel = (sum(lista) / len(lista))
        print(medel)

