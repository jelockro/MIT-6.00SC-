# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random
import numbers

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def shiftSingleCase(alphabet, shift):
    #creates a shifted dictionary
    shifted = {}
    #creates an index so that when the end of the list is reached
    #index goes to the beginning
    index = 0
    lastIndex = len(alphabet) -1        #indices range from 0 to [len(list) -1]
    
    #fill the dictionary with the alphabets used as keys and the alphabet[index] as values
    for char in alphabet:
        if (index + shift) > lastIndex:       #reached the end of the list
            charIndex = abs(lastIndex - (index + shift)) - 1
        else:
            charIndex = index + shift
        #add to the dict
        shifted.update({char: alphabet[charIndex]})
        index += 1
    return shifted    



def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    ### TODO.
        
    
    # all possible transformable characters
    lowercase_and_space = string.ascii_lowercase + ' '
    uppercase_and_space = string.ascii_uppercase + ' '

    # shifting through cases separately, will this create an error for double ' '
    shifted_lowercase_and_space = shiftSingleCase(lowercase_and_space, shift)
    shifted_uppercase_and_space = shiftSingleCase(uppercase_and_space, shift)

    # Construct Caesar cipher dictionary
    # Add uppercase letters first so ' ' will be overwritten to point to lowercase letter
    shifted = {}
    shifted.update(shifted_uppercase_and_space)
    shifted.update(shifted_lowercase_and_space)
    return shifted

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    return build_coder(shift)
    
def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    return build_coder(-shift)
 

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    ### TODO.
    codedText = ''
    for char in text:
        if char in coder:
            codedText += coder[char]
        else:
            codedText += char
    return codedText 

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    ### TODO.
    # My original code for this section, too cumbersome
    #coder=build_coder(shift)
    #encodedText = ''
    #for i in text:
    #    if i in coder:
    #        encodedText += coder[i]
    #    else:
    #        encodedText += i
    #return encodedText

    return apply_coder(text, build_encoder(shift))
    
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    ### TODO

 ##### This is my original code:   
##    selection = {}
##    for shift in range(28):
##        encodedText = apply_coder(text, build_decoder(shift))
##        letters_and_space = string.ascii_lowercase + string.ascii_uppercase + ' '
##        cleanString = ''
##        for i in encodedText:
##            if i in letters_and_space:
##                cleanString += i
##        cleanString=cleanString.lower()
##        listofwords=string.split(cleanString)
##        counter = 0
##        for word in listofwords:
##            if is_word(wordlist, word) == True:
##                counter += 1
##        selection[n] = counter
##    return max(selection, key=lambda key: selection[key])

 ##### Code I would like to try out from morganwilde
 ##### How are punctuation handled?
 ##### answer: the is_word function strips words of punctuation
    
    bestGuess = (0,0,0)
    for shift in range(0, 28):
        shiftedText = apply_coder(text, build_decoder(shift))
        words = shiftedText.split(' ')
        
    ## len(words) is how many 'words' created by the split
    ## if all these 'words' are found in wordlist
    ## it is assumed that the cipher has been decoded

        allWords = len(words)
        foundWords = 0

        iterations = 0
    ## test to see if words are in wordlist
        for word in words:
            if is_word(wordlist, word) and iterations == foundWords and word != 'i':
                #print wordlist         #debug
                foundWords += 1
                if bestGuess[1] < foundWords or bestGuess[2] < len(word):
                    bestGuess = (shift, foundWords, len(word))
                    #print bestGuess    #debug
            iterations += 1
    ## check if it is equal to the number of words found
        if foundWords == allWords:
            return shift ##code ends and the shift used is returned
    return bestGuess
    
#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.
    ## n is a tuple of two indices
    ## n[0] = index to start shift
    ## n[1] = the shift
    encodedtext=text
    for n in shifts:
        encodedtext= encodedtext[:n[0]] + apply_shift(encodedtext[n[0]:],n[1])
    return encodedtext


  
##    coder = build_coder(shifts[1])
##    encodedText = ''
##    for i in text:
##        if i in coder:
##            encodedText += coder[i]
##        else:
##            encodedText += i
##    return encodedText 
#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
X = 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
##encodedpractice = apply_shifts(practicetext, [(8,3), (14,2)])
shiftlist =[]
found_words=[]
def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """    
    ### TODO.
    #best case scenario is no shifts, then testing for one shift
    #start will be placed arbitrarily and then it will recursively move backwards
    #rationale is that we want to find exactly where shift occurs
    #shifting will be done left to right up until the start point
    #?how do we check for that?
    ###
    
    ##print 'encoded text is:', encodedpractice #debug
    
    while True:
        counter = 0
        specialA =[]
        specialdecoded =[]
        for shift in range(27):
            #print 'shift is:', shift #debug
            newstart = start
            decoded_text = apply_shift(text[newstart:], -shift)
            #print 'decoded text is:', decoded_text #debug

	## the 's' variable will include properly decoded words:
	## 'text[:newstart]', and will include the accumulative shifts done by recursion

            s = text[:newstart] + decoded_text  

	#####    
	##split the text to be tested for individual words for testing
	##Look for spaces beginning at the location specified by the start parameter
	#####
	
            splitDecoded = decoded_text.split()
            first_word = splitDecoded[0]
            #print '(1)first_word:', first_word
		
	#####
	##if split_text_for_test[0] is a word then we recursively run this algorithm
	##on the same text, but starting at the location where the space was found
	#####

            if is_word(wordlist, decoded_text):
                  
                #print 'appended print list with "shift, newStart";', shiftlist #debug
                #print 'Have we found the last word?:', decoded_text    #debug
                if shift !=0:
                    shiftlist.append((newstart,shift))
                break
                    
            if is_word(wordlist, first_word): 
                #print 'entered is_word if statement'

                #if counter > 0:
                    #if len(first_word) < len(found_words[len((found_words)-1)])
                    
                if len(first_word) < 5:
                    #print 'MIGHT HAVE FOUND A WORD:', first_word
                    found_words.append(first_word)
                    specialdecoded.append(decoded_text)
                    #print 'special decoded', specialdecoded
                    counter += 1
                    if counter == 1:
                        #print 'debug start and shift:', newstart, shift
                        specialA.append((newstart, shift))
                    #print 'specialA:', specialA                     
                    #print 'counter:', counter
                    #print 'found_words:', found_words
                    continue
                
                else:                
                    #print 'entered elif'
                    #print counter
                    if shift !=0:
                        shiftlist.append((newstart,shift))   
                    newstart +=  len(first_word) + 1
                    #print 'found a word:', first_word      #debug
                    found_words.append(first_word)
                    #print 'found_words', found_words  
                    #print counter
                    #print 'shift when word was found:', shift       #debug
                    #print 'appended print list with "shift, newStart";', shiftlist     #debug
                    return find_best_shifts_rec(wordlist,s, newstart)

            #print 'anyone here'
            if shift > 25 and counter > 0:
                #print 'entered special condition'
                #print 'first word:', first_word
               # print 'found_words:', found_words
                #print 'len(first_word):', len(first_word)
                #print 'len(found_words[-1]):', len(found_words[-1])
                
                if is_word(wordlist, first_word):
                    if len(first_word) < len(found_words[-1]):
                        newstart = specialA[-1][0]
                        shift = specialA[-1][1]
                #decoded_text = apply_shift(text[newstart:], -shift)
                #print 'decoded_text:', decoded_text
                #print 'counter:', counter
                if counter == 1:
                    specialdecoded = specialdecoded[0]

                if counter > 1:
                    if len(found_words[-2]) > len (found_words[-1]):
                        specialdecoded = specialdecoded[-2]
                        found_words.pop(-1)
                    else:
                        specialdecoded = specialdecoded[-1]
                        found_words.pop(-2)
                            
                s = text[:newstart] + specialdecoded
                splitDecoded = specialdecoded.split()
                first_word = splitDecoded[0]
                #print '(2)first_word:', first_word
                if is_word(wordlist, first_word): 
                    if shift !=0:
                        shiftlist.append((newstart,shift))   
                newstart +=  len(first_word) + 1
                #print 'found a word:', first_word      #debug
                found_words.pop()
                found_words.append(first_word)
                #print 'shift when word was found:', shift       #debug
                #print 'appended print list with "shift, newStart";', shiftlist     #debug
                return find_best_shifts_rec(wordlist,s, newstart)

            #print 'first_word', first_word
              
        #print 'approaching the break'  debug
        
        break           
    ## end of recursing loop and shifting range
    ## return the list of shifts
    #print ' '.join(found_words)
    return shiftlist
    

def decrypt_fable():
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.
    X = get_fable_string()
    find_best_shifts_rec(wordlist, X, 0)
    #
    reverseList =[]
    for i in shiftlist:
        newShift = -i[1]
        reverseList.append([i[0],newShift])
    print reverseList
    print apply_shifts(X,reverseList)
    
    


    
#What is the moral of the story?
#
#
#
#
#

