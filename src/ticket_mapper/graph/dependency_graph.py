from typing import List,Dict

from src.ticket_mapper.graph.parser import create_tree, extract_imports


class DependencyGraph:
    def __init__(self):
        self.forward_graph:Dict[str,List[str]] = {}
        self.reverse_graph:Dict[str,List[str]] = {}

    def resolve_relative_imports(self):
        pass

    def add_in_graph(self,file_path:str, imported_files:List[str]):

        if file_path not in self.forward_graph:
            self.forward_graph[file_path] = imported_files
        else:
            self.forward_graph[file_path].extend(imported_files)

        for imported_file in imported_files:
            if imported_file not in self.reverse_graph:
                self.reverse_graph[imported_file] = [file_path]
            else:
                self.reverse_graph[imported_file].append(file_path)

    def find_affected_files(self,file_path:str):
        return self.reverse_graph.get(file_path,[])

file_path = 'src/ticket_mapper/graph/hello.py'
root = create_tree(file_path=file_path)

imports = []
extract_imports(root,imports)

imports = list(set(imports))

dg = DependencyGraph()
dg.add_in_graph(file_path=file_path,imported_files=imports)

print(dg.forward_graph,end='\n-----------\n')
print(dg.reverse_graph,end='\n-----------\n')
