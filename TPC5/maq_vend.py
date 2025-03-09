import ply.lex as lex
import json
import sys
from datetime import datetime

saldo = 0
try:
    with open("stock.json", "r", encoding="utf-8") as f:
        stock = json.load(f)
except FileNotFoundError:
    with open("stock.json", "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4, ensure_ascii=False)

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'ADICIONAR',
    'COIN',
    'COMMA',
    'PERIOD',
    'CODE',
    'STRING',
    'NUMBER'
)

t_LISTAR     = r'LISTAR'
t_MOEDA      = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR       = r'SAIR'
t_ADICIONAR  = r'ADICIONAR'
t_COMMA      = r','
t_PERIOD     = r'\.'

def t_COIN(t):
    r'\d+(e|c)'
    return t

def t_CODE(t):
    r'[A-Z]\d{2}'
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"maq: Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def moeda_para_centimos(valor_moeda):
    if valor_moeda.endswith('e'):
        return int(valor_moeda[:-1]) * 100
    elif valor_moeda.endswith('c'):
        return int(valor_moeda[:-1])
    return 0

def formatar_centimos(centimos):
    euros = centimos // 100
    cents = centimos % 100
    resultado = ""
    if euros > 0:
        resultado += f"{euros}e"
    if cents > 0:
        resultado += f"{cents}c"
    if resultado == "":
        resultado = "0c"
    return resultado

def calcular_troco(centimos):
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    troco = {}
    for moeda in moedas:
        quantidade = centimos // moeda
        if quantidade > 0:
            troco[moeda] = quantidade
            centimos %= moeda
    return troco

def formatar_troco(troco):
    partes = []
    for moeda in sorted(troco.keys(), reverse=True):
        if moeda >= 100:
            valor_str = f"{moeda//100}e"
        else:
            valor_str = f"{moeda}c"
        partes.append(f"{troco[moeda]}x {valor_str}")
    if len(partes) > 1:
        return ", ".join(partes[:-1]) + " e " + partes[-1]
    elif partes:
        return partes[0]
    else:
        return "0c"

def listar_produtos():
    print("maq:")
    print("cod    | nome                        | quantidade  | preço")
    print("----------------------------------------------------------")
    for produto in stock:
        print(f"{produto['cod']:<7}| {produto['nome']:<28}| {produto['quant']:<12}| {produto['preco']}")

def processar_comando(comando):
    global saldo, stock
    lexer.input(comando)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    if not tokens_list:
        return
    token = tokens_list[0]

    if token.type == "LISTAR":
        listar_produtos()
    
    elif token.type == "MOEDA":
        moedas = [tok.value for tok in tokens_list[1:] if tok.type == "COIN"]
        valor_total = sum(moeda_para_centimos(moeda) for moeda in moedas)
        saldo += valor_total
        print(f"maq: Saldo = {formatar_centimos(saldo)}")
    
    elif token.type == "SELECIONAR":
        if len(tokens_list) < 2 or tokens_list[1].type != "CODE":
            print("maq: Comando inválido. Produto não especificado.")
            return
        
        codigo = tokens_list[1].value
        produto = next((item for item in stock if item['cod'] == codigo), None)
        
        if produto is None:
            print("maq: Produto inexistente.")
            print(f"maq: Saldo = {formatar_centimos(saldo)}")
            return
        
        if produto['quant'] <= 0:
            print("maq: Produto esgotado.")
            print(f"maq: Saldo = {formatar_centimos(saldo)}")
            return
        
        preco_centimos = int(round(produto['preco'] * 100))
        
        if saldo < preco_centimos:
            print("maq: Saldo insuficiente para satisfazer o seu pedido")
            print(f"maq: Saldo = {formatar_centimos(saldo)}; Pedido = {formatar_centimos(preco_centimos)}")
            return
        
        produto['quant'] -= 1
        saldo -= preco_centimos
        print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
        print(f"maq: Saldo = {formatar_centimos(saldo)}")

    elif token.type == "ADICIONAR":
        args = [t for t in tokens_list[1:] if t.type != "COMMA" and t.type != "PERIOD"]
        
        if len(args) < 4:
            print('maq: Comando ADICIONAR inválido. Use: ADICIONAR <codigo> , <"nome"> , <quant> , <preco> .')
            return
        
        codigo = args[0].value
        nome = args[1].value
        quantidade = args[2].value
        preco = args[3].value
        
        produto_existente = next((item for item in stock if item['cod'] == codigo), None)
        
        if produto_existente:
            produto_existente['quant'] += quantidade
            print(f'maq: Produto "{nome}" atualizado, nova quantidade: {produto_existente["quant"]}.')
        else:
            stock.append({"cod": codigo, "nome": nome, "quant": quantidade, "preco": preco})
            print(f'maq: Produto "{nome}" adicionado com quantidade {quantidade} e preço {preco}.')
    
    elif token.type == "SAIR":
        if saldo > 0:
            troco = calcular_troco(saldo)
            troco_str = formatar_troco(troco)
            print(f"maq: Pode retirar o troco: {troco_str}.")
        
        print("maq: Até à próxima")
        
        try:
            with open("stock.json", "w", encoding="utf-8") as f:
                json.dump(stock, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"maq: Erro ao guardar o ficheiro JSON: {str(e)}")
        
        sys.exit(0)
    else:
        print("maq: Comando não reconhecido.")

def main():
    global saldo, stock
    data_atual = datetime.today().strftime('%Y-%m-%d')
    print(f"maq: {data_atual}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    while True:
        try:
            comando = input(">> ")
            processar_comando(comando)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nmaq: Operação interrompida pelo utilizador.")
            if saldo > 0:
                troco = calcular_troco(saldo)
                troco_str = formatar_troco(troco)
                print(f"maq: Pode retirar o troco: {troco_str}.")
            print("maq: Até à próxima")
            with open("stock.json", "w", encoding="utf-8") as f:
                json.dump(stock, f, indent=4, ensure_ascii=False)
            sys.exit(0)

if __name__ == "__main__":
    main()