s = 'mat'
def f(s):
    if len (s) <= 1:
        print 's=', s
        return s
    print 's[0]=', s[0]
    return f(f(s[1:])) + s[0]
	
