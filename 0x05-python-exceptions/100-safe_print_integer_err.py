#!/usr/bin/python3
def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        is_int = False
        print(f"Exception: {err}")
    return is_int
