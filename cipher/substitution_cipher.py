def substitution_cipher(normal_letter, sub_letter, message):
    cipher_text = ""
    for letter in message:
        index = normal_letter.find(letter.upper())
        if letter.isalpha():
            if letter.isupper():
                cipher_text += letter.replace(letter ,sub_letter[index])
            else:
                cipher_text += letter.replace(letter ,(sub_letter[index]).lower())
        elif letter.isnumeric():
            cipher_text += letter.replace(letter ,sub_letter[index])
        else:
            cipher_text += letter
    return cipher_text

normal_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
substitution_letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(substitution_cipher(normal_letter, substitution_letter, "While these methods are simple to understand and implement They are not secure for protecting sensitive data"))