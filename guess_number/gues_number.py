from random import randint


def get_user_number():
    """the function gets the player's answers
    and checks for errors

    :return: integer number from 1..100
    """
    while True:
        try:
            result = int(input('Guess the number: '))
            if result < 1 or result > 100:
                print('Number is from 1 to 100.')
            else:
                break
        except ValueError:
            print("I's not number")

    return result


def guess_the_number():
    """Main function Guess The Number aplication"""

    secret_number = randint(1, 100)

    while True:
        usr_number = get_user_number()
        if secret_number == usr_number:
            print('Great, you are a winner')
            break
        else:
            if secret_number > usr_number:
                print('To small..')
            else:
                print('To big..')


if __name__ == '__main__':
    guess_the_number()
