class StudentProfile:
    # Create the class-level object counter
    profile_count=0
    def __init__(self, name):
        # Store the name
        self.name=name
        # Increase the shared counter
        StudentProfile.profile_count+=1
n = int(input("Enter the number of profiles to create:"))
students = []
# Read n names and create n StudentProfile objects
for i in range(n):
    name=input("Enter the name:").strip()
    student=StudentProfile(name)
    students.append(name)
# Print the number of created profiles
print("Profiles Created:", StudentProfile.profile_count)