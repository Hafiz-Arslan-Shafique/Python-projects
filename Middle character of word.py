##-- You are going to be given a word.
##--  Your job is to return the middle character of the word.
##--  If the word's length is odd, return the middle character.
##--  If the word's length is even, return the middle 2 characters.

##--          test => es
##--          testing => t
##--          A => A






name ="arslanshafique"
n = len(name)
if n % 2 == 0:
    print(name[int(n/2) - 1:int(n/2) + 1])
else:
    print(name[int(n / 2)])

