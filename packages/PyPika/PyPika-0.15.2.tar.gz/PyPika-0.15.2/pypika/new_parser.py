from sly import (
    Lexer,
    Parser,
)


def pattern(pattern, *extra):
    patterns = [pattern, *extra]

    def decorate(func):
        pattern = '|'.join(f'({pat})' for pat in patterns)
        if hasattr(func, 'pattern'):
            func.pattern = pattern + '|' + func.pattern
        else:
            func.pattern = pattern
        return func

    return decorate


def rule(rule, *extra):
    rules = [rule, *extra]

    def decorate(func):
        func.rules = [*getattr(func, 'rules', []), *rules[::-1]]
        return func

    return decorate


class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {NUMBER, ID, WHILE, IF, ELSE, PRINT,
              PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
              EQ, LT, LE, GT, GE, NE}

    literals = {'(', ')', '{', '}', ';'}

    # String containing ignored characters
    ignore = ' \t'

    # Regular expression rules for tokens
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    EQ = r'=='
    ASSIGN = r'='
    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'
    NE = r'!='

    @pattern(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['print'] = PRINT

    ignore_comment = r'\#.*'

    # Line number tracking
    @pattern(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens

    # Grammar rules and actions
    @rule('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @rule('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @rule('term')
    def expr(self, p):
        return p.term

    @rule('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @rule('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @rule('factor')
    def term(self, p):
        return p.factor

    @rule('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @rule('"(" expr ")"')
    def factor(self, p):
        return p.expr


if __name__ == '__main__':
    data = '3 + 42 * (3 - 9)'

    lexer = CalcLexer()
    parser = CalcParser()

    result = parser.parse(lexer.tokenize(data))
    print(result)
