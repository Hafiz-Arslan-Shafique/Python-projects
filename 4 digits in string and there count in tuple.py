##  You are given a string.
###   Suppose a character ‘c’ occurs 4 times in the string.
###   Replace these consecutive occurrences of the character 'c' with (4, c) in the string.


string="11222333344444555555"
count=1
str=string[0]
for i in range(1,len(string)):
    if string[i]==str:
        count+=1
    else:
        print(f"({count},{str})",end=" ")
        str=string[i]                                  #######========== question
        count=1

print(f"({count},{str})",end=" ")
