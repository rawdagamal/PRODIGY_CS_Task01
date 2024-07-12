def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            shifted = ord(char) + shift  # Calculate the new position of the encrypted character
            if char.islower():  # If the character is lowercase
                if shifted > ord('z'):  # Ensure the character does not exceed lowercase bounds
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  # If the character is uppercase
                if shifted > ord('Z'):  # Ensure the character does not exceed uppercase bounds
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)  # Add the encrypted character to the encrypted text
        else:
            encrypted_text += char  # If the character is not an alphabet letter, add it unchanged to the encrypted text
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is an alphabet letter
            shifted = ord(char) - shift  # Calculate the new position of the decrypted character
            if char.islower():  # If the character is lowercase
                if shifted < ord('a'):  # Ensure the character does not fall below lowercase bounds
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():  # If the character is uppercase
                if shifted < ord('A'):  # Ensure the character does not fall below uppercase bounds
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)  # Add the decrypted character to the decrypted text
        else:
            decrypted_text += char  # If the character is not an alphabet letter, add it unchanged to the decrypted text
    return decrypted_text

def main():
    message = input("Enter message to encrypt/decrypt: ")  # Receive message from user
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))  # Receive shift value from user
            break  # If a valid integer is entered, exit the loop
        except ValueError:
            print("Invalid input! Please enter an integer.")

    encrypted_message = caesar_encrypt(message, shift)  # Encrypt the message
    decrypted_message = caesar_decrypt(encrypted_message, shift)  # Decrypt the message
    
    print("Encrypted message:", encrypted_message)  # Print the encrypted message
    print("Decrypted message:", decrypted_message)  # Print the decrypted message

if __name__ == "__main__":
    main()