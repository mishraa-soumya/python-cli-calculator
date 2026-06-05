# Build a calculator application

from operations import add, subtract, multiply, divide

def calci(ops, num1, num2):
    if ops == 'add':
        sum = add(num1, num2)
        return sum
    elif ops == 'subtract':
        diff = subtract(num1, num2)
        return diff
    elif ops == 'multiply':
        product = multiply(num1, num2)
        return product
    elif ops == 'divide':
        quotient = divide(num1, num2)
        return quotient
    else:
        print("Invalid operation")

print(f"Addition Result: {calci('add', 8.5, 1)}")
print(f"Subtraction Result: {calci('subtract', 85, 15)}")
print(f"Multiplication Result: {calci('multiply', 7, 7)}")
print(f"Division Result: {calci('divide', 150, 20)}")
