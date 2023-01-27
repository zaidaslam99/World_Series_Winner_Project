# This program reads this file and creates a dict in which the keys are the names of the teams and each key assoicated
    # value is the name of the team that won that year, the program should prompt the user for a year in the range of
    # 1903 through 2009 it should then display the name of the team that won the World Series that year and the number
    # of times that team has won the World Series.

def main():

    world_series_parsed_list, set_world_series = read_from_file_function()

    dict_world_series = set_dict_world_series_function(world_series_parsed_list, set_world_series)

    years = get_year_function()

    dict_to_zip_years_team_won = year_to_team_function(years, world_series_parsed_list)

    display_data(dict_to_zip_years_team_won, dict_world_series)

    print(f"dict_to_zip: {dict_to_zip_years_team_won}")
    print(f"dict_world_series: {dict_world_series}")

def read_from_file_function():

    world_series_file = open("WorldSeriesWinners.txt", "r")

    world_series_obj = world_series_file.readlines()

    world_series_parsed_list = []

    index = 0

    while index < len(world_series_obj):
        element = world_series_obj[index].rstrip("\n")
        world_series_parsed_list.append(element)
        index += 1

    # Get the total amount of teams that played
    set_world_series = set(world_series_parsed_list)

    return world_series_parsed_list, set_world_series

def get_year_function():

    year_world_series = []

    for year in range(1903, 2007):
        year_world_series.append(year)

    return year_world_series

def set_dict_world_series_function(world_series_parsed_list, set_world_series_names):

    dict_world_series = {}

    for each_name in set_world_series_names:
        dict_world_series[each_name] = world_series_parsed_list.count(each_name)

    print()
    print("The team and the amount that the team won dict is below:")
    print(dict_world_series)

    return dict_world_series

def year_to_team_function(years, world_series_parsed_list):

    year_to_team_dict = {}

    # Zip function allows us to use two list together and have key and value pairs
    zip_years_team_won = zip(years, world_series_parsed_list)

    # Convert to dict file from zip
    dict_to_zip_years_team_won = dict(zip_years_team_won)

    # Display the results
    print()
    print("The team that won each year from 1903 to 2009: ")
    print(dict_to_zip_years_team_won)

    return dict_to_zip_years_team_won

def display_data(dict_to_zip_years_team_won, dict_world_series):

    print()
    user_input_year = int(input("Enter a year from 1903 to 2009: "))

    if user_input_year >= 1903 and user_input_year <= 2009:

        print(f"The team that won in {str(user_input_year)} was {dict_to_zip_years_team_won[user_input_year]}")

        if dict_to_zip_years_team_won[user_input_year] in dict_world_series.keys():

            team = dict_to_zip_years_team_won[user_input_year]

            print(f"The amount of times that {dict_to_zip_years_team_won[user_input_year]} won is "
                  f"{dict_world_series[team]} times")

    while user_input_year <= 1903 or user_input_year >= 2009:

        user_input_year = int(input("Enter a proper year from 1903 to 2009: "))

        if user_input_year >= 1903 and user_input_year <= 2009:

            print(f"The team that won in {str(user_input_year)} was {dict_to_zip_years_team_won[user_input_year]}")

            if dict_to_zip_years_team_won[user_input_year] in dict_world_series.keys():
                team = dict_to_zip_years_team_won[user_input_year]

                print(f"The amount of times that {dict_to_zip_years_team_won[user_input_year]} won is "
                      f"{dict_world_series[team]} times")

main()
