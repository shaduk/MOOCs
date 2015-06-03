'''HANGMAN PART 1: IS THE WORD GUESSED?  (5/5 points)
Please read the Hangman Introduction before starting this problem. The helper functions you will be creating in the next three exercises are simply suggestions, but you DO have to implement them if you want to get points for this Hangman Problem Set. If you'd prefer to structure your Hangman program in a different way, feel free to redo this Problem Set in a different way. However, if you're new to programming, or at a loss of how to construct this program, we strongly suggest that you implement the next three helper functions before continuing on to Hangman Part 2.

We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print isWordGuessed(secretWord, lettersGuessed)
False
For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
'''

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count+=1
    if count==len(secretWord):
        
        return True
    else:
        return False
        
        
'''PRINTING OUT THE USER'S GUESS  (5/5 points)
Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getGuessedWord(secretWord, lettersGuessed)
'_ pp_ e'
When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

'''

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    ans = ''
    for i in secretWord:
        if i in lettersGuessed:
            ans = ans + i
        else:
            ans = ans + '_ '
    return ans

'''PRINTING OUT ALL AVAILABLE LETTERS  (5/5 points)
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getAvailableLetters(lettersGuessed)
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:

>>> import string
>>> print string.ascii_lowercase
abcdefghijklmnopqrstuvwxyz
'''

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    masterlist1 = string.ascii_lowercase
    masterlist2 = ''
    for i in masterlist1:
        if i in lettersGuessed:
            masterlist2 = masterlist2 + ''
        else:
            masterlist2 = masterlist2 + i
    return masterlist2
    
'''HANGMAN PART 2: THE GAME  (15/15 points)
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).
Sample Output
The output of a winning game should look like this...
And the output of a losing game should look like this...

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to raw_input to get the user's guess.
'''

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+ str(len(secretWord)) +" letters long."
    guesses = 8
    lettersGuessed = []
    mistakesMade = 0
    print "----------------------------------------"
    while (guesses!=0 and isWordGuessed(secretWord, lettersGuessed) == False):
        
        print "You have "+str(guesses)+" guesses left"
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        print "Please guess a letter: ",
        guess = raw_input()
        guesslower = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        elif guess in secretWord:
            lettersGuessed.append(str(guesslower))
            print "Good guess: "+ getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(str(guesslower))
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guesses = guesses - 1
            mistakesMade = mistakesMade + 1
        
        print "-------------------------------------------------------------"
    if isWordGuessed(secretWord, lettersGuessed)==True:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was "+secretWord


#HANGMAN - COMPLEX TESTS  (20/20 points)

# When your hangman function passes the checks in the previous
# box, paste your function definition here to test it on harder 
# input cases.

def hangmancomplex(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+ str(len(secretWord)) +" letters long."
    guesses = 8
    lettersGuessed = []
    mistakesMade = 0
    print "----------------------------------------"
    while (guesses!=0 and isWordGuessed(secretWord, lettersGuessed) == False):
        
        print "You have "+str(guesses)+" guesses left"
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        print "Please guess a letter: ",
        guess = raw_input()
        guesslower = guess.lower()
        if guesslower in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        elif guesslower in secretWord:
            lettersGuessed.append(str(guesslower))
            print "Good guess: "+ getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(str(guesslower))
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guesses = guesses - 1
            mistakesMade = mistakesMade + 1
        
        print "-------------------------------------------------------------"
    if isWordGuessed(secretWord, lettersGuessed)==True:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was "+secretWord
        
        