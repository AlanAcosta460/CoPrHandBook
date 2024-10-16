import os
import re

themes = ('Algebra', 'DataStructures', 'DynamicProgramming', 'StringProcessing', 'LinearAlgebra', 'Combinatorics', 'NumericalMethods', 'Graphs', 'Miscellaneous')
doc_path = './Tex/handBook.tex'

def separete_name(name):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', name)

def read_index(file):
    index = {}
    with open(file, 'r', encoding='utf-8') as f:
        text = f.readlines()

    for line in text[1:]:
        match = re.search(r'(\d+)\.\s*\[(.*?)\]\((.*?)\)', line)
        if match:
            number = match.group(1)
            name = match.group(2)
            path = match.group(3)
            index[number] = (name, path)

    return index

def extract_content(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.readlines()

    description = text[0].split('// ', 1)[1]

    return description, text

def append_code(description, text):
    with open(doc_path, 'a', encoding='utf-8') as doc_file:
        doc_file.write(f'{description}\n')
        doc_file.write('\\begin{lstlisting}')
        for line in text[1:]:
            doc_file.write(f'{line}')
        doc_file.write('\\end{lstlisting}\n\n')


def main():
    main_directory = './Algorithms/'

    with open(doc_path, 'w', encoding='utf-8'):
        pass
    
    template = './Algorithms/Template/template.cpp'
    description, text = extract_content(template)

    with open(doc_path, 'a', encoding='utf-8') as doc_file:
        doc_file.write('\\section{Template}\n')

    append_code(description, text)

    for theme_name in themes:
        path_theme = main_directory + theme_name + '/'

        with open(doc_path, 'a', encoding='utf-8') as doc_file:
            doc_file.write(f'\\section{{{separete_name(theme_name)}}}\n')
        
        index_theme = read_index(path_theme + 'index.md')

        for number, (name, file) in sorted(index_theme.items()):
            with open(doc_path, 'a', encoding='utf-8') as doc_file:
                doc_file.write(f'\\subsection{{{separete_name(name)}}}\n')
            
            path_subtheme = path_theme + file[1:]
            index_subtheme = read_index(path_subtheme + 'index.md')

            for number, (name, file) in sorted(index_subtheme.items()):
                with open(doc_path, 'a', encoding='utf-8') as doc_file:
                    doc_file.write(f'\\subsubsection{{{separete_name(name)}}}\n')

                path_subsubtheme = path_subtheme + file
                description, text = extract_content(path_subsubtheme)

                append_code(description, text)
                
if __name__ == '__main__':
    main()
