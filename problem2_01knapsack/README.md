# Problem 2: 0/1 Knapsack

## Overview

For the Dynamic Programming category, the 0/1 Knapsack problem was selected because it demonstrates how breaking a problem into overlapping subproblems and storing intermediate results can guarantee an optimal solution, something a greedy, item-by-item choice cannot do when items cannot be split. The program prompts the user to enter a knapsack capacity and a list of items, each with a value and a weight. It builds a dynamic programming table bottom-up, uses that table to determine the maximum achievable value, and backtracks through the table to identify exactly which items make up the optimal solution.

## Dynamic Programming Strategy

The 0/1 Knapsack problem asks: given a set of items, each with a value and a weight, and a knapsack with a fixed weight capacity, which combination of items maximizes total value without exceeding the capacity, given that each item can either be taken whole or left behind (no fractional items)? A greedy approach, such as always picking the item with the best value-to-weight ratio, does not guarantee an optimal answer here, because taking a high-ratio item early can block a better combination of items later. Dynamic programming solves this by building a table `tab[i][w]`, where each cell holds the best possible value achievable using only the first `i` items with a knapsack capacity of `w`. The table is filled row by row: for each item, if its weight fits within the current capacity `w`, the algorithm compares the value obtained by including the item (its value plus the best value left over from the remaining capacity) against the value obtained by excluding it (the best value already found using only the previous items). The larger of the two is stored. If the item's weight does not fit, its value is simply carried over from the previous row. Once the table is complete, `tab[n][capacity]` holds the maximum achievable value, and walking backwards through the table (checking where the value changed from one row to the next) reveals exactly which items were included in that optimal solution.

## Features

- Accepts interactive console input for the knapsack capacity and each item's value and weight
- Validates all numeric input, rejecting non-numbers and re-prompting the user
- Enforces a minimum capacity of 0 and a minimum item weight of 1
- Supports any number of items via a repeated "add another item?" prompt
- Builds the full 0/1 Knapsack DP table (`tab[i][w]`) using bottom-up tabulation
- Prints a formatted, aligned view of the DP table
- Backtracks through the table to determine exactly which items were selected
- Displays the capacity and total number of items entered
- Lists each selected item with its weight and value
- Shows total weight used versus capacity
- Displays the final maximum achievable value
- Handles a zero-capacity edge case, reporting that no items fit
- Handles an exact-fit case where the chosen items use the full capacity

## Requirements

- Python 3
- No external Python libraries are required

## Project Files

```text
problem2_knapsack/
├── problem2_knapsack.py
├── README.md
└── samples/
    ├── sample_input.txt
    └── sample_output.txt
```

## Running the Program

Open a terminal in the `problem2_knapsack` folder and run:

```bash
python3 problem2_knapsack.py
```

You will first be prompted for the knapsack capacity, then for each item's value and weight. After each item, you'll be asked whether you want to add another one.

Example:

```text
Please add capacity: 10

--- Item 1 ---
Please add value: 300
Please add weight: 2

Do you want to add another item? (y/n): y
```

## Program Output

The program displays:

1. The full DP table (`tab[i][w]`)
2. The capacity entered
3. The number of items entered
4. The list of selected items (weight and value for each)
5. Total weight used out of the available capacity
6. The maximum value achievable in the knapsack

## Validation

The main correctness check is done by tracing the DP table against known, hand-checkable inputs:

```text
Capacity + item list → Build DP table → Backtrack selected items → Compare against expected optimal value
```

The implementation passes validation when the value in `tab[n][capacity]` matches the true optimal value for the test case, and the backtracked item list sums to exactly that value without exceeding the capacity.

## Example Test Cases

### Test Case 1: Normal Case

**Input**

```text
Please add capacity: 10

--- Item 1 ---
Please add value: 300
Please add weight: 2

Do you want to add another item? (y/n): y

--- Item 2 ---
Please add value: 200
Please add weight: 1

Do you want to add another item? (y/n): y

--- Item 3 ---
Please add value: 400
Please add weight: 5

Do you want to add another item? (y/n): y

--- Item 4 ---
Please add value: 500
Please add weight: 3

Do you want to add another item? (y/n): n
```

**Output**

```text
========================================
Results
========================================
DP Table
        0    1    2    3    4    5    6    7    8    9   10
i=0     0    0    0    0    0    0    0    0    0    0    0
i=1     0    0  300  300  300  300  300  300  300  300  300
i=2     0  200  300  500  500  500  500  500  500  500  500
i=3     0  200  300  500  500  500  600  700  900  900  900
i=4     0  200  300  500  700  800 1000 1000 1000 1100 1200

Capacity: 10
Items entered: 4

Items to take:
  Item 1: weight=2, value=300
  Item 3: weight=5, value=400
  Item 4: weight=3, value=500

Weight used: 10 / 10
Maximum value in Knapsack = 1200
```

### Test Case 2: Exact Fit Case

**Input**

```text
Please add capacity: 6

--- Item 1 ---
Please add value: 10
Please add weight: 1

Do you want to add another item? (y/n): y

--- Item 2 ---
Please add value: 20
Please add weight: 2

Do you want to add another item? (y/n): y

--- Item 3 ---
Please add value: 30
Please add weight: 3

Do you want to add another item? (y/n): n
```

**Output**

```text
========================================
Results
========================================
DP Table
        0    1    2    3    4    5    6
i=0     0    0    0    0    0    0    0
i=1     0   10   10   10   10   10   10
i=2     0   10   20   30   30   30   30
i=3     0   10   20   30   40   50   60

Capacity: 6
Items entered: 3

Items to take:
  Item 1: weight=1, value=10
  Item 2: weight=2, value=20
  Item 3: weight=3, value=30

Weight used: 6 / 6
Maximum value in Knapsack = 60
```

Every item's weight adds up to exactly the capacity (1 + 2 + 3 = 6), so all three items are taken and the knapsack is filled completely.

### Test Case 3: Zero Capacity Edge Case

**Input**

```text
Please add capacity: 0

--- Item 1 ---
Please add value: 10
Please add weight: 1

Do you want to add another item? (y/n): y

--- Item 2 ---
Please add value: 20
Please add weight: 2

Do you want to add another item? (y/n): y

--- Item 3 ---
Please add value: 30
Please add weight: 3

Do you want to add another item? (y/n): n
```

**Output**

```text
========================================
Results
========================================
DP Table
        0
i=0     0
i=1     0
i=2     0
i=3     0

Capacity: 0
Items entered: 3

No items fit in the knapsack.
Maximum value in Knapsack = 0
```

With a capacity of 0, no item (all of which have a weight of at least 1) can ever be added, so the maximum value is 0.
