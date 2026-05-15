
print("#calculator of two-operand")
num_1 = float(input("Enter number 1:"))
operator = input("Enter the operator:")
num_2 = float(input("Enter number 2:"))

if operator == '+':
    result = num_1 + num_2
    print("Addition:",result)

elif operator == '-':
    result = num_1 - num_2
    print("Subtraction:",result)

elif operator == '*':
    result = num_1 * num_2
    print("Multiplication:",result)

elif operator == '/':
    if num_2 != 0:
        result = num_1/num_2
        print("Division:",result)
    else:
        print("Invalid|For division denominator must be greater than 0.")

else:
    print("Invalid operator.")


