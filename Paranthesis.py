##--    Write a function that takes a string of parentheses, 
##--    and determines if the order of the parentheses is valid.
##--    The function should return true if the string is valid,
##--    and false if it's invalid.
##--    
##--    "()"              =>  true
##--    ")(()))"          =>  false
##--    "("               =>  false
##--    "(())((()()))(())"  =>  true



def parentheses(val):
    left, right = 0, 0
    for i in val:
        if i == "(":
            left += 1
        else:
            right += 1
        if left < right:
            break
    if left == right:
        return True
    else:
        return False

print(parentheses("((()))"))
print(parentheses("(())((()()))(())"))
print(parentheses("(()) ((()()) ())"))


