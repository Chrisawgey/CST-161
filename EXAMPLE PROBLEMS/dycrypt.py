def caesar_cipher(text, key, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if mode == 'encrypt':
                #it first calculates the ASCII value of the current character using ord(char). 
                # It subtracts the shift value to make the character relative to 'A' or 'a'.
                #It subtracts the key to perform the Caesar cipher decryption.
                #it takes the result modulo 26 to ensure it wraps around the alphabet.
                #Finally, it adds back the shift value and converts the result to a character using chr().
                shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        elif char.isdigit():
            if mode == 'encrypt':
                shifted_digit = (int(char) + key) % 10
            else:
                shifted_digit = (int(char) - key) % 10
            result += str(shifted_digit)
        else:
            result += char

    return result

# Get user input for the text, key, and mode (encrypt or decrypt)
text = input("Enter the text: ")
key = int(input("Enter the key (a number between 1 and 25): "))
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

if 1 <= key <= 25 and mode in ['encrypt', 'decrypt']:
    if mode == 'encrypt':
        result_text = caesar_cipher(text, key, mode='encrypt')
    else:
        result_text = caesar_cipher(text, key, mode='decrypt')
    print("Result: ", result_text)
else:
    print("Invalid key or mode. The key should be a number between 1 and 25, and the mode should be 'encrypt' or 'decrypt'.")
