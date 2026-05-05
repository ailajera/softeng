"""
Ask the user to enter a number
Convert the input into an integer
Check if the number is divisible by 2
If it is divisible by 2, print "Even"
Otherwise, print "Odd"


2.
Ask the user to enter a password
Compare the input to a correct password (you choose one, e.g. "python123")
If the password is correct:
Print "Access granted"
If the password is wrong:
Print "Access denied"

"""
"""
num1 = int(input("enter a number:"))

if num1 %2 == 0:
    print("Even")
else:
    print("Odd")
    """
answer = "123"

pas = str(input("Input pasword: "))

if pas == answer:
    print ("Access granted")
else:
    print("Denied")