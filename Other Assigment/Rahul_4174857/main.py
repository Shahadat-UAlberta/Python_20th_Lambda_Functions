# Sample List
lst = [10, 21, 30, 45, 63, 76, 82]

is_even = lambda x: x % 2 == 0

even_count = len(list(filter(is_even, lst)))
odd_count = len(lst) - even_count

print("Number of even integers :", even_count)
print("Number of odd integers :", odd_count)