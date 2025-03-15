##-- Sum all the numbers of a given array ( cq. list ), 
##-- except the highest and the lowest element ( by value, not by index! ).
##--  You can not use the if statement.

#------ Example
####--- { 6, 2, 1, 8, 10 } => 16



list_of_numbers = [1, 2, 3, 4, 7, 15, 25]
list_of_numbers.remove(max(list_of_numbers))
list_of_numbers.remove(min(list_of_numbers))
print(sum(list_of_numbers))
