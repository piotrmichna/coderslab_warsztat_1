from random import randint


def get_user_number():
    return int(input('Guess the number: '))


def guess_the_number():
    secret_number = randint(1, 100)

    while True:
        usr_number = get_user_number()
        if secret_number == usr_number:
            print('Great, you are a winner')
            break
        else:
            print('You missed the number..')


if __name__ == '__main__':
    guess_the_number()
