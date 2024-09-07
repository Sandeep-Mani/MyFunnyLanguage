# https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
from lexer import Lexer
from pathlib import Path


def main():
    print("Hello world")
    inputText = Path('src/testProgram.mfl').read_text();
    lexer = Lexer().get_lexer()
    for token in lexer.lex(inputText):
        print(token)


if (__name__ == "__main__"):
    main()
