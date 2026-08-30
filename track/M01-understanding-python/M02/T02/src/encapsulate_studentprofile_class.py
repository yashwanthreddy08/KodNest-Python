class StudentProfile:
    def __init__(self, student_id, name, score, skills):
        # Store private attributes
        self.__student_id = student_id
        self.__name = name
        self.__score = score
        self.__skills = []

        # Add initial skills
        for skill in skills:
            self.add_skill(skill)

    # Read-only property for student_id
    @property
    def student_id(self):
        return self.__student_id

    # Property for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        # Remove surrounding spaces
        new_name = new_name.strip()

        # Accept only non-empty names
        if new_name:
            self.__name = new_name

    # Property for score
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        # Accept only scores from 0 to 100
        if 0 <= new_score <= 100:
            self.__score = new_score

    # Read-only property for skills
    @property
    def skills(self):
        # Return tuple so outside code cannot modify the list
        return tuple(self.__skills)

    # Method to add a skill
    def add_skill(self, new_skill):
        # Remove surrounding spaces
        new_skill = new_skill.strip()

        # Add only if non-empty and not already present
        if new_skill and new_skill not in self.__skills:
            self.__skills.append(new_skill)

    # String representation of the object
    def __str__(self):
        return (
            "STUDENT PROFILE\n"
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__name}\n"
            f"Score: {self.__score}\n"
            f"Skills: {', '.join(self.__skills)}"
        )


# Input
student_id = int(input("Enter the student ID:"))
name = input("Enter the name:").strip()
initial_score = int(input("Enter the score:"))
skills_input = input("Enter the skills:").strip()
new_score = int(input("Enter the new score:"))
new_skill = input("Enter the new skill:").strip()


# Convert comma-separated skills into a list
initial_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]


# Create exactly one StudentProfile object
student = StudentProfile(
    student_id,
    name,
    initial_score,
    initial_skills
)


# Update the score through the property
student.score = new_score


# Add the skill through the method
student.add_skill(new_skill)


# Print the final object
print(student)