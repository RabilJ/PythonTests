a = 8
if a == 5:
    print('5')
elif a == 6:
    print('6')
elif a == 7:
    print('7')
else:
    print('8')

string = ''
for letter in ['a','b','c','d','e']:
    string += letter.upper()
    if len(string) == 5:
        print(string)

number = 0
longString = ''
while number <= 10:
    number = number + 1
    string = str(number)
    longString += string+' '
    if number == 10 :
        print(longString)
