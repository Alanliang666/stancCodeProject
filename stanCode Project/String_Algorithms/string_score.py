"""
File: string_score.py
Name: Alan
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    Tests the score function with different example strings.
    """
    print(score('1aB4rC'))  # digit->1 ; upper->2; lower->3
    # 12
    print(score('aaaaA3'))
    # 15


def score(string):
    """
    : param string : str, The input string to be evaluated
    : return : int, The calculated total score
    Calculates the total score of a string based on character types.
    """
    count = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isupper():
            count += 2
        elif ch.islower():
            count += 3
        else:
            count += 1
    return count


if __name__ == '__main__':
    main()
