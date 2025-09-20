print("This program changes Octal numbers to Decimal numbers.")

num = input("Please enter your octal number: ")
number = int(num)
decNum = 0
exp = 0

if number == 0:
    decNum = "0"
else:
    while number > 0:
        digit = number % 10
        decNum += (8 ** exp) * digit
        number //= 10
        exp += 1

print("Your Octal value of {number} in Decimal form is:", decNum)
        