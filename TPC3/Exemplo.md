# Conversor de Markdown para HTML

Este script em Python permite converter ficheiros de Markdown (`.md`) para ficheiros HTML, o que permite a criação de páginas web a partir de textos com formatação simples. Além das funcionalidades básicas de transformação de cabeçalhos, listas numeradas e parágrafos, o script processa também formatações inline como Links, imagens, negrito e itálico. Utiliza expressões regulares para identificar e substituir estes padrões.

## Funcionalidades

- **Cabeçalhos:**  
  Converte as linhas que começam com 1 a 3 símbolos `#` em elementos HTML `&lt;h1&gt;`, `&lt;h2&gt;` ou `&lt;h3&gt;`, conforme o número de símbolos.

- **Listas Numeradas:**  
  Agrupa as linhas iniciadas por um número seguido de ponto e espaço (ex.: `1. Item`) e converte-as numa lista ordenada (`&lt;ol&gt;`), envolvendo cada item com `&lt;li&gt;`.

- **Parágrafos:**  
  Linhas de texto sem formatação específica são envolvidas com `&lt;p&gt;`.

- **Formatação Inline:**  
  A função `process_inline` utiliza regex para converter:
  - **Imagens:** Em `&lt;img src="url" alt="texto alternativo"/&gt;`.
  - **Links:** Em `&lt;a href="url"&gt;texto&lt;/a&gt;`.
  - **Negrito:** Em `&lt;b&gt;texto&lt;/b&gt;`.
  - **Itálico:** Em `&lt;i&gt;texto&lt;/i&gt;`.

## Explicação Detalhada das Expressões Regulares

Abaixo encontra-se uma explicação pormenorizada de cada expressão regular utilizada no script:

### 1. Cabeçalhos

Regex: `r'^(#{1,3})\s+(.*)'`

- **^**  
  Indica o início da linha.

- **(#{1,3})**  
  Um grupo de captura que procura entre 1 e 3 ocorrências do símbolo `#`. O número de `#` determina o nível do cabeçalho (ex.: 1 para `&lt;h1&gt;`, 2 para `&lt;h2&gt;`, etc.).

- **\s+**  
  Corresponde a um ou mais espaços. Este espaço separa os símbolos `#` do texto do cabeçalho.

- **(.*)**  
  Um grupo de captura que obtém o restante da linha, ou seja, o conteúdo do cabeçalho.


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


### 5. Negrito

Regex: `r'\*\*(.*?)\*\*'`

- **\*\***  
  Corresponde a dois asteriscos que marcam o início do texto a ser colocado em negrito.

- **(.*?)**  
  Grupo de captura Lazy que obtém o texto a ser formatado em negrito.

- **\*\***  
  Corresponde a dois asteriscos que marcam o fim do texto.


### 6. Itálico

Regex: `r'\*(.*?)\*'`

- **\***  
  Corresponde a um asterisco que marca o início do texto a ser formatado em itálico.

- **(.*?)**  
  Grupo de captura Lazy que obtém o texto a converter.

- **\***  
  Corresponde ao asterisco que marca o fim do texto.


## Utilização do Script

Para converter um ficheiro Markdown para HTML, execute o script da seguinte forma:

```bash
python3 tpc3.py nome_do_ficheiro.md
