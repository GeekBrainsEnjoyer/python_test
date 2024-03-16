import argparse


def prime_num(num):
    prime = True

    if num < 2 or num > 100000:
        return 'Число должно быть больше 1 и меньше 100000'
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False

        return 'Простое' if prime else 'Не является простым'


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Enter num.')
    parser.add_argument('num', type=int, default=False)

    arg = parser.parse_args()

    print(prime_num(arg.num))
