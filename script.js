// Helper function to keep shifts within bounds of 'A'-'Z'
function shiftCharacter(char, shift) {
    const base = 'A'.charCodeAt(0);
    return String.fromCharCode(((char.charCodeAt(0) - base + shift + 26) % 26) + base);
}

// Function to encipher
function vigenereCipher(text, key, encrypt = true) {
    const result = [];
    const cleanText = text.toUpperCase().replace(/[^A-Z]/g, ''); // Only A-Z
    const cleanKey = key.toUpperCase().replace(/[^A-Z]/g, '');

    if (cleanKey.length === 0) {
        alert("Please enter a valid key.");
        return '';
    }

    let keyIndex = 0;

    for (let i = 0; i < cleanText.length; i++) {
        const textChar = cleanText[i];
        const keyChar = cleanKey[keyIndex % cleanKey.length];
        const shift = keyChar.charCodeAt(0) - 'A'.charCodeAt(0);

        const newChar = encrypt
            ? shiftCharacter(textChar, shift)
            : shiftCharacter(textChar, -shift);

        result.push(newChar);
        keyIndex++;
    }

    return result.join('');
}

function encipher() {
    const text = document.getElementById("text").value;
    const key = document.getElementById("key").value;
    const result = vigenereCipher(text, key, true);
    document.getElementById("result").innerText = result || "Invalid input.";
}

function decipher() {
    const text = document.getElementById("text").value;
    const key = document.getElementById("key").value;
    const result = vigenereCipher(text, key, false);
    document.getElementById("result").innerText = result || "Invalid input.";
}
