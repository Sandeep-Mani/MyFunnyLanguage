# https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
from lexer import Lexer
def main():
    print("Hello world")
    inputText = """
        print(1 + (1 - 1*2))
    """
    lexer = Lexer().get_lexer()
    for token in lexer.lex(inputText):
        print(token)


if (__name__ == "__main__"):
    main()
