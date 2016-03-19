#encoding=utf8
'''
Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).

factorial(1) → 1
factorial(2) → 2
factorial(3) → 6

http://codingbat.com/prob/p154669
'''
def RecursiveFactorial(n):
    if n == 0:
        return 1 #0! = 1
    else:
        return n * RecursiveFactorial(n - 1) #n! = n * (n-1)!

print "factorial(%d) -> %d" %(0, RecursiveFactorial(0))
print "factorial(%d) -> %d" %(5, RecursiveFactorial(5))
print "factorial(%d) -> %d" %(10, RecursiveFactorial(10))
print "factorial(%d) -> %.0f" %(20, RecursiveFactorial(20))