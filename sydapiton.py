def factorial(input):
    if input == 0 or input == 1:
        return input
    else:
        return input * (factorial(input-1))


num = 5
print(factorial(num))
print(num)
