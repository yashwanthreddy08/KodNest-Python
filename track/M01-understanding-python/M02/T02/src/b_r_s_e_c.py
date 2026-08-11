def check_eligibility (marks, attendance, project_completed):
    if marks>=60 and attendance>=75 and project_completed=="yes":
        return "Eligible"
    else:
        return "Not Eligible"

# Read the student's details
marks = int(input("Enter the marks: "))
attendance = int(input("Enter the attendance: "))
project_completed = input("Enter the status of project completed  (yes/no): ").strip().lower()
#Call the function and print the returned result
result = check_eligibility(marks, attendance, project_completed)
print(result)