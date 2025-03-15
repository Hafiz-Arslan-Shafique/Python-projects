##   3.	     Factorial Calculation
##   Write a Python function that calculates
##   the factorial of a given non-negative integer using recursion.



def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)

print(fact(4))
