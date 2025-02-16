import re
import sys

def parse_line(line):
    #divide a linha nos ;, mas ignora ; dentro de aspas (se houverem)
    fields = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    #remove os espaços em branco e as aspas dos campos
    fields = [field.strip().strip('"') for field in fields]
    return fields

def main():
    csv_file = sys.argv[1]

    composers = set()
    period_distribution = {}
    period_titles = {}
    buffer = ''

    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            #ignora o cabeçalho
            next(file)

            for line in file:
                buffer += line
                #verifica se a linha está completa (7 campos)
                if buffer.count(';') >= 6:
                    fields = parse_line(buffer)
                    if len(fields) == 7:
                        nome = fields[0].strip()
                        periodo = fields[3].strip()
                        compositor = fields[4].strip()

                        composers.add(compositor)

                        period_distribution[periodo] = period_distribution.get(periodo, 0) + 1

                        if periodo not in period_titles:
                            period_titles[periodo] = []
                        period_titles[periodo].append(nome)

                    buffer = ''
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        sys.exit(1)

    #ordenar compositores períodos e títulos
    sorted_composers = sorted(composers)
    sorted_periods = sorted(period_distribution.keys())
    for periodo in period_titles:
        period_titles[periodo].sort()

    #print dos resultados
    print("Lista ordenada alfabeticamente dos compositores musicais:")
    for compositor in sorted_composers:
        print(compositor)

    print("\nDistribuição das obras por período:")
    for periodo in sorted_periods:
        print(f"{periodo}: {period_distribution[periodo]}")

    print("\nDicionário de períodos com títulos ordenados:")
    for periodo in sorted_periods:
        print(f"{periodo}: {period_titles[periodo]}")

if __name__ == "__main__":
    main()