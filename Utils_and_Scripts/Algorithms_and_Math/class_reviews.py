"""
File: class_reviews.py
Name: Alan
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
EXIT = -1


def main():
    """
    Calculate and store each class score, output each class maximum, minimum, average score
    """
    # Initialize SC001 variables
    c_001 = 0
    max_001 = -float('inf')
    min_001 = float('inf')
    t_001 = 0

    # Initialize SC101 variables
    c_101 = 0
    max_101 = -float('inf')
    min_101 = float('inf')
    t_101 = 0

    while True:
        stan_class = input('Which class? ')
        if stan_class == str(EXIT):
            break
        stan_class = stan_class.lower()  # Convert input to lowercase
        if stan_class == 'sc001':
            max_001, min_001, c_001, t_001 = update_scores(c_001, max_001, min_001, t_001)
        elif stan_class == 'sc101':
            max_101, min_101, c_101, t_101 = update_scores(c_101, max_101, min_101, t_101)
        else:
            print('No this class, please retype the class')
    if c_001 == 0 and c_101 == 0:  # Check if no scores were entered
        print('No class scores were entered')
    else:
        print_class_result('SC001', max_001, min_001, c_001, t_001)
        print_class_result('SC101', max_101, min_101, c_101, t_101)


def update_scores(count, maximum, minimum, total):
    """
    Prompts the user for a score and updates the class statistics.
    :param maximum: float, maximum number in the class
    :param minimum: float, minimum number in the class
    :param count: int, count total data in the class
    :param total: float, calculate total scores in the class
    :return maximum: float, maximum number in the class
    :return minimum: float, minimum number in the class
    :return count: int, count total data in the class
    :return total: float, calculate total scores in the class
    """
    score = float(input('Score: '))
    if score > maximum:
        maximum = score
    if score < minimum:
        minimum = score
    total += score
    count += 1
    return count, maximum, minimum, total


def print_class_result(class_name, maximum, minimum, count, total):
    """
    Prints the statistics for a specific class.
    If no scores were entered, prints a 'No score' message.
    :param class_name: str, name the class
    :param maximum: float, maximum number in the class
    :param minimum: float, minimum number in the class
    :param count: int, count total data in the class
    :param total: float, calculate total scores in the class
    """
    print('==============' + class_name + '==============')
    if count == 0:
        print('No score for ' + class_name)

    else:
        avg = total / count
        print('Max (' + class_name[-3:] + ') : ' + str(int(maximum)))
        print('Min (' + class_name[-3:] + ') : ' + str(int(minimum)))
        print('Avg (' + class_name[-3:] + ') : ' + str(avg))

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #


if __name__ == '__main__':
    main()
