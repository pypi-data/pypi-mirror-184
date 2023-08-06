from argparse import ArgumentParser


class ArgumentParserBuilder:
    def __init__(self):
        self.parser = ArgumentParser(description="A Simple Static Site Generator")

    def add_arguments(self):
        self.parser.add_argument('-p', '--pages', default='./pages.json', help='The location of your pages file')
        self.parser.add_argument('-c', '--content', default='./content/', help='The location of your content directory')
        self.parser.add_argument('-o', '--output', default='./static/', help='The location of your output directory')
        self.parser.add_argument('-t', '--templates', default='./templates/', help='The location of your templates directory')