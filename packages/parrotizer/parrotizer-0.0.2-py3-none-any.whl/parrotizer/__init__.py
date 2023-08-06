from argparse import ArgumentParser
from string import ascii_letters
import sys

import pyperclip

LETTER_TEMPLATE = ':parrot-{}:'
SEPARATOR = '  '


def parrotize_letter(letter):
    if letter == ' ':
        return SEPARATOR * 2
    if letter not in ascii_letters:
        return SEPARATOR
    return LETTER_TEMPLATE.format(letter.lower())


def parrotize_string(string):
    return ''.join(map(parrotize_letter, string))


def get_args():
    parser = ArgumentParser("Parrotizer")
    parser.add_argument(
        'phrase',
        help="the words/phrase to parrotize. Defaults to clipboard contents.",
        default=pyperclip.paste()
    )
    parser.add_argument(
        '-c', '--clipboard',
        action='store_true',
        help='Place parrotized text on the clipboard.'
    )
    args = parser.parse_args()
    return args


def cli_print():
    args = get_args()
    string = parrotize_string(args.phrase)
    if args.clipboard:
        pyperclip.copy(string)
    print(string)


if __name__ == '__main__':
    cli_print()
