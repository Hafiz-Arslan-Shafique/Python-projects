##  2.	  Check Palindrome
##  Write a Python function to check
##  if a given string is a palindrome 
##  (reads the same forwards and backwards).
##  Ignore case and spaces.



def check_palindrome(string):
    rev_str=''.join(string[::-1])
    if rev_str == string:
        print(f"the given string '{string}' is palindrome ")
    else:
        print(f"the given string '{string}' is not palindrome ")

string="arsral"
check_palindrome(string)


