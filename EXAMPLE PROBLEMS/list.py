def even(data):
    return data % 2 == 0

def odd(data):
    return not even(data)

li = [4, 78, 23, 4, 7, 34, 100, 23, 25]

even_numbers = list(filter(even, li))
odd_numbers = list(filter(odd, li))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
