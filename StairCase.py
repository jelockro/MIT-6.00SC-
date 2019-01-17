import sys




def rotateMatrix(matrix, k, queries):
    if k > len(matrix):
        k = k % len(matrix)
        #print k
    matrix = matrix[len(matrix) - k:] +  matrix[:len(matrix) - k]
    print matrix
    for a0 in xrange(q):
        #print matrix
        m = int(raw_input().strip())
        print matrix[m]


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
#for a0 in xrange(q):
#    m = int(raw_input().strip())
rotateMatrix(a, k, q)

