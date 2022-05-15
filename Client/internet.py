import requests
import argparse
from lxml import etree
from io import StringIO


def create_main_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8000, type=int)

    return parser


def CheckedInput(validate, text):
    while True:
        x = input(text)
        if validate(x):
            return x


def comment(address):
    def CommentValidate(x):
        return x != ""

    def markValidate(x):
        try:
            x = int(x)
            return 0 <= x <= 10
        except ValueError:
            return False

    requests.post(address + 'create-comment', data={
        'name': input('Teacher Full Name: '),
        'comment': CheckedInput(CommentValidate, 'Comment: '),
        'mark': int(CheckedInput(markValidate, 'Mark(number from 0 to 10): '))
    })


def get_characters(address):
    req = requests.post(address + 'account', data=dict(
        name=input('Teacher Full Name: ')
    )).text
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(req), parser)
    print("\n".join([h4.text for h4 in tree.xpath("/html/body/h4")]))


def graceful_exit():
    ack = input('Are you sure you want to leave (Y/N)?')
    if ack[0].lower() == 'y':
        print('Goodbye!')
        exit()
    elif ack[0].lower() == 'n':
        print("OK, let's continue")
    else:
        print('Stupid input, but continue')

