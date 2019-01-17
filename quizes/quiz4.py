wordlist  = ['run', 'file', 'options', 'window', 'ruun']
lStr = 'nru'

def findAll (wordlist, lStr):
    result = []
    sortedL = sorted (lStr)
    
    for word in wordlist:
        sortedW = sorted (word)
        print sortedW
        if sortedW == sortedL:
            result.append(sortedW)
    return result
    print result

findAll (wordlist, lStr)
