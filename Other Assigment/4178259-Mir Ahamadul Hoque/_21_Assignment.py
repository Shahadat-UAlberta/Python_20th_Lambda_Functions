# WRITE A PYTHON PROGRAM TO COUNT EVEN AND ODD IN A LIST OF INTEGERS USING LAMBDA FUNCTION.


lst = [1,6,8,9,10,44,16,18,15,17]

even_numbers = filter(lambda num: num % 2 == 0,lst)

print(list(even_numbers))

odd_numbers = filter(lambda num: num % 2 != 0,lst)

print(list(odd_numbers))

print('-------------------------------')

even_numbers2 = list(filter(lambda num: num % 2 == 0,lst))
print(even_numbers2)

odd_numbers = list(filter(lambda num: num % 2 != 0,lst))
print(odd_numbers)

print('-------------------------------')

even_numbers2 = len(list(filter(lambda num: num % 2 == 0,lst)))
print(even_numbers2)

odd_numbers = len(list(filter(lambda num: num % 2 != 0,lst)))
print(odd_numbers)

print('-------------------------------')

even_numbers2 = len(list(filter(lambda num: num % 2 == 0,lst)))
print(even_numbers2)

odd_numbers = len(list(filter(lambda num: num % 2 != 0,lst)))
print(odd_numbers)

print('-------------------------------')

even_numbers2 = len(list(filter(lambda num: num % 2 == 0,lst)))
print(even_numbers2)

odd_numbers = len(list(filter(lambda num: num % 2 != 0,lst)))
print(odd_numbers)
