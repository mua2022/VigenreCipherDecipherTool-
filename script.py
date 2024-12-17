def shift_character(char, shift, encrypt=True):
    """
    Shifts a character within A-Z by a given shift value.
    For decryption, the shift is subtracted.
    """
    base = ord('A')
    if encrypt:
        return chr((ord(char) - base + shift) % 26 + base)
    else:
        return chr((ord(char) - base - shift + 26) % 26 + base)


def vigenere_cipher(text, key, encrypt=True):
    """
    Encrypts or decrypts the given text using the Vigenère Cipher method.
    :param text: The input plaintext or ciphertext (string).
    :param key: The keyword used for encryption/decryption (string).
    :param encrypt: True for encryption, False for decryption.
    :return: The resulting ciphertext or plaintext.
    """
    result = []
    clean_text = text.upper().replace(" ", "")  # Ignore spaces and convert to uppercase
    clean_key = key.upper().replace(" ", "")    # Clean the key

    if not clean_key:
        print("Error: Key cannot be empty.")
        return ""

    key_index = 0
    key_length = len(clean_key)

    for char in clean_text:
        if char.isalpha():  # Only process alphabetic characters
            shift = ord(clean_key[key_index % key_length]) - ord('A')
            result_char = shift_character(char, shift, encrypt)
            result.append(result_char)
            key_index += 1
        else:
            # If it's not an alphabetic character, keep it unchanged
            result.append(char)

    return "".join(result)


def main():
    print("===== Vigenère Cipher Tool =====")
    print("1. Encrypt")
    print("2. Decrypt")

    # Prompt user for mode
    choice = input("Choose an option (1/2): ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice. Exiting...")
        return

    # Prompt user for input
    text = input("Enter the text (plaintext or ciphertext): ").strip()
    key = input("Enter the key (keyword): ").strip()

    if not key or not text:
        print("Error: Text and key cannot be empty.")
        return

    # Perform encryption or decryption based on user's choice
    if choice == '1':
        result = vigenere_cipher(text, key, encrypt=True)
        print(f"\nEncrypted Ciphertext: {result}")
    else:
        result = vigenere_cipher(text, key, encrypt=False)
        print(f"\nDecrypted Plaintext: {result}")


if __name__ == "__main__":
    main()
