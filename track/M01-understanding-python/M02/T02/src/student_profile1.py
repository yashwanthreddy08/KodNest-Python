class StudentProfile:
    def __init__(self,student_id,name,course,score,is_placed):
        self.student_id=student_id
        self.name =name
        self.course=course
        self.score=score
        self.is_placed=is_placed

    def __str__(self):
        placement_input= "Placed" if self.is_placed else "Not Placed"
        return(
            f"STUDENT PROFILE \n"
        f"Student ID: {student_id}\n"
        f"Name: {name}\n"
        f"Course: {course}\n"
        f"Score: {score}\n"
        f"Placement Status: {placement_input}\n"
        )

student_id = int(input("Enter Student ID: "))
name = input("Enter Name: ").strip()
course =input("Enter Course: ").strip()
score =float(input("Enter Score: "))
placement_input = input("Enter Placement Status: ").strip()
#Convert placement_input into a Boolean value
is_placed =placement_input.lower() =="yes"

#Create a StudentProfile object using keyword arguments
student = StudentProfile(student_id, name, course, score, is_placed)
print(student)
