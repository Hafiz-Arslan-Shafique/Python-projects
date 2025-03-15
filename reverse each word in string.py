##-- Complete the function that accepts a string parameter,
##-- and reverses each word in the string. 
##-- All spaces in the string should be retained.

##--  "This is an example!" ==> "sihT si na !elpmaxe"
##-- "double  spaces"      ==> "elbuod  secaps"





def reverse_word_of_string(Str):
    words = (Str.split(" "))
    rev = ' '.join(val[::-1] for val in words)
    print(rev)

string="My name is Arslan"
reverse_word_of_string(string)