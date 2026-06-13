def boardGenerate(): 
    print("     |     |     ")
    print("  -  |  -  |  -  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  -  |  -  |  -  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  -  |  -  |  -  ")
    print("     |     |     ")

def winnerStatement(winnerNumber): 
    if(winnerNumber == 2): 
        print("Congratulations! X has won the game")
    else: 
        print("Congratulations! O has won the game")

def winLogic(boardMatrix): 
    #Rows
    if(boardMatrix[0][0] == boardMatrix[0][1] == boardMatrix [0][2] != 0): 
        winnerStatement(boardMatrix[0][0])
        return True   
    elif(boardMatrix[1][0] == boardMatrix[1][1] == boardMatrix [1][2] != 0): 
        winnerStatement(boardMatrix[1][0])
        return True
    elif(boardMatrix[2][0] == boardMatrix[2][1] == boardMatrix [2][2] != 0): 
        winnerStatement(boardMatrix[2][0])
        return True
          
        #Columns
    elif(boardMatrix[0][0] == boardMatrix[1][0] == boardMatrix [2][0] != 0): 
        winnerStatement(boardMatrix[0][0])
        return True
    elif(boardMatrix[0][1] == boardMatrix[1][1] == boardMatrix [2][1] != 0): 
        winnerStatement(boardMatrix[0][1])
        return True
    elif(boardMatrix[0][2] == boardMatrix[1][2] == boardMatrix [2][2] != 0): 
        winnerStatement(boardMatrix[0][2])
        return True
    
        #Diagonal
    elif(boardMatrix[0][0] == boardMatrix[1][1] == boardMatrix [2][2] != 0): 
        winnerStatement(boardMatrix[0][0])
        return True
    elif(boardMatrix[2][0] == boardMatrix[1][1] == boardMatrix [0][2] != 0): 
        winnerStatement(boardMatrix[2][0])
        return True

    else: 
        return False
            
def runGame():
    #Intializing vairables 

    boardMatrix = [[0,0,0],
                   [0,0,0],
                   [0,0,0]]
    winCondition_X = False
    winCondition_O = False
    userRow = 0
    userColumn = 0 

    while(winCondition_X == False and winCondition_O == False): 
        userInput_X = (input("Enter where you would like to place (X) IE. Row 0  column 1 = 0: ")) 
        userRow = int(userInput_X[0:1])
        userColumn = int(userInput_X[1:2])
        boardMatrix[userRow][userColumn] = 2
        if(winLogic(boardMatrix) == True): 
            break
        else: 
            pass

        userInput_O = input("Enter where you would like to place (O) IE. Row 0  column 1 = 01: ")
        userRow = int(userInput_O[0:1])
        userColumn = int(userInput_O[1:2])
        boardMatrix[userRow][userColumn] = 1
        if(winLogic(boardMatrix) == True): 
            break
        else: 
            pass
        
       
runGame()