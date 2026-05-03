import pandas as pd  # import pandas to handle CSV
import json  # import json to read JSON file
from pathlib import Path  # handle file paths


# function to display data
def display(title, data):
    print("\n" + "=" * 50)  # separator
    print(title)  # title
    print("=" * 50)
    print(data.to_string(index=False))  # print table


# function to load max grades from JSON
def load_max_points(file):
    with open(file, "r") as f:  # open JSON file
        data = json.load(f)  # read JSON

    max_points = {}

    for item in data:  # loop through JSON list
        name = item["name"].lower()  # get type
        max_points[name] = item["maximum_points_per_task"]  # store max grade

    return max_points


def main():
    folder = Path.cwd()  # current folder

    grades_file = folder / "grades.csv"  # CSV path
    json_file = folder / "tasks.json"  # JSON path

    max_points = load_max_points(json_file)  # load max grades from JSON

    df = pd.read_csv(grades_file)  # read CSV

    display("ALL GRADES", df)  # show all data

    # discussion grades
    discussions = df[df["type"].str.lower() == "discussion"]
    display("DISCUSSION GRADES", discussions)

    # unit 1 grades (week1)
    display("UNIT 1 GRADES", df[["type", "week1"]])

    # clean data
    for i in df.index:
        task_type = df.loc[i, "type"].lower()  # type
        max_grade = max_points.get(task_type, 50)  # get max from JSON

        for col in df.columns[1:]:
            grade = df.loc[i, col]

            if grade < 0:
                df.loc[i, col] = 0  # fix negative

            elif grade > max_grade:
                df.loc[i, col] = max_grade  # cap to max

    display("CLEANED DATA", df)  # show cleaned


if __name__ == "__main__":
    main()
