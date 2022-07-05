#!/usr/bin/python3
"""Read text file and prints to stdout"""


def read_file(filename=""):
    with open(filename, mode='r') as file:
        print(file.read())
