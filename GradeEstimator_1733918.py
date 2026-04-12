#!/usr/bin/env python
# coding: utf-8

# This program asks the user for their first and last name,
# formats the name properly, displays a greeting,
# and calculates total points for discussions, course projects, and core assessments.
# It also checks if the student got maximum points for all assignments.

# USER INPUT SECTION

# Ask the user to enter their first name
first_name = input("Enter your first name: ")

# Ask the user to enter your last name
last_name = input("Enter your last name: ")

# Remove spaces before and after the names
first_name = first_name.strip()
last_name = last_name.strip()

# Convert names to proper format
first_name = first_name.capitalize()
last_name = last_name.capitalize()

# Print greeting
print("Hello " + last_name + ", " + first_name)

# CLASS DEFINITIONS

class Discussions:
    maximum_points_per_task = 50
    tasks_per_semester = 8
    display_name = "discussion"

class Course_projects:
    maximum_points_per_task = 50
    tasks_per_semester = 8
    display_name = "course project"

class Core_assesments:
    maximum_points_per_task = 50
    tasks_per_semester = 4
    display_name = "core assessment"

# UNIT POINTS


# Unit 1
Unit1_discussion_points = 43
Unit1_course_project_points = 50
Unit1_core_assesment_points = 49

# Unit 2 (NO core assessment here)
Unit2_discussion_points = 45
Unit2_course_project_points = 48

# Unit 3
Unit3_discussion_points = 50
Unit3_course_project_points = 49
Unit3_core_assesment_points = 48

# LISTS

total_discussion_points = [
    Unit1_discussion_points,
    Unit2_discussion_points,
    Unit3_discussion_points
]

total_course_project_points = [
    Unit1_course_project_points,
    Unit2_course_project_points,
    Unit3_course_project_points
]

# Only include units that actually have core assessments
total_core_assessment_points = [
    Unit1_core_assesment_points,
    Unit3_core_assesment_points
]

# TOTALS

discussion_total = sum(total_discussion_points)
course_project_total = sum(total_course_project_points)
core_assessment_total = sum(total_core_assessment_points)

# MAX POSSIBLE

max_discussion_points = Discussions.tasks_per_semester * Discussions.maximum_points_per_task
max_course_project_points = Course_projects.tasks_per_semester * Course_projects.maximum_points_per_task
max_core_assessment_points = Core_assesments.tasks_per_semester * Core_assesments.maximum_points_per_task

# FUNCTION

def check_max_points(grades_list, max_points, display_name):
    all_max = True

    for grade in grades_list:
        if grade < max_points:
            all_max = False

    if all_max:
        print("Congrats! You got maximum points for ALL " + display_name + " homeworks so far!")
    else:
        print("Unfortunately you did not get maximum points for ALL " + display_name + " homeworks")
        
# OUTPUT

print("Currently you have {} points for discussions out of {}".format(discussion_total, max_discussion_points))
print("Currently you have {} points for course projects out of {}".format(course_project_total, max_course_project_points))
print("Currently you have {} points for core assessments out of {}".format(core_assessment_total, max_core_assessment_points))


# CHECK RESULTS

check_max_points(total_discussion_points, Discussions.maximum_points_per_task, Discussions.display_name)
check_max_points(total_course_project_points, Course_projects.maximum_points_per_task, Course_projects.display_name)
check_max_points(total_core_assessment_points, Core_assesments.maximum_points_per_task, Core_assesments.display_name)
