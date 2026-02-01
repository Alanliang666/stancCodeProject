"""
File: hangman.py
Name: Alan
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Playing the hangman game, guess the word until hit the string or end game in the 7 times turns
    """
    count = 0  # initialize the wrong guess turn

    # Game start info
    n = random_word()
    dashed = replace_dashed(n)
    print_status(count, dashed)

    # Keeping guess until lose the game or bingo!!
    while N_TURNS != count:
        ans = input('Your guess: ')
        if not ans.isalpha() or len(ans) != 1:  # Avoid the wrong format enter the function
            print('illegal format')
        else:
            ans = ans.upper()  # case-insensitive process
            dashed, count = contain_checker(ans, n, dashed, count)
            check_game_over(count, dashed, n)
            if dashed == n:
                break


def replace_dashed(n):
    """
    @param n: str, the answer word
    @return: str, a string composed entirely of dashes
    Creates a dashed string of the same length as the answer.
    """
    dashed = ''
    for i in range(len(n)):
        dashed += '-'
    return dashed


def print_status(count, dashed):
    """
    @param count: int, current number of wrong guesses
    @param dashed: str, current dashed string state
    Printing the status current count and dashed
    """
    print('The word looks like: ' + dashed)
    print('You have ' + str(N_TURNS - count) + ' wrong guesses left.')


def replace_ans(ans, n, dashed):
    """
    @param ans: str, the character guessed by the user
    @param n: str, the correct answer word
    @param dashed: str, current dashed string state
    @return: str, the updated dashed string with the correct guess revealed
    Reveals the guessed character in the dashed string.
    """
    ans_word = ''
    for i in range(len(n)):
        if n[i] == ans:
            ans_word += ans
        else:
            ans_word += dashed[i]
    return ans_word


def contain_checker(ans, n, dashed, count):
    """
    @param ans: str, the character guessed by the user
    @param n: str, the correct answer word
    @param dashed: str, current dashed string state
    @param count: int, current number of wrong guesses
    @return (str,int): containing the updated dashed string and error count
    Check if the user's guess is in the answer word.
    Update the dashed string or the wrong guess count accordingly.
    """
    if ans in n:
        dashed = replace_ans(ans, n, dashed)
        print('You are correct!')
    else:
        count += 1
        print('There is no ' + ans + "'s in the word.")
    return dashed, count


def check_game_over(count, dashed, n):
    """
    @param count: int, current number of wrong guesses
    @param dashed: str, current dashed string state
    @param n: str, the correct answer word
    Determines if the game has ended (win or loss) and prints the result.
    If the game continues, it prints the current status.
    """
    if dashed == n:
        print('You win!!')
        print('The answer is: ' + n)
    elif N_TURNS == count:
        print('You are completely hung :( ')
        print('The answer is: ' + n)
    else:
        print_status(count, dashed)


def random_word():
    """
    @return: str, random string maker
    Make a random string
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
