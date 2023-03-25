# Write a Python Program to count even and Odd in a List of Integers using Lambda Function.
lst = []
number = int(input("ENTER THE NUMBER OF ELEMENTS: "))
if number == 0:
    print("SORRY, NO LIST CAN BE CREATED BECAUSE THE NUMBER OF ELEMENT IS 0")
elif number != 0:
    for i in range(0, number):
        elements = int(input())
        lst.append(elements)
    print(f"THE LIST AS YOU INPUTTED: {lst}")
    odd_list = list(filter(lambda num: num % 2 != 0, lst))
    print(f"THE ODD NUMBERS ARE: {list(odd_list)}")

    even_list = list(filter(lambda num: num % 2 == 0, lst))
    print(f"THE EVEN NUMBERS ARE: {list(even_list)}")

    print(f"THE NUMBER OF ODD NUMBERS: {len(odd_list)}")
    print(f"THE NUMBER OF EVEN NUMBERS: {len(even_list)}")



