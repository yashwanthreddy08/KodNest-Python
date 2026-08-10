word= input("Enter a word: ")
first = int(input("Enter a number1: "))
second = int(input("Enter a number2: "))
third =int(input("Enter a number3: "))
numbers = [first, second, third]
record =(first, second, third)
# Slice the string, list and tuple
print("Middle:", word [1:-1])
print("First Two:", numbers [:2])
print("Reversed Tuple:", record [::-1])