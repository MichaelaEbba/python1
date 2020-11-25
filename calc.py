def result_calc_add(x, y):
    return x + y 


def result_calc_sub(x, y):
    return x - y


def result_calc_mult(x, y):
    return x * y


def result_calc_div(x, y):
    return x / y


def print_calc(number):
    print(number)
    if number < 50: 
       print("Less than fifty")
    elif number == 50:
        print("Fifty")
    elif 50 < number < 100:
        print("Almost a hundred")
    elif number == 100:
        print("Spot on")
    elif number > 100:
        print("Missed the spot")
    else:
        print("Nope")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator: ")
if operator == "+":
    print_calc(result_calc_add(num1, num2))
if operator == "-":
    print_calc(result_calc_sub(num1, num2))
if operator == "*":
    print_calc(result_calc_mult(num1, num2))
if operator == "/":
    print_calc(result_calc_div(num1, num2))

