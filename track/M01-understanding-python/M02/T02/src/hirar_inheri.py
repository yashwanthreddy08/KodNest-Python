class StudentProfile:
    # Parent class constructor
    def __init__(self, name):
        self.name = name

    # Parent class method
    def display_profile(self):
        print(self.name)


class FresherStudent(StudentProfile):
    pass


class ExperiencedStudent(StudentProfile):
    pass


# Take input
fresher_name = input("Enter the fresher student name: ").strip()
experienced_name = input("Enter the experienced student name: ").strip()

# Create objects
fresher = FresherStudent(fresher_name)
experienced = ExperiencedStudent(experienced_name)

# Display profiles
print(f"Fresher Student: {fresher.name}")
print(f"Experienced Student: {experienced.name}")