# Processador de Texto com Soma de Números

Este programa realiza a soma de sequências de números presentes num texto, seguindo regras específicas. O programa lê o texto linha por linha e mantém o estado da soma entre as linhas.

## Funcionalidades Principais

1. **Soma de Números**:
   - O programa identifica e soma sequências específicas de dígitos no texto.
   - Exemplo: No texto `livro 123d  carro`, o número `123` é adicionado à soma.

2. **Controlo de Estado ("on" e "off")**:
   - Quando encontra a palavra `off` (em qualquer combinação de maiúsculas e minúsculas), o programa para de somar os números seguintes.
   - Quando encontra a palavra `on` (em qualquer combinação de maiúsculas e minúsculas), o programa volta a somar os números.
   - Exemplo: No texto `ON 123 off 456 ON 789`, ele soma `123` e `789`, mas ignora `456`.

3. **Exibição da Soma**:
   - Sempre que o programa encontra o caractere `=`, ele exibe o valor atual da soma.
   - Exemplo: No texto `ON 123 =`, o programa exibe `Soma atual: 123`.

4. **Leitura Interativa**:
   - O programa lê o texto linha por linha e processa cada linha imediatamente.
   - O valor da soma é mantido entre as linhas, permitindo que o estado e o valor acumulado sejam preservados.
   - Exemplo: Para o texto `On 123 =`, será exibido `Soma atual: 123`. Se depois escrever `ofF 456 oN 789 =`, será exibido `Soma atual: 912`.

## Como Usar

1. Executar o programa no terminal:
   ```bash
   python3 tpc1.py