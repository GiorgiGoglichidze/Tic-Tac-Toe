import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

winner = None 
gameisrunning = True
player= "X"

def printboard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print("----------")
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print("----------")
    print(f'{board[6]} | {board[7]} | {board[8]}')

def playermakemove(board):
    global player
    if gameisrunning:
        index = int(input("Choose your square(1-9): "))
        index -= 1

        if index < 0 or index > 8:
            print('Wrong input')
            playermakemove(board)
            
        else:
            if board[index]=="-":
                board[index] = player
            else:
                print("Wrong input nigga try again")
                playermakemove(board)


def checkcolumns(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3] 
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]

def checkrows(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1] 
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]

def checkdiagonals(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
    elif board[6] == board[4] == board[2] and board[6] != "-":
        winner = board[6]

def checkthewin(board):
    global winner
    global gameisrunning
    if gameisrunning:
        checkcolumns(board)
        checkdiagonals(board)
        checkrows(board)
        if winner != None:
            print(f'Winner is {winner} !!!')
            printboard(board)
            gameisrunning = False

def checktie(board):
    global gameisrunning
    if gameisrunning:
        if "-" not in board and winner == None:
            print("It's a Tie")
            gameisrunning = False
            printboard(board)

def changeturns():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def bot1(board):
    global player
    if gameisrunning:
        liste = []
        for i in range(9):
            if board[i] == "-":
                liste.append(i)
        x=random.choice(liste)
        board[x] = player

def bot2(board):

    if gameisrunning:
        column1=board[0:3]
        column2=board[3:6]
        column3=board[6:9]
        
        row1=board[0] + board[3] + board[6]
        row2=board[1] + board[4] + board[7]
        row3=board[2] + board[5] + board[8]

        diagonal1 = board[0] + board[4] + board[8]
        diagonal2 = board[2] + board[4] + board[6]

        if player == "O":
            antiplayer = "X"
        else:
            antiplayer = "O"
        #Next 30 lines of code is to help bot if he is close to winning to get his victory

        if column1.count(player) == 2 and "-" in column1:
            c = column1.index("-")
            board[c] = player
        elif column2.count(player) == 2 and "-" in column2:
            c = column2.index("-")
            board[c + 3] = player
        elif column3.count(player) == 2 and "-" in column3:
            c = column3.index("-")
            board[c + 6] = player

        elif row1.count(player) == 2 and "-" in row1:
            c = row1.index("-")
            board[c*3] = player
        elif row2.count(player) == 2 and "-" in row2:
            c = row2.index("-")
            board[c*3 + 1] = player
        elif row3.count(player) == 2 and "-" in row3:
            c = row3.index("-")
            board[c*3 + 2] = player

        elif diagonal1.count(player) == 2 and "-" in diagonal1:
            c = diagonal1.index("-")
            board[c * 4] = player
        elif diagonal2.count(player) == 2 and "-" in diagonal2:
            c = diagonal2.index("-")
            board[(c+1)*2] = player


        #Next 30 lines of code is for bot to try and stop your victory
            

        elif column1.count(antiplayer) == 2 and "-" in column1:
            c = column1.index("-")
            board[c] = player
        elif column2.count(antiplayer) == 2 and "-" in column2:
            c = column2.index("-")
            board[c + 3] = player
        elif column3.count(antiplayer) == 2 and "-" in column3:
            c = column3.index("-")
            board[c + 6] = player

        elif row1.count(antiplayer) == 2 and "-" in row1:
            c = row1.index("-")
            board[c*3] = player
        elif row2.count(antiplayer) == 2 and "-" in row2:
            c = row2.index("-")
            board[c*3 + 1] = player
        elif row3.count(antiplayer) == 2 and "-" in row3:
            c = row3.index("-")
            board[c*3 + 2] = player

        elif diagonal1.count(antiplayer) == 2 and "-" in diagonal1:
            c = diagonal1.index("-")
            board[c * 4] = player
        elif diagonal2.count(antiplayer) == 2 and "-" in diagonal2:
            c = diagonal2.index("-")
            board[(c+1)*2] = player


        else:
            bot1(board)






question = input("SinglePlayer(enter 1) or MultiPlayer(enter 2): ")

if question == "2":
    while gameisrunning:
        printboard(board)
        playermakemove(board)
        checkthewin(board)
        checktie(board)
        changeturns()


elif question == "1":

    choose=input("Choose X or O: ")

    if choose == "X":
        player = "X"
        while gameisrunning:
            printboard(board)
            playermakemove(board)
            checkthewin(board)
            checktie(board)
            changeturns()
            bot2(board)
            checkthewin(board)
            checktie(board)
            changeturns()


    elif choose == "O":

        while gameisrunning:
            bot2(board)
            printboard(board)
            checkthewin(board)
            checktie(board)
            changeturns()
            playermakemove(board)
            checkthewin(board)
            checktie(board)
            changeturns()
    else:

        print("Wrong input try again nigga")






