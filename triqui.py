import random

def printIntro(introFile):
    '''
        Firma:
            (string) -> ()

        Sinopsis:
            función que imprime el contenido de un archivo en pantalla, en este
    		caso, el mensaje de bienvenida al juego

        Entradas y salidas:
            - inputFile: Nombre del archivo que contiene la presentación del juego
            - returns: None, solo imprime el archivo leído en pantalla

        Ejemplos de uso:

            printIntro("intro.txt")

            ████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗
            ╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║
               ██║   ██████╔╝██║██║   ██║██║   ██║██║
               ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║
               ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║
               ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝
        '''

    # Desarrolle el cuerpo de la función aquí...

    #"comentarios mios" se abre  el archivo con with palabra reseveda que hace que cierre el codigo  en modo lectura ("r") usando codificación UTF-8
    # aqui permite leer correctamente los caracteres especiales del banner 
    
    #otra forma de poderlo abrir
    # with open(introFile, "r", encoding="utf-8") as archivo:
    #  contenido = archivo.read()
    # print(contenido)


    file = open("./intro.txt","r", encoding="utf-8")
    contenido = file.read()
    file.close()
    print(contenido)




    pass

def drawBoard(board):
    # Esta función imprime el tablero en la consola
    # Argumentos:
    # Board: Lista de strings que representa el estado del tablero

    # Desarrolle el cuerpo de la función aquí...

   
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    return [" "] * 9

    



    pass

def inputPlayerLetter():
    


    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".

    # retorna una lista de strings donde la letra escogida por el usuario
    # ocupa la primera posición y la letra que le corresponde a la computadora
    # ocupa la segunda posición.

    # Desarrolle el cuerpo de la función aquí...
    while True:
        simbolo = input("Digite el simbolo con el que desea jugar con el que se identifica (X o O)").upper()
        if simbolo == "X" or simbolo == "O":
            if simbolo == "X":
                return ["X", "O"]# si el usuario ingresa x la computadora es 0
            else:
                return ["O", "X"] # si el usuario ingresa o la computadora es x

            break

    pass

def whoGoesFirst():
    # Esta función escoge de forma aleatoria quien inicial el juego.

    # Retorna el string "Usuario" si el usuario inicia el juego o
    # el string "Computadora" si la computadora inicia el juego.

    # Desarrolle el cuerpo de la función aquí...
    if random.randint(0, 1) == 0:
        return "Usuario" # si es 0 empieza el usuario
    else:
        return "Computadora" # y si es uno empieza la computadora
        
    pass

def makeMove(board, letter, move):
    # Esta función actualiza el estado del tablero.
    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.

    # Desarrolle el cuerpo de la función aquí...
    board[move] = letter
    return board



    
    pass

def isWinner(board, letter):
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

    # Desarrolle el cuerpo de la función aquí...
    ganadora_1 = board[0] == board[1] == board[2] == letter
    ganadora_2 = board[3] == board[4] == board[5] == letter
    ganadora_3 = board[6] == board[7] == board[8] == letter
    ganadora_4 = board[0] == board[3] == board[6] == letter
    ganadora_5 = board[1] == board[4] == board[7] == letter
    ganadora_6 = board[2] == board[5] == board[8] == letter
    ganadora_7 = board[0] == board[4] == board[8] == letter
    ganadora_8 = board[2] == board[4] == board[6] == letter

    # Verificar si alguna jugada es verdadera
    if (ganadora_1 or ganadora_2 or ganadora_3 or
        ganadora_4 or ganadora_5 or ganadora_6 or
        ganadora_7 or ganadora_8):
        return True
    else:
        return False
    pass

def isSpaceFree(board, move):
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...


    # una casilla vacia se representa con un espacio " "
    casilla_vacia = " "

    # verificacion de que + si la casilla elegida está vacía
    if board[move - 1] == casilla_vacia:
        return True
    else:
        print("Elige otra casilla")
        return False
    pass

def getPlayerMove(board):
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.


    # Desarrolle el cuerpo de la función aquí...

    while True:
        move = input("Elige una casilla (1-9): ")
        if move.isdigit(): #Verifica que lo que escribió el jugador sea un número (no letras ni símbolos), y si no es un numero salta una casilla
            move = int(move)
            if 1 <= move <= 9 and board[move-1] == " ":
                board[move-1] = inputPlayerLetter   # asigna X u O en la casilla
                break
        print("Casilla inválida u ocupada, intenta de nuevo.")
    pass

def chooseRandomMoveFromList(board, movesList):
    # Esta función escoge de forma aleatoria una casilla vacía del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # moveList: Lista que contiene los números de las casillas a verificar (ver documento de la práctica).

    # Esta función debe retornar alguno de los números de casillas en moveList
    # desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    # esta función debe retornar el valor None.

    # Desarrolle el cuerpo de la función aquí...
    pass

def getComputerMove(board, computerLetter):
    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    # Desarrolle el cuerpo de la función aquí...

    # 1. Verificar si la computadora puede ganar...

    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...

    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...

    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...

    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...

    pass

def isBoardFull(board):
    # Esta función verifica si el tablero está lleno.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    # En caso contrario debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    if " " in board:
        return False
    else:
        return True

    pass