# coding=utf-8
import logging
import ply.lex as lex

tokens = (
        'SECTION',
        'LINE',
        'CR',
)

def t_SECTION(t):
    r'(?m)^\[.*\]'
    return t

def t_LINE(t):
    r'(?m)^.+'
    return t

def t_CR(t):
    r'\n'
    return t

def t_error(t):
    logging.fatal("Illegal character: %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
