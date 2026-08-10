def check_sign(number):
    if number>0:
        result="Positive"
    elif number<0:
        result="Negative"
    else:
        result="Zero"
    return result

number = int(input("Enter a number: "))
result = check_sign(number)
print(result)