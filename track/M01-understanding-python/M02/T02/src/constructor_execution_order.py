class Employee:
    def __init__(self, name):
        print("Employee constructor")
        self.name = name

class Developer (Employee):
#Add the child constructor
    def __init__(self, name):
        print("Developer constructor started")
        super().__init__(name)
        print("Developer constructor completed")
        print("Developer:", name)

name=input("Enter the name: ").strip()

# Create the object and display the name
dev1=Developer (name)