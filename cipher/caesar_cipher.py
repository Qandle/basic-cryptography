def caesar_cipher(shift, shifted_number, message):
    cipher_text = ""
    if shift == "left":
        for letter in message:
            if letter.isalpha():
                if letter.isupper():
                    cipher_letter = chr(((ord(letter) - 65 + 26 - shifted_number) % 26) + 65)
                    cipher_text += cipher_letter
                else:
                    cipher_letter = chr(((ord(letter) - 97 + 26 - shifted_number) % 26) + 97)
                    cipher_text += cipher_letter
            else:
                cipher_text += letter
    if shift == "right":
        for letter in message:
            if letter.isalpha():
                if letter.isupper():
                    cipher_letter = chr(((ord(letter) - 65 + shifted_number) % 26) + 65)
                    cipher_text += cipher_letter
                else:
                    cipher_letter = chr(((ord(letter) - 97 + shifted_number) % 26) + 97)
                    cipher_text += cipher_letter
            else:
                cipher_text += letter
    return cipher_text

print(caesar_cipher("left", 1, "BCD"))
print(caesar_cipher("right", 1, "abc"))

print(caesar_cipher("right", 5, "While these methods are simple to understand and implement They are not secure for protecting sensitive data"))