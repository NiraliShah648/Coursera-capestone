def multiplication(num1, num2):
    return num1 * num2

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

value1 = 6
value2 = 3

print(value1, "/", value2, "=", divide(value1, value2))
print(value1, "*", value2, "=", multiplication(value1, value2))
print(value1, "+", value2, "=", addition(value1, value2))
print(value1, "-", value2, "=", subtraction(value1, value2))
