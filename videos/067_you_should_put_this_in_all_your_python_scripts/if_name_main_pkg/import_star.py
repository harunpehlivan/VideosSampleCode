from if_name_main_pkg.bad_script import *


def compute_val():
    l = [0, 1, 2, 3, 4, 5]

    return sum(useful_function(l[(7 * i + 6) % len(l)]) for _ in range(10))


def main():
    val = compute_val()
    print(f'{val=}')


if __name__ == '__main__':
    main()
