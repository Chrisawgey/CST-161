def find_gcd(a, b):
    while b:
        a, b = b, a % b
        print(f"Step: {a} = {a} % {b}" if b else f"Step: GCD = {a}")
    return a

# Get user input 
smaller_number = int(input("Enter the smaller number: "))
larger_number = int(input("Enter the larger number: "))

if smaller_number > larger_number:
    smaller_number, larger_number = larger_number, smaller_number

gcd = find_gcd(larger_number, smaller_number)
print(f"The greatest common divisor is {gcd}")

