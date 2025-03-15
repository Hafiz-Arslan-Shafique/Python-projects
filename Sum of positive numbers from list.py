## You get an array of numbers,
## and return the sum of all of the positive ones.
## Example [1, -4, 7, 12] => 1+7+12 = 20. 
## If there is nothing to sum return 0. You can not use the if statement.


list_of_numbers = [2, -4, 9, 36]
filtr=filter(lambda i: i > 0, list_of_numbers)
print(sum(list(filtr)))
