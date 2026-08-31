class Employee:
    #Add the constructor
    def __init__(self,name):
        self.name = name
class Developer (Employee):
#Add the constructor and display_profile()
    def __init__(self,name, language):
        super().__init__(name)
        self.language=language
    def display_profile():
        return f"Employee: {name}\nLanguage: {language}"
name =input("Employee Name: ").strip()
language =input("Coding Language: ").strip()

#Create a Developer object and display its profile
developer_1=Developer (name, language)
print(Developer.display_profile())