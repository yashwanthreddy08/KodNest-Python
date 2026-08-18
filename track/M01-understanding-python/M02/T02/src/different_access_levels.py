class CandidateProfile():
    def __init__(self,name,email,score):
        self.name=name
        self._email=email
        self.__score=score
    def __str__(self):
        return f"Name: {self.name}"
    def get_email(self):
        return f"Email: {self._email}"
    def get_score(self):
        return f"Score: {self.__score}"
name=input("Enter the name: ")
email=input("Enter the email: ")
score=int(input("Enter the score: "))
candidate=CandidateProfile(name,email,score)
print(candidate)
print(candidate.get_email)
print(candidate.get_score)
