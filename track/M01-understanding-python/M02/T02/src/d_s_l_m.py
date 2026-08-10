original_scores = []
for _ in range(3):
    original_scores.append(int(input("Enter a score: ")))
alias_scores = original_scores

replacement_score = int(input("Enter a replacement score: "))
additional_score = int(input("Enter an additional score: "))

#Modify the shared list through alias_scores
alias_scores [0]=replacement_score
alias_scores.append(additional_score)

# Display both variables and check whether they share one object
print("Original:", original_scores)
print("Alias:", alias_scores)
print(f"Shared Object: {alias_scores is alias_scores}")