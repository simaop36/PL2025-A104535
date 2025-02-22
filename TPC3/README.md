# Conversor de Markdown para HTML

Este script em Python permite converter ficheiros de Markdown (`.md`) para ficheiros HTML, o que permite a criação de páginas web a partir de textos com formatação simples. Além das funcionalidades básicas de transformação de cabeçalhos, listas numeradas e parágrafos, o script processa também formatações inline como Links, imagens, negrito e itálico. Utiliza expressões regulares para identificar e substituir estes padrões.

## Funcionalidades

- **Cabeçalhos:**  
  Converte as linhas que começam com 1 a 3 símbolos `#` em elementos HTML `<h1>`, `<h2>` ou `<h3>`, conforme o número de símbolos.

- **Listas Numeradas:**  
  Agrupa as linhas iniciadas por um número seguido de ponto e espaço (ex.: `1. Item`) e converte-as numa lista ordenada (`<ol>`), envolvendo cada item com `<li>`.

- **Parágrafos:**  
  Linhas de texto sem formatação específica são envolvidas com `<p>`.

- **Formatação Inline:**  
  A função `process_inline` utiliza regex para converter:
  - **Imagens:** Em `<img src="url" alt="texto alternativo"/>`.
  - **Links:** Em `<a href="url">texto</a>`.
  - **Negrito:** Em `<b>texto</b>`.
  - **Itálico:** Em `<i>texto</i>`.

## Explicação Detalhada das Expressões Regulares

Abaixo encontra-se uma explicação pormenorizada de cada expressão regular utilizada no script:

### 1. Cabeçalhos

Regex: `r'^(#{1,3})\s+(.*)'`

- **^**  
  Indica o início da linha.

- **(#{1,3})**  
  Um grupo de captura que procura entre 1 e 3 ocorrências do símbolo `#`. O número de `#` determina o nível do cabeçalho (ex.: 1 para `<h1>`, 2 para `<h2>`, etc.).

- **\s+**  
  Corresponde a um ou mais espaços. Este espaço separa os símbolos `#` do texto do cabeçalho.

- **(.*)**  
  Um grupo de captura que obtém o restante da linha, ou seja, o conteúdo do cabeçalho.

*Exemplo:*  
Uma linha como `## Título` é processada de forma a gerar `<h2>Título</h2>`.

### 2. Listas Numeradas

Regex: `r'^\d+\.\s+(.*)'`

- **^**  
  Indica o início da linha.

- **\d+**  
  Corresponde a um ou mais dígitos, que representam o número do item da lista.

- **\.**  
  Corresponde a um ponto literal, que deve seguir o número.

- **\s+**  
  Corresponde a um ou mais espaços após o ponto.

- **(.*)**  
  Captura o restante da linha, que é o conteúdo do item da lista.

*Exemplo:*  
Uma linha como `1. Primeiro item` será convertida num item de lista, que posteriormente é envolvido por `<ol>` e `<li>`.

### 3. Imagens

Regex: `r'!\[(.*?)\]\((.*?)\)'`

- **!\[**  
  Corresponde à sequência literal `![`, que indica o início da sintaxe para imagens.

- **(.*?)**  
  Um grupo de captura Lazy que obtém o texto alternativo (alt) da imagem.

- **\]**  
  Corresponde ao carácter `]` que fecha o texto alternativo.

- **\(**  
  Corresponde ao carácter `(` que inicia a especificação do URL da imagem.

- **(.*?)**  
  Outro grupo de captura Lazy que obtém o URL da imagem.

- **\)**  
  Corresponde ao carácter `)` que fecha o URL.

*Exemplo:*  
A String `![Descrição](imagem.jpg)` é convertida em `<img src="imagem.jpg" alt="Descrição"/>`.

### 4. Links

Regex: `r'\[(.*?)\]\((.*?)\)'`

- **\[**  
  Inicia a correspondência do texto da Links.

- **(.*?)**  
  Grupo de captura Lazy que obtém o texto da Links.

- **\]**  
  Fecha o texto da Links.

- **\(**  
  Inicia a correspondência do URL da Links.

- **(.*?)**  
  Grupo de captura Lazy que obtém o URL.

- **\)**  
  Fecha o URL.

*Exemplo:*  
A String `[Google](https://www.google.com)` é convertida em `<a href="https://www.google.com">Google</a>`.

### 5. Negrito

Regex: `r'\*\*(.*?)\*\*'`

- **\*\***  
  Corresponde a dois asteriscos que marcam o início do texto a ser colocado em negrito.

- **(.*?)**  
  Grupo de captura Lazy que obtém o texto a ser formatado em negrito.

- **\*\***  
  Corresponde a dois asteriscos que marcam o fim do texto.

*Exemplo:*  
A String `**texto em negrito**` é convertido em `<b>texto em negrito</b>`.

### 6. Itálico

Regex: `r'\*(.*?)\*'`

- **\***  
  Corresponde a um asterisco que marca o início do texto a ser formatado em itálico.

- **(.*?)**  
  Grupo de captura Lazy que obtém o texto a converter.

- **\***  
  Corresponde ao asterisco que marca o fim do texto.

*Exemplo:*  
A String `*texto em itálico*` é convertido em `<i>texto em itálico</i>`.

## Utilização do Script

Para converter um ficheiro Markdown para HTML, execute o script da seguinte forma:

```bash
python3 tpc3.py nome_do_ficheiro.md
