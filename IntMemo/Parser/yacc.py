# coding=utf-8
import logging

import ply.yacc as yacc
from Parser.lex import tokens

def p_memo(p):
    ''' memo : memo section
             | section
    '''
    if len(p) == 2 and p[1]:
        if not p[0]:
            p[0] = [p[1]]
        else:
            p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = []
        if p[2]:
            p[0].append(p[2])

def p_section(p):
    ''' section : SECTION content'''
    p[0] = {
        'section': p[1],
        'content': p[2],
    }

def p_line(p):
    ''' line : CR
             | LINE
    '''
    p[0] = p[1]

def p_content(p):
    ''' content : content line
                | line
    '''
    if len(p) == 2 and p[1]:
        if not p[0]:
            p[0] = [p[1]]
        else:
            p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = []
        if p[2]:
            p[0].append(p[2])


def p_error(p):
    logging.fatal("Syntax Error in input: %s" % p)

parser = yacc.yacc()
