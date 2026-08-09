# Problem 2: 0/1 Knapsack

## Overview

For the Dynamic Programming category, the selected algorithm is 0/1 Knapsack, a classic optimization problem where each item can either be included once or left out entirely, with the goal of maximizing the total value without exceeding a given weight capacity. The program will take the capacity of the knapsack along with the weights and values of each item, build a dynamic programming table to calculate the maximum value possible without exceeding the capacity of the knapsack, and determine which items to select to get the optimal result, ensuring that the solution is both accurate and easy to verify through the displayed table and final output.

## Dynamic Programming Strategy

The dynamic programming approach occurs in the 0/1 Knapsack solution by comparing the overall value of including an item or excluding it, both values are calculated using previously solved subproblems, keeping whichever value is higher, provided the weight does not go over the knapsack capacity. At the beginning, a two-dimensional table is created where each cell stores the maximum value that can be obtained using the given number of items and a given knapsack capacity (W3Schools.com, 2026). The table is filled in a forward, bottom-up manner, starting from the base case and building up to the full item count and capacity. For each item, the algorithm checks whether the current item can fit into the current capacity. If the item's weight is less than or equal to the current capacity, the algorithm compares two possibilities: including the item or excluding it (Sandhu, 2024). The maximum of these two values are stored in the table. If the item cannot fit, the value from the previous row is carried forward. This process continues until the table is filled. After the table is fully constructed, the program then walks backwards through it to identify which items were selected. This is a dynamic programming approach because the program creates optimal substructure from the best value for a given capacity is built from the best values of smaller subproblems already sorted in the table, while also showing overlapping subproblems because each smaller subproblem is solved once and reused, rather than being recalculated and repeate

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
problem2_01knapsack/
├── problem2_01knapsack.py
└── README.md
```

## Running the Program

Open a terminal in the `problem2_01knapsack` folder and run:

```bash
python3 problem2_01knapsack.py
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

The program checks several possible item combinations and selects Item 1, Item 3, and Item 4 because they give the maximum value of 1200 without exceeding the capacity of 10.

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

### Test Case 3: Zero-Capacity Edge Case

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

### Test Case 4: Small Capacity Case

**Input**

```text
Please add capacity: 1

--- Item 1 ---
Please add value: 300
Please add weight: 2

Do you want to add another item? (y/n): y

--- Item 2 ---
Please add value: 200
Please add weight: 3

Do you want to add another item? (y/n): y

--- Item 3 ---
Please add value: 400
Please add weight: 4

Do you want to add another item? (y/n): n
```

**Output**

```text
========================================
Results
========================================
DP Table
       0  1
i=0    0  0
i=1    0  0
i=2    0  0
i=3    0  0

Capacity: 1
Items entered: 3

No items fit in the knapsack.
Maximum value in Knapsack = 0
```

With a capacity of 1, every item's weight is greater than the knapsack capacity, so no item can be selected and the maximum value is 0.

### Test Case 5: Classic Optimal-Combination Case

**Input**

```text
Please add capacity: 50

--- Item 1 ---
Please add value: 60
Please add weight: 10

Do you want to add another item? (y/n): y

--- Item 2 ---
Please add value: 100
Please add weight: 20

Do you want to add another item? (y/n): y

--- Item 3 ---
Please add value: 120
Please add weight: 30

Do you want to add another item? (y/n): n
```

**Output**

```text
========================================
Results
========================================
DP Table
         0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50
i=0      0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
i=1      0    0    0    0    0    0    0    0    0    0   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60   60
i=2      0    0    0    0    0    0    0    0    0    0   60   60   60   60   60   60   60   60   60   60  100  100  100  100  100  100  100  100  100  100  160  160  160  160  160  160  160  160  160  160  160  160  160  160  160  160  160  160  160  160  160
i=3      0    0    0    0    0    0    0    0    0    0   60   60   60   60   60   60   60   60   60   60  100  100  100  100  100  100  100  100  100  100  160  160  160  160  160  160  160  160  160  160  180  180  180  180  180  180  180  180  180  180  220

Capacity: 50
Items entered: 3

Items to take:
  Item 2: weight=20, value=100
  Item 3: weight=30, value=120

Weight used: 50 / 50
Maximum value in Knapsack = 220
```

The program selects Item 2 and Item 3 because their combined value of 220 is the best possible result within the capacity of 50.
