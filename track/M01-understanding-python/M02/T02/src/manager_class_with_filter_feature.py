# Create the StudentProfile class
class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id=student_id
        self.name=name
        self.course=course
    def __str__(self):
        return f"{self.student_id} {self.name} {self.course}"
# Create the PlacementManager class
class PlacementManager:
    def __init__(self):
        self.student_profiles=[]
    def add_student_profiles (self, student_profile):
        self.student_profiles.append(student_profile)
    def find_student_by_course(self, student_course):
        result=[]
        for student in self.student_profiles:
            if student.course==student_course:
                result.append(student)
        return result
# Read the student details
manager =PlacementManager()
n=int(input("Enter number of students: "))
for i in range(n):
    student_id=int(input("Enter Student ID: "))
    name=input("Enter Name: ").strip().title()
    course=input("Enter Course: ").strip().title()
    student=StudentProfile(student_id, name, course)
    manager.add_student_profiles (student)
required_course=input("Enter the required course: ").title()
result=manager.find_student_by_course(required_course)
# Filter and display the matching students
if result:
    for student in result:
        print(student)
else:
    print(f"No students found for course: {required_course}")