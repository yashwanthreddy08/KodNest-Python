def calculate(first_number, second_number, operator):
    if operator=="+":
        result=first_number+second_number
    elif operator=="-":
        result=first_number-second_number
    elif operator=="*":
        result=first_number*second_number
    else:
        result=first_number/second_number
    return result

first_number = int(input("Enter a number: "))

second_number = int(input("Enter a number: "))

operator= input("Entet a operator: ").strip()

result = calculate(first_number, second_number, operator)

print(result)