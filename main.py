def encrypt(my_text, my_shift):
    shifted_word = ""
    for i in range(len(my_text)):
        index_in_alphabet = alphabet.index(my_text[i])
        shifted_word += alphabet[index_in_alphabet + my_shift]
    print(f"{my_text} shifted by {my_shift} positions is {shifted_word}")


def decrypt(my_text, my_shift):
    shifted_word = ""
    for i in range(len(my_text)):
        index_in_alphabet = alphabet.index(my_text[i])
        shifted_word += alphabet[index_in_alphabet - my_shift]
    print(f"{my_text} shifted by {my_shift} positions is {shifted_word}")


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Enter 'encode' to encrypt, or 'decode' to decrypt : ").lower()

if direction != "encode" or direction != "decode":
    print("Please enter a valid option : ")
    direction = input("Enter 'encode' to encrypt, or 'decode' to decrypt : ").lower()

text = input("Type your message here : ").lower()
shift = int(input("Enter the shift number here : "))
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)




