def logBase2(n):
 """assumes that n is a positive int
 returns a float that approximates the log base 2 of n"""
 import math
 return math.log(n, 2)

def f(n):
    if n < 1:
        return
    curDigit = int(logBase2(n))
    ans = 'n = '
    while curDigit >= 0:
        print "curDigit is:!", curDigit
        if n%(2**curDigit) < n:
            ans = ans + '1'
            print ans
            n = n - 2**curDigit
            print 'whle loop n=', n
        else:
            print "ans:" , ans
            ans = ans + '0'
            print "ans:", ans
        curDigit -= 1
    return ans
for i in range(3):
    print f(i) 
