import sys

def soma_sequencias_numeros():
    soma = 0
    soma_ativa = True  # se não tiver on nem off começa a somar
    digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        # Ler uma linha do stdin
        linha = sys.stdin.readline()
        if not linha:
            break

        i = 0
        while i < len(linha):
            # Verificar se encontramos "off"
            if i + 2 < len(linha) and linha[i:i+3].lower() == "off":
                soma_ativa = False
                i += 3
                continue

            # Verificar se encontramos "on"
            if i + 1 < len(linha) and linha[i:i+2].lower() == "on":
                soma_ativa = True
                i += 2
                continue

            # Verificar se encontramos um número
            if linha[i] in digitos and soma_ativa:
                numero_str = ""
                # Captura todos os dígitos consecutivos
                while i < len(linha) and linha[i] in digitos:
                    numero_str += linha[i]
                    i += 1
                # Converte a string de dígitos para inteiro e adiciona à soma
                soma += int(numero_str)
                continue

            # Verificar se encontramos o caractere '='
            if linha[i] == '=':
                #print("\n")
                print(f"Soma atual: {soma}")
            i += 1  # Avança para o próximo caractere


soma_sequencias_numeros()