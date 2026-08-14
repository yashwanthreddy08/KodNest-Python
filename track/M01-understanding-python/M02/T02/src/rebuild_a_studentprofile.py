class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.experience=experience
        self.skills=skills

student_id = int(input("Enter Student ID: "))
name = input("Enter Name: ").strip()
course = input("Enter Course: ").strip()
experience = int(input("Enter Experience: "))
skills = input("Enter Skills: ").split()
# Create one StudentProfile object
student=StudentProfile (student_id, name, course, experience, skills)
# Print the data stored in the object
print(
    f"Student ID: {student_id}\n"
    f"Name: {name}\n"
    f"Course: {course}\n"
    f"Experience in Years: {experience}\n"
    f"Skills: {', '.join(skills)}"
)