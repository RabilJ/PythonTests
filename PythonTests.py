def do_math (num1, num2=7):
    result = num1 + num2
    result = result + 10
    result = result / 2
    result = result - num2
    return result

print(do_math(2,3)) 
print(do_math(2))