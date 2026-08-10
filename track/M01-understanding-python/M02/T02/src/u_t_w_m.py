# Read the course details
course_name=input("Enter the course name: ")
current_week=input("Enter the current week: ")
course_status=input("Enter the course status: ")

# Create the original tuple
course_details=(course_name,current_week, course_status)

# Read the updated week
updated_week=input("Enter the week: ")

#Create and assign a new tuple
course_details=(course_details[0], updated_week, course_details [2])

# Display the updated tuple
print(course_details)