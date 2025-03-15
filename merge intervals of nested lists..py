# Write a Python function that takes a list of intervals (e.g., [[1, 3], [2, 4], [5, 7]]) and merges overlapping intervals.
# Example: Input:  → Output: [[1, 4], [5, 7]].


a=[[1, 3], [2, 4], [5, 7]]
a.sort() 
print(a)
s = [a[0]] 
for i in range(1, len(a)): 
    if a[i][0] <= s[-1][1]:  
        s[-1][1] = max(s[-1][1], a[i][1])  
    else:
        s.append(a[i])  
print(s)