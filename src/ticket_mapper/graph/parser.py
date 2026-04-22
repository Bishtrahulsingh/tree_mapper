import tree_sitter_python as tspython
import tree_sitter_javascript as tsjavascript
from tree_sitter import Language, Parser
from pathlib import Path
import requests

#reads file from local
def read_file(file_path):
    content = None
    path = Path(file_path)
    extension = path.suffix

    if extension == '.py':
        language = Language(tspython.language())
    elif extension in ['.js', '.jsx', '.ts', '.tsx']:
        language = Language(tsjavascript.language())
    else:
        raise  Exception(f'Currently this file type is not supported: {extension}')

    with open(file_path,'rb') as f:
            content = f.read()

    return content,language

#create tree from content and language provided by read_file
def create_tree(file_path):
    file_content, language = read_file(file_path)
    parser = Parser(language)
    tree = parser.parse(file_content)

    return tree.root_node


#extracts import statements of file
def extract_imports(root,results:list):

    stack = [root]

    print(root)

    while stack:
        node = stack.pop()

        if node.type == 'import_statement':
            for child in node.children:
                if child.type == 'dotted_name':
                    results.append(child.text.decode())
                elif node.type == 'aliased_import':
                    name = node.child_by_field_name('name')
                    if name:
                        results.append(name.text.decode())

        if node.type == 'import_from_statement':
            module = node.child_by_field_name('module_name')

            if module:
                results.append(module.text.decode())
        stack.extend(node.children)

