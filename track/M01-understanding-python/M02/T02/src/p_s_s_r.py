skills = []
#Read and store five skills

for i in range (5):
    skills.append(str(input("Enter a skill: ")))

# Convert the list into a tuple
skills=tuple(skills)

# Create the required slices
first_three=skills [0:3]
last_two =skills [3:5]
alternate_skills=skills [0:5:2]
reversed_skills=skills [::-1]

# Display all required results
print("Skill Record:", skills)
print("First Three:", first_three)
print("Last Two:", last_two)
print("Alternate Skills:", alternate_skills)
print("Reversed Skills:", reversed_skills)