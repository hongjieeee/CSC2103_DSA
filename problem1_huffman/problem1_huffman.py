class Node:
    def __init__(self, character, frequency, order, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.order = order
        self.left = left
        self.right = right

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
    nodes = []
    next_order = 0

    # Create one leaf node for every unique character.
    for character in frequencies:
        nodes.append(
            Node(
                character=character, frequency=frequencies[character], order=next_order
            )
        )
        next_order += 1

    if len(nodes) == 0:
        return None

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

        # The combined parent becomes available for the next greedy step.
        nodes.append(parent_node)

    return nodes[0]


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


def decode_text(encoded_text, root):
    # Decode a Huffman bit string by traversing the tree.
    if root is None:
        return ""

    # If the input contains only one unique character.
    if root.is_leaf():
        for bit in encoded_text:
            if bit != "0":
                raise ValueError("A single character Huffman tree only accepts code 0.")

        return root.character * len(encoded_text)

    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left

        elif bit == "1":
            current_node = current_node.right

        else:
            raise ValueError("Encoded text must contain only 0 and 1.")

        if current_node is None:
            raise ValueError("The encoded text does not match the Huffman tree.")

        if current_node.is_leaf():
            decoded_text += current_node.character
            current_node = root

    if current_node is not root:
        raise ValueError("Encoded text ends with an incomplete Huffman code.")

    return decoded_text


def display_character(character):
    # make space readable in the console output
    if character == " ":
        return "[space]"

    return character


def display_results(text, frequencies, codes, encoded_text, decoded_text):
    # Display the code table, encoded result, and validation.
    print("\nRESULT")
    print("=" * 50)

    print("{:<18} {:<12} {}".format("Character", "Frequency", "Code"))

    print("-" * 50)

    for character in frequencies:
        print(
            "{:<18} {:<12} {}".format(
                display_character(character), frequencies[character], codes[character]
            )
        )

    original_bits = len(text.encode("utf-8")) * 8
    encoded_bits = len(encoded_text)

    print("-" * 50)
    print("Original text       :", text)
    print("Encoded bit string  :", encoded_text)
    print("Decoded text        :", decoded_text)

    if decoded_text == text:
        print("Validation          : PASS")
    else:
        print("Validation          : FAIL")

    print("Original UTF-8 size :", original_bits, "bits")
    print("Encoded data size   :", encoded_bits, "bits")

    if original_bits > 0:
        saving_percentage = ((original_bits - encoded_bits) * 100) / original_bits

        print("Data-bit saving     : {:.2f}%".format(saving_percentage))


def main():
    print("=" * 50)
    print("HUFFMAN CODING - GREEDY ALGORITHM (Problem 1)")
    print("=" * 50)

    text = input("Enter text to encode: ")

    if text == "":
        print("Error: input cannot be empty.")
        return

    frequencies = count_frequencies(text)

    tree = build_huffman_tree(frequencies)

    codes = build_codes(tree)

    encoded_text = encode_text(text, codes)

    decoded_text = decode_text(encoded_text, tree)

    display_results(text, frequencies, codes, encoded_text, decoded_text)


if __name__ == "__main__":
    main()
