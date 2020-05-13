num_1 = input("Enter first number:")
num_2 = input("Enter second number:")

try:
    print num_1/num_2
except ZeroDivisionError:
    print "You have an zero division error"
