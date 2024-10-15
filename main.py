import os

def get_dirs(directory):
    dir_names = {}
    for name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, name)):
            name = name.split('_', 1)
            dir_number = int(name[0])
            dir_name = name[1]
            dir_names[dir_number] = dir_name
    return dir_names

def get_files(directory):
    file_names = {}
    for name in os.listdir(directory):
        name = name.split('_', 1)
        file_number = int(name[0])
        file_name = name[1]
        file_names[file_number] = file_name
    return file_names

def append_tex(doc_file, title, description, text):
    doc_file.write(f'\\subsubsection{{{title}}}\n')
    doc_file.write(f'{description}\n')
    doc_file.write('\\begin{lstlisting}')
    for line in text[1:]:
        doc_file.write(f'{line}')
    doc_file.write('\\end{lstlisting}\n\n')

def main():
    doc_path = './Tex/handBook.tex'
    
    main_directory = './Algorithms/'
    sec_names = get_dirs(main_directory)

    with open(doc_path, 'w', encoding='utf-8') as doc_file:
        for number, name in sorted(sec_names.items()):
            sub_directory = main_directory + str(number) + '_' + name + '/'

            doc_file.write(f'\\section{{{name}}}\n')

            subsec_names = get_dirs(sub_directory)

            if not subsec_names:
                subsec_names = get_files(sub_directory)

                for number, name in sorted(subsec_names.items()):
                    file = sub_directory + str(number) + '_' + name
                    
                    with open(file, 'r', encoding='utf-8') as f:
                        text = f.readlines()

                    preamble = text[0].split('// ', 2)
                    title = preamble[1]
                    description = preamble[2]

                    append_tex(doc_file, title, description, text)
            else: 
                for number, name in sorted(subsec_names.items()):
                    subsub_directory = sub_directory + str(number) + '_' + name + '/'

                    doc_file.write(f'\\subsection{{{name}}}\n')

                    subsubsec_names = get_files(subsub_directory)

                    for number, name in sorted(subsubsec_names.items()):
                        file = subsub_directory + str(number) + '_' + name
                        
                        with open(file, 'r', encoding='utf-8') as f:
                            text = f.readlines()

                        preamble = text[0].split('// ', 2)
                        title = preamble[1]
                        description = preamble[2]

                        append_tex(doc_file, title, description, text)
                
if __name__ == '__main__':
    main()
    print('test')
