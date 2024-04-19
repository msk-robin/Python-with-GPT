#Write a Python program to check if a number is positive, negative, or zero. Take the number as input from the user
 
number = int(input("\nPlease enter a number: "))

if number < 0:
    print("\nThe number you entered is negative\n")
elif number > 0:
    print("\nThe number you entered is positive\n")
else:
    print("\nThe number you entered is zero\n") 
    
#Write a Python program to check if a year is a leap year or not. Take the year as input from the user.

Year = int(input("Check if a year is a leap year or not here. Please enter Year: "))


if Year % 4 == 0:
    print("\nThat is a leap year")

else:
    print("\nThat is not a leap year")
    
#Loops:
#Write a Python program to print the Fibonacci series up to a specified number of terms. Take the number of terms as input from the user.
# fibanacci_terms=int(input("\n Enter the number of terms"))
# a, b= 0,1
# count = 0

# Take the number of terms as input from the user
num_terms = int(input("\nEnter the number of terms: "))

# Initialize the first two terms of the series
a, b = 0, 1
count = 0

if num_terms <= 0:
    print("\nPlease enter a positive number!")
elif num_terms == 1:
    print(f"\nFibonacci series up to {num_terms} term")
    print(a)
else:
    print(f"\nFibonacci series up to {num_terms} terms\n")
    while count < num_terms:
        print(a,end=" ")
        nth_number = a + b
        a = b
        b = nth_number
        count +=1
        
        
                    # dejavu
            # password = input("\nEnter password ")
            # count = 0
            # alphabet 
            # int
            # for characters in password:
            #     if characters != int and != alphabet:
            #         characters = special

            # while len(password) < 6:
            #     print(Please)
            #     for alphabet in password:
            #         if count < 2:
            #             print("\nPassword must have atleast 3 characters.")






#Write a Python program to find the factorial of a number using a while loop. Take the number as input from the user.


factorial_num = int(input("\nEnter a number & find it's factorial value: "))

factorial=1
if factorial_num < 0:
    print("\nFactorial does not exist for negative numbers")
    
elif factorial_num == 0:
    print(f"The factorial of 0 is 1")
else:
    while factorial_num > 0:
        factorial *=factorial_num
        factorial_num -=1
        print(f"The factorial of {factorial_num} is, {factorial}")
        



