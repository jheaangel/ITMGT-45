'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    4 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.


    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "


    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.


    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.


    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if shift == ' ':
        return ' '

    shifted_letter = ord(letter) + shift
    if shifted_letter > ord('Z'):
        shifted_letter -= 26

    return chr(shifted_letter)




def caesar_cipher(message, shift):
    '''Caesar Cipher.
    6 points.

    Apply a shift number to a string of uppercase English letters and spaces.


    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.


    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    ciphered_message = ""
    for char in message:
        if char.isalpha():
            ciphered_char = chr(ord(char) + shift)
            if ciphered_char > 'Z':
                ciphered_char = chr(ord(ciphered_char) - 26)
        else:
            ciphered_char = char
        ciphered_message += ciphered_char
    return ciphered_message



def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    4 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.


    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "


    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.


    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    letter_code = ord(letter)
    shift_code = ord(letter_shift) - ord('A')
    if letter_code == ord(' '):
        return ' '
    shifted_code = letter_code + shift_code
    if shifted_code > ord('Z'):
        shifted_code -= 26
    return chr(shifted_code)



def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    6 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.


    Example:
    vigenere_cipher("A C", "KEY") -> "K A"


    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".


    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.


    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    board = []
    for i in range(26):
        row = []
        for j in range(26):
            row.append(chr((i + j) % 26 + ord('A')))
        board.append(row)

    new_key = (key * (len(message) // len(key) + 1))[:len(message)]

    vigenere_text = ""
    for i, char in enumerate(message):
        if char == ' ':
            vigenere_text += ' '
        else:
            vigenere_text += board[ord(char) - ord('A')
                                   ][ord(new_key[i]) - ord('A')]

    return vigenere_text
