def boardGenerate(boardMatrix): 
    myBoard = ("""
      |     |     
   """+str(boardMatrix[0][0]) +"""  |  """+str(boardMatrix[0][1])+"""  |  """+str(boardMatrix[0][2])+"""  
 _____|_____|_____
      |     |     
   """+str(boardMatrix[1][0])+"""  |  """+str(boardMatrix[1][1])+"""  |  """+str(boardMatrix[1][2])+"""  
 _____|_____|_____
      |     |     
   """+str(boardMatrix[2][0])+"""  |  """+str(boardMatrix[2][1])+"""  |  """+str(boardMatrix[2][2])+"""  
      |     |     """)
    myBoard = myBoard.replace("0", "-")
    myBoard = myBoard.replace("1", "O")
    myBoard = myBoard.replace("2", "X")

    print(myBoard)

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
    boardGenerate(boardMatrix)

    while(winCondition_X == False and winCondition_O == False): 
        
        illegalPlacement = False
        
        while(illegalPlacement != True): 
            userInput_X = (input("Enter where you would like to place (X) IE. Row 0  column 1 = 0: ")) 
            userRow = int(userInput_X[0:1])
            userColumn = int(userInput_X[1:2])
            if(boardMatrix[userRow][userColumn] != 0): 
                print("You cant place in this position try again")
            else: 
                boardMatrix[userRow][userColumn] = 2
                illegalPlacement = True

        boardGenerate(boardMatrix)

        if(winLogic(boardMatrix) == True): 
            break
        else: 
            pass
        
        illegalPlacement = False
        
        while(illegalPlacement != True): 
            userInput_O = input("Enter where you would like to place (O) IE. Row 0  column 1 = 01: ")
            userRow = int(userInput_O[0:1])
            userColumn = int(userInput_O[1:2])
            if(boardMatrix[userRow][userColumn] != 0): 
                print("You cant place in this position try again")
            else: 
                boardMatrix[userRow][userColumn] = 1
                illegalPlacement = True
        
        boardGenerate(boardMatrix)

        if(winLogic(boardMatrix) == True): 
            break
        else: 
            pass
        
runGame()