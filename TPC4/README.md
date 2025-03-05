# Analisador Léxico

Este projeto implementa um analisador léxico para queries semelhante ao SPARQL em Python, com recurso à biblioteca PLY (Python Lex-Yacc). O analisador identifica componentes léxicos (tokens) em queries e gera um relatório com os tokens encontrados.

## Funcionalidades Principais
- Reconhece elementos básicos de queries
- Gera um arquivo com a lista de tokens identificados
- Reconhece erros léxicos básico

## Tokens Reconhecidos
| Token        | Descrição                                     | Exemplo                     |
|--------------|-----------------------------------------------|-----------------------------|
| `SELECT`     | Palavra reservada para seleção                | `SELECT`                    |
| `WHERE`      | Palavra reservada para condição               | `WHERE`                     |
| `LIMIT`      | Palavra reservada para limite de resultados   | `LIMIT`                     |
| `LBRACE`     | Delimitador de abertura                       | `{`                         |
| `RBRACE`     | Delimitador de fechamento                     | `}`                         |
| `DOT`        | Ponto final                                   | `.`                         |
| `NUMLIT`     | Literal numérico                              | `1000`                      |
| `STRLIT`     | Literal de string com idioma opcional         | `"Chuck Berry"@en`          |
| `VARIABLE`   | Variável (começa com ?)                       | `?nome`                     |
| `PREDICATE`  | Predicado (propriedade)                       | `dbo:MusicalArtist`         |
| `COMMENT`    | Comentário (inicia com #)                     | `# DBPedia: obras`          |

## Como Utilizar
1. **Execução**
   ```bash
   python3 analisador_lexico.py arquivo_entrada.txt
   ```

2. **Saída**
   - Será gerado um arquivo `.tokens` com o mesmo nome do arquivo de entrada
   - Formato da saída:
     ```
     Type: TOKEN_TYPE, Value: TOKEN_VALUE, Line: LINE_NUMBER
     ```

## Exemplo de Uso
**Entrada (`test.txt`)**:
```sparql
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

**Saída (`exemplo.tokens`)**:
```
Tipo: COMMENT, Valor: # DBPedia: obras de Chuck Berry, Linha: 2
Tipo: SELECT, Valor: select, Linha: 5
Tipo: VARIABLE, Valor: ?nome, Linha: 5
...
Tipo: LIMIT, Valor: LIMIT, Linha: 11
Tipo: NUMLIT, Valor: 1000, Linha: 11
```

## Tratamento de Erros
- Caracteres não reconhecidos são reportados com número da linha
- O analisador continua a execução após erros
- Mensagens de erro são enviadas para a saída padrão de erro (stderr)


