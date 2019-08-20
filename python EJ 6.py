def imprimeCositos(filas):
    largo = filas*2
    #parte 1
    for i in range(filas):
        for i in range(largo):
            print("*", end="")
        print()
    #parte 2
    largo=2
    for i in range(filas):
        for i in range(largo):
            print("*", end="")
        largo += 2
        print()


imprimeCositos(5)
