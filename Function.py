import re
 
def user(person):
    while person:
        user_name=input("\nEnter name: ")
        security_key=input("\nEnter password: ")
          
        if user_name.isdigit() == True:
            print("\nPlease enter a valid name")
            continue 
        print(f"\n Hi {user_name},\n Your account was successfully created!\n")
        break
    return user_name,security_key

#How can I access that tuple and manipulate (the return value tuple)

client = user("person")
print(client)

def calculate(x, y):
    subtraction = x - y
    addition = x + y
   
    return subtraction, addition

# Call the function and unpack the returned tuple
sub, add = calculate(10, 5)
print("\nAddition:", add)  # Output: Addition: 15
print("\nSubtraction:", sub)  # Output: Subtraction: 5




# Area of a Circle:
#Write a Python function named calculate_area_circle that takes the radius of a circle as input and returns the area of the circle. Use the formula: area = π * radius^2.
def calculate_area_circle():
    radius = int(input("\nEnter the radius of the circle: "))
    area = 3.14159 * radius**2
    return area

answer = calculate_area_circle()
print(answer)

# Check Even or Odd:
#Write a Python function named check_even_odd that takes an integer as input and returns "Even" if the number is even and "Odd" if the number is odd.
def check_even_odd():
    checker = int(input("\nTo check even or odd, please enter a number: "))
    if checker % 2 == 0 :
        print("\nThis is an even number!")
    else:
        print("\nThis is an odd number!")
        
check_even_odd()

#Maximum of Three Numbers:
#Write a Python function named find_max that takes three numbers as input and returns the maximum of the three numbers.
def find_max():
    listed = []
    count = 0
    while count < 3 :
        n = count 
        test = int(input(f"\nEnter 3 different numbers one at a time and \nlet me check the largest number you entered. Number {n + 1}: "))
        listed.append(test)
        count += 1
    print(max(listed))
    
find_max()



#Below are 5 practices on basic concepts, including function syntax, parameters, return values, and function scope,          

#Function to Calculate the Area of a Rectangle:
"""Write a Python function named calculate_area_rectangle that 
takes the length and width of a rectangle as input parameters 
and returns the area of the rectangle. Test your function with
different values for length and width."""            

def calculate_area_rectangle():
    while calculate_area_rectangle:
        length = float(input("\nEnter the length of the rectangle: "))
        width = float(input("\nEnter the width of the rectangle: ")) 
        if length == width:
            print("\nYou're values create a perfect square, please check the values and try again.")
            continue
        elif width > length:
            print("\nWidth cannot be greater than length, please check the values and try again.") 
            continue
        else:
            area = length * width
            break
    return area

answer = calculate_area_rectangle()
print(f"\nThe are of the rectangle is : {answer}")

#Function to Check if a Number is Prime:
"""Write a Python function named is_prime that takes an integer as 
input and returns True if the number is prime and False otherwise. 
Test your function with different numbers."""

def is_prime(number):
    #Checks if a given number is prime.
    
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisors from 2 to the square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, prime

number = int(input("\nEnter a number to find out if it is a prime number: "))

if is_prime(number):
    print(f"\n{number} is a prime number")
else:
    print(f"\n{number} is not a prime number")



#Function to Count Vowels in a String:
"""Write a Python function named count_vowels that takes a string as 
input and returns the count of vowels (a, e, i, o, u) in the string. 
Test your function with different strings."""

def count_vowels(string):
    vowels = ['a', 'e' ,'i', 'o', 'u']
    count = 0 

    for character in string:
        if character in vowels:
            count += 1        
    return count
    
string = (input("\nEnter a string to count it's vowels. ").lower())
vowel_count = count_vowels(string)
print(f"\n{string.capitalize()}\nThe string above has {vowel_count} vowels.")

#Function to Reverse a List:
"""Write a Python function named reverse_list that takes a list as 
input and returns a new list with the elements reversed. Test your 
function with different lists."""

#CHEECK HOW TO CONVERT A LIST BACK TO A SINGLE STRING
def reverse_list(digits):
    listing = []
    for digit in digits:
        listing.append(digit)
        
    listing.reverse()
    return listing

digits = input("\nEnter a list of digits or words to reverse them: ")
checker = reverse_list(digits)
print(f"\n{''.join(checker)}")

#Function to Generate Fibonacci Sequence:
"""Write a Python function named generate_fibonacci
that takes an integer n as input and returns a list
containing the first n numbers of the Fibonacci sequence.
Test your function with different values of n"""

def generate_fibonacci(nth):
    a, b =[ 0, 1]
    count = 0
    fibonacci_list = []
    
    while count < nth:
        print(a, end="")
        num = a + b
        a = b
        b = num
        count += 1

nth = int(input("\nEnter an integer to generate the equivalent fibonacci sequence: "))
generate_fibonacci(nth)

#Below are two practices on function parameters

#Function with Default Parameters:
"""Write a Python function named greet_user that takes a 
name as input and prints a greeting message. If no name 
is provided, the function should use the default name 
"Guest". Test your function with different names and 
verify that it behaves correctly when a name is 
provided and when no name is provided."""

def greet_user(name="Guest"):
    message = f"\nHi {name}, welcome to all seasons!"
    return message

user_1 = greet_user("Paul")
user_2 = greet_user()
print(f"\n{user_1} \n{user_2}")


#Function with Keyword Arguments:
"""Write a Python function named calculate_discount that calculates the discounted price 
of an item based on its original price and a discount percentage. The function should
have two parameters: original_price and discount_percentage. If no discount_percentage
is provided, the function should apply a default discount of 10%. Test your function 
by calling it with different values for original_price and discount_percentage, using 
both positional and keyword arguments"""

def calculate_discount(original_price, discount_percentage = 0.1 ):
    discount_price = original_price * discount_percentage
    return discount_price

item_1 = calculate_discount(original_price = 5000, discount_percentage = 0.2)
item_2 = calculate_discount(2000) 
print(f"\nDiscount for item one is {item_1} \nDiscount for item two is {item_2}")





