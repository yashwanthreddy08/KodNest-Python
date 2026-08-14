class StudentProfile:
    def __init__(self, name, experience, skills):
        self.name=name
        self.experience=experience
        self.skills=skills
    def update_experience(self, new_experience):
        # Replace the current experience
        self.experience=new_experience
    def add_skill(self, new_skill):
        # Add the new skill to the existing list
        self.skills.append(new_skill)

name = input("Enter name: ").strip()
experience = int(input("Enter experience: "))
skills= input("Enter skills: ").split()

new_experience = int(input("Enter new experience: "))
new_skill = input("Enter new skill: ").strip()
# Create one StudentProfile object
student =StudentProfile(name, experience, skills)

# Update the student's experience
student.update_experience (new_experience)

#Add the new skill
student.add_skill(new_skill)

# Print the updated profile
print(
    f"Name: {name}\n"
    f"Experience: {experience}"
    f"Skills: {', '.join(skills)}"
)