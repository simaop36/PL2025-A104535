#!/usr/bin/env python3
import os
import ply.lex as lex
import sys
import re

# Lista de tokens corrigida e renomeada corretamente
tokens = [
    'COMMENT',
    'SELECT',
    'WHERE',
    'LIMIT',
    'LBRACE',
    'RBRACE',
    'DOT',
    'NUMLIT',
    'STRLIT',
    'VARIABLE',
    'PREDICATE'
]

def t_COMMENT(t):
    r'\#.*'
    return t

def t_SELECT(t):
    r'(?i:SELECT)'
    return t

def t_WHERE(t):
    r'(?i:WHERE)'
    return t

def t_LIMIT(t):
    r'(?i:LIMIT)'
    return t

def t_LBRACE(t):
    r'{'
    return t

def t_RBRACE(t):
    r'}'
    return t

def t_DOT(t):
    r'\.'
    return t

def t_NUMLIT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRLIT(t):
    r'"(?P<LIT>.*?)"(?:@(?P<LANG>\w{2,}))?'
    t.value = re.match(t_STRLIT.__doc__, t.value).groupdict()
    return t

def t_VARIABLE(t):
    r'\?\w+'
    return t

def t_PREDICATE(t):
    r'a|(?:\w|:)+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f'Error :"{t.value[0]}"', file=sys.stderr)
    t.lexer.skip(1)


def processa_texto(conteudo):
    analisador = lex.lex()
    analisador.input(conteudo)
    tokens = []
    
    while True:
        tok = analisador.token()
        if not tok:
            break
        tokens.append(f"Type : {tok.type}, Value : {tok.value}, Line : {tok.lineno}")
    
    return '\n'.join(tokens)

def main():
    if len(sys.argv) != 2:
        print("Use: python3 analisador_lexico.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    base_name = os.path.splitext(input_file)[0]
    output_file = base_name + ".tokens"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{input_file}' não encontrado")
        sys.exit(1)
    
    resultado = processa_texto(conteudo)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(resultado)
    
    print(f"Análise concluída. Tokens salvos em: {output_file}")

if __name__ == "__main__":
    main()