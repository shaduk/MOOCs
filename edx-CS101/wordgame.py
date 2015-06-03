
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    total = 0
    for i in word:
        total = total + SCRABBLE_LETTER_VALUES[i]
    total = total*len(word)
    if len(word)==n:
        total= total+50
    return total


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    copy = hand.copy()
    for i in word:
        for j in copy:
            if i==j and copy[i]!=0:
                copy[i]=copy[i]-1
    return copy

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    copy = hand.copy()
    b = False
    for i in word:
        if i in copy.keys() and copy[i]!=0:
           
            b = True
           
            copy[i] = copy[i] - 1 
        else:
            b = False
            break
          
    if word in wordList and b:
        
        return True
    else:
        return False


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    count = 0
    for i in hand.keys():
        if hand[i]!=0:
            count = count + hand[i]
    return count 
    
def playHand(hand, wordList, n):
       # Keep track of the total score
    
    total = 0
    
    # As long as there are still letters left in the hand:
    
    while calculateHandlen(hand)!=0:
        
        # Display the hand

        print "Current Hand: ",
        print str(displayHand(hand))
        
        # Ask user for input
        
        print "Enter word, or a to indicate that you are finished: ",
        user_res = raw_input()
        
        # If the input is a single period:
        
        if user_res==".":
            
            # End the game (break out of the loop)
            break
        
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(user_res, hand, wordList)==False:
            
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."
            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total = total + getWordScore(user_res, n)
                print user_res+" earned "+ str(getWordScore(user_res,n))+ " points. Total: "+str(total)
                # Update the hand 
                hand = updateHand(hand, user_res)
               

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    return total


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand = None
    print "Enter n to deal a new hand, r to replay the last hand, or e to end game: ",
    response = raw_input()
    n = HAND_SIZE
    while(response!="n" or response!="r" or response!="e"):
        if response=="n":
            hand = dealHand(n)
            playHand(hand, wordList, n)
            print "Enter n to deal a new hand, r to replay the last hand, or e to end game: ",
            response = raw_input()
        elif response=="r":
            if hand!=None:
                playHand(hand, wordList, n)
                print "Enter n to deal a new hand, r to replay the last hand, or e to end game: ",
                response = raw_input()
            else:
                print "You have not played a hand yet. Please play a new hand first!"
                print "\n"
                print "Enter n to deal a new hand, r to replay the last hand, or e to end game: ",
                response = raw_input()
        elif response=="e":
            return None
        else:
            print "Invalid command."
            print "Enter n to deal a new hand, r to replay the last hand, or e to end game: ",
            response = raw_input()
            

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
   # Create a new variable to store the maximum score seen so far (initially 0)
    total = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    score = 0
    # For each word in the wordList
    for i in wordList:
        # If you can construct the word from your hand
        if isValidWord(i, hand, wordList):
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            
            # Find out how much making that word is worth
            score = getWordScore(i, n)
            # If the score for that word is higher than your best score
            if score>total:
                total = score
                bestWord = i
                # Update your best score, and best word accordingly


    # return the best word you found.
    return bestWord

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0 
 
    while calculateHandlen(hand)!=0:
        print "Current Hand: ",
        for letter in hand.keys():
            for j in range(hand[letter]):
                
                print letter,              # print all on the same line
        print
        def compChooseWord(hand, wordList, n):
            """
            Given a hand and a wordList, find the word that gives 
            the maximum value score, and return it.

            This word should be calculated by considering all the words
            in the wordList.

            If no words in the wordList can be made from the hand, return None.

            hand: dictionary (string -> int)
            wordList: list (string)
            returns: string or None
            """
           # Create a new variable to store the maximum score seen so far (initially 0)
            total = 0
            # Create a new variable to store the best word seen so far (initially None)  
            bestWord = None
            score = 0
            # For each word in the wordList
            for i in wordList:
                # If you can construct the word from your hand
                if isValidWord(i, hand, wordList):
                # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
                    
                    # Find out how much making that word is worth
                    
                    score = getWordScore(i, n)
                    # If the score for that word is higher than your best score
                    if score>total:
                        total = score
                        bestWord = i
                        # Update your best score, and best word accordingly


            # return the best word you found.
            return bestWord
        bestword = compChooseWord(hand, wordList, n)
        if bestword==None:
            score = 0
            break
        else:
            score = getWordScore(bestword, n)
            total = total + score
            hand = updateHand(hand, bestword)
            print "\""+bestword+"\" earned "+str(score) +" points. Total: "+str(total)+" points \n"
     
       
    
    print "Total score: "+ str(total) + " points."

def playGame2(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    def response():
        print "Enter n to deal a new hand, r to replay the last hand, or e to end game: ",
        res = raw_input()
        return res
    
    def mode():
        print "Enter u to have yourself play, c to have the computer play: ",
        mod = raw_input()
        return mod
    
    res = response()

    n = HAND_SIZE
    hand = None
    while(True):
        
        if res=="e":
            break
        elif res=="n":
            hand = dealHand(n)
            mod = mode()
            while(True):
                if mod=="u":
                    playHand(hand, wordList, n)
                    break
                elif mod=="c":
                    compPlayHand(hand, wordList, n)
                    break
                    
                else:
                    print "Invalid Command\n"
                    mod = mode()
            res = response() 
            
        elif res=="r":
           
            if hand!=None:
                mod = mode()
                while(True):
                    if mod=="u":
                        playHand(hand, wordList, n)
                        break
                    elif mod=="c":
                        compPlayHand(hand, wordList, n)
                        break
                        
                    else:
                        print "Invalid Command\n"
                        mod = mode()
            else:
                print "You have not played a hand yet. Please play a new hand first!"
              
            res = response()     
            
        else:
            print "Invalid Command\n"
            res = response()
    
   