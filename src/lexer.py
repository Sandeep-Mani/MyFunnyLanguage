from rply import LexerGenerator, ParserGenerator, Token


class Lexer:
    def __init__(self):
        self.lexer_gen = LexerGenerator()
        self._add_tokens()
        self.lexer = self.lexer_gen.build()

    def _add_tokens(self):
        self.lexer_gen.add('NUMBER', r'\d+')
        self.lexer_gen.add('SUM', r'\+')
        self.lexer_gen.add('SUB', r'-')
        self.lexer_gen.add('MULTIPLY', r'\*')
        self.lexer_gen.add('DIVIDE', r'/')

        self.lexer_gen.add('PRINT', r'print')

        self.lexer_gen.add('IF', r'if')
        self.lexer_gen.add('ELSE', r'else')

        self.lexer_gen.add('OPEN_PAREN', r'\(')
        self.lexer_gen.add('CLOSE_PAREN', r'\)')
        self.lexer_gen.add('LBRACE', r'\{')
        self.lexer_gen.add('RBRACE', r'\}')

        self.lexer_gen.add('FOR', r'for')
        self.lexer_gen.add('SEMICOLON', r';')

        self.lexer_gen.add('EQUAL', r'==')
        self.lexer_gen.add('ASSIGN', r'=')
        self.lexer_gen.add('LT', r'<')
        self.lexer_gen.add('GT', r'>')

        self.lexer_gen.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer_gen.ignore(r'\s+')

    def tokenize(self, code):
        return self.lexer.lex(code)
