import re
import sys
import os

def markdown_html(input_text):
    lines = input_text.split('\n')
    html = []
    in_list = False
    list_items = []

    for line in lines:
        # Processar cabeçalhos
        header_match = re.match(r'^(#{1,3})\s+(.*)', line)
        if header_match:
            level = len(header_match.group(1))
            text = process_inline(header_match.group(2))
            html.append(f'<h{level}>{text}</h{level}>')
            continue

        # Processar listas numeradas
        list_match = re.match(r'^\d+\.\s+(.*)', line)
        if list_match:
            if not in_list:
                in_list = True
            list_items.append(list_match.group(1))
            continue
        else:
            if in_list:
                html.append('<ol>')
                for item in list_items:
                    processed_item = process_inline(item)
                    html.append(f'<li>{processed_item}</li>')
                html.append('</ol>')
                list_items = []
                in_list = False

        # Processar linhas normais
        if not in_list and line.strip() != '':
            processed_line = process_inline(line)
            html.append(f'<p>{processed_line}</p>')

    # Processar lista final se existir
    if in_list:
        html.append('<ol>')
        for item in list_items:
            processed_item = process_inline(item)
            html.append(f'<li>{processed_item}</li>')
        html.append('</ol>')

    return '\n'.join(html)

def process_inline(text):
    # Ordem de processamento importante
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    return text

def main():
    input_file = sys.argv[1]
    base_name = os.path.splitext(input_file)[0]
    output_file = base_name + ".html"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{input_file}' não encontrado")
        sys.exit(1)
    
    html_content = markdown_html(markdown_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Conversão concluída. HTML gerado no ficheiro: {output_file}")

if __name__ == "__main__":
    main()