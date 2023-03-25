lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_checker = len(list(filter(lambda value: (value % 2 != 0), lst)))
even_checker = len(list(filter(lambda value: (value % 2 == 0), lst)))
print(odd_checker)
print(even_checker)
