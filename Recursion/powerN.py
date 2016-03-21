#encoding=utf8
'''
Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power,
so powerN(3, 2) is 9 (3 squared).

powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27

http://codingbat.com/prob/p158888
'''
def powerN(base, power):
    if power == 1:
        return base
    else:
        return base * powerN(base, power - 1)

print "powerN(%d, %d) -> %d"%(3, 1, powerN(3, 1))
print "powerN(%d, %d) -> %d"%(3, 2, powerN(3, 2))
print "powerN(%d, %d) -> %d"%(3, 3, powerN(3, 3))
print "powerN(%d, %d) -> %d"%(3, 3, powerN(4, 4))
print "powerN(%d, %d) -> %d"%(15, 6, powerN(15, 6))