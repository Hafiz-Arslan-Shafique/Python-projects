##--   Our football team has finished the championship. 
###--  Our team's match results are recorded in a collection of strings. 
###--  Each match is represented by a string in the format x:y,
###--  where x is our team and y is our opponents score. 
###--  The rules to calculate score is 

##--   1: If x > y: 3 points
##--   2: If x < y: 0 point
##--   3: If x = y: 1 point

##--   We need to write a function that takes this collection 
###--  and returns the number of points
###--  our team (x) got in the championship by the rules given above.




def Score(Match_Results):
    points = 0
    for j in Match_Results:
        x, y = map(int, j.split(':'))
        if x > y:
            points += 3
        elif x == y:
            points += 1
    return points


results = []
num = int(input("Enter the number of matches"))
for i in range(1, num+1):
    match_result = input(f"Enter the match {i}'s result")
    results.append(match_result)
totalpoints = Score(results)
print(f"your team earned {totalpoints} points in the championship.")

