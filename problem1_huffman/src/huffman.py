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
