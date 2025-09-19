print("This program changes Decimal Numbers to Octal")
number = int(input("Please enter your decimal number: "))
octNum = ""

if number == 0:
    octNum = "0"
else:
    while number > 0:
        digit = number % 8
        octNum = str(digit) + octNum
        number //= 8

print("Your Decimal value of {number} in Octal form is:", octNum)