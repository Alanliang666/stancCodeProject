"""
File: caesar.py
Name: Alan
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Input
        Get secret number to make new alphabet, and get ciphered string to deciphered
    Output
        Use string show the deciphered answer
    """
    secret_number = int(input('Secret number: '))
    ciphered_string = input("What's the ciphered string? ")
    ans = deciphered(secret_number, ciphered_string)
    print('The deciphered string is: ' + ans)


def deciphered(secret_number, ciphered_string):
    """
    :parma secret_number: int
    :parma ciphered_string: str
    :return: str
    """
    ciphered_string = ciphered_string.upper()  # Case-insensitive process
    new_alphabet = ''
    last_num = ALPHABET[26 - secret_number:]  # Gets the last [secret_number] letters
    new_alphabet += last_num  # Places them at the beginning
    for i in range(len(ALPHABET) - secret_number):  # Since letters can't repeat, exclude the ones we already have
        ch = ALPHABET[i]
        new_alphabet += ch

    ans = ''
    for i in ciphered_string:  # Break down each ciphered
        spot = new_alphabet.find(i)
        if not i.isalpha():  # Symbol need extra process
            ans += i
        else:
            for j in range(len(ALPHABET)):
                new_ch = ALPHABET[j]
                if spot == j:
                    ans += new_ch
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
