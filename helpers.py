
reputation_points: int = 0
folklore_points: int = 0
red_points: int = 0
lover_points: int = 0

def find_points_1(q1: str) -> int:
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    if q1 == 'cat1':
        red_points = red_points + 1
        return red_points
    elif q1 == 'cat2':
        folklore_points = folklore_points + 1
        return folklore_points
    elif q1 == 'cat3':
        reputation_points = reputation_points + 1
        return reputation_points
    elif q1 == 'cat4':
        lover_points = lover_points + 1
        return lover_points

def find_points_2(q2: str) -> int:
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    if q2 == 'season1':
        reputation_points = reputation_points + 1
        return reputation_points
    elif q2 == 'season2':
        red_points = red_points + 1
        return red_points
    elif q2 == 'season3':
        folklore_points = folklore_points + 1
        return folklore_points
    elif q2 == 'season4':
        lover_points = lover_points + 1
        return lover_points

def find_points_3(q3: str) -> int:
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    if q3 == 'bevy1':
        folklore_points = folklore_points + 1
        return folklore_points
    elif q3 == 'bevy2':
        red_points = red_points + 1
        return red_points
    elif q3 == 'bevy3':
        lover_points = lover_points + 1
        return lover_points
    elif q3 == 'bevy4':
        reputation_points = reputation_points + 1
        return reputation_points

def find_points_4(q4: str) -> int:
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    if q4 == 'tbt':
        reputation_points = reputation_points + 1
        return reputation_points
    elif q4 == 'tbt2':
        lover_points = lover_points + 1
        return lover_points
    elif q4 == 'tbt3':
        red_points = red_points + 1
        return red_points
    elif q4 == 'tbt4':
        folklore_points = folklore_points + 1
        return folklore_points

def find_points_5(q5: str) -> int: 
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    if q5 == 'house1':
        folklore_points = folklore_points + 1
        return folklore_points
    elif q5 == 'house2':
        lover_points = lover_points + 1
        return lover_points
    elif q5 == 'house3':
        red_points = red_points + 1
        return red_points
    elif q5 == 'house4':
        reputation_points = reputation_points + 1
        return reputation_points

def find_points_6(q6: str) -> int:
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    if q6 == 'tv1':
        folklore_points = folklore_points + 1
        return folklore_points
    elif q6 == 'tv2':
        red_points = red_points + 1
        return red_points
    elif q6 == 'tv3':
        lover_points = lover_points + 1
        return lover_points
    elif q6 == 'tv4':
        reputation_points = reputation_points + 1
        return reputation_points

def find_points_7(q7: str) -> int: 
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    if q7 == 'unc1':
        red_points = red_points + 1
        return red_points
    elif q7 == 'unc2':
        folklore_points = folklore_points + 1
        return folklore_points
    elif q7 == 'unc3':
        lover_points = lover_points + 1
        return lover_points
    elif q7 == 'bevy4':
        reputation_points = reputation_points + 1
        return reputation_points

points: dict[str, int] = {"lover": lover_points, "reputation": reputation_points, 
                            "red": red_points, "folklore": folklore_points}


def find_result(points: dict[str, int]) -> str:
    global reputation_points
    global folklore_points
    global red_points
    global lover_points
    winner: str = ""
    sort_points = sorted(points.items(), key=lambda x: x[1], reverse= True)
    for a_tuple in sort_points:
        winner= sort_points[a_tuple][0]
        result = open("../index.html").read().format(winner= winner)
        return result 
    