from argparse import ArgumentParser


class ArgumentParserBuilder:
    def __init__(self):
        self.parser = ArgumentParser()

    def add_arguments(self):
        self.parser.add_argument('-p', '--pages', default='./pages.json')
        self.parser.add_argument('-c', '--content', default='./content/')
        self.parser.add_argument('-o', '--output', default='./static/')
        self.parser.add_argument('-t', '--templates', default='./templates/')