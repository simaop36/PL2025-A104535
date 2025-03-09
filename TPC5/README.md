# Máquina de Vending

Este relatório descreve a implementação de um sistema que simula uma máquina de vending. O programa foi desenvolvido em Python e utiliza um analisador léxico para interpretar os comandos introduzidos pelo utilizador, além de armazenar e gerir o stock de produtos num ficheiro JSON.

## Arquitetura do Sistema

### Componentes Principais

1. **Analisador Léxico**: Implementado através da biblioteca `ply.lex`, responsável por decompor os comandos introduzidos pelo utilizador em tokens que o sistema consegue interpretar.

2. **Gestão de Stock**: Os produtos disponíveis são armazenados num ficheiro `stock.json`, o qual é carregado no início da execução do programa e atualizado quando termina.

3. **Gestão de Saldo**: O sistema mantém um registo do saldo atual do utilizador, que pode ser incrementado através da introdução de moedas.

4. **Processador de Comandos**: Interpreta os tokens gerados pelo analisador léxico e executa as ações correspondentes.

## Funcionalidades

### Comandos Disponíveis

O sistema reconhece os seguintes comandos:

- **LISTAR**: Apresenta a lista de produtos disponíveis na máquina, incluindo código, nome, quantidade e preço.
  
- **MOEDA [valor]**: Permite introduzir moedas para aumentar o saldo. O valor pode ser especificado em euros (e) ou cêntimos (c), por exemplo, `MOEDA 1e 50c`.
  
- **SELECIONAR [código]**: Seleciona um produto para compra através do seu código. O sistema verifica se o produto existe, se há stock disponível e se o saldo é suficiente.
  
- **ADICIONAR [código], ["nome"], [quantidade], [preço]**: Adiciona um novo produto ao stock ou atualiza a quantidade de um produto existente.
  
- **SAIR**: Termina a sessão, devolve o troco (se existir) e guarda o estado atual do stock.

### Gestão de Moeda

- O sistema considera a quantidade introduzida pelo utilizador como o valor total das moedas introduzidas e não como moedas individuais.
- É feito o calculo do saldo para as operações `MOEDA` e `SELECIONAR`. Neste último se o saldo for inferior ao valor do produto, não é possivel comprar esse produto, o que evita situações de saldo negativo.

### Gestão de Stock

O stock é guardado num ficheiro JSON com a seguinte estrutura para cada produto:

```json
{
    "cod": "A01",               // Código do produto
    "nome": "Coca-Cola 330ml",  // Nome do produto
    "quant": 8,                 // Quantidade disponível
    "preco": 1.2                // Preço em euros
}
```

### Tokens do Analisador Léxico

O analisador léxico reconhece diversos tipos de tokens:

- Comandos: `LISTAR`, `MOEDA`, `SELECIONAR`, `SAIR`, `ADICIONAR`
- Valores: `COIN` (moedas), `CODE` (códigos de produto), `STRING` (nomes), `NUMBER` (quantidades e preços)
- Separadores: `COMMA` (vírgula), `PERIOD` (ponto)

## Gestão de Erros

O sistema inclui tratamento de erros para diversas situações:

- Carateres inválidos nos comandos
- Comandos não reconhecidos
- Produtos inexistentes ou esgotados
- Saldo insuficiente para comprar um produto
- Formato incorreto para o comando `ADICIONAR`
