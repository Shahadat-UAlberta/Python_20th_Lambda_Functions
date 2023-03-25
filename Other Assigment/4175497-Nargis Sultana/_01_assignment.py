#Write a Python Program to count even and Odd in a List of Integers using Lambda Function.

A_list = [2,3,4,5,6,7,8,10]
count_even= len(list(filter(lambda num: num%2==0, A_list)))
count_odd= len(list(filter(lambda num: num%2==1, A_list)))
print("The number of even numbers of the list is: ", count_even)
print("The number of odd numbers of the list is: ", count_odd)