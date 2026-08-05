marks=int(input("Enter a marks: "))
attendance=int(input("Enter the attendance percentage: "))
project_status=input("Enter the Project Status (yes/no): ")
if marks>=60 and attendance>=75:
    if project_status=="yes":
        print("Eligible")
    else:
        print("Not Eligible")
else: 
    print("Not Eligible")