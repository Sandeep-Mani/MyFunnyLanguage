from rply import ParserGenerator
from mfl_ast import Divide, Multiply, Number, Sum, Sub, Print

class Parser():
    def __init__(self) -> None:
        # A list of all token names accepted by the parser.
        self.pg = ParserGenerator(
            [
                'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
                'SEMI_COLON', 'SUM', 'SUB', 'NUMBER', 'MULTIPLY',
                'DIVIDE'
            ]
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULTIPLY expression')
        @self.pg.production('expression : expression DIVIDE expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)

            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

            elif operator.gettokentype() == 'MULTIPLY':
                return Multiply(left, right)
             
            elif operator.gettokentype() == 'DIVIDE':
                return Divide(left, right)

        
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)


    def get_parser(self):
        return self.pg.build()
