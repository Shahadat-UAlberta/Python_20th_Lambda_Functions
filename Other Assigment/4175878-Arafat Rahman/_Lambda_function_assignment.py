lst=[1,2,3,4,5,6,7,8,9,10]
odd_list = filter(lambda odd_sum: odd_sum % 2 == 1,lst)
even_list =filter(lambda even_sum: even_sum % 2 == 0,lst)
print(list(odd_list))
print(list(even_list))


