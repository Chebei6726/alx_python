#!/usr/bin/python3
def is_prime(number):
   if number <= 1:
    return False

   for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False

   return True

try:
    # Get a number from the user
    number_to_check = int(input("Enter a number to check if it's prime: "))
    #Call function & print
    if is_prime(number_to_check):
        print(f"{number_to_check} is a prime number.")
    else:
        print(f"{number_to_check} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")