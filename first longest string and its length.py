##-- You are given an array(list) strarr of strings and an integer k.
#  Your task is to return the first longest string consisting of k consecutive strings taken in the array.
##-  strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
##-          Concatenate the consecutive strings of strarr by 2, we get:
##-          treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
##-          folingtrashy ("12)  concatenation of strarr[1] and strarr[2]
##-          trashyblue   ("10)  concatenation of strarr[2] and strarr[3]
##-          blueabcdef   ("10)  concatenation of strarr[3] and strarr[4]
##-          abcdefuvwxyz ("12)  concatenation of strarr[4] and strarr[5]
##-          Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
##-          The first that came is "folingtrashy" so 
##-          longest_consec(strarr, 2) should return "folingtrashy".







star = ["tree", "filing", "trashy", "blue", "Hafiz", "Arslan", "Shafique"]
newList = []
for i in range(0, len(star)-1):
    index_limit=star[i:i+2]              ## index limit to join
    jointed = ''.join(index_limit)
    newList.append(jointed)
    longest = max(newList, key=len)
print(f"first longest String is: {longest} and its size is {len(longest)}")
