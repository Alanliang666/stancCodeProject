"""
File: name_sq.py (extension)
Name: Alan
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    Prompts the user for a name and generates a square pattern based on that name.
    """
    print('This program prints a name in a square pattern!')
    name = input('Name: ')
    print(name)
    column(name)
    print(reverse(name))


def column(name):
    """
    @param name: str, The name provided by the user
    Prints the vertical sides of the square pattern.
    It iterates through the middle characters of the name
    """
    for i in range(len(name)-2):
        print(name[i+1], end='')  # Print left side letter
        for j in range(len(name)-2):  # Print middle space
            print(' ', end='')
        print(name[len(name)-i-2])  # Print right side letter


def reverse(name):
    """
    @param name: str, The string to be reversed
    @return: str, The reversed string
    Reverses the given string.
    """
    ans = ''
    for i in range(len(name)):
        ans = name[i] + ans
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
