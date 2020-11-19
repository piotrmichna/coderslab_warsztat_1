from random import randint


def get_user_number():
    while True:
        try:
            result=int(input('Guess the number: '))
            break
        except ValueError:
            print("I's not number")


def guess_the_number():
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
