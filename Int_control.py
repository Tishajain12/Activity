'''Design and write a program to calculate Net Run Rate scored by the two teams use controls 
to validate a condition such that the team with the higher run rate will top the points table 
and also think for the tie-breaker condition.'''

t1_score = int(input("Total runs scored by Team 1: "))
t1_over= int(input("Total overs faced by Team 1: "))
t1_run = int(input("Total runs conceded by Team 1: "))
t1_bowled= int(input("Total overs bowled by Team 1: "))
t2_score = int(input("Total runs scored by Team 2: "))
t2_over = int(input("Total overs faced by Team 2: "))
t2_run = int(input("Total runs conceded by Team 2: "))
t2_bowled= int(input("Total overs bowled by Team 2: "))
t1_Nrr = (t1_score / t1_over) - (t1_run / t1_bowled)
print("Team1 Net Run Rate=",round(t1_Nrr,2))
t2_Nrr = (t2_score / t2_over) - (t2_run / t1_bowled)
print("Team2 Net Run Rate=",round(t2_Nrr,2))
if t1_Nrr > t2_Nrr:
    print("Team 1 has a higher Net Run Rate and tops the points table.")
elif t2_Nrr > t1_Nrr:
    print("Team 2 has a higher Net Run Rate and tops the points table.")
else:
    t1_wc = int(input("wickets taken by Team 1: "))
    t2_wc = int(input("wickets taken by Team 2: "))
    
    if t1_wc > t2_wc:
        print("Team 1 has a higher Net Run Rate and more wickets and tops the points table")
    elif t2_wc > t1_wc:
        print("Team 2 has a higher Net Run Rate and more wickets and tops the points table")
    else:
        print("Both teams have the same Net run rate and wickets taken and are tied on points")

