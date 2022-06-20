#!/usr/bin/python3
import re


def safe_print_integer(value):
    is_int = True
    try:
        int(value)
    except ValueError:
        print(end='')
        is_int = False
    else:
        print("{:d}".format(value))
    finally:
        return is_int
