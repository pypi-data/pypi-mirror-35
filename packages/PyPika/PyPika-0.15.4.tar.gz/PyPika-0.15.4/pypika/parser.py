from sly import (
    Lexer,
    Parser,
    lex,
)

from pypika import (
    Query,
    Table,
    terms,
)


def token(pattern, *extra):
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


def case_insenstive_regex(word):
    return ''.join('[{upper}{lower}]'.format(upper=letter.upper(),
                                             lower=letter.lower())
                   if letter != ' ' else
                   ' '
                   for letter in word)


class SQLLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {SELECT, CREATE, UPDATE, DELETE,
              FROM, GROUP_BY, LIMIT, HAVING,
              DISTINCT, ALL, AS,
              PLUS, MINUS, TIMES, DIVIDE,
              INT, DECIMAL, STRING, NULL, TRUE, FALSE,
              NAME,
              NOT_EQUALS, GTE, LTE, GT, LT, EQUALS
              }

    # String containing ignored characters between tokens

    ignore = ' \t'
    ignore_newline = r'\n+'

    literals = set(r'(){}.,;\'"')

    # reserved words
    SELECT = case_insenstive_regex(r'select')
    CREATE = case_insenstive_regex(r'create')
    UPDATE = case_insenstive_regex(r'update')
    DELETE = case_insenstive_regex(r'delete')

    DISTINCT = case_insenstive_regex(r'distinct')
    ALL = case_insenstive_regex(r'all')
    FROM = case_insenstive_regex(r'from')
    GROUP_BY = case_insenstive_regex(r'group by')
    HAVING = case_insenstive_regex(r'having')
    LIMIT = case_insenstive_regex(r'limit')

    AS = case_insenstive_regex(r'as')

    NULL = case_insenstive_regex(r'null')
    TRUE = case_insenstive_regex(r'true')
    FALSE = case_insenstive_regex(r'false')

    PLUS = r'\+'
    MINUS = r'\-'
    TIMES = r'\*'
    DIVIDE = r'\/'

    NOT_EQUALS = r'!='
    GTE = r'=>'
    LTE = r'=<'
    GT = r'>'
    LT = r'<'
    EQUALS = r'='

    NAME = '[a-zA-Z_][a-zA-Z0-9_]*'

    @token(r'-?\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t

    @token(r'-?(\d*\.\d+|\d+\.\d*)')
    def DECIMAL(self, t):
        t.value = float(t.value)
        return t

    @token(r'\'[^\'\n]+\'')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t


class PypikaExpressionParser(Parser):
    tokens = SQLLexer.tokens

    # def __init__(self, tables):
    #     self.tables = tables

    """
    QUERIES
    """

    @rule(r'SELECT select_expressions FROM table_expressions ";"',
          r'SELECT DISTINCT select_expressions FROM table_expressions ";"')
    def select_query(self, p):
        query = Query \
            .from_(*p.table_expressions) \
            .select(*p.select_expressions)

        if 'DISTINCT' in p._namemap:
            query = query.distinct()

        return query

    """
    REPETITIONS
    """

    @rule(r'select_expressions "," select_expression',
          r'select_expression')
    def select_expressions(self, p):
        if 'select_expressions' in p._namemap:
            return p.select_expressions + [p.select_expression]
        return [p.select_expression]

    @rule(r'table_expressions "," table_expression',
          r'table_expression')
    def table_expressions(self, p):
        if 'table_expressions' in p._namemap:
            return p.table_expressions + [p.table_expression]
        return [p.table_expression]

    """
    EXPRESSIONS
    """

    @rule(r'term AS alias_expression')
    def select_expression(self, p):
        return p.term

    @rule(r'term')
    def select_expression(self, p):
        return p.term

    @rule(r'family_name "." TIMES')
    def select_expression(self, p):
        return terms.Star()

    @rule(r'TIMES')
    def select_expression(self, p):
        return terms.Star()

    @rule(r'schema_name "." table_name AS alias_expression')
    def table_expression(self, p):
        return Table(p.table_name, schema=p.schema_name).as_(p.alias_expression)

    @rule(r'schema_name "." table_name')
    def table_expression(self, p):
        return Table(p.table_name, schema=p.schema_name)

    @rule(r'table_name AS alias_expression')
    def table_expression(self, p):
        return Table(p.table_name).as_(p.alias_expression)

    @rule(r'table_name')
    def table_expression(self, p):
        return Table(p.table_name)

    """
    TERMS
    """

    @rule(r'value')
    def term(self, p):
        return p.value

    @rule(r'string')
    def value(self, p):
        return p[0]

    @rule(r'numeric')
    def value(self, p):
        return p[0]

    @rule(r'boolean')
    def value(self, p):
        return p[0]

    @rule(r'null')
    def value(self, p):
        return p[0]

    """
    DATA TYPES
    """

    @rule(r'TRUE')
    def boolean(self, p):
        return True

    @rule(r'FALSE')
    def boolean(self, p):
        return False

    @rule(r'INT')
    def numeric(self, p):
        return p[0]

    @rule(r'DECIMAL')
    def numeric(self, p):
        return p[0]

    @rule(r'NULL')
    def null(self, p):
        return None

    @rule(r'STRING')
    def string(self, p):
        return p[0]

    """
    NAMES AND ALIASES
    """

    @rule(r'name_expression')
    def alias_expression(self, p):
        return p.name_expression

    @rule(r'name_expression')
    def family_name(self, p):
        return p.name_expression

    @rule(r'name_expression')
    def schema_name(self, p):
        return p.name_expression

    @rule(r'name_expression')
    def table_name(self, p):
        return p.name_expression

    @rule(r'NAME',
          r'""" NAME """')
    def name_expression(self, p):
        return p.NAME


if __name__ == '__main__':
    queries = [
        "Sum(v_hotelads_summary.clicks)",
        "100 * Sum(v_hotelads_summary.revenue)/Sum(v_hotelads_summary.cost)",
        "Sum(v_hotelads_summary.cost) / Sum(v_hotelads_summary.clicks)",
        "Sum(v_dashboard_sem_overall.revenue) / SumFloat(v_dashboard_sem_overall.clicks)",
        "Coalesce(Sum(v_programmatic_summary.ad_clicks)/SumFloat(v_programmatic_summary.impressions), 0)",
        "Count(hpa_health_price_accuracy.accurate)",
        "Count(1)",
        "Max(import_stats_p.import_dt)",
        "Min(DateDiff('day', import_stats_p.import_dt, Now()))",

        "case "
        "when Sum(email_aggregate_v.sends) = 0 then 0 "
        "else (Sum(email_aggregate_v.unique_opens) / Sum(email_aggregate_v.sends)) * 100)",
    ]

    lexer = SQLLexer()
    parser = PypikaExpressionParser()
    for query in queries:
        try:
            print(query)
            tokens = lexer.tokenize(query)
            print(list(tokens))
            pypika_query = parser.parse(tokens)
            print(pypika_query)

            print('\n\n\n')
        except (lex.LexError, lex.LexerBuildError) as e:
            print(e)
