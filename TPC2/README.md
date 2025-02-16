# README.md

## Processamento de Ficheiro CSV em Python sem utilizar o módulo `csv`

Este projeto implementa um script Python que processa um ficheiro CSV com informações sobre obras musicais, sem utilizar o módulo `csv`. O objetivo é extrair e organizar os dados para gerar três resultados principais:

1. **Uma lista ordenada alfabeticamente dos compositores musicais.**
2. **A distribuição das obras por período.**
3. **Um dicionário que associa cada período a uma lista alfabética dos títulos das obras desse período.**

O código lida com campos separados por ponto e vírgula (`;`), mesmo quando esses campos contêm aspas e caracteres especiais. A seguir, descrevemos o funcionamento do código.

---

## Estrutura do Ficheiro CSV

O ficheiro CSV tem as colunas organizadas da seguinte forma:

1. **Nome da obra**
2. **Descrição da obra**
3. **Ano de criação**
4. **Período**
5. **Compositor**
6. **Duração**
7. **ID**

Exemplo de linha válida:

```csv
Rage Over a Lost Penny;"The ""Rondo alla ingharese quasi un capriccio""...";1745;Barroco;Krebs, Johann Ludwig;01:00:26;O2
```

---

## Explicação do Código

### 1. Função `parse_line`

A função `parse_line` é responsável por dividir uma linha do CSV em campos, ignorando os delimitadores (`;`) que aparecem dentro de aspas.

#### **Expressão Regular Utilizada**

```python
fields = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
```

**Como funciona a expressão:**

- `;` - O ponto e vírgula é o delimitador principal.
- `(?=...)` - Utilizamos uma "positive lookahead" para garantir que o ponto e vírgula seja seguido de um número par de aspas.
- `(?:[^"]*"[^"]*")*` - Esta parte corresponde a pares de aspas, garantindo que não dividimos campos que contêm ponto e vírgula dentro de aspas.
- `[^"]*$` - Garante que o ponto e vírgula a ser dividido não está dentro de um par de aspas.

Assim, mesmo linhas como a seguir são processadas corretamente:

```csv
"Sinfonia nº 5";"Descrição com ponto e vírgula; dentro";"1804";"Clássico";"Beethoven";"00:30:00";"123"
```

Após a separação, a função remove os espaços em branco e as aspas com o comando:

```python
fields = [field.strip().strip('"') for field in fields]
```

---

### 2. Leitura e Processamento do Ficheiro

O ficheiro é lido linha por linha. Caso uma linha esteja incompleta (menos de 7 campos), o código acumula a linha no buffer até que a linha completa seja obtida.

```python
buffer += line
if buffer.count(';') >= 6:
    fields = parse_line(buffer)
```

Essa abordagem permite o tratamento correto de campos multilineares.

---

### 3. Organização e Apresentação dos Dados

Após o processamento das linhas, os dados são organizados em três estruturas:

- `composers` (conjunto) - para armazenar os compositores de forma única.
- `period_distribution` (dicionário) - para contar o número de obras por período.
- `period_titles` (dicionário) - para armazenar, em listas ordenadas, os títulos das obras de cada período.

#### **Exibição dos Resultados**

1. **Lista de compositores (ordem alfabética)**

```python
sorted_composers = sorted(composers)
for compositor in sorted_composers:
    print(compositor)
```

2. **Distribuição das obras por período**

```python
sorted_periods = sorted(period_distribution.keys())
for período in sorted_periods:
    print(f"{período}: {period_distribution[período]}")
```

3. **Dicionário de períodos com os títulos das obras (ordenados)**

```python
for período in sorted_periods:
    print(f"{período}: {period_titles[período]}")
```

---

## Tratamento de Erros

Caso ocorra algum erro durante a leitura ou o processamento do ficheiro, o programa exibe uma mensagem de erro e finaliza a execução com um código de saída 1:

```python
except Exception as e:
    print(f"Erro ao processar o ficheiro: {e}")
    sys.exit(1)
```

---

