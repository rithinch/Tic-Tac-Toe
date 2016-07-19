"""
    Tic Tac Toe Game
    Tic-Tac-Toe.py
    Features: 2 player game, saving multiple games and Diferent leves
              of computer AI (including Impossobile, which is unbeatable)

    http://rithinch.weebly.com/blog/artificial-intelligence-within-tic-tac-toe
        
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 16/04/16
    
"""
import random
import pickle
import itertools

def resetGame():
    """This function sets the game properties to default, mainly used when the user wants to start a new game"""
    
    global base,play,count,finalResult,breaking,saved_games,gameplay,player_lastmove,comp_lastmove
    
    base = ["0","1","2","3","4","5","6","7","8"] #Base is the game board
    play = []  #This list will contain x and o. so play[0] is always player 1's choice and play[1] is the opponent.
    count = [0,1]  #count[0] keeps a track of the number of moves made by both players in a game. count[1] is used for printing the list of saved games when user selects the option to continue a game.
    finalResult = "none"  #By default it will be none, but if a player wins it will change to "won" or if its a tie it will be changed to "tie"
    breaking = False  #used for breaking out of the bigger loops in one and two player game functions.
    saved_games = {}
    gameplay = ["n","playerturn","gamemode","default_game_name","difficulty"]
    player_lastmove = [] #this list stores all the moves made by the player
    comp_lastmove= []
    
    ##########################################################################################################################################
    #                                           GAME PROPERTIES EXPLANINED (gameplay list)
    
    #gameplay[0] is to store the game type, if it is a continued game it will be "y" else it's "n"
    #gameplay[1] keeps a track of the turns. if its player 1's turn it will be "p1", for player 2 "p2", and for computer "comp"
    #gameplay[2] stores the game mode. if its 1 player mode it will be "1p" or for 2 player it will be "2p"
    #gameplay[3] stores the game name (if it has one), which will be used for saving the game (the key for an entry in save_games dictionary)
    #gameplay[4] stroes the game difficulty. it will vary from "EASY", "MEDIUM", "IMPOSSIBLE"
    
    ##########################################################################################################################################

    
def saveGame(overwrite):
    """This function is called when user wants to save the game.
       Function Parameter: only "yes" or "no" as a string.
       This main purpose of giving input to this function is to give user an option to overwrite an existing saved game.
       This function creates a file with name "SavedGames" and extension .ttt (tic tac toe)"""
        
    global breaking
    try:
        file = open("SavedGames.ttt","rb")
        saved_games = pickle.load(file)
        file.close()
    except (FileNotFoundError,EOFError):
        file = open("SavedGames.ttt","wb")
        file.close()
        saved_games = {"Challenge Game":[["0","1","x","3","o","5","x","7","8"],"p1","1p",3,"o","x","MEDIUM"]}

        ########################################################################################################
        # STRUCTURE OF DICTIONARY BEING SAVED INTO FILE                                                        #
        # The key of an entry to the dictionary will be the name of the saved game entered by user.            #
        # The following required data which will be assigned to each key will be in a list                     #
        # element [0] of the list is the base (game board) at the moment when it is being saved                #
        # element [1] of the list stores the turn of a person (gameplay[1])                                    #
        # element [2] of the list stores the game mode (gameplay[2])                                           #
        # element [3] of the list stores the count of the moves played (count[0])                              #
        # element [4] of the list stores player 1's selection either x or o (play[0])                          #
        # element [5] of the list stores opponent's selection (play[1])                                        #
        # element [6] of the list stores the game difficulty                                                   #
        ########################################################################################################
        
    if overwrite == "yes":
        save_name = gameplay[3]
    else:
        save_name = input("Save the game with name: ")
    file = open("SavedGames.ttt","wb")
    saved_games[save_name] = [base,gameplay[1],gameplay[2],count[0],play[0],play[1],gameplay[4]] #creating a new entry/updating the old entry
    pickle.dump(saved_games,file)
    breaking = True
    print("\nGame has been saved as "+save_name+".")
    file.close()
    

def loadFile(game_name):
    """ This function is used to load the game properties from the save file and assign them in running game.
        Funtion Parameter: the name of the saved game which the user wants to open as a string.""" 
    global base
    file = open("SavedGames.ttt","rb")
    data = pickle.load(file)
    gameplay[0] = "y"
    gameplay[3] = game_name
    base = data[game_name][0]
    gameplay[1] = data[game_name][1] 
    gameplay[2] = data[game_name][2]
    count[0] = data[game_name][3]
    play.append(data[game_name][4])
    play.append(data[game_name][5])
    gameplay[4] = data[game_name][6]                                               
    file.close()
    
def delgame():
    """ This function deletes a particular saved game when completed."""
    if gameplay[0] == "y":
        file = open("SavedGames.ttt","rb")
        data = pickle.load(file)
        file.close()
        saved_games = data
        del saved_games[gameplay[3]]
        file = open("SavedGames.ttt","wb")
        pickle.dump(saved_games,file)
        file.close()
    else:
        pass
        
def returntoMenu():
    """This function asks the user if they want to run the program from start again"""
    while True:
        goback = input("Do you want to go back to main Menu? (y/n)\n")
        if goback == "y":
            StartGame()
            break
        elif goback == "n":
            print("\n---------- GAME CLOSED ----------\n")
            break           
        else:
            print("Invalid entry. Enter y or n only.")
    
def printgameBoard():
    """This function is used to print the game board after every move"""
    print((base[0] + " | " + base[1] + " | " + base[2]).center(34))
    print("-----------".center(34))
    print((base[3] + " | " + base[4] + " | " + base[5]).center(34))
    print("-----------".center(34))
    print((base[6] + " | " + base[7] + " | " + base[8]).center(34))
    print("\n")
    

def gameMenu():
    """ This function is used to print the game menu and it outputs the user selected option"""
    print("-----------------------------------")
    print(("TIC TAC TOE GAME - By Rithin \n"))
    print("(1) One Player ")
    print("(2) Two Player ")
    print("(3) Continue Saved Game ")
    print("(4) Exit \n")
    while True:       
        try:
            option = int(input("Select an option: "))
            if option<=3 and option >0:
                print("-----------------------------------")
                return option
            elif option == 4:
                return option
            else:
                print("Invalid Option. Please try again.\n")
                                     
        except ValueError:
            print("Invalid Option. Please try again.\n")
    
def selectAI_level():
    """ This funcion asks the user to select a Computer Level """
    print("Choose the difficulty level of computer: \n")
    print("(1) Easy")
    print("(2) Medium")
    print("(3) Impossible")
    while True:
        try:
            option = int(input("\nChoice: ")) #Stores the choosen level in gameplay[4]
            if option == 1:
                gameplay[4] = "EASY"   
                return
            elif option == 2:
                gameplay[4] = "MEDIUM"
                return
            elif option == 3:
                gameplay[4] = "IMPOSSIBLE"
                return
            else:
                print("Invalid Option. Please try again.")
        except ValueError:
            print("Invalid Option. Please try again.")

def x_or_o():
    """ This function is used by player 1 to select either x or o and in this game x always makes the first move"""
    while True:
        selection = input("Player 1: Pick one x or o?\n")
        if selection == "x":
            play.append(selection)
            play.append("o")
            gameplay[1] = "p1"
            break
        elif selection == "o":
            play.append(selection)
            play.append("x")
            if gameplay[2] == "1p":
                gameplay[1] = "comp"
            else:
                gameplay[1] = "p2"
            break
        else:
            print("Enter x or o in lower case only. \n")
        
        
def availability(n):
    """ This function is used to check if a spot in the board is empty (available) or not. Its input is the number of the location (integer)
        and outputs "y" it is available else "n" """
    if base[n] == "x" or base[n] == "o": 
        return "n"
    else:
        return "y"


def askMove(player):
    """ This function is used for asking player 1 or player 2 where they want to place their move.
        Input is either 1 or 2 as an integer only """ 
    if player == 1:
        string = "Player 1: "
        number = 0
    elif player == 2:
        string = "Player 2: "
        number = 1

    while True:
        try:
            print("Tip: Enter 11 to Save game")
            selectedlocation = int(input(string+"Where do you want to place "+play[number]+"?\n"))
            return selectedlocation
            break
        except ValueError:
            print("Invalid entry.")
            print("Only numbers should be entered.")
            print("Please try again. \n")
    
        
def player1Move():
    """This function is called when its Player 1's turn to make a move."""
    while True:
        selectedlocation = askMove(1)
        if selectedlocation >=0 and selectedlocation <=8:
            n = selectedlocation
            if availability(n) == "y":
                base[n] = play[0]
                count[0] = count[0]+1
                player_lastmove.append(n)
                print("\n")
                break
            else:
                print("It is not possible to place "+play[0]+" there.")
                print("Please try again. \n")

        elif selectedlocation == 11:
            if gameplay[0] == "y":
                while True:
                    overwrite = input("Do you want to overwrite the existing saved file? (y/n) \n")
                    if overwrite == "y":
                        saveGame("yes")
                        break
                    elif overwrite == "n":
                        saveGame("no")
                        break
                    else:
                        print("Invalid entry. Enter y or n only.")
                break
            else:
                saveGame("no")
                break
            

        else:
            print("It is not possible to place "+play[0]+" there.")
            print("Only the numbers shown on the board are possible.")
            print("Please try again. \n")


def player2Move():
    """This function is called when its Player 2's turn to make a move."""
    while True:
        selectedlocation = askMove(2)
        if selectedlocation >=0 and selectedlocation <=8:
            n = selectedlocation
            if availability(n) == "y":
                base[n] = play[1]
                count[0] = count[0]+1
                print("\n")
                break
            else:
                print("It is not possible to place "+play[1]+" there.")
                print("Please try again. \n")
        elif selectedlocation == 11:
            if gameplay[0] == "y":
                while True:
                    overwrite = input("Do you want to overwrite the existing saved file? (y/n) \n")
                    if overwrite == "y":
                        saveGame("yes")
                        break
                    elif overwrite == "n":
                        saveGame("no")
                        break
                    else:
                        print("Invalid entry. Enter y or n only.")
                break
            else:
                saveGame("no")
                break

        else:
            print("It is not possible to place "+play[1]+" there.")
            print("Only the numbers shown on the board are possible.")
            print("Please try again. \n")

def AI_corner():
    """This function is returns a move which is in one of the corners in the board"""
    while True:
        corners = [0,2,6,8]
        move = corners[random.randint(0,3)]
        if availability(move) == "y":
            return move
        
def AI_Impossible():
    """This function returns a move by the computer and it is called everytime when its the computers turn,
       only when the user sets the difficulty level to IMPOSSIBLE."""
    
    if count[0]<=2: #when less than or equal to 2 moves played on board
        if play[1]=="o":
            if player_lastmove[0]!=4: 
                return 4 
            else:
                move = AI_corner()
                return move
        else:
            if len(player_lastmove)==1 and availability(4) == "y":
                return 4
            elif availability(4) == "y":
                return 4
            else:
                move = AI_corner()
                return move
            
    if count[0]>2: #when greater than two moves played on board
        for i in range(0,len(AI)):
            (move1,move2,move3) = (AI[i])
            if base[move1] == play[1] and base[move2] == play[1]: #Attacking 
                if availability(move3)=="y":
                    return move3

        for i in range(0,len(AI)):
            (move1,move2,move3) = (AI[i])
            if base[move1]==play[0] and base[move2] == play[0]:  #Defensive
                if availability(move3) == "y":  #if the 3rd likely move position is not occupied by player 0 
                    return move3
                
        if count[0] == 3 and play[0] == "x": #to block any tricky play
            if base[5] == "x" and (base[1] == "x" or base[0] == "x"):
                return 2
            elif base[5] =="x" and base[7] == "x":
                return 8
            elif base[1] == "x" and base[6] == "x":
                return 0
            elif base[6] == "x" and base[5] == "x":
                return 8 
            elif comp_lastmove[0] == 4 and availability(3) == "y":
                return 3

        for i in range(0,len(AI)):
            (move1,move2,move3) = (AI[i])
            if base[move1] == play[0] and (move2 in [0,2,6,8]) and availability(move2)=="y": #to block any tricky play 
                return move2
            
    
        for i in range(0,len(AI)):
            (move1,move2,move3) = (AI[i])
            if move1 == play[1]: #creating chance for a win
                if availability(move2) == "y": 
                    return move2
            else: #If there is no chance of anyone winning, then a random move will be made
                while True:
                    move = random.randint(0,8)
                    if availability(move) == "y":
                        return move

def AI_Easy():
    """This function returns a move by the computer and it is called everytime when its the computers turn,
       only when the user sets the difficulty level to EASY."""
    for i in range(0,len(AI)):
        (move1,move2,move3) = (AI[i])
        if base[move1] == play[1] and base[move2] == play[1]: #Attacking
            if availability(move3)=="y":
                return move3
    while True:
        move = random.randint(0,8)
        if availability(move) == "y":
            return move

def AI_Medium():
    """This function returns a move by the computer and it is called everytime when its the computers turn,
       only when the user sets the difficulty level to MEDIUM."""
    for i in range(0,len(AI)):
        (move1,move2,move3) = (AI[i])
        if base[move1] == play[1] and base[move2] == play[1]: #Attacking
            if availability(move3)=="y":
                return move3
            
    for i in range(0,len(AI)):
        (move1,move2,move3) = (AI[i])
        if base[move1] == play[0] and base[move2] == play[0]: #Defense
            if availability(move3)=="y":
                return move3
        elif availability(move1) == "y" and move1 in [0,2,6,8]:
            return move1

    while True:
        move = random.randint(0,8)
        if availability(move) == "y":
            return move
        
        
def computerMove():
    """This function is called when its computer's turn to make a move."""
    if gameplay[4] == "IMPOSSIBLE":
        move = AI_Impossible()
        base[move] = play[1]
        comp_lastmove.append(move)
        count[0] = count[0] + 1       
    elif gameplay[4] == "MEDIUM":
        move = AI_Medium()
        base[move] = play[1]
        count[0] = count[0]+1
    else:
        move = AI_Easy()
        base[move] = play[1]
        count[0] = count[0]+1
        
            

def compAI():
    """This function is used to make a list of the possible combinations of the winning moves.
       It is called only once, when the user selects a one player game."""
    global AI
    winMoves = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8)]
    PossibleWins = []
    for i in range(0,len(winMoves)):
        PossibleWins.append(list(itertools.permutations(winMoves[i])))
        
    AI = list(itertools.chain.from_iterable(PossibleWins))
      
def checkWin(n):
    """This function checks if x or o has won and also if its a tie.
       function input is "x" or "o" string.
       It returns "y" if a player wins, or "t" if its a tie, else "n".
       which will be used in further parts of the program."""
    
    if base[0] == n and base[1] == n and base[2]==n:
        return "y"
    elif base[3] == n and base[4] == n and base[5]==n:
        return "y"
    elif base[6] == n and base[7] == n and base[8]==n:
        return "y"
    elif base[0] == n and base[3] == n and base[6]==n:
        return "y"
    elif base[1] == n and base[4] == n and base[7]==n:
        return "y"
    elif base[2] == n and base[5] == n and base[8]==n:
        return "y"
    elif base[2] == n and base[4] == n and base[6]==n:
        return "y"
    elif base[0] == n and base[4] == n and base[8]==n:
        return "y"
    elif count[0] == 9:
        return "t"
    else:
        return "n"


def Result(player):
    """ This function is final check for a win, main purpose is to break the flow of the 1p and 2p games
        and print a clear winning message.
        function input is "x" or "o" string."""
    global breaking,finalResult
    result = checkWin(player)
    if result=="y":
        finalResult = "won"
        printgameBoard()
        breaking = True
        delgame()
    elif result == "t":
        printgameBoard()
        finalResult = "tie"
        breaking = True
        delgame()
    else:
        pass


def onePlayerEnd():
    """This function is used for printing the "one player game ended" message."""
    print("\n--------- 1P GAME ENDED ---------\n")


def twoPlayerEnd():
    """This function is used for printing the "two player game ended" message."""
    print("\n--------- 2P GAME ENDED ---------\n")
    
    
def onePlayerGame():
    """This function sets the program flow of a one player game."""
    print(("  AI LEVEL: "+gameplay[4]+"\n").center(34))
    compAI()
    while count[0]<=9:
        if gameplay[1] == "p1":
            printgameBoard()
            gameplay[1] = "p1"
            player1Move()
            Result(play[0])
            if breaking == True:
                if finalResult == "tie":
                    print(("It is a tie!").center(34))
                elif finalResult == "won":
                    print(("Player 1 ("+play[0]+") wins!").center(34))
                onePlayerEnd()
                returntoMenu()
                break
            else:
                gameplay[1] = "comp"
        else:
            gameplay[1] = "comp"
            computerMove()
            Result(play[1])
            if breaking == True:
                if finalResult == "tie":
                    print(("It is a tie!").center(34))
                elif finalResult == "won":
                    print(("Computer ("+play[1]+") wins!").center(34))
                onePlayerEnd()
                returntoMenu()
                break
            else:
                gameplay[1] = "p1"


    
def twoPlayerGame():
    """This function sets the program flow of a two player game."""
    while count[0]<=9:
        if gameplay[1] == "p1":
            printgameBoard()
            gameplay[1] = "p1"
            player1Move()
            Result(play[0])
            if breaking == True:
                if finalResult == "tie":
                    print(("It is a tie!").center(34))
                elif finalResult == "won":
                    print(("Player 1 ("+play[0]+") wins!").center(34))
                twoPlayerEnd()
                returntoMenu()
                break
            else:
                gameplay[1] = "p2"
        else:
            printgameBoard()
            gameplay[1] = "p2"
            player2Move()
            Result(play[1])
            if breaking == True:
                if finalResult == "tie":
                    print(("It is a tie!").center(34))
                elif finalResult == "won":
                    print(("Player 2 ("+play[1]+") wins!").center(34))
                
                twoPlayerEnd()
                returntoMenu()
                break
            else:
                gameplay[1] = "p1"


def continueGame():
    """This function is called only when the user chooses continue game option.
       It Used for opening the saved games file, presenting the available saved games in a menu
       and making the user select a choice or get back to menu"""
    
    try:
        file = open("SavedGames.ttt","rb")
        saved_games = pickle.load(file)
        print("Choose the game you wish to continue from the list below :\n")
        saved_options = {}
        useroption = saved_games.keys()
        for i in useroption:
            print(str(count[1])+") " + i)
            saved_options[count[1]] = i
            count[1] = count[1] + 1
            file.close()
        while True:
            if len(saved_games.keys())==0:
                print("There are no saved games.")
                print("Please save a game and try again")
                print("..and you have finished the challenge game!!\n")
                returntoMenu()
                break
            else:
                try:
                    print("\nTip: Enter 0 to go back to main menu.")
                    choice = int(input("Choice: "))
                    if choice in saved_options:
                        game_name = saved_options[choice]
                        loadFile(game_name)
                        if gameplay[2] == "1p":
                            print("\n--------- 1P GAME STARTED ---------\n")
                            onePlayerGame()
                        else:
                            print("\n--------- 2P GAME STARTED ---------\n")
                            twoPlayerGame()
                        break
                    elif choice == 0:
                        StartGame()
                        break
                    else:
                        print("Invalid Entry")
                        print("Only choices shown above are available")
                        print("Please try again. \n")
                        
                        
                except ValueError:
                    print("Only the choice numbers should be entered")
                    print("Please try again \n")
                    
                               
    except (FileNotFoundError,EOFError,UnboundLocalError):
        print("There are no saved games.")
        print("Please save a game and try again.\n")
        print("Unlock a challenge after")
        print("saving first game!!\n")
        returntoMenu()
            
def StartGame():
    """This function is used to start the program""" 
    option = gameMenu()
    resetGame()
    if option== 1:
        gameplay[2] = "1p"
        selectAI_level()
        x_or_o()
        print("\n--------- 1P GAME STARTED ---------\n")
        onePlayerGame()
                                        
    elif option == 2:
        gameplay[2] = "2p"
        x_or_o()
        print("\n--------- 2P GAME STARTED ---------\n")
        twoPlayerGame()

    elif option == 3:
        print("\n----------- SAVED GAMES -----------\n")
        continueGame()

    elif option == 4:
        print("\n----------- TIC TAC TOE CLOSED -----------\n")



StartGame()   


    
    



