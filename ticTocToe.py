# Feature required:
#     Printing a board
#     Take player input
#     Check win or tie 
#     Switch player
#     check for win or tie
#     this will loop continuously

# Global variable
board=["-","-","-","-","-","-","-","-","-"]
currentPlayer='X'
def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def playerInput(board):
    inp=int(input("Select a spot 1-9: "))
    if board[inp-1]=="-":
        board[inp-1]=currentPlayer
    else:
        print("space already filled")
gameRunning=True

def checkHorizontal(board):
    global winner
    if board[0]==board[1]==board[2]and board[0]!="-":
        winner=board[0]
        return True
    if board[3]==board[4]==board[5]and board[3]!="-":
        winner=board[3]
        return True
    if board[6]==board[7]==board[8]and board[6]!="-":
        winner=board[6]
        return True
   
def checkVertical(board):
    global winner
    if board[0]==board[3]==board[6]and board[0]!="-":
        winner=board[0]
        return True
    if board[1]==board[4]==board[7]and board[1]!="-":
        winner=board[3]
        return True
    if board[2]==board[5]==board[8]and board[2]!="-":
        winner=board[2]
        return True
   
def checkDiagonal(board):
    global winner
    if board[0]==board[4]==board[8]and board[0]!="-":
        winner=board[0]
        return True
    if board[2]==board[4]==board[6]and board[2]!="-":
        winner=board[2]
        return True
def checkIfWin(board):    
    global gameRunning
    if checkHorizontal(board):
        printboard(board)
        print(f"the winner is {winner}!")
        gameRunning=False
    if checkVertical(board):
        printboard(board)
        print(f"the winner is {winner}!")
        gameRunning=False
    if checkDiagonal(board):
        printboard(board)
        print(f"the winner is {winner}!")
        gameRunning=False
       
def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printboard(board)
        print("It is a tie")
        gameRunning=False
   
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"
       
while gameRunning:
    printboard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    checkIfWin(board)
    checkIfTie(board)
