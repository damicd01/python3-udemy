def stableford_points(hcp,par,index,score):
    sf_score = { -4:6, -3:5, -2:4, -1:3, 0:2, 1:1 }
    diff = score - par
    if hcp > 18 and index <= hcp % 18 and diff == -4:
        print ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -4:
        print ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -3:
        print ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -3:
        print ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -2:
        print ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -2:
        print ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -1:
        print ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -1:
        print ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 0:
        print ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 0:
        print ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 1:
        print ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 1:
        print ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -4:
        print ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -3:
        print ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -2:
        print ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -1:
        print ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 0:
        print ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 1:
        print ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index <= hcp % 18 and diff == -4:
        print ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -4:
        print ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -3:
        print ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -3:
        print ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -2:
        print ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -2:
        print ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -1:
        print ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -1:
        print ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 0:
        print ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 0:
        print ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 1:
        print ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 1:
        print ((sf_score.get(diff)))
    else:
        print('0')

hcp = 

stableford_points(15,4,15,4)
