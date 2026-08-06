# Read the limit
limit=int(input("Enter a limit: "))
# Initialize the 1000 variable and total
number=1
total=0
# Examine every number from 1 to limit
while number<=limit:
    if number%2==0:
        total=total+number
    number=number+1
# Display the result
print("Even Sum:", total)