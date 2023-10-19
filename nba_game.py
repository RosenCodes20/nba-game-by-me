import random

nba_team = input("Enter the first NBA team to compete:")
nba_second_team = input("Enter the second NBA team to compete: ")
names_of_nba_players = ["Curry", "LeBron James", "Kawhi Leonard", "Michael Jordan", "Dennis Rodman", "Klay Thompson"]
names_of_the_second_nba_players = ["Chris Paul", "Kevin Durant", "Yao Ming", "Scottie Pipen", "Shaquille O'Neal"]
first_team_points = 0
second_team_points = 0
while True:
    print("-" * 30)
    print("To stop the game you need to enter 'End of the game!'")

    points_for_team_one = input("Enter team one point(one,two,three,miss): ")
    points_for_team_two = input("Enter team two point(one,two,three,miss): ")

    if points_for_team_one == "one":
        print(
            f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and scores 1 point!")

        first_team_points += 1


    elif points_for_team_one == "two":
        print(
            f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and scores 2 points!")

        first_team_points += 2



    elif points_for_team_one == "three":
        print(
            f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and "
            f"scores 3 points!")
        first_team_points += 3

    elif points_for_team_one == "miss":
        print(
            f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and misses!")
        first_team_points += 0

    if points_for_team_two == "one":
        print(
            f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and scores 1 point!")

        second_team_points += 1

    elif points_for_team_two == "two":
        print(f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and "
              f"scores 2 points!")
        second_team_points += 2


    elif points_for_team_two == "three":
        second_team_points += 3
        print(
            f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and scores 3 points!")

    elif points_for_team_two == "miss":
        second_team_points += 0
        print(
            f"{random.choice(names_of_nba_players)} passes to {random.choice(names_of_the_second_nba_players)} and misses!")

    if points_for_team_one == "End of the game!" or points_for_team_two == "End of the game!":
        break
    else:
        continue


if first_team_points > second_team_points:
    print(f"{nba_team} won with {first_team_points}:{second_team_points}!\nWhat a game it was!!")

elif first_team_points < second_team_points:
    print(f"{nba_second_team} won with {first_team_points}:{second_team_points}!\nWhat a game it was!!")

elif first_team_points == second_team_points:
    print(f"Draw there {first_team_points}:{second_team_points}!\nSee you in the overtime!")
