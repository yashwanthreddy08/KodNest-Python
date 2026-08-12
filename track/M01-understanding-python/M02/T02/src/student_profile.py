class StudentProfile:
    def __init__(self,student_id,name,course,score=0.0,skills=None,student_placed=False):
        self.student=student_id
        self.name=name
        self.course=course
        self.score=score
        self.skills=[] if skills is None else list(skills)
        self.student_placed=student_placed

    def __str__(self):
        skills_str=",".join(self.skills) if self.skills else "NA"
        placement_status="Placed" if self.student_placed else "Not Placed"
        return(
        f"Student ID: {self.student}\
        Name: {self.name}\
        Course: {self.course}\
        score: {self.score}\
        skills: {skills_str}\
        Status: {placement_status}")

student=StudentProfile("id001","john","CS",90.0,["python","sql"],True)
print(student)