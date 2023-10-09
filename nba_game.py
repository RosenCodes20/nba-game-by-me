nba_team = input("Enter the first NBA team to compete:")
nba_second_team = input("Enter the second NBA team to compete:")
points_for_team_one = input("Enter team one point(one,two,three,miss):")
first_team_points = 0
second_team_points = 0
while points_for_team_one  != "End of the game!":
    points_for_team_one = str(points_for_team_one )
    points_for_team_two = input("Enter team two point(one,two,three,miss):")

    if points_for_team_one == "one":
        first_team_points += 1
    elif points_for_team_one == "two":
        first_team_points += 2
    elif points_for_team_one == "three":
        first_team_points += 3
    else:
        first_team_points += 0

    if points_for_team_two == "one":
        second_team_points += 1
    elif points_for_team_two == "two":
        second_team_points += 2
    elif second_team_points == "three":
        second_team_points += 3
    else:
        second_team_points += 0

    points_for_team_one = input("Enter team one point(one,two,three,miss):")

if first_team_points > second_team_points:
    print(f"{nba_team} won with {first_team_points}:{second_team_points}!\nWhat a game it was!!")
elif first_team_points < second_team_points:
    print(f"{nba_second_team} won with {first_team_points}:{second_team_points}!\nWhat a game it was!!")
elif first_team_points == second_team_points:
    print(f"Draw there {first_team_points}:{second_team_points}!\nSee you in the overtime!")
