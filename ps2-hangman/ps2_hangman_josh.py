# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

#//Main Program
def hangman():
    wordlist=load_words()
    hiddenWord = choose_word(wordlist).lower() #this is the computer chosen word
    print hiddenWord
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is ", len(hiddenWord),"letters long."
    wrongGuesses = 8
    guessedLetters=""
    while (True):   #this is the main loop, which will terminate when the game \
                    #over
        print "------------"
        print "You have ", wrongGuesses, "left."
        print "Available letters: ", get_unguessed(guessedLetters)
        newGuess = raw_input("Please enter your guess: ").lower() #get guess
        guessedLetters += newGuess      #add guess to guessedLetters
        wrongGuesses = test_guess(wrongGuesses,newGuess,hiddenWord,guessedLetters)
        if wrongGuesses == 0:
            print "Sorry, no more turns. The word is:", hiddenWord
            break
        if get_blanks_and_guesses (hiddenWord, guessedLetters) == hiddenWord:
            print "Congratulations! You Win!"
            break  
        


#//Modules
#-------------------------------------------

#function to get guess from player
def test_guess(wrongGuesses,newGuess,hiddenWord,guessedLetters):
    if newGuess in hiddenWord:
        print "Good Guess:", get_blanks_and_guesses(hiddenWord, guessedLetters)
    else:
        print "Oops! That letter is not in my word:" , get_blanks_and_guesses(hiddenWord, guessedLetters)
        wrongGuesses -= 1
        print wrongGuesses
    return wrongGuesses


#funtion to fill in blanks and letters, and determine if the word has been guessed
#and then terminate the loop with a False type
def get_blanks_and_guesses (hiddenWord, guessedLetters):
    '''compare hidden word with guesses'''
    visible = ""  #a string of blanks and letters that show the prorgress of guesses
    for letter in hiddenWord:
        if letter in guessedLetters:
            visible += letter
        else:
            visible += " _ "
    else:
        return visible

#create a function to show letters that have not beem guessed using string.lowercase
def get_unguessed(guessedLetters):
    '''sting.lowercase[:26] will create a list of all letters\
    compare a list,tuple,or dic named guessedLeters with string.lowercase to return a list that omits the \
    guessedLetters'''
    lettersLeft=""
    for letters in string.lowercase[:26]:
        if letters not in guessedLetters:
            lettersLeft += letters
    return lettersLeft

hangman()

            
    


