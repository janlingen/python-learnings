class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        FileSystem._validate_path(path)
        dirs = path[1:].split("/")
        bottom = self._find_bottom_node(dirs[:-1])
        if dirs[-1] not in bottom.children:
            new_dir = Directory(dirs[-1])
            bottom.add_node(new_dir)
        else:
            raise ValueError("Dir already exists")


    def create_file(self, path, contents):
        FileSystem._validate_path(path)
        dirs = path[1:].split("/")
        bottom = self._find_bottom_node(dirs[:-1])
        if dirs[-1] not in bottom.children:
            new_file = File(dirs[-1])
            new_file.write_contents(contents)
            bottom.add_node(new_file)
        else:
            raise ValueError("File already exists")

    def read_file(self, path):
        FileSystem._validate_path(path)
        dirs = path[1:].split("/")
        bottom = self._find_bottom_node(dirs[:-1])
        if dirs[-1] not in bottom.children:
            raise ValueError("File does not exist")
        else:
            return bottom.children[dirs[-1]].contents

    def delete_directory_or_file(self, path):
        FileSystem._validate_path(path)
        dirs = path[1:].split("/")
        bottom = self._find_bottom_node(dirs[:-1])
        if dirs[-1] not in bottom.children:
            raise ValueError("File/Directory does not exist")
        else:
            bottom.delete_node(dirs[-1])

    def size(self):
        file_lst = []
        path_to_go = [self.root]
        result = 0
        while len(path_to_go) > 0:
            for i in path_to_go.pop(0).children.values():
                if isinstance(i, Directory):
                    path_to_go.append(i)
                if isinstance(i, File):
                    file_lst.append(i)
        for i in file_lst:
            result += len(i)
        return result

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    def _find_bottom_node(self, node_names):
        curr_node = self.root
        for name in node_names:
            if not isinstance(curr_node, Directory) or name not in curr_node.children:
                raise ValueError("Not a Directory or not found.")
            curr_node = curr_node.children[name]
        return curr_node

class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

                
