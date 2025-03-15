##  1.	     Find the Average
##  Write a Python function that takes a list of numbers as input
##  and returns their average. Handle empty lists by returning None.




def average(list):
    if len(list)!=0:
        sum=0
        for i in list:
             sum+=i
        print(sum/len(list))
    else:
        print("None")
       
list=[]
average(list)
