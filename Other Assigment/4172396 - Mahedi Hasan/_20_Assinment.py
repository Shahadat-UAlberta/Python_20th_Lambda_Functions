## Write a Pthon program to count even and odd in a list of integers using lambda function.

lst = [1,2,3,4,5,6]

evn_lst = filter(lambda num: num % 2 == 0,lst)
odd_lst = filter(lambda num: num % 2 != 0,lst)
print(list(evn_lst))
print(list(odd_lst))
