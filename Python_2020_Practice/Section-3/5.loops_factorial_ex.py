def factorial(number):
    result = 1
    while number>0:
        result = result*number
        number = number - 1
    return result

in_variable = input("Enter the number to find the factorial: ")
print factorial(in_variable)
