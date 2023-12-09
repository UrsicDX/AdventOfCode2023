class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree_from_file(filename):
    table = {}
    pattern = ""
    with open(filename, 'r') as file:
        pattern = file.readline().strip()  
        for line in file:
            if line.strip():  
                parts = line.strip().split(' = ')
                key = parts[0]
                children = parts[1].strip('()').split(', ')
                table[key] = tuple(children)
    return pattern, build_tree(table)

def build_tree(table):
    nodes = {key: Node(key) for key in table}
    for key, (left_val, right_val) in table.items():
        nodes[key].left = nodes.get(left_val)
        nodes[key].right = nodes.get(right_val)
    return nodes

def find_shortest_path(start_node, target_value, pattern):
    def traverse(start_node, pattern):
        node = start_node
        path = ""
        pattern_index = 0

        while node is not None:
            if node.value == target_value:
                return path
            path += pattern[pattern_index]
            node = node.left if pattern[pattern_index] == 'L' else node.right
            pattern_index = (pattern_index + 1) % len(pattern)

        return None

    return traverse(start_node, pattern)

# Example usage
filename = "input.txt"
pattern, nodes = build_tree_from_file(filename)
start_node = nodes["AAA"]
shortest_path = find_shortest_path(start_node, "ZZZ", pattern)

print("Shortest path:", shortest_path)
print("Len:", len(shortest_path))