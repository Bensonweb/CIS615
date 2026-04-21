#!/usr/bin/env python
# coding: utf-8

# Import json module so we can read data from tasks.json file
import json


# =========================
# NEW CLASS: Task_type
# =========================

# Create a class that represents each task type
class Task_type:
    
    # Constructor that initializes object properties
    def __init__(self, name, display_name, tasks_per_semester, maximum_points_per_task):
        self.name = name  # internal name of task type
        self.display_name = display_name  # user-friendly name
        self.tasks_per_semester = tasks_per_semester  # number of tasks
        self.maximum_points_per_task = maximum_points_per_task  # max points per task


# =========================
# READ JSON FILE
# =========================

# Open the tasks.json file in read mode
with open("tasks.json", "r") as file:
    
    # Load JSON data into Python structure (list/dictionary)
    data = json.load(file)


# =========================
# STORE TASK TYPES IN LIST
# =========================

# Create an empty list to store Task_type objects
task_types_list = []

# Loop through each task type in JSON file
for task in data:
    
    # Create a new Task_type object using JSON values
    task_obj = Task_type(
        task["name"],  # name from JSON
        task["display_name"],  # display name
        task["tasks_per_semester"],  # number of tasks
        task["maximum_points_per_task"]  # max points
    )
    
    # Add the created object to the list
    task_types_list.append(task_obj)


# =========================
# CALCULATE MAXIMUM POINTS
# =========================

# Initialize total maximum points variable
total_max_points = 0

# Loop through each task type object in the list
for task in task_types_list:
    
    # Calculate total points for this task type
    task_total = task.tasks_per_semester * task.maximum_points_per_task
    
    # Add to overall total
    total_max_points += task_total


# =========================
# DISPLAY RESULT
# =========================

# Print the final maximum grade
print("Maximum grade you can get for this class is:", total_max_points)
