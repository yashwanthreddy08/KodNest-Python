name = input("Enter the name: ")
course = input("Enter the course: ")
score = int(input("Enter the score: "))
# Create the tuple
student_record = (name, course, score)
# Unpack the tuple
name, course, score=student_record
# Display the unpacked values
print("Name:",name)
print("Course:", course)
print("Score:", score)