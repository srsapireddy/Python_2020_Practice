def average(A):
    result = 0
    for x in A:
        result = result + x/len(A)
    return result

numbers = [4,4,4,4]
print average(numbers)
