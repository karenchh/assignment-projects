
#In this program we are checking whether the number entered by the user is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0 :
    print("The number is even. ")
elif number % 3 == 0 :
    print("The number is odd. ")
else :
    print("The number is not even nor odd. ")