class TrainingBatch:
    #Create the shared class variables
    platform_name="KodNest"
    batch_name="Python Batch 1"
    def __init__(self, student_name, score):
    #Store the object-specific values
        self.student_name=student_name
        self.score=score
student1_name = input("Enter the first student name: ").strip()
student1_score= int(input("Enter the first student score: "))
student2_name = input("Enter the second student name: ").strip()
student2_score= int(input("Enter the second student score: "))

#Create two TrainingBatch objects
student1=TrainingBatch(student1_name, student1_score)
student2=TrainingBatch(student2_name, student2_score)

#Print the shared batch information
print("Platform:", TrainingBatch.platform_name)
print("Batch: ", TrainingBatch.batch_name)

#Print the information of both students
print("Student 1:", student1.student_name+", Score:", student1.score)
print("Student 2:", student2.student_name+", Score:", student2.score)