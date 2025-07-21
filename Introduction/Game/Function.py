# Import Funtions
import os    


#Create Board and User Variables
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']           
Winner = 1    
Running = 0
Draw = -1   
view = 0
Stop = 1       
Game = Running    
Mark = 'X'


# Function for Show Game Board    
def ShowBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")   

# Function for Checks position is null or not    
def Position(x):    
    if(board[x] == ' '):
        print("Entered your position ")
        return True    
    else:
        print("Entered your position ")
        return False
        
# Function  for winning or draw of game 
def Probability():
    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] == board[3] != ' '):    
        Game = Winner    
    elif(board[4] == board[5]  == board[6]  != ' '):    
        Game = Win    
    elif(board[7] == board[8] == board[9]  != ' '):    
        Game = Winner    
    #Vertical Winning Condition    
    elif(board[1] == board[4] == board[7] != ' '):    
        Game = Winner    
    elif(board[2] == board[5] == board[8] != ' '):    
        Game = Winner    
    elif(board[3] == board[6] == board[9] != ' '):    
        Game = Winner    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] == board[9] != ' '):    
        Game = Winner    
    elif(board[3] == board[5] == board[7] != ' '):    
        Game= Winner   
    #Game Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw 
    else:            
        Game=Running
   

def StartGame():
    user=1
    usea = ''
    userb = ''
    count = 1
    print("Tic-Tac-Toe Game")    
    print("Player 1 [X], Player 2 [O]")
    # Get user input for their names
    usera = input("Enter your User A name :")
    userb = input("Enter your User B name :")
    # Start game
    while(Game == Running):    
        os.system('cls')
        # Display Board
        ShowBoard()
        # Mark the position inputs
        if(user % 2 != 0):    
            print("User A")    
            Mark = 'X'
                 
        else:    
            print("User B")    
            Mark = 'O'
        # Get user numbers for position inputs     
        option = int(input("Enter the number [1-9] for your position : "))
        if (0<option<10):
            if(Position(option)):    
                board[option] = Mark    
                user+=1    
                Probability()
        else :
            print("Invalid Option")
            print("Input Number (1-9)")
    
    os.system('cls')
    # Show the game board
    ShowBoard()
    # Draw of game and update to user history into database
    if(Game==Draw):    
        print("Game Draw")
        # Import Function to connect with Database
        import mysql.connector
        conDict = {'host':'localhost',
                    'database':'programming',
                    'user':'root',
                    'password':''}
        db = mysql.connector.connect(**conDict)
        cursor = db.cursor()
        # Insert data
        myInsertText = "INSERT INTO game_history VALUES(%s,%s,'Draw',%s)"
        myValues = (usera,userb,count)
        cursor.execute(myInsertText,myValues)
        db.commit()
        db.close
        count += 1
    # Winner of game and update to user history into database
    elif(Game==Winner):    
            user-=1    
            if(user%2!=0):    
                print("User A Won the Game")
                # Import Function to connect with Database
                import mysql.connector
                conDict = {'host':'localhost',
                            'database':'programming',
                            'user':'root',
                            'password':''}
                db = mysql.connector.connect(**conDict)
                cursor = db.cursor()
                # Insert data
                myInsertText = "INSERT INTO game_history VALUES(%s,%s,'A',%s)"
                myValues = (usera,userb,count)
                cursor.execute(myInsertText,myValues)
                db.commit()
                db.close
                count += 1
            else:    
                print("User B Won the Game")
                # Import Function to connect with Database
                import mysql.connector
                conDict = {'host':'localhost',
                            'database':'programming',
                            'user':'root',
                            'password':''}
                db = mysql.connector.connect(**conDict)
                cursor = db.cursor()
                # Insert data
                myInsertText = "INSERT INTO game_history VALUES(%s,%s,'B',%s)"
                myValues = (usera,userb,count)
                cursor.execute(myInsertText,myValues)
                db.commit()
                db.close
                count += 1
            
# Define function for Mainmenu of program
def Mainmenu():
    view = 0
    # Display Menu
    print("------- Mainmenu -------")
    print("1) New Game ")
    print("2) Game History ")    
    print("0) Exit Game ")
    view = int(input("Enter the Option : "))
    if (view == 1):
        # Recall define part
        StartGame()
        Mainmenu()

    elif(view == 2):
        print("View of Game Played")
        # Import database connection and Display the History
        import mysql.connector
        
        conDict = {'host':'localhost',
                    'database':'programming',
                    'user':'root',
                    'password':''}
        db = mysql.connector.connect(**conDict)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM game_history")
        data = cursor.fetchall()
        for item in data:
            print(item)

        db.close
        # Go to again main menu
        Mainmenu()
    elif(view == 0):
        # Exit the program
        print("Exit the Game")
        exit
    else:
        print("Invalid Option")
        Mainmenu()
    
# End of the program 


