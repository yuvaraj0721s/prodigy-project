def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher."""
    encrypted_text = ""
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Check if character is a letter (ignoring non-alphabetic characters)
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # If not an alphabetic character, don't change it
            encrypted_text += char
    
    return encrypted_text


def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher."""
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher Encryption/Decryption Program")
    
    # Take user input for the text and shift value
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (an integer): "))
    
    # Ask user for encryption or decryption choice
    choice = input("Do you want to (e)ncrypt or (d)ecrypt the message? ").lower()
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")


if __name__ == "__main__":
    main()
