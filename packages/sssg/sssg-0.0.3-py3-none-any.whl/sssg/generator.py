from json import loads 
from argparse import Namespace
from os import path, makedirs

from .schemas import Page



class Generator:
    def __init__(self, args: Namespace):
        self.pages_base_path = args.pages
        self.templates_base_path = args.templates 
        self.output_base_path = args.output
        self.content_base_path = args.content

    def load_pages(self):
        pages_file = open(self.pages_base_path)
        self.pages = [Page(**page_data) for page_data in loads(pages_file.read())]
        pages_file.close()

    def generate_page(self, page: Page):
        template_file_path = path.join(self.templates_base_path, page.template) 
        target_file_path = path.join(self.output_base_path, page.target)
        content_file_paths = page.content

        directory = path.dirname(target_file_path)
        if not path.isdir(directory):
            makedirs(directory)

        template_file = open(template_file_path)
        target_file = open(target_file_path, 'w+')

        template = template_file.read()
        content = {}
        for var_name, var_fp in content_file_paths.items():
            content_file = open(path.join(self.content_base_path, var_fp))
            content[var_name] = content_file.read()
            content_file.close()

        target = template.format(**content)
        target_file.write(target)
        template_file.close()
        target_file.close()

    def generate(self):
        self.load_pages()

        for page in self.pages:
            self.generate_page(page)

