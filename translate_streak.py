import pandas as pd

def streak_points(streak: str):
    points_dict = {'W': 3, 'D': 1, 'L': 0 }
    alpha_values = []
    for character in streak:
        if character == 'n' or character == 'a':
            pass
        elif character == '0':
            pass
        else:
            alpha_values.append(points_dict[character])  # Adds each character's value to alpha_values.
    return alpha_values

def points_calculator(x):
    w = [0.2, 0.4, 0.6, 0.8, 1.0]
    products = []
    streak_length = len(x)
    
    if streak_length == len(w):
        for i, j in zip(w,x):
            products.append(i * j)
        form = sum(products)

    elif streak_length < len(w):
        for i, j in zip(w[-1*streak_length:],x[-1*streak_length:]):
            products.append(i * j)
        form = sum(products)

    elif streak_length > len(w):
        for i, j in zip(w,x[-1*len(w):]):
            products.append(i * j)
        form = sum(products)

    return form


full['Streak_When_Home'] = full['Streak_When_Home'].astype(str)
full['Streak_When_Home'] = full['Streak_When_Home'].apply(streak_points)
full['Streak_When_Home'] = full['Streak_When_Home'].apply(points_calculator)


full['Streak_When_Away'] = full['Streak_When_Away'].astype(str)
full['Streak_When_Away'] = full['Streak_When_Away'].apply(streak_points)
full['Streak_When_Away'] = full['Streak_When_Away'].apply(points_calculator)

full['Total_Streak_Home'] = full['Total_Streak_Home'] = full['Total_Streak_Home'].astype(str)
full['Total_Streak_Home'] = full['Total_Streak_Home'].apply(streak_points)
full['Total_Streak_Home'] = full['Total_Streak_Home'].apply(points_calculator)

full['Total_Streak_Away'] = full['Total_Streak_Away'] = full['Total_Streak_Away'].astype(str)
full['Total_Streak_Away'] = full['Total_Streak_Away'].apply(streak_points)
full['Total_Streak_Away'] = full['Total_Streak_Away'].apply(points_calculator)
