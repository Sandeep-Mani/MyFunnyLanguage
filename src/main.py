# https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
from lexer import Lexer
from parser import Parser
from pathlib import Path

def main():
    text_input = Path("src/testProgram.mfl").read_text()
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()

if (__name__ == "__main__"):
    main()
