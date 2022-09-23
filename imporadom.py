import random 

while True:

    aleatorio = random.randrange(0, 3)
    elijePc = ""
    print("1. piedra")
    print("2. papel")
    print("3. tijera")
    opcion = int(input("elige tu opcion "))

    if opcion == 1:
        elijeUsuario = "piedra"
    if opcion == 2:
        elijeUsuario = "papel"
    if opcion == 3:
        elijeUsuario = "Tijera"
    print("Elejiste: ", elijeUsuario)

    if aleatorio == 0: 
        elijePc "Piedra"
    if aleatorio == 1:
        elijePc "papel"
    if aleatorio == 2: 
        elijePc "Tijera"
    print("La maquina elijio:", elijePc)
    print("...")
    if elijePc == "Piedra" and elijeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
    elif elijePc == "papel"  and elijeUsuario == "Tijera":
        print("Ganaste, Tijera corta papel")
    elif elijePc == "Tijera" and elijeUsuario == "piedra":
        print("Ganaste, Piedra machaca Tijera")
    if elijePc == and elijeUsuario == "piedra":
        print("Perdiste, papel envuelve piedra")    
    elif elijePc == "Papel" and elijeUsuario == "Piedra":
        print("perdiste, Tijera corta papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("Perdiste, piedra machaca Tijera")
    elif elijePc == elijeUsuario:
        print("empate")

    play:again = input("Quieres jugar de nuevo (S/n) ): ")
    if play_again.lower() != "s":
        break