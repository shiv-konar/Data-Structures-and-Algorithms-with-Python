#encoding=utf8
'''

We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on.
Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.

triangle(0) → 0
triangle(1) → 1
triangle(2) → 3

http://codingbat.com/prob/p194781
'''

def TriangleBlocks(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + TriangleBlocks(n - 1)

for i in range(0, 11):
    print "triangle(%d) -> %d" %(i, TriangleBlocks(i))
