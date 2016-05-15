# Hangman
# Ronak Pradeep
import string
import random
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading the word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    b=0
    for c in secretWord:
        if c in lettersGuessed:
            b=1
        else:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    g=''
    for i in range(len(secretWord)):
     if secretWord[i] in lettersGuessed:
      g=g+str(secretWord[i])
     else:
      g=g+'_'
    return g



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    la='abcdefghijklmnopqrstuvwxyz'
    gaa=''
    t=0
    for dee in la:
     if dee in lettersGuessed:
      t=0
     else:
      gaa=gaa+dee
    return gaa

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
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-----------'
    lettersGuessed=[]
    mistakesMade=0
    availableLetters=getAvailableLetters(lettersGuessed)
    while getGuessedWord(secretWord, lettersGuessed)!=secretWord:
        print 'You have ' + str(8-mistakesMade) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        user_input=raw_input('Please guess a letter: ')
        if user_input not in getAvailableLetters(lettersGuessed):
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
        elif user_input in secretWord:   #situation where guess is right
            lettersGuessed+=user_input
            print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
            if(isWordGuessed(secretWord, lettersGuessed)==True):
                print "Congratulations, you won!"
                break
        else: #situation where guess is wrong
            lettersGuessed+=user_input
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
            mistakesMade+=1
            if mistakesMade==8:
                print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
                break
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
