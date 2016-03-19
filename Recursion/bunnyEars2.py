#encoding=utf8
'''

We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears.
The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot.
Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5

http://codingbat.com/prob/p107330
'''
def bunnyEars2(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return 2 + bunnyEars2(n - 1)  #even bunnies with 3 ears
    else:
        return 3 + bunnyEars2(n - 1)  #odd bunnies with 2 ears

print "bunnyEars2(%d) -> %d"%(0, bunnyEars2(0))
print "bunnyEars2(%d) -> %d"%(1, bunnyEars2(1))
print "bunnyEars2(%d) -> %d"%(2, bunnyEars2(2))
print "bunnyEars2(%d) -> %d"%(5, bunnyEars2(5))
print "bunnyEars2(%d) -> %d"%(10, bunnyEars2(10))
print "bunnyEars2(%d) -> %d"%(10, bunnyEars2(11))