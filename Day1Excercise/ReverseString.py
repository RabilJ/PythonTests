def reverse_string(word):
    return word[::-1]

def reverse_string_alternative(word):
    return "".join(reversed(word))

print(reverse_string("Robot"))

print(reverse_string_alternative("Robot"))
