
import triqui as t

# 1. Mostrar mensaje de bienvenida

t.printIntro("intro.txt")

turn ="" # Indica quién tiene el turno para jugar, el usuario o la computadora.
while True:

    # 2. Crear el tablero
    board = [' '] * 10
    
    # 3. El usuario debe seleccionar la marca
    playerLetter, computerLetter = t.inputPlayerLetter()
    
    # 4. Quién va primero el usuario o la computadora?
    turn = t.whoGoesFirst()
    print(turn + ' va primero.')

    jugando = True # El juego ha iniciado

    while jugando:
        if turn == 'Usuario': # 5. Turno del usuario

            # a. Mostrar tablero
            t.drawBoard(board)
            #break # aqui imprime el tablero sin el break lo imprime infinito 

            # b. Pedir jugada al usuario
            move = t.getPlayerMove(board)
            
            # c. Actualizar el tablero
            t.makeMove(board, playerLetter, move)

            # d. Verificar si el usuario ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
            if t.isWinner(board, playerLetter):
                t.drawBoard(board)
                print("bien hecho haz ganado")
                jugando = False
            

            # e. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            elif t.isBoardFull(board):
                t.drawBoard(board)
                print("aqui hay un empate")
                jugando = False
            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno
            else:
                turn = 'Computadora'

        else:  # 6. Turno de la computadora

          

            # a. Computadora hace jugada.
            move = t.getComputerMove(board, computerLetter)
            # b. Actualizar el tablero.
            t.makeMove(board, computerLetter, move)

            # c. Verificar si la computadora ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
            if t.isWinner(board, computerLetter):
                t.drawBoard(board)
                print("la computadora gano, buen intenta ala proxima")
                jugando = False

            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            elif t.isBoardFull(board):
                t.drawBoard(board)
                print("hay un empate")
                jugando = False
            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.
            else:
                turn = 'Usuario'

           
    # 7. Preguntar si el usuario quiere jugar una vez mas
    if not t.playAgain():
        break
    #    Si no, finalizar el programa.

