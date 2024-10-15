import os

def get_sections(directory):
    section_names = {}
    for name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, name)):
            name = name.split('_', 1)
            section_number = int(name[0])
            section_name = name[1]
            section_names[section_number] = section_name
    return section_names

def get_subsections(directory):
    subsection_names = {}
    for name in os.listdir(directory):
        name = name.split('_', 1)
        subsection_number = int(name[0])
        subsection_name = name[1]
        subsection_names[subsection_number] = subsection_name
    return subsection_names

def main():
    doc_path = './Tex/handBook.tex'
    
    main_directory = './Algorithms/'
    section_names = get_sections(main_directory)

    with open(doc_path, 'w', encoding='utf-8') as doc_file:
        for number, name in sorted(section_names.items()):
            directory = main_directory + str(number) + '_' + name + '/'

            doc_file.write(f'\\section{{{name}}}\n')

            subsection_names = get_subsections(directory)

            for number, name in sorted(subsection_names.items()):
                file = directory + str(number) + '_' + name
                
                with open(file, 'r', encoding='utf-8') as f:
                    text = f.readlines()

                preamble = text[0].split('// ', 2)
                title = preamble[1]
                description = preamble[2]
                
                doc_file.write(f'\\subsection{{{title}}}\n')
                doc_file.write(f'{description}\n')
                doc_file.write('\\begin{lstlisting}')
                for line in text[1:]:
                    doc_file.write(f'{line}')
                doc_file.write('\\end{lstlisting}\n\n')
            
        
if __name__ == '__main__':
    main()
 