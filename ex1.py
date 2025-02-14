
#This is program is to determine the price of the movie ticket according to the age of the user 

print("Hello customer")

age = int(input("Enter your age: "))

if age < 5 :
    print("The ticket is for free. ")
elif age >= 5 and age <= 10 :
    print("The ticket price is $5. ")
elif age >= 11 and age <= 20 :
    print("The ticket costs $10. ") 
else :
    print("tHe ticket costs $15. ")

print("Thank you for you purchase.  ")