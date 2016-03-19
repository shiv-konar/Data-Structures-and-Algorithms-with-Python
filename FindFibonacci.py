#encoding=utf8
'''
The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.

fibonacci(0) → 0
fibonacci(1) → 1
fibonacci(2) → 1

http://codingbat.com/prob/p120015
'''

def FindFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FindFibonacci(n - 1) + FindFibonacci(n - 2)

print "fibonacci(%d) -> %.0f" %(0, FindFibonacci(0))
print "fibonacci(%d) -> %.0f" %(1, FindFibonacci(1))
print "fibonacci(%d) -> %.0f" %(2, FindFibonacci(2))
print "fibonacci(%d) -> %.0f" %(3, FindFibonacci(3))
print "fibonacci(%d) -> %.0f" %(10, FindFibonacci(10))
print "fibonacci(%d) -> %.0f" %(20, FindFibonacci(20))
print "fibonacci(%d) -> %.0f" %(40, FindFibonacci(40))