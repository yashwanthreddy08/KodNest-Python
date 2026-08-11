sentence = input("Enter the sentence: ")
# Clean and normalize the sentence
cleaned= sentence.strip()
remove =cleaned.replace(".","")
normalized=remove.lower()
words=normalized.split()
#Split the sentence and create the slug
slug="-".join(words)
# Produce the uppercase form and search result
uppercase=normalized.upper()
search=input("Enter the Search word: ")
find=normalized.find(search)
# Display all processed values
print("Cleaned:", cleaned)
print("Normalized:", normalized)
print("Words:", words)
print("Slug:",slug)
print("Uppercase:", uppercase)
print("Python Position:", find)