# Define the list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define the lambda function to check if a number is even
is_even = lambda x: x % 2 == 0

# Define the lambda function to check if a number is odd
is_odd = lambda x: x % 2 != 0

# Use filter() to get the even numbers from the list and count them
even_count = len(list(filter(is_even, numbers)))

# Use filter() to get the odd numbers from the list and count them
odd_count = len(list(filter(is_odd, numbers)))

# Print the results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
