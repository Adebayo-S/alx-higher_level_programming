#!/usr/bin/python3
def safe_print_integer(value):
    is_int = True
    try:
        value / 3
    except (ValueError, TypeError):
        print(end='')
        is_int = False
    else:
        print("{:d}".format(value))
    return is_int
