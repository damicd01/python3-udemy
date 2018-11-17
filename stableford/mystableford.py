def shots_per_hole(hcp,index):
    if hcp > 18 and hcp % 18 >= index:
        return 2
    elif hcp > 18 and hcp % 18 < index:
        return 1
    elif hcp == 18:
        return 1
    elif hcp < 18 and hcp % 18 <= index:
        return 1
    else:
        return 0

sf_score = { -4:6, -3:5, -2:4, -1:3, 0:2, 1:1, 2:0 }

def stableford_score(hcp,par,score,index):
    if hcp > 18 and hcp % 18 >= index:
        par = par + shots_per_hole(hcp,index)
        return(sf_score.get(score-par))
    elif hcp > 18 and hcp % 18 < index:
        par = par + shots_per_hole(hcp,index)
        return(sf_score.get(score-par))
    elif hcp == 18:
        par = par + shots_per_hole(hcp,index)
        return(sf_score.get(score-par))
    elif hcp < 18 and hcp % 18 >= index:
        par = par + shots_per_hole(hcp,index)
        return(sf_score.get(score-par))
    else:
        return 0

stableford_points = 0
starting_hole = 1

hcp = int(input("What is your hcp = "))
print("")

for hole in range(0,18):
    par = int(input("Hole {} par = ".format(starting_hole)))
    score = int(input("Hole {} score = ".format(starting_hole)))
    index = int(input("Hole {} stroke index = ".format(starting_hole)))
    print("")
    stableford_points += stableford_score(hcp,par,score,index)
    starting_hole += 1

print("Your stableford score is", stableford_points)
