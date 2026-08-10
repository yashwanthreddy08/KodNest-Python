n = int(input("Enter a number: "))
scores = []
# Read and store all scores
for i in range(n):
    scores.append(int(input("Enter the score: ")))

search_score = int(input("Enter the score to search: "))
# Display the highest, lowest and total scores
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print( "Total Score:", sum (scores))
# Display whether search_score is present
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")