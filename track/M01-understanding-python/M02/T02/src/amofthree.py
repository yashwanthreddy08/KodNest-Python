limit = int(input("Enter a limit: "))
target = int(input("Enter a target: "))
count = 0
total = 0
found =False
# Examine every number from 1 to the limit
for i in range(1,limit+1):
    if i%3==0:
        count+=1
        total+=i
        if i==target:
            found=True

# Display the count, total and search result
print(f"Count: {count}")
print(f"Sum: {total}")
if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")