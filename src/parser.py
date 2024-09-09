from rply import ParserGenerator

from AstNodes import BinOpNode, IfElseNode, ForNode, NumberNode, BlockNode, VariableNode, PrintNode, AssignNode, \
    EqualNode, LessThanNode, GreaterThanNode


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'SUM', 'SUB', 'MULTIPLY', 'DIVIDE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'IF', 'ELSE', 'LBRACE', 'RBRACE', 'FOR', 'SEMICOLON', 'EQUAL', 'ASSIGN', 'LT', 'GT', 'ID', 'PRINT']
        )
        self._build_parser()

    def _build_parser(self):
        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return NumberNode(p[0].getstr())

        @self.pg.production('expression : ID')
        def expression_variable(p):
            return VariableNode(p[0].getstr())

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_parens(p):
            return p[1]

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULTIPLY expression')
        @self.pg.production('expression : expression DIVIDE expression')
        def expression_binop(p):
            left = p[0]
            operator = p[1].getstr()
            right = p[2]
            return BinOpNode(left, operator, right)

        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def print_statement(p):
            return PrintNode(p[2])

        @self.pg.production('expression : ID ASSIGN expression')
        def assignment(p):
            return AssignNode(p[0].getstr(), p[2])

        @self.pg.production('statement : expression')
        def expression_statement(p):
            return p[0]

        @self.pg.production('statement : IF OPEN_PAREN expression CLOSE_PAREN block ELSE block')
        @self.pg.production('statement : IF OPEN_PAREN expression CLOSE_PAREN block')
        def if_else(p):
            condition = p[2]
            if_block = p[4]
            if len(p) == 7:
                else_block = p[6]
                return IfElseNode(condition, if_block, else_block)
            return IfElseNode(condition, if_block)

        @self.pg.production('block : LBRACE statement RBRACE')
        def block(p):
            return BlockNode([p[1]])

        @self.pg.production('statement : FOR OPEN_PAREN expression SEMICOLON expression SEMICOLON expression CLOSE_PAREN block')
        def for_loop(p):
            init = p[2]
            condition = p[4]
            increment = p[6]
            block = p[8]
            return ForNode(init, condition, increment, block)

        @self.pg.production('expression : expression EQUAL expression')
        def expression_equal(p):
            left = p[0]
            right = p[2]
            return EqualNode(left, right)

        @self.pg.production('expression : expression LT expression')
        def expression_lt(p):
            left = p[0]
            right = p[2]
            return LessThanNode(left, right)

        @self.pg.production('expression : expression GT expression')
        def expression_gt(p):
            left = p[0]
            right = p[2]
            return GreaterThanNode(left, right)

        self.pg.build()

    def parse(self, tokens):
        return self.pg.build().parse(tokens)
