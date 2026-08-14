class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id=student_id
        self.name=name
        self.course=course

first_id= int(input("Enter Student ID: "))
first_name = input("Enter Name: ").strip()
first_course = input("Enter Course: ").strip()

second_id= int(input("Enter Student ID: "))
second_name = input("Enter Name: ").strip()
second_course = input("Enter Course: ").strip()

# Create the first StudentProfile object
student1=StudentProfile(first_id, first_name, first_course)

# Create the second StudentProfile object
student2=StudentProfile (second_id, second_name, second_course)

# Print the first student's data
print(
    f"Student 1\n"
    f"ID: {student1.student_id}\n"
    f"Name: {student1.name}\n"
    f"Course: {student1.course}"
)
# Print the second student's data
print(
    f"Student 2\n"
    f"ID: {student2.student_id}\n"
    f"Name: {student2.name}\n"
    f"Course: {student2.course}"
)
