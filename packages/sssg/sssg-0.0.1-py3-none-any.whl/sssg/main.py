from argument_parser_builder import ArgumentParserBuilder 
from generator import Generator 


if __name__ == '__main__':
    builder = ArgumentParserBuilder()
    
    builder.add_arguments()
    args = builder.parser.parse_args()

    generator = Generator(args)
    generator.generate()