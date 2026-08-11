# Read the number of registration entries
n=int(input("Enter the number of registration entries: "))
# Create an empty set to store unique student IDs
registrations = set()
#Read and store the student IDS
for i in range(n):
    student_id = input("Enter the Student Id : ").strip()
    registrations.add(student_id)
# Read the student ID to search
search_id= input("Enter the Student Id to search: ").strip()
unique_count=len(registrations)
duplicate_count=n-unique_count
# Print the counts
print(f"Unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")
if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")