#encoding=utf8
'''
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

count7(717) → 2
count7(7) → 1
count7(123) → 0

http://codingbat.com/prob/p101409
'''
def count7(n):
    if n <= 9 and n % 7 == 0:  #check if we have reached the first digit starting from the units place and if the first digit is 7
        return 1
    elif n <=9 and n % 7 != 0:  #check if we have reached the first digit starting from the units place and if the first digit is not 7
        return 0
    else:  #check if the units place digit is a 7 or not
        if (n % 10) % 7 == 0:
            return 1 + count7(n / 10)
        else:
            return 0 + count7(n / 10)

print count7(717)
print count7(798734897)
print count7(123)