lst = input().split()


odd = list(filter(lambda value: int(value) % 2 == 1, lst))
even = list(filter(lambda value: int(value) % 2 == 0, lst))
print("Odd numbers List: ", list(odd))
print("Even numbers List: ", list(even))

print("Total odd numbers: ", len(odd))
print("total even numbers: ", len(even))
