# Problem 1: Huffman Coding

## Overview

For Greedy Algorithm category, Huffman Coding was selected because it is a lossless compression algorithm that able to assign the shorter binary codes to characters with high frequencies and longer binary code to less frequent characters. The program will count the character frequencies, builds a Huffman tree and encodes the user input. It also decodes the result to check whether the original text can be recovered correctly or not.

---

## Greedy Strategy

For the greedy algorithm problem, our group had selected Huffman Coding. Huffman Coding is a lossless compression algorithm that will convert characters into binary codes based on their frequencies. The main workflow for this algorithm is that the characters that appear more often will receive a shorter binary code and the characters that appear less often will receive a longer binary code. By using this algorithm, the total number of bits that required to represent the text can be reduced Our program will prompt user to enter a text string. It first counts how many times each character appears. After that, a Huffman tree will be build and binary codes is generated for every unique character. The original text is then encoded by replacing each character with the Huffman code. A decoding function was also included in the program as it helps to verify the result. The correct result is prove by the decoding text is the same as the original input.

---

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

---

## Requirements

- Python 3
- No external Python libraries are required

---

## Project Files

```text
problem1_huffman/
├── problem1_huffman.py
├── README.md
└── samples/
    ├── sample_input.txt
    └── sample_output.txt
```

---

## Running the Program

Open a terminal in the `problem1_huffman` folder and run:

```bash
python3 problem1_huffman.py
```

Enter a non-empty text string when prompted.

### Example

```text
Enter text to encode: banana
```

---

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

---

## Validation

The main correctness check uses round-trip validation:

```text
Original text → Encode → Decode → Compare with original
```

The implementation passes validation when the decoded text is exactly equal to the original input.

---

# Example Test Cases

## Test Case 1: Testing Normal Strings (Words)

### Input

```text
==================================================
HUFFMAN CODING - GREEDY ALGORITHM (Problem 1)
==================================================
Enter text to encode: banana
```

### Output

```text
RESULT
==================================================
Character          Frequency    Code
--------------------------------------------------
b                  1            10
a                  3            0
n                  2            11
--------------------------------------------------
Original text       : banana
Encoded bit string  : 100110110
Decoded text        : banana
Validation          : PASS
Original UTF-8 size : 48 bits
Encoded data size   : 9 bits
Data-bit saving     : 81.25%
```

---

## Test Case 2: Testing Upper Case and Lower Case Alphabets

### Input

```text
=================================================
HUFFMAN CODING - GREEDY ALGORITHM (Problem 1)
==================================================
Enter text to encode: AaAaAa
```

### Output

```text
RESULT
==================================================
Character          Frequency    Code
--------------------------------------------------
A                  3            0
a                  3            1
--------------------------------------------------
Original text       : AaAaAa
Encoded bit string  : 010101
Decoded text        : AaAaAa
Validation          : PASS
Original UTF-8 size : 48 bits
Encoded data size   : 6 bits
Data-bit saving     : 87.50%
```

---

## Test Case 3: Testing Numbers Only

### Input

```text
==================================================
HUFFMAN CODING - GREEDY ALGORITHM (Problem 1)
==================================================
Enter text to encode: 123341233123
```

### Output

```text
RESULT
==================================================
Character          Frequency    Code
--------------------------------------------------
1                  3            111
2                  3            10
3                  5            0
4                  1            110
--------------------------------------------------
Original text       : 123341233123
Encoded bit string  : 11110001101111000111100
Decoded text        : 123341233123
Validation          : PASS
Original UTF-8 size : 96 bits
Encoded data size   : 23 bits
Data-bit saving     : 76.04%
```

---

## Test Case 4: Numbers and Special Character

### Input

```text
==================================================
HUFFMAN CODING - GREEDY ALGORITHM (Problem 1)
==================================================
Enter text to encode: 123341233123$
```

### Output

```text
RESULT
==================================================
Character          Frequency    Code
--------------------------------------------------
1                  3            01
2                  3            10
3                  5            11
4                  1            000
$                  1            001
--------------------------------------------------
Original text       : 123341233123$
Encoded bit string  : 0110111100001101111011011001
Decoded text        : 123341233123$
Validation          : PASS
Original UTF-8 size : 104 bits
Encoded data size   : 28 bits
Data-bit saving     : 73.08%
```

---

## Test Case 5: Just 1 Empty Space (or Empty String)

### Input

```text
==================================================
HUFFMAN CODING - GREEDY ALGORITHM (Problem 1)
==================================================
Enter text to encode:
```

### Output

```text
RESULT
==================================================
Character          Frequency    Code
--------------------------------------------------
[space]            1            0
--------------------------------------------------
Original text       :
Encoded bit string  : 0
Decoded text        :
Validation          : PASS
Original UTF-8 size : 8 bits
Encoded data size   : 1 bits
Data-bit saving     : 87.50%
```
---

## Test Case 6: Full Capability Testing

### Input

```text
==================================================
HUFFMAN CODING - GREEDY ALGORITHM (Problem 1)
==================================================
Enter text to encode: aaaaaaaaaabbbbbcccd A! 321
```

## Output

```text
RESULT
==================================================
Character          Frequency    Code
--------------------------------------------------
a                  10           0
b                  5            111
c                  3            100
d                  1            10110
[space]            2            1010
A                  1            10111
!                  1            11000
3                  1            11001
2                  1            11010
1                  1            11011
--------------------------------------------------
Original text       : aaaaaaaaaabbbbbcccd A! 321
Encoded bit string  : 000000000011111111111111110010010010110101010111110001010110011101011011
Decoded text        : aaaaaaaaaabbbbbcccd A! 321
Validation          : PASS
Original UTF-8 size : 208 bits
Encoded data size   : 72 bits
Data-bit saving     : 65.38%
```
