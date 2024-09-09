from lexer import Lexer
from parser import Parser


def main():
    lexer = Lexer()
    parser = Parser()

    code = """
    for (i = 0; i < 5; i = i + 1) {
        print(i);
        if (i == 3) {
            x = i + 10;
            print(x);
        }
    }
    """

    tokens = lexer.tokenize(code)
    print(list(tokens))
    parsed_program = parser.parse(tokens)
    parsed_program.eval()


if __name__ == "__main__":
    main()
