import random
#The line above imports the random module, to be used to generate random numbers later on.
def loginProcess():
    global login
    login=False
    print("\n\n")
    print("Login Process:")
    file= open("UserDetails.txt","r")
    usernames=[]
    passwords=[]
    playerNames=[]
    contents= True
    while contents != "":
        contents=file.readline()
        contents=contents.strip()
        splitContents=contents.split(",")
        if len(splitContents)==1:
            break
        usernames.append(splitContents[0])
        passwords.append(splitContents[1])
        playerNames.append(splitContents[2])
    file.close()
    user= input("What is your username?\n")
    for i in usernames:
        if i ==user:
            passw=input("What is your password?\n")
            iOfPass= usernames.index(i)
            password= passwords[iOfPass]
            if passw == password:
                print("You have logged in!")
                playerName=playerNames[iOfPass]
                global nameOfPlayer
                nameOfPlayer=playerName
                print("Welcome",playerName,"! \n")
                login= True
            else:
                print("Your password is incorrect")
                quit()
               
        
#The subroutine above reads the "UserDetails" file to act as a reference for usernames and passwords to then authenticate the user's input of their username
#and password, outputting a string if the login is successful.


def registrationProcess():
    file=open("UserDetails.txt","r")
    usernames=[]
    passwords=[]
    playerNames=[]
    contents= True
    while contents != "":
        contents=file.readline()
        contents=contents.strip()
        splitContents=contents.split(",")
        if len(splitContents)==1:
            break
        usernames.append(splitContents[0])
        passwords.append(splitContents[1])
        playerNames.append(splitContents[2])
    file.close()
    playerName= ""
    while playerName=="" or duplicate== True:
        playerName= input("What is your name?\n")
        for i in playerNames:
            if i == playerName:
                print("This name already exists.")
                duplicate= True
                break
            else:
                duplicate=False
    playerUsername=""
    while playerUsername =="" or duplicate== True:
        playerUsername=input("What would you like your username to be?\n")
        for i in usernames:
            if i == playerUsername:
                print("This username already exists.")
                duplicate= True
                break
            else:
                duplicate= False
#Checks for duplicate
    playerPassword= input("What would you like your password to be?\n")
    usernames.append(playerUsername)
    passwords.append(playerPassword)
    playerNames.append(playerName)
    File= open("UserDetails.txt","w")
    playerDetails=[]
    for x in usernames:
        playerDetails.append(x)
    for y in passwords:
        iOfUD= passwords.index(y)
        playerDetails[iOfUD]=playerDetails[iOfUD] +","+ y
    for z in playerNames:
        iOfUD= playerNames.index(z)
        playerDetails[iOfUD]= playerDetails[iOfUD] +","+z
    for i in playerDetails:
        if playerDetails.index(i)== 0:
            File.write(i)
            File.write("\n")
        else:
            File.close()
            File= open("UserDetails.txt","a")
            File.write(i)
            File.write("\n")
    File.close()
    loginProcess()
#The subroutine above takes in details from the user and then writes it back onto the file in the correct format with username, password and player name
#separated by commas on each line.

def aAndR():                                                                                           #aAndR = Authentication and Registration
    loginChoice=input("""Choose one of the options from below by typing its corresponding number:
1.  Login
2.  Register
:""")
    while loginChoice != "1" and loginChoice != "2":                    
       loginChoice=input("""Choose one of the options from below by typing its corresponding number:
1.  Login
2.  Register
:""")
    if loginChoice == "1":
        loginProcess()
    elif loginChoice == "2":
        registrationProcess()
#The subroutine above asks the user for an input of either 1 or 2, where depending on which is chosen, the allocated subroutine is run. For 1, it is the
#loginProcess() subroutine and for 2, it is the registrationProcess() subroutine.


def theGame():
    file= open("Songs.txt","r")
    artists=[]
    songs=[]
    contents=True
    while contents != "":
        contents= file.readline()
        contents=contents.strip()
        splitContents= contents.split(",")
        if len(splitContents)==1:
            break
        artists.append(splitContents[0])
        songs.append(splitContents[1])
    file.close()
#The block of code above opens and reads the file names "Songs", separating the artist names and song names and then appending them to two separate lists.
    unchosenArtists=[]
    unchosenSongs=[]
    for i in artists:
            unchosenArtists.append(i)
    for i in songs:
            unchosenSongs.append(i)
    print("""\n Each question will be presented in this form:
              [Artist Name: Song Initials with spaces] \n""")
    gameOver=False
    score=0
#This block of code duplicates the artists and songs lists to be used later. Then the code prints the form of the questions and lastly initializes the
#gameOver and score variables, where gameOver is set to False so that the while loop can be entered. The score is set to 0 to be incremented later.
    while gameOver==False:
        if len(unchosenArtists) == 0:
            for i in artists:
                unchosenArtists.append(i)
            for i in songs:
                unchosenSongs.append(i)
        maximumNumber= ((len(unchosenSongs))-1)
        randomNumber=random.randint(0,maximumNumber)
        randomSong= unchosenSongs[randomNumber]
        SongFirstLetters=""
        for i in range(len(randomSong)):
            if i == 0:
                SongFirstLetters+= randomSong[i]
            elif randomSong[i] == " ":
                SongFirstLetters+= " "
                SongFirstLetters+= randomSong[i+1]
        SongArtist= unchosenArtists[randomNumber]
        question= SongArtist+ ":" + SongFirstLetters
        unchosenArtists.pop(randomNumber)
        unchosenSongs.pop(randomNumber)
#The following code generates a random index and then makes the question with the randomly chosen song, removing that song from the list so that it cannot
#be chosen again.
        print("\n\n")
        print("[",question,"""]
Type the song's full name here (without missing capitals for each word) \n""")
        answer= input("Type your answer here:")
        if answer == randomSong:
            score+=3
        else:
            print("That was incorrect. You have one more chance.")
            print("[",question,"]  Type the song's full name here (without missing capitals for each word) \n")
            answer= input("Type your answer here:")

            if answer == randomSong:
                score+=1
            else:
                print("That was incorrect. You lose.")
                print("Game Over")
                gameOver= True
#The following code prints the question while asking for the answer, which is checked if it is correct and depending on the number of attempts increments
#their score, until they get a quetion wrong twice, setting gameOver to true and exiting the loop.
    print("You scored",score,"points!")
    print("\n\n")
    file2=open("playerScores.txt","r")
    playerNames=[]
    scores=[]
    contents= True
    while contents != "":
        contents=file2.readline()
        contents=contents.strip()
        splitContents= contents.split(",")
        if len(splitContents)==1:
            break
        playerNames.append(splitContents[0])
        scores.append(splitContents[1])
    file2.close()
    playerNames.append(nameOfPlayer)
    scores.append(score)
    Sorted= False
#The next block of code opens and reads from the file "playerScores" separating scores and allocated player names into different lists and then appending
#the new score and player name. Lastly, it initializes the variable Sorted to False to enter the next while loop.
    if len(scores) <2:
        Sorted=True
    while Sorted == False:
        Swap=0
        for i in range(len(scores)-1):
            if i== (len(scores)):
                break
            elif int(scores[i]) < int(scores[i+1]):
                tempScore= scores[i]
                scores[i]=scores[i+1]
                scores[i+1]=tempScore
                tempPlayerName= playerNames[i]
                playerNames[i]=playerNames[i+1]
                playerNames[i+1]=tempPlayerName
                Swap+=1
        if Swap == 0:
            Sorted= True
#The following code above checks that the list has more than 1 item to sort the list and then utilizes a bubble sort to sort the scores and player names
#from high to low. 
    if len(playerNames)<5:
        print("These are the top",len(playerNames),"scores!")
        for i in range(len(playerNames)):
            print (playerNames[i] +" with "+ str(scores[i])+" points!")
    else:
        print("These are the top 5 scores")
        for i in range(5):
            print(playerNames[i] +" with "+ str(scores[i])+" points!")
#The block of code above outputs the top 5 scorers if there are 5 or more recorded scores, if not it will print all the scores.

    File = open("playerScores.txt","w")
    playerScoreDetails=[]
    for x in range(len(playerNames)):
        playerScoreDetails.append(playerNames[x])
    for y in range(len(playerScoreDetails)):
        playerScoreDetails[y]=playerScoreDetails[y]+ ","+ str(scores[y])
    for i in range(len(playerScoreDetails)):
        File.write(playerScoreDetails[i])
        File.write("\n")
    quit()
#The last block of code in the subroutine, opens the file "playerScores" in write mode to then write all the score details onto the file in the correct
#format.
aAndR()
if login==True:
    theGame()
    

#The last 2 lines of code run the aAndR() subroutine and then the theGame() subroutine.
