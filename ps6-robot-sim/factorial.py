import sys


n = int(raw_input().strip())

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    print num
factorial(n)
