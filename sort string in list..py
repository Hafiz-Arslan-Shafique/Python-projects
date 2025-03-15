## 2.	Custom Sorting
## Write a Python function that sorts a list of strings
## based on their lengths. If two strings have the same length,
## sort them alphabetically.



li=['arslan', 'Haafiz', 'adnan', 'shafique']
sort=sorted(li,key=lambda x :(len(x),x.lower()))
print(sort)

