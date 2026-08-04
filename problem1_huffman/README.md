# Problem 1: Huffman Coding

## Overview

For Greedy Algorithm category, Huffman Coding was selected because it is a lossless compression algorithm that able to assign the shorter binary codes to characters with high frequencies and longer binary code to less frequent characters. The program will count the character frequencies, builds a Huffman tree and encodes the user input. It also decodes the result to check whether the original text can be recovered correctly or not.

## Greedy Strategy

For the greedy algorithm problem, our group had selected Huffman Coding. Huffman Coding is a lossless compression algorithm that will convert characters into binary codes based on their frequencies. The main workflow for this algorithm is that the characters that appear more often will receive a shorter binary code and the characters that appear less often will receive a longer binary code. By using this algorithm, the total number of bits that required to represent the text can be reduced Our program will prompt user to enter a text string. It first counts how many times each character appears. After that, a Huffman tree will be build and binary codes is generated for every unique character. The original text is then encoded by replacing each character with the Huffman code. A decoding function was also included in the program as it helps to verify the result. The correct result is prove by the decoding text is the same as the original input.

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
├── README.md
└── samples/
    ├── sample_input.txt
    └── sample_output.txt
```

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
