#!/usr/bin/env python
# coding: utf-8

# In[1]:

# This program asks the user for their first and last name,
# formats the name properly, displays a greeting,
# and calculates total points for discussions, course projects, and core assessments.

# Ask the user to enter their first name
first_name = input("Enter your first name: ")

# Ask the user to enter their last name
last_name = input("Enter your last name: ") 

# Remove spaces before and after the names
first_name = first_name.strip()  
last_name = last_name.strip()    

# Convert names to proper format (capitalize first letter only)
first_name = first_name.capitalize() 
last_name = last_name.capitalize()    

# Print greeting in required format
print("Hello " + last_name + ", " + first_name)

#  UNIT 1 POINTS.

# Store points for Unit 1 discussion
Unit1_discussion_points = 43 

# Store points for Unit 1 course project
Unit1_course_project_points = 50

# Store points for Unit 1 core assessment
Unit1_core_assesment_points = 49  

# UNIT 2 POINTS

# Store expected or actual points for Unit 2 discussion
Unit2_discussion_points = 45 

# Store expected or actual points for Unit 2 course project
Unit2_course_project_points = 48

# Store expected or actual points for Unit 2 core assessment
Unit2_core_assesment_points = 47 

# MAXIMUM POINTS 

# Store maximum points for each task
task_maximum_points = 50  # Maximum possible points per assignment

#  CREATE LISTS

# Create a list for discussion points including Unit 1 and Unit 2
total_discussion_points = [Unit1_discussion_points, Unit2_discussion_points]

# Create a list for course project points including Unit 1 and Unit 2
total_course_project_points = [Unit1_course_project_points, Unit2_course_project_points]

# Create a list for core assessment points including Unit 1 and Unit 2
total_core_assessment_points = [Unit1_core_assesment_points, Unit2_core_assesment_points]

# CALCULATE TOTALS

# Calculate total discussion points using sum() function
discussion_total = sum(total_discussion_points)

# Calculate total course project points using sum() function
course_project_total = sum(total_course_project_points)

# Calculate total core assessment points using sum() function
core_assessment_total = sum(total_core_assessment_points)

# CALCULATE MAXIMUM POSSIBLE POINTS

# Calculate maximum possible discussion points (8 assignments * max points)
max_discussion_points = 8 * task_maximum_points

# Calculate maximum possible course project points (8 assignments * max points)
max_course_project_points = 8 * task_maximum_points

# Calculate maximum possible core assessment points (4 assignments * max points)
max_core_assessment_points = 4 * task_maximum_points

# DISPLAY RESULTS

# Display discussion results using format()
print("Currently you have {} points for discussions out of {}".format(discussion_total, max_discussion_points))

# Display course project results using format()
print("Currently you have {} points for course projects out of {}".format(course_project_total, max_course_project_points))

# Display core assessment results using format()
print("Currently you have {} points for core assessments out of {}".format(core_assessment_total, max_core_assessment_points))


# In[ ]:




