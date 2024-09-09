from rply.token import BaseBox


class NumberNode(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinOpNode(BaseBox):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        if self.operator == '+':
            return self.left.eval() + self.right.eval()
        elif self.operator == '-':
            return self.left.eval() - self.right.eval()
        elif self.operator == '*':
            return self.left.eval() * self.right.eval()
        elif self.operator == '/':
            return self.left.eval() // self.right.eval()


class PrintNode(BaseBox):
    def __init__(self, expression):
        self.expression = expression

    def eval(self):
        result = self.expression.eval()
        print(result)
        return result


class IfElseNode(BaseBox):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def eval(self):
        if self.condition.eval():
            return self.if_block.eval()
        elif self.else_block:
            return self.else_block.eval()


class BlockNode(BaseBox):
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        result = None
        for statement in self.statements:
            result = statement.eval()
        return result


class ForNode(BaseBox):
    def __init__(self, init, condition, increment, block):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.block = block

    def eval(self):
        self.init.eval()
        while self.condition.eval():
            self.block.eval()
            self.increment.eval()


variables = {}


class VariableNode(BaseBox):
    def __init__(self, name):
        self.name = name

    def eval(self):
        return variables[self.name]


class AssignNode(BaseBox):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def eval(self):
        variables[self.name] = self.expression.eval()
        return variables[self.name]


class EqualNode(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        # Evaluate both left and right expressions
        left_value = self.left.eval()
        right_value = self.right.eval()

        # Return the result of equality check
        return left_value == right_value


class LessThanNode(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        # Evaluate both left and right expressions
        left_value = self.left.eval()
        right_value = self.right.eval()

        # Return the result of the less-than check
        return left_value < right_value


class GreaterThanNode(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        # Evaluate both left and right expressions
        left_value = self.left.eval()
        right_value = self.right.eval()

        # Return the result of the less-than check
        return left_value > right_value
