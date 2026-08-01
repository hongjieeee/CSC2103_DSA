# Problem 1: Huffman Coding

## Overview

This console-based program implements the Huffman Coding algorithm using a greedy approach. It accepts a text string, counts the frequency of each character, constructs a Huffman tree, generates prefix-free binary codes, and encodes the original text.

The program also decodes the encoded bit string to verify that the original text can be recovered correctly.

## Greedy Strategy

At each stage, the algorithm selects the two available nodes with the lowest frequencies. These nodes become the left and right children of a newly created parent node.

The frequency of the parent node is calculated as the sum of the two selected frequencies. The parent node is then returned to the available node list.

This process continues until only one node remains, which becomes the root of the Huffman tree.

The minimum-frequency nodes are selected through a manual linear scan. Built-in sorting and priority-queue libraries are not used for the core algorithm.

## Features

- Accepts console user input
- Counts character frequencies manually
- Constructs a Huffman tree
- Generates prefix-free Huffman codes
- Encodes the original text
- Decodes the encoded bit string
- Validates the decoded result
- Displays a formatted character-frequency-code table
- Estimates the original and encoded data sizes
- Handles spaces and single-character inputs
- Rejects empty input

## Requirements

- Python 3
- No external Python libraries are required

## Project Files

```text
problem1_huffman/
├── problem1_huffman.py
├── test_huffman.py
├── README.md
└── samples/
    ├── sample_input.txt
    └── sample_output.txt
```

`test_huffman.py` contains the automated tests and may be maintained by the testing and verification team member.

## Running the Program

Open a terminal in the `problem1_huffman` folder and run:

```bash
python3 problem1_huffman.py
```

Enter a non-empty text string when prompted.

Example:

```text
Enter text to encode: banana
```

## Running the Tests

Open a terminal in the `problem1_huffman` folder and run:

```bash
python3 test_huffman.py
```

## Program Output

The program displays:

1. Each unique character
2. Character frequency
3. Generated Huffman code
4. Original text
5. Encoded bit string
6. Decoded text
7. Validation status
8. Original UTF-8 size
9. Encoded data size
10. Estimated data-bit saving

## Validation

The main correctness check uses round-trip validation:

```text
Original text → Encode → Decode → Compare with original
```

The implementation passes validation when the decoded text is exactly equal to the original input.

## Example Test Cases

TODO:
