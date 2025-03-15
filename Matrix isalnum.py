## You are given a N x M grid of strings.
##  It consists of alphanumeric spaces and characters,
##  spaces, and symbols (!,@,#,$,%,&). To decode a string,
##  you need to read each column and select only alphanumeric characters and concatenate them. 
## If there are symbols between two alphanumeric characters of the decoded script,
## then replace them with empty string ‘’. 
## You need to do this without using the if condition.

##  Input:
##  7 3
##  Tsi
##  h%x
##  i #
##  sM 
##  $a 
##  #t%
##  ir!

##  Output
##  This is Matrix#  %!



matrix = [
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "ir!"
]

def isalnum(x):
        return x.isalnum()

for i in range(len(matrix[0])):
    for val in matrix:
        filt=filter(isalnum,val[i])        
        result=''.join(filt)
        print(result,end=' ')
