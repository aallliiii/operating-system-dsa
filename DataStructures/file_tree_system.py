class FileNode:
    def __init__(self, name, is_directory=True):
        self.name = name
        self.is_directory = is_directory
        self.children = []

class FileSystem:
    def __init__(self):
        self.root = FileNode("root")

    def add(self, parent_name, name, is_directory=True):
        parent = self.find(self.root, parent_name)
        if parent and parent.is_directory:
            new_node = FileNode(name, is_directory)
            parent.children.append(new_node)
            return f"{'Folder' if is_directory else 'File'} '{name}' added under '{parent_name}'."
        return f"Parent folder '{parent_name}' not found or is not a directory."

    def delete(self, name):
        if self.root.name == name:
            return "Cannot delete the root directory."

        parent, node_to_delete = self.find_with_parent(self.root, None, name)
        if node_to_delete:
            parent.children.remove(node_to_delete)
            return f"{'Folder' if node_to_delete.is_directory else 'File'} '{name}' deleted."
        return f"'{name}' not found."

    def search(self, name):
        node = self.find(self.root, name)
        if node:
            return f"{'Folder' if node.is_directory else 'File'} '{name}' found."
        return f"'{name}' not found."

    def display(self):
        return self.display_helper(self.root, level=0)

    def find(self, node, name):
        if node.name == name:
            return node
        for child in node.children:
            result = self.find(child, name)
            if result:
                return result
        return None

    def find_with_parent(self, node, parent, name):
        if node.name == name:
            return parent, node
        for child in node.children:
            result = self.find_with_parent(child, node, name)
            if result[1]:
                return result
        return None, None

    def display_helper(self, node, level):
        output = "  " * level + f"{'[Folder]' if node.is_directory else '[File]'} {node.name}\n"
        for child in node.children:
            output += self.display_helper(child, level + 1)
        return output

if __name__ == "__main__":
    fs = FileSystem()

    # print(fs.add("root", "Documents", True))
    # print(fs.add("root", "Photos", True))
    # print(fs.add("Documents", "Resume.docx", False))
    # print(fs.add("Photos", "Vacation.jpg", False))

    # print("\nFile System Hierarchy:")
    # print(fs.display())

    # print(fs.search("Photos"))
    # print(fs.search("Resume.docx"))
    # print(fs.search("Music"))

    # print("\nDeleting 'Vacation.jpg':")
    # print(fs.delete("Vacation.jpg"))
    # print("\nFile System Hierarchy After Deletion:")
    # print(fs.display())
