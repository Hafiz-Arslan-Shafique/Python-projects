##--   Complete the solution so that 
##--   the function will break up camel casing, 
##--   using a space between words.

##--   "camelCasing"  =>  "camel Casing"
##--   "identifier"   =>  "identifier"
##--   ""   =>  ""





real = "camelCase"
listed = list(real)
for i in reversed(range(len(listed))):
    if listed[i].isupper():
        listed.insert(i, ' ')
spaced_string = ''.join(listed)
print(spaced_string)

