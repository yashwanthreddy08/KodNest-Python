class StudentProfile:
    def __init__(
        self, student_id,
        name,
        course,
        experience,
        skills
        ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills
    def __str__(self):
        return f"STUDENT PROFILE\n"f"Student ID: {self.student_id}\n"f"Name: {self.name}\n"f"Course: {self.course}\n"f"Experience: {self.experience}\n"f"Skills: {', '.join(self.skills)}"  

student_id = int(input("Enter Student ID: "))
name = input("Enter Name: ").strip()
course =input("Enter Course: ").strip()
experience = int(input("Enter Experience: "))
skills = input("Enter Skills: ").split()

# Create one StudentProfile object
student =StudentProfile(student_id, name, course, experience, skills)

# Display the object using print(student)
print(student)