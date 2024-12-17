# Vigenère Cipher - Encipher & Decipher Tool

This project is a simple **Vigenère Cipher** tool that allows users to **encrypt** and **decrypt** text using a keyword. It is implemented in HTML, CSS, and JavaScript, making it lightweight and easily hostable on GitHub Pages.

## 🔗 Live Demo
You can try the tool live here: [**GitHub Pages**](https://mua2022.github.io/vigenrecipherdeciphertool)

---

## ⚡ What is the Vigenère Cipher?

The **Vigenère Cipher** is a method of encrypting text that extends the Caesar Cipher by using a keyword. It operates as follows:

1. Each letter in the plaintext is shifted based on the position of the corresponding letter in the keyword.
2. The keyword repeats when it's shorter than the plaintext.

For example:

- **Plaintext**: `HELLO`
- **Key**: `KEY`
- **Encryption**:
   - `H` + `K` = `R` (Shift by 10)
   - `E` + `E` = `I` (Shift by 4)
   - `L` + `Y` = `J` (Shift by 24)
   - `L` + `K` = `V` (Shift by 10)
   - `O` + `E` = `S` (Shift by 4)

Thus, the **ciphertext** becomes: `RIJVS`.

---

## 📑 Features

- **Encipher** text using a keyword.
- **Decipher** text back to the original plaintext.
- Provides clear explanations of how the Vigenère Cipher works.
- Clean and intuitive user interface.
- Fully client-side implementation (no backend required).

---

## 🚀 How It Works

### Encryption

1. Convert the plaintext and keyword to uppercase.
2. Align each letter of the plaintext with the keyword. Repeat the keyword if necessary.
3. For each character in the plaintext:
   - Calculate the shift based on the corresponding keyword letter.
   - Shift the plaintext letter forward by the keyword shift (mod 26 to stay within A-Z).
4. Return the encrypted text.

### Decryption

1. Use the same keyword as encryption.
2. For each character in the ciphertext:
   - Calculate the shift based on the keyword letter.
   - Shift the ciphertext letter backward by the keyword shift (mod 26 to stay within A-Z).
3. Return the decrypted plaintext.

---

## 🛠️ How to Use the Tool

1. Open the tool in your browser or on the [GitHub Pages link](https://mua2022.github.io/vigenrecipherdeciphertool).
2. Enter the text you want to encrypt or decrypt.
3. Provide a **keyword** (this is required for both encryption and decryption).
4. Click **Encipher** to encrypt the text or **Decipher** to decrypt it.
5. The result will be displayed in the output area.

---

## 🧩 File Structure

vigenreCipherDecipherTool/<br>
                            │<br>
                            ├── index.html   # Main HTML structure <br>
                            ├── style.css    # Styling for the webpage<br>
                            └── script.js    # JavaScript logic for enciphering and deciphering



---

## 💻 Code Explanation

### `script.js` Logic

1. **Helper Function**:
   - `shiftCharacter(char, shift)`:
     - Shifts a character within 'A'-'Z' bounds by the given amount.

2. **Vigenère Cipher Function**:
   - `vigenereCipher(text, key, encrypt)`:
     - Takes the input text, key, and a flag (encrypt or decrypt).
     - Processes each letter, calculates shifts, and returns the result.

3. **Encipher & Decipher**:
   - `encipher()` and `decipher()` functions:
     - Get input from the user.
     - Call the main Vigenère function with the correct mode.
     - Display the result in the HTML.

### Example:

For plaintext `ATTACKATDAWN` with keyword `LEMON`:

| Plaintext | A | T | T | A | C | K | A | T | D | A | W | N |
|-----------|---|---|---|---|---|---|---|---|---|---|---|---|
| Key       | L | E | M | O | N | L | E | M | O | N | L | E |
| Ciphertext| L | X | F | O | P | V | E | F | R | N | H | R |

The ciphertext is `LXFOPVEFRNHR`.

---

# Vigenère Cipher - Python Script

This Python script allows users to **encrypt** and **decrypt** text using the Vigenère Cipher method. The Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to determine shifting values for each letter in the plaintext.

---

## 🚀 How the Script Works

### 1. **Core Functions**

#### `shift_character(char, shift, encrypt=True)`
- **Purpose**: Shifts a character within the range 'A' to 'Z' by a given shift value.
- **Parameters**:
  - `char`: Single uppercase character (e.g., 'A').
  - `shift`: The shift value calculated from the keyword.
  - `encrypt`: Boolean flag (True for encryption, False for decryption).
- **How It Works**:
  - Converts the character into a numeric position (`0–25`) using `ord`.
  - Shifts forward (for encryption) or backward (for decryption).
  - Wraps around using `% 26` to stay within the alphabet range.

#### `vigenere_cipher(text, key, encrypt=True)`
- **Purpose**: Enciphers or deciphers the input text using the keyword.
- **Parameters**:
  - `text`: The input plaintext or ciphertext (string).
  - `key`: The keyword used for encryption/decryption.
  - `encrypt`: Boolean flag (True for encryption, False for decryption).
- **How It Works**:
  1. Converts both the `text` and `key` to uppercase and removes spaces.
  2. Loops through each letter in the text:
     - Calculates the shift using the corresponding key letter.
     - Calls `shift_character` to perform the shift.
     - Handles non-alphabetic characters (keeps them unchanged).
  3. Returns the resulting string.

---

### 2. **Program Flow**

#### Step 1: Prompt User for Input
- The script starts by displaying a menu:
===== Vigenère Cipher Tool =====

1. Encrypt
2. Decrypt

- The user selects **Encrypt** (1) or **Decrypt** (2).

#### Step 2: Input Text and Key
- The user enters:
- **Text**: The plaintext or ciphertext.
- **Key**: The keyword used for shifting.

#### Step 3: Perform Encryption or Decryption
- Based on the user's choice:
- Calls the `vigenere_cipher` function with `encrypt=True` for encryption.
- Calls the `vigenere_cipher` function with `encrypt=False` for decryption.

#### Step 4: Display the Result
- The resulting ciphertext or plaintext is displayed.

---

## 📄 Hosting Instructions

You can host this project on GitHub Pages in three steps:

1. **Upload Files**: Push the `index.html`, `style.css`, and `script.js` files to a GitHub repository.
2. **Enable Pages**:
   - Go to **Settings** > **Pages**.
   - Under "Source," select `main` branch and save.
3. Access your live site at:  
   `https://<your-username>.github.io/<repository-name>`

---

## 🛡️ License

This project is licensed under the MIT License. Feel free to use, modify, and share.

---

## 👨‍💻 Author

**[MUA EMMANUEL]**  
GitHub: [**mua2022**](https://github.com/mua2022)

---

## 🎯 Contributing

Contributions are welcome! If you find a bug or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

### 🔗 References

- [Vigenère Cipher - Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
- [GitHub Pages Documentation](https://pages.github.com)
