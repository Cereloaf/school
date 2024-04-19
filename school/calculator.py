print("simple calculator(+,-,*,/)")

a = float(input("enter a number:     "))
b = input("operation(+,-,*,/): ")
c = float(input("enter a number:     "))

if b == '+':
    sum = a + c
elif b == '-':
    sum = a - c
elif b == '*':
    sum = a * c
elif b == '/':
    if c == 0:
        print("Error!")
    else:
        sum = a / c
else:
    print("Error!")

print("Result:", sum)