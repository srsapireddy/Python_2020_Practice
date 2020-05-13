def factorial(number):
    result = 1
    for x in range(1,number + 1):
        result = result*x
    return result

in_variable = input("Enter the number to find the factorial: ")
print factorial(in_variable)
