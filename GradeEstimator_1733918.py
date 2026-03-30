# This program asks the user for their first and last name
# and then prints the full name

# Ask the user to enter their first name and store it in a variable
first_name = input("Enter your first name: ")

# Ask the user to enter their last name and store it in another variable
last_name = input("Enter your last name: ")

# Combine the first name and last name with a space in between
full_name = first_name + " " + last_name

# Print the full name to the screen
# Remove spaces before and after the names
first_name = first_name.strip()  
last_name = last_name.strip()    

# Convert names to proper format (capitalize first letter only)
first_name = first_name.capitalize() 
last_name = last_name.capitalize()    

# Print greeting in required format
print("Hello " + last_name + ", " + first_name)

# Store points for Unit 1 discussion
Unit1_discussion_points = 43  # Change this to your actual or expected score

# Store points for Unit 1 course project
Unit1_course_project_points = 50  # Change this to your actual or expected score

# Store points for Unit 1 core assessment
Unit1_core_assesment_points = 49  # Change this to your actual or expected score

# Store maximum points for each task
task_maximum_points = 50  # Maximum possible points

# Calculate total points using variables
total_points = Unit1_discussion_points + Unit1_course_project_points + Unit1_core_assesment_points

# Display total points
print("Total Points:", total_points)

# Check if maximum points were achieved for discussion
print("Got maximum points for Unit 1 discussion?", Unit1_discussion_points == task_maximum_points)

# Check if maximum points were achieved for course project
print("Got maximum points for Unit 1 course project?", Unit1_course_project_points == task_maximum_points)

# Check if maximum points were achieved for core assessment
print("Got maximum points for Unit 1 core assessment?", Unit1_core_assesment_points == task_maximum_points)
