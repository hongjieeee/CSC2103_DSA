class Node:
    def __init__(self, character, frequency, order, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.order = order
        self.left = left
        self.right = right

        # Store all symbols contained inside this subtree.
        if character is not None:
            self.symbols = [character]
        else:
            self.symbols = left.symbols + right.symbols

    def is_leaf(self):
        # Return True when this node represents an original character.
        return self.left is None and self.right is None


def count_frequencies(text):
    # Count how many times each character appears.
    frequencies = {}

    for character in text:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1

    return frequencies


def remove_smallest_node(nodes):
    # Find and remove the lowest-priority node.
    smallest_index = 0

    for index in range(1, len(nodes)):
        current_node = nodes[index]
        smallest_node = nodes[smallest_index]

        # A lower frequency receives higher priority.
        if current_node.frequency < smallest_node.frequency:
            smallest_index = index

        # Use earlier order as a tiebreaker when frequencies are equal.
        elif current_node.frequency == smallest_node.frequency:
            if current_node.order < smallest_node.order:
                smallest_index = index

    return nodes.pop(smallest_index)


def build_huffman_tree(frequencies):
    # Build the Huffman tree and record every greedy combination.
    nodes = []
    combine_steps = []
    next_order = 0

    # Create one leaf node for every unique character.
    for character in frequencies:
        nodes.append(
            Node(
                character=character,
                frequency=frequencies[character],
                order=next_order,
            )
        )
        next_order += 1

    if len(nodes) == 0:
        return None, combine_steps

    # Continue until all nodes have been combined into one root.
    while len(nodes) > 1:
        # Greedy choice: remove the two currently lowest-frequency nodes.
        left_node = remove_smallest_node(nodes)
        right_node = remove_smallest_node(nodes)

        parent_node = Node(
            character=None,
            frequency=left_node.frequency + right_node.frequency,
            order=next_order,
            left=left_node,
            right=right_node,
        )
        next_order += 1

        # Record this step for the console output and report screenshots.
        combine_steps.append((left_node, right_node, parent_node))

        # The combined parent becomes available for the next greedy step.
        nodes.append(parent_node)

    return nodes[0], combine_steps


def build_codes(node, current_code="", codes=None):
    # Traverse the Huffman tree recursively and assign binary codes.
    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.is_leaf():
        # A one character input still requires a usable binary code.
        if current_code == "":
            codes[node.character] = "0"
        else:
            codes[node.character] = current_code

        return codes

    # Left edge represents 0.
    build_codes(node.left, current_code + "0", codes)

    # Right edge represents 1.
    build_codes(node.right, current_code + "1", codes)

    return codes


def encode_text(text, codes):
    # Replace each original character with its Huffman code.
    encoded_text = ""

    for character in text:
        encoded_text += codes[character]

    return encoded_text
