# Caesar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(original_text, shift_amount, operation):
    output_text = ""

    for char in original_text:
        if char.isalpha():
            cur_index = alphabet.index(char)
            shifted_index = cur_index + \
                shift_amount if operation == 'encode' else cur_index - shift_amount
            shifted_index %= len(alphabet)
            output_text += alphabet[shifted_index]
        else:
            output_text += char

    print(f"The {operation}d result is: {output_text}")

should_continue = True

while should_continue: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    answer = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if answer == 'no':
        should_continue = False
        print('Goodbye!')