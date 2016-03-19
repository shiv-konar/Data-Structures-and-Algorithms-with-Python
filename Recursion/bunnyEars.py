#encoding=utf8
'''
We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively
 (without loops or multiplication).

bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4

http://codingbat.com/prob/p183649
'''

def bunnyEars(n):
    if n == 0:
        return 0
    else:
        return 2 + bunnyEars(n - 1)

print "bunnyEars(%d) -> %d"%(0, bunnyEars(0))
print "bunnyEars(%d) -> %d"%(1, bunnyEars(1))
print "bunnyEars(%d) -> %d"%(2, bunnyEars(2))
print "bunnyEars(%d) -> %d"%(10, bunnyEars(10))