def stableford_points(hcp,par,index,score):
    sf_score = { -4:6, -3:5, -2:4, -1:3, 0:2, 1:1, 2:0 }
    diff = score - par
    if hcp > 18 and index <= hcp % 18 and diff == -4:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -4:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -3:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -3:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -2:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -2:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -1:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -1:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 0:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 0:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 1:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 1:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 2:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 2:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -4:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -3:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -2:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -1:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 0:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 1:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 2:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index <= hcp % 18 and diff == -4:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -4:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -3:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -3:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -2:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -2:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -1:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -1:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 0:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 0:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 1:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 1:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 2:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 2:
        return ((sf_score.get(diff)))
    else:
        return '0'

stableford_score = 0
starting_hole = 1
hcp = int(input("What is your hcp = "))
course = input("Where did you play? ")

myfile = open("scorecard.txt", "w")
myfile.write(course)

for hole in range(0,2):
    par = int(input("Hole par = "))
    myfile.write(str(par))
    score = int(input("Hole score = "))
    myfile.write(str(score))
    index = int(input("Hole stroke index = "))
    myfile.write(str(index))
    stableford_score += stableford_points(hcp,par,index,score)

myfile.write(str(stableford_score))
print("Your stableford score is", stableford_score)
