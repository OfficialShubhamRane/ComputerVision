#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gameBoard(row=0, column=0):
    global player, turnCounter, winnerFound
    
    try:
        if(game[row][column] == 0 and winnerFound == 0):              #Checking if the spot is valid                 
            game[row][column] = player                                #Puting a mark successfully 
            turnCounter += 1
            print("Player " + str(player) + " played!!!")
            print("   0  1  2")
            for count,row in enumerate(game):
                print(count,row)                 #Printing game board
                
            print("turn no: " + str(turnCounter))
                  
            if(turnCounter >= 5):
                checkWinner(game)
                
            #Changing the player
            if(player == 1):            
                player = 2
            elif(player == 2):
                player = 1
        elif(winnerFound == 0):
            print("Spot is not empty")
        else:
            pass
        
    except IndexError as e:
        print("Index should be 0 or 1 or 2",e)
        

def checkWinner(game):
    global winnerFound, winningStmt
    
    for i in range(3):                                # Horizontal Winner
        winner = game[i][1]
        if(game[i][0]==winner and game[i][2]==winner and winner!=0):
            winningStmt = str(winner) + " is winner on "+ str(i) +"th row"
            winnerFound = 1
            return 0
    
    for i in range(3):                                # Vertical Winner
        winner = game[1][i]
        if(game[0][i]==winner and game[2][i]==winner and winner!=0):
            winningStmt = str(winner) + " is winner on "+ str(i) +"th column"
            winnerFound = 1
            return 0
            
    winner = game[1][1]
    if(game[0][0]==winner and game[2][2]==winner and winner!=0):
        winningStmt = str(winner) + " is winner on declining diagonal"
        winnerFound = 1
        return 0
    
    winner = game[1][1]
    if(game[0][2]==winner and game[2][0]==winner and winner!=0):
        winningStmt = str(winner) + " is winner on inclining diagonal"
        winnerFound = 1
        return 0
            
            #MAIN
game = [[0,0,0],[0,0,0],[0,0,0]]
print("Play game, player 'X' is = '1' and player 'O' is ='2'")
player = 1
turnCounter = 0
winnerFound = 0
winningStmt = ""


for j in range(len(game)*len(game)):
    if(winnerFound == 0):
        row = int(input("Enter Row: "))
        col = int(input("Enter Col: "))
        gameBoard(row, col)
    else:
        print(winningStmt)
        break
            
            #Both are winning but 1 wins first for Horizontal
# gameBoard(1,0)
# gameBoard(0,0)
# gameBoard(1,1)
# gameBoard(0,1)
# gameBoard(1,2)
# gameBoard(0,2)
            #winner is 1 for Horizontal
# gameBoard(0,0)
# gameBoard(2,0)
# gameBoard(0,1)
# gameBoard(2,1)
# gameBoard(0,2)
            #winner is 1 for vertical
# gameBoard(0,1)
# gameBoard(0,2)
# gameBoard(1,1)
# gameBoard(2,2)
# gameBoard(2,1)
            #winner is 2 for inclining diagonal
# gameBoard(0,1)
# gameBoard(1,1)
# gameBoard(2,2)
# gameBoard(0,2)
# gameBoard(2,1)
# gameBoard(2,0)

