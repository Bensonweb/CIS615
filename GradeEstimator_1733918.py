# import pandas so we can read csv files
import pandas as pd

# import json so we can read json file
import json

# import Path to work with files
from pathlib import Path


# function to load max points from tasks.json
def load_max_points(file):

    # open json file
    with open(file, "r") as f:

        # load json data
        data = json.load(f)

    # create empty dictionary
    max_points = {}

    # loop through tasks
    for item in data:

        # get task type name
        name = item["name"].lower()

        # save max points
        max_points[name] = item["maximum_points_per_task"]

    # return dictionary
    return max_points


# main function
def main():

    # get current folder
    folder = Path.cwd()

    # path to tasks.json
    json_file = folder / "tasks.json"

    # path to grades csv
    grades_file = folder / "grades_50.csv"

    # TO TEST grades_50.csv
    # replace above line with:
    # grades_file = folder / "grades_50.csv"

    # load max points
    max_points = load_max_points(json_file)

    # read csv file
    df = pd.read_csv(grades_file)

    # display all grades
    print("\nALL GRADES")
    print(df)

    # display discussion grades only
    print("\nDISCUSSION GRADES")
    discussions = df[df["type"].str.lower() == "discussion"]
    print(discussions)

    # display unit 1 grades
    print("\nUNIT 1 GRADES")
    print(df[["type", "week1"]])

    # clean data
    for i in df.index:

        # get task type
        task_type = df.loc[i, "type"].lower()

        # get max grade
        max_grade = max_points.get(task_type, 50)

        # loop through week columns
        for col in df.columns[1:]:

            # get grade
            grade = df.loc[i, col]

            # skip empty cells
            if pd.isna(grade):
                continue

            # if grade less than 0
            if grade < 0:

                # replace with 0
                df.loc[i, col] = 0

            # if grade bigger than max
            elif grade > max_grade:

                # replace with max
                df.loc[i, col] = max_grade

    # display cleaned data
    print("\nCLEANED DATA")
    print(df)

    # variable for earned points
    earned_points = 0

    # variable for maximum points
    maximum_points = 0

    # calculate totals
    for i in df.index:

        # get task type
        task_type = df.loc[i, "type"].lower()

        # get max grade
        max_grade = max_points.get(task_type, 50)

        # loop through week columns
        for col in df.columns[1:]:

            # get grade
            grade = df.loc[i, col]

            # count only non-empty grades
            if pd.notna(grade):

                # add earned points
                earned_points += grade

                # add max possible points
                maximum_points += max_grade

    # display totals
    print("\nYou have", earned_points, "out of", maximum_points)

    # calculate percentage
    percentage = (earned_points / maximum_points) * 100

    # display percentage
    print("Your percentage is:", round(percentage, 2))

    # calculate letter grade
    if percentage > 90:

        # grade A
        letter = "A"

    elif percentage > 80:

        # grade B
        letter = "B"

    elif percentage > 70:

        # grade C
        letter = "C"

    elif percentage > 60:

        # grade D
        letter = "D"

    else:

        # grade F
        letter = "F"

    # display letter grade
    print("Your letter grade is:", letter)


# run program
if __name__ == "__main__":
    main()
