import argparse
from argparse import ArgumentParser


class Parser(argparse.ArgumentParser):
    def error(self, message: str):
        print('sadasdasd')


parser = argparse.ArgumentParser(usage='blablasdalsbd')

parser.add_argument("param", nargs='*')
parser.add_argument("parama", nargs='*')

args = parser.parse_args()

if args.param is None:
    print('edi kontol')
    parser.print_usage()
else:
    print(args)
