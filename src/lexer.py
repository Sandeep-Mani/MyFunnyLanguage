from rply import LexerGenerator

class Lexer:
    def __init__(self) -> None:
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Paranthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'-')
        self.lexer.add('MULTIPLY', r'\*')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore space
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
