from ps3a import *
import time
from perm import *
from robotart import robot_print

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    permDict ={}
    perms =[]
    print "Let me think..."
    for num in range(hand_size+1):
        perms.extend(get_perms(hand, num))
    for i in perms:
        if is_valid_word(i,hand, word_list) == True:
            permDict[get_word_score(i, hand_size)]= i
            print ".",
    permlist = sorted(permDict.keys(), reverse=True)
    if permlist == []:
        return '0'
    bestWord = permDict[permlist[0]]
    return bestWord
    print "the word with the highest score of", permlist[0], "is %s" % bestWord
    
    
        
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    totalScore=0
    lastHand = dict (hand)
    while True:
        display_hand(hand)
        if hand == '':
            print 'Nailed It!'
        word = comp_choose_word(hand, word_list)
        if word == '0':
            print "Darn, I have no more choices, please end this turn while I nap."
            return lastHand
            return False
        elif is_valid_word(word, hand, word_list) == False:
            print "Invalid word, please try again."
        else:
            print 'I have chosen for my illustrious word:', word
            totalScore += get_word_score(word,hand_size)
            print '"%s" earned %s points. Total: %s points.' % (word, get_word_score(word, hand_size), totalScore)
            update_hand(hand, word)
            


#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    lastHand = {}
    while True:
        status = raw_input("Please enter 'n', for new hand; 'r' for replay of last hand; or 'e' to exit the game....:")
        if status == 'e':
            return False
        else:
            print "Please enter 'n', 'r' or 'e'."  
        if status == 'n' or 'r':
            playerStatus = raw_input("Please enter 'u' to play yourself or 'c' to watch computer play:")
            if playerStatus == 'u' and status == 'n':
                lastHand = play_hand(deal_hand(hand_size), word_list)
            if playerStatus == 'u' and status == 'r':
                play_hand(lastHand, word_list)
            if playerStatus == 'c' and status == 'n':
                lastHand = comp_play_hand(deal_hand(hand_size), word_list)
            if playerStatus == 'c' and status == 'r':
                comp_play_hand(lastHand, word_list)
          
#
# Build data structures used for entire session and play game
#
robot_print()
if __name__ == '__main__':
    word_list = load_words()
    hand_size=7
    play_game(word_list)
 
   
    
    
