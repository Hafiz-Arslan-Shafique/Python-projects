##  5.	  Find Common Elements
##  Write a Python function that takes two lists
##  and returns a list of their common elements,
##  sorted in ascending order.



def common_elem(list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
            list3.sort()
    return list3

list=[7,6,5,4,3,2,1]
list0=[4,5,6,7,8,9,10]
print(common_elem(list,list0))


