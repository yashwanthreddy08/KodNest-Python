# Read how many numbers will be entered
number_count=int(input("enter the number count: "))
# Initialize the counters and total
positive_count=0
negative_count=0
zero_count=0
total=0
# Read and analyze each number
for i in range(1, number_count+1):
    n=int(input("Enter a number: "))
    if n>0:
        positive_count+=1
        total+=n
    elif n<0:
        negative_count+=1
        total+=n
    else:
        zero_count+=1
        total+=n
# Display the final analysis
print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Zero Count:", zero_count)
print("Total:", total)