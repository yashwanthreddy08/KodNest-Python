class StudentProfile:
    def __init__(self,name,score):
        self.name=name
        self.__score=score
    def get_score(self):
        return f"Final Score: {self.__score}"
    def set_score(self,new_score):
        if 0<=new_score<=100:
            self.__score=new_score
            return True
        return False
name=input("Enter the name: ").strip()
initial_score=int(input("Enter the score:"))
new_score=int(input("Enter the new score: "))

student=StudentProfile(name,initial_score)

result=student.set_score(new_score)

if result:
    print("Score Updated")
else:
    print("Invalid Score")

print(f"Name: {student.name}")
print(student.get_score())