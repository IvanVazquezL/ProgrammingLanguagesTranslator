import ply.lex as lex
import ply.yacc as yacc
import sys
import logging


def parserFile():
    # TOKENS
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE_KEYWORD',
        'console.log': 'CONSOLE_KEYWORD',
        'for': 'FOR_KEYWORD',
        'return': 'RETURN',
        'alert': 'ALERT',
        'function': 'FUNCTION',
    }

    tokens = [
        'POINT',
        'PLUS',
        'MINS',
        'OPEN_BRACKET',
        'CLOSE_BRACKET',
        'OPEN_PARENTHESIS',
        'CLOSE_PARENTHESIS',
        'OPEN_SQUARE_BRACKET',
        'CLOSE_SQUARE_BRACKET',
        'COMMA',
        'TIMES',
        'DIVIDE',
        'SEMICOLON',
        'EQUAL',
        'QUOTE',
        'RELOP',
        'ID',
        'CTE_STRING',
        'CTE_FLOAT',
        'CTE_INTEGER',
        'CTE_CHAR',
        'BOOLEAN',
        'CONCATENATE'
    ] + list(reserved.values())

    t_POINT = r'\.'
    t_OPEN_BRACKET = r'\{'
    t_CLOSE_BRACKET = r'\}'
    t_OPEN_PARENTHESIS = r'\('
    t_CLOSE_PARENTHESIS = r'\)'
    t_OPEN_SQUARE_BRACKET = r'\['
    t_CLOSE_SQUARE_BRACKET = r'\]'
    t_COMMA = r'\,'
    t_DIVIDE = r'\/'
    t_SEMICOLON = r'\;'
    t_PLUS = r'\+'
    t_MINS = r'\-'
    t_TIMES = r'\*'
    t_QUOTE = r'\''
    t_EQUAL = r'\='
    t_CONCATENATE = r'\&'

    t_ignore = " \t"
    t_CTE_CHAR = r'\'.*\''
    t_RELOP = r'>=|<=|==|<|>'

    def t_newline(t):
        r'\n+'

    def t_CTE_STRING(t):
        r'\"(\\.|[^"\\])*\"'
        return t

    def t_CTE_FLOAT(t):
        r'-?\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_CTE_INTEGER(t):
        r'-?\d+'
        t.value = int(t.value)
        return t

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if t.value in reserved:
            t.type = reserved[t.value]
        else:
            if t.type == 'ID':
                v.Id = t.value
        return t

    def t_error(t):
        print("ERROR at '%s'" % t.value)
        t.lexer.skip(1)

    # BUILD THE LEXER
    lexer = lex.lex()

    def p_START(t):
        '''
            START : START_MODULE CALL
        '''

    def p_START_MODULE(t):
        '''
            START_MODULE : MODULE START_MODULE
                        |   EMPTY
        '''

    def p_MODULE(t):
        '''
            MODULE : FUNCTION ID OPEN_PARENTHESIS MODULE_ARGUMENTS
        '''

    def p_MODULE_ARGUMENTS(t):
        '''
            MODULE_ARGUMENTS : ID MODULE_COMMA MODULE_BODY
        '''

    def p_MODULE_COMMA(t):
        '''
            MODULE_COMMA : COMMA MODULE_ARGUMENTS
                        | EMPTY
        '''

    def p_MODULE_BODY(t):
        '''
            MODULE_BODY : CLOSE_PARENTHESIS OPEN_BRACKET BLOCK CLOSE_PARENTHESIS
        '''

    def p_BLOCK(t):
        '''
            BLOCK : STATEMENT BLOCK
                | EMPTY
        '''

    def p_STATEMENT(t):
        '''
            STATEMENT : RETURN_CHECK
        '''
    def p_RETURN_CHECK(t):
        '''
            RETURN_CHECK : RETURN EXPRESIONS SEMICOLON
        '''


    def p_empty(t):
        '''
            EMPTY :
        '''
    log = logging.getLogger()

    parser = yacc.yacc()

    while True:
        try:
            s=input('')
        except EOFError:
            break
        parser.parse(s)
