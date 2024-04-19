#List Manipulation

numbers = [1, 2, 3, 4, 5]

#Print the length of the list.
print(len(numbers))

# Print the first 3 elements of the list.
print(numbers[0:3])

#Append the number 6 to the end of the list and print the modified list.
numbers.append(6)
print(numbers)

#Remove the element at index 2 and print the modified list.
numbers.pop(2)
print(numbers)

#Tuple Manipulation:
person = ('John', 30, 'Male')

#Print the length of the tuple.
print(len(person))

#Print the last element of the tuple.
print(person[2])

#. Convert the tuple to a list and append the element 'Engineer' to the list. Print the modified list.
Employee =list(person)
Employee.append("Engineer")
print(Employee)

# Extract the first two elements of the tuple and print them.
print(person[:2])

#Dictionary Manipulation:

person = {'name': 'John', 'age': 30, 'gender': 'Male'}

# Print the length of the dictionary.
print(len(person))

# Print the value associated with the key 'age'.
print(person.get('age'))

# Add a new key-value pair {'city': 'New York'} to the dictionary and print the modified dictionary.
person['city']= 'New York'
print(person)

# Remove the key 'gender' from the dictionary and print the modified dictionary.
gender = person.pop('gender')
print(person)                
                
#Set Manipulation:

numbers = {1, 2, 3, 4, 5}

# Print the length of the set.
print(len(numbers))

# Add the number 6 to the set and print the modified set.
numbers.add(6)
print(numbers)

# Remove the number 3 from the set and print the modified set.
numbers.remove(3)
print(numbers)

# Create a new set {4, 5, 6, 7, 8} and perform the following set operations: 
digits = {4,5,6,7,8}

# Union of the two sets
Sumup = numbers.union(digits)
print(Sumup)

# Intersection of the two sets
Sumup = numbers.intersection(digits)
print(Sumup)

# Difference between the two sets
Sumup = numbers.difference(digits)
print(Sumup)


def count_vowels():
    vowels = ['a', 'e' ,'i', 'o', 'u']
    count = 0
    string= (input("\nEnter a string to count it's vowels. ").lower())
#    string.lower()
    print(string)
    
    for character in string:
        if character in vowels:
            count += 1
            
    return count
    
vowel_count = count_vowels()
print(f"\nThe string has {vowel_count} vowels.")


def reverse_list():
    listing = []
    digits = input("\nEnter a list of digits or words to reverse them: ")
    
    for digit in digits:
        listing.append(digit)

    listing.reverse()
    return listing

checker = reverse_list()
print(checker)

def generate_fibonacci():
    n_interger = ("\nEnter an integer: ")
    pass

#Function with Default Parameters:
"""Write a Python function named greet_user that takes a 
name as input and prints a greeting message. If no name 
is provided, the function should use the default name 
"Guest". Test your function with different names and 
verify that it behaves correctly when a name is 
provided and when no name is provided."""

def greet_user(name="Guest"):
    message = f"Hi {name}, welcome to all seasons!"
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

item_1 = calculate_discount(original_price = 1000, discount_percentage = 0.2)
item_2 = calculate_discount(2000) 
print(f"\n{item_1} \n{item_2}")