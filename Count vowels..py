##  5.	    Count Vowels
##  Write a Python function that takes a string
##  as input and returns the count of vowels
##  (a, e, i, o, u) in the string (case-insensitive).





str1=" shafique"
vowels=['a','e','i','o','u']

filtered_ob=filter(lambda ch:ch in vowels, str1)
print(list(filtered_ob))
