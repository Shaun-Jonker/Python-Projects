import cal

while True:
    number_one = float(input("Type your first number:"))
    operator = input("+ , - , * , / ?:")
    number_two = float(input("type your second number:"))

    if operator == '+':
        print(cal.add(number_one, number_two))
    elif operator == '-':
        print(cal.subtract(number_one, number_two))
    elif operator == '*':
        print(cal.multiply(number_one, number_two))
    elif operator == '/':
        print(cal.divide(number_one, number_two))
    else:
        print("Invalid operator")
        quit()

    quit()