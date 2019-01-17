import string
import random
import numbers

def build_coder(shift):
    assert shift >= 0 and shift < 27, 'shift %s is not between 0 and 27' % shift
    assert isinstance(shift, numbers.Integral), 'shift is not an integer'

    coder = {}

    lowercase_and_space = string.ascii_lowercase + ' '
    uppercase_and_space = string.ascii_uppercase + ' '

    #shift letters over shift many places

    shifted_lowercase_and_space = lowercase_and_space[shift:] + lowercase_and_space[:shift]
    shifted_uppercase_and_space = uppercase_and_space[shift:] + uppercase_and_space[:shift]

    #construct the cipher dictionary
    #if uppercase letters are added first, ' ' will be overwritten to point to lowercase
    #not sure why

    for i in range(len(uppercase_and_space)):
        coder[uppercase_and_space[i]] = shifted_uppercase_and_space[i]

    for i in range(len(lowercase_and_space)):
        coder[lowercase_and_space[i]] = shifted_lowercase_and_space[i]

    return coder
