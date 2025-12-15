"""
File: similarity.py (extension)
Name:
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Acquires two DNA sequences from the user and displays the substring from the longer sequence
    that has the highest similarity to the shorter sequence.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')
    ans = (homology(long_sequence, short_sequence))
    print('The best match is ' + ans)


def homology(long, short):
    """
    :param long : str, The longer DNA sequence to be searched.
    :param short : str, The target DNA sequence to match.
    :return: str, The substring from 'long_seq' with the highest matching score.
    Finds the substring in 'long_seq' that best matches 'short_seq'.
    """
    long = long.upper()  # Convert to uppercase for case-insensitive comparison
    short = short.upper()
    count = 0
    maximum = 0
    ans = ''

    for i in range(len(long)-len(short)+1):  # Add +1 to include the last possible substring in the range
        new_long = long[i:len(short)+i]  # Extract a substring from the long sequence with the same length
        for j in range(len(new_long)):  # Iterate through characters to compare them index by index
            if new_long[j] == short[j]:
                count += 1
        if maximum < count:  # Update the best match if the current substring has a higher score
            maximum = count
            ans = new_long
            count = 0  # Reset the count for the next iteration
        else:
            count = 0
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
