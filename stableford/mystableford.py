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

stableford_points = 0

hcp = int(input("What is your hcp = "))


for hole in range(0,2):
    par = int(input("Hole par = "))
    score = int(input("Hole score = "))
    index = int(input("Hole stroke index = "))
    stableford_points += stableford_score(hcp,par,score,index)


print("Your stableford score is", stableford_points)
