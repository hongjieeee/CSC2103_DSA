# Problem 3: A* Heuristic Pathfinding

## Overview

For the Heuristic Algorithm category, the A* Search Algorithm was selected because it is able to find the shortest valid path between a selected starting cell and destination cell. The program uses both the actual distance travelled and the estimated distance remaining to guide the search. It accepts a user-created grid, avoids blocked cells, checks valid neighbouring cells, and displays the final path using `X`. The complete path is also printed as a sequence of coordinates so that the result can be checked clearly.

---

## Heuristic Strategy

For the heuristic algorithm problem, our group selected the A* Search Algorithm. A* is a pathfinding algorithm that evaluates each cell by combining the actual distance from the starting cell with the estimated distance to the destination.

The calculation used is:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` is the actual distance travelled from the starting cell.
- `h(n)` is the estimated distance from the current cell to the destination.
- `f(n)` is the total estimated cost of travelling through the current cell.

The program uses Euclidean distance as the heuristic:

```text
h(n) = √((row1 - row2)² + (column1 - column2)²)
```

The cell with the lowest `f` value is selected from the open list. The algorithm then checks its neighbouring cells, ignores invalid or blocked cells, and updates a neighbour when a shorter path is found. This process continues until the destination is reached or no valid path remains.

---

## Features

- Accepts console user input
- Accepts different numbers of rows and columns
- Creates a user-defined grid
- Uses `1` to represent an open cell
- Uses `0` to represent a blocked cell
- Uses `X` to display the final path
- Supports horizontal, vertical, and diagonal movement
- Calculates Euclidean distance
- Uses an open list and a closed list
- Avoids blocked and processed cells
- Stores parent coordinates for path reconstruction
- Displays the path visually on the grid
- Prints the full path as coordinates
- Validates positive grid dimensions
- Validates starting and destination coordinates
- Rejects a blocked starting cell
- Detects a blocked destination cell
- Displays searched cells when no valid path exists

---

## Requirements

- Python 3
- No external Python libraries are required

---

## Project Files

```text
problem3_astar/
├── problem3_astar.py
├── README.md
└── samples/
    ├── sample_run_1.png
    ├── sample_run_2.png
    └── sample_output.txt
```

The actual file names may be changed depending on the structure of the repository.

---

## Running the Program

Open a terminal in the `problem3_astar` folder and run:

```bash
python3 problem3_astar.py
```

For Windows, the following command can also be used:

```bash
python problem3_astar.py
```

The program will first ask for the number of rows and columns. The user must then enter the grid row by row before entering the starting and destination coordinates.

---

## Grid Representation

The program uses the following symbols:

| Symbol | Meaning |
|---|---|
| `1` | Open cell that can be used |
| `0` | Blocked cell or wall |
| `X` | Cell included in the final path |
| `X` in failed output | Cell explored before the search failed |

Rows and columns start from `0`.

For example, in a `5 × 5` grid:

```text
Rows:    0 to 4
Columns: 0 to 4
```

---

## Input and Output Design

| Component | Design |
|---|---|
| Input | Number of rows and columns, grid values, starting coordinates, and destination coordinates |
| Valid data | Positive grid dimensions, grid rows with the correct number of values, and coordinates within the grid |
| Grid values | `1` for an open cell and `0` for a blocked cell |
| Main output | `Found!`, a visual grid with the path marked using `X`, and the complete coordinate sequence |
| Validation | Checks positive dimensions, row length, coordinate boundaries, and blocked start or destination cells |
| Error handling | Displays messages for invalid dimensions, incorrect row lengths, blocked cells, invalid coordinates, and unavailable paths |

---

## Program Input

The user enters:

1. Number of rows
2. Number of columns
3. Grid values for every row
4. Starting-cell coordinates
5. Destination-cell coordinates

### Example Input

```text
Enter number of rows: 5
Enter number of columns: 5

Enter the grid row by row
Row 0: 1 1 1 1 1
Row 1: 0 0 1 0 0
Row 2: 1 0 0 1 1
Row 3: 1 1 0 1 1
Row 4: 1 1 1 1 0

Enter Start cell (row col): 0 0
Enter Destination cell (row col): 4 0
```

---

## Program Output

When the path is found, the program displays:

1. A `Found!` message
2. Column labels
3. Row labels
4. The grid with the final path marked using `X`
5. The complete path as coordinates

### Example Output

```text
Calculating path...

Found!
column: 0 1 2 3 4
---------

row 0:  X X 1 1 1
row 1:  0 0 X 0 0
row 2:  1 0 0 X 1
row 3:  1 1 0 X 1
row 4:  X X X 1 0

Path:(0, 0) --> (0, 1) --> (1, 2) --> (2, 3) -->
(3, 3) --> (4, 2) --> (4, 1) --> (4, 0)
```

The visual grid makes the route easier to understand, while the coordinate sequence shows the exact order in which the final path moves.

---

## Main Data Structures

### Cell Objects

Each position in the grid is represented by a `cell` object.

```python
class cell:
    def __init__(self, a=0, b=0, blocked=False):
        self.a = a
        self.b = b
        self.pa = -1
        self.pb = -1

        self.g = float('inf')
        self.h = 0
        self.f = float('inf')

        self.blocked = blocked
```

Each cell stores:

| Attribute | Purpose |
|---|---|
| `a` | Row position |
| `b` | Column position |
| `pa` | Parent row |
| `pb` | Parent column |
| `g` | Actual distance from the starting cell |
| `h` | Estimated distance to the destination |
| `f` | Total estimated cost |
| `blocked` | Shows whether the cell is blocked |

### Open List

The open list stores cells that have been discovered but have not yet been fully processed.

```python
open_list = []
```

The algorithm selects the cell with the lowest `f` value from this list.

### Closed List

The closed list stores cells that have already been processed.

```python
closed_list = []
```

This prevents the same cell from being processed repeatedly.

### Path List and Path Set

The path list stores the final coordinates in order.

```python
path = []
```

The path set is used to check quickly whether a coordinate belongs to the path.

```python
path_set = set(path)
```

---

## Main Functions

### Heuristic Function

The `Heuristic()` function calculates the Euclidean distance between two cells.

```python
def Heuristic(a, b):
    return ((a.a - b.a)**2 + (a.b - b.b)**2)**0.5
```

This is suitable because the program allows both straight and diagonal movement.

---

### Positive Integer Validation

The `Check_valid_positive_integer()` function rejects row or column values that are zero or negative.

```python
def Check_valid_positive_integer(value):
    if value <= 0:
        print("\nvalue cannot be 0 or less\n")
        return False
    else:
        return True
```

---

### Blocked Cell Validation

The `Check_start_dest_blocked()` function checks whether the starting or destination cell is blocked.

```python
def Check_start_dest_blocked(start, end):
    if start.blocked:
        print("start cell is blocked")
        return True

    elif end.blocked:
        print("end cell is blocked")
        return True

    else:
        return False
```

---

### Neighbour Finding

The program checks eight possible directions around the current cell.

```python
directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (1, -1), (-1, 1), (1, 1)
]
```

The first four directions represent straight movement, while the last four represent diagonal movement.

The neighbour coordinates are calculated using:

```python
for da, db in directions:
    na = current.a + da
    nb = current.b + db
```

A neighbour is skipped when:

- It is outside the grid
- It is blocked
- It has already been processed

---

### Cost Updating

The new movement cost is calculated using:

```python
new_g = current.g + Heuristic(current, neighbour)
```

If the new path is shorter than the previous path, the neighbour is updated.

```python
if new_g < neighbour.g:
    neighbour.pa = current.a
    neighbour.pb = current.b

    neighbour.g = new_g
    neighbour.h = Heuristic(neighbour, end_cell)
    neighbour.f = neighbour.g + neighbour.h

    open_list.append(neighbour)
```

---

### Path Creation

The `Create_path()` function follows the parent coordinates from the destination back to the starting cell.

```python
path = []

while current.pa != -1 and current.pb != -1:
    path.append((current.a, current.b))
    current = cells[current.pa][current.pb]

path.append((start_cell.a, start_cell.b))
path.reverse()
```

After the path is reversed, it is displayed from the starting cell to the destination.

---

### Failed Path Output

When no valid route exists, the `failed_path()` function displays the cells that were explored.

```python
def failed_path(closed_list):
    path_set = set(closed_list)
```

The program then prints:

```text
there is no valid path from start to destination
```

---

## Validation

The main correctness check is based on the final path:

```text
Start cell → Valid open cells → Destination cell
```

The implementation is considered correct when:

- The first coordinate is the selected starting cell
- The last coordinate is the selected destination
- Every coordinate is within the grid
- Every path cell is open
- No blocked cell is included
- Each movement follows an allowed direction
- The visual `X` path matches the coordinate path
- A failure message is shown when no route exists

---

# Example Test Cases

## Test Case 1: Normal 5 × 5 Grid with Obstacles

### Input

```text
Enter number of rows: 5
Enter number of columns: 5

Row 0: 1 1 1 1 1
Row 1: 0 0 1 0 0
Row 2: 1 0 0 1 1
Row 3: 1 1 0 1 1
Row 4: 1 1 1 1 0

Enter Start cell (row col): 0 0
Enter Destination cell (row col): 4 0
```

### Output

```text
Calculating path...

Found!
column: 0 1 2 3 4
---------

row 0:  X X 1 1 1
row 1:  0 0 X 0 0
row 2:  1 0 0 X 1
row 3:  1 1 0 X 1
row 4:  X X X 1 0

Path:(0, 0) --> (0, 1) --> (1, 2) --> (2, 3) -->
(3, 3) --> (4, 2) --> (4, 1) --> (4, 0)
```

### Result

```text
PASS
```

The algorithm successfully finds a valid path around the blocked cells.

---

## Test Case 2: Open 3 × 3 Grid

### Input

```text
Enter number of rows: 3
Enter number of columns: 3

Row 0: 1 1 1
Row 1: 1 1 1
Row 2: 1 1 1

Enter Start cell (row col): 0 0
Enter Destination cell (row col): 2 2
```

### Output

```text
Found!
column: 0 1 2
-----

row 0:  X 1 1
row 1:  1 X 1
row 2:  1 1 X

Path:(0, 0) --> (1, 1) --> (2, 2)
```

### Result

```text
PASS
```

The algorithm uses diagonal movement to find the shortest path.

---

## Test Case 3: Start and Destination Are the Same

### Input

```text
Enter number of rows: 3
Enter number of columns: 3

Row 0: 1 1 1
Row 1: 1 1 1
Row 2: 1 1 1

Enter Start cell (row col): 1 1
Enter Destination cell (row col): 1 1
```

### Output

```text
Found!
Path:(1, 1)
```

### Result

```text
PASS
```

The program correctly identifies that no movement is required.

---

## Test Case 4: Blocked Starting Cell

### Input

```text
Enter number of rows: 3
Enter number of columns: 3

Row 0: 0 1 1
Row 1: 1 1 1
Row 2: 1 1 1

Enter Start cell (row col): 0 0
```

### Output

```text
Error: Please enter a coordinate that is not blocked
```

### Result

```text
PASS
```

The program rejects the blocked starting coordinate and asks for another coordinate.

---

## Test Case 5: Blocked Destination Cell

### Input

```text
Enter number of rows: 3
Enter number of columns: 3

Row 0: 1 1 1
Row 1: 1 1 1
Row 2: 1 1 0

Enter Start cell (row col): 0 0
Enter Destination cell (row col): 2 2
```

### Output

```text
Calculating path...

end cell is blocked
```

### Result

```text
PASS
```

The program detects that the destination cell is blocked and stops the search.

---

## Test Case 6: No Valid Path

### Input

```text
Enter number of rows: 5
Enter number of columns: 5

Row 0: 1 1 1 1 1
Row 1: 0 0 0 0 0
Row 2: 1 1 1 1 1
Row 3: 1 1 1 1 1
Row 4: 1 1 1 1 1

Enter Start cell (row col): 0 0
Enter Destination cell (row col): 4 4
```

### Output

```text
column: 0 1 2 3 4
-------------------

row 0:  X X X X X
row 1:  0 0 0 0 0
row 2:  1 1 1 1 1
row 3:  1 1 1 1 1
row 4:  1 1 1 1 1

there is no valid path from start to destination
```

### Result

```text
PASS
```

The algorithm explores all reachable cells and correctly reports that the destination cannot be reached.

---

## Test Case 7: Invalid Coordinates

### Input

```text
Enter number of rows: 5
Enter number of columns: 5

Enter Start cell (row col): 6 2
```

### Output

```text
Error: Please enter a valid coordinate
```

### Result

```text
PASS
```

The program rejects coordinates that are outside the grid boundaries.

---

## Strengths

| Strength | Description |
|---|---|
| Finds the shortest valid path using A* | The algorithm combines actual and estimated distances to guide the search efficiently. |
| Supports eight movement directions | The program can move horizontally, vertically, and diagonally. |
| Avoids blocked cells | Blocked cells are skipped and cannot become part of the path. |
| Validates important user inputs | The program checks dimensions, coordinates, and blocked starting or destination cells. |
| Displays the path clearly | The result is shown visually using `X` and as a coordinate sequence. |

---

## Limitations

| Limitation | Description |
|---|---|
| Diagonal corner cutting is possible | The program may move diagonally between blocked side cells. |
| Regular lists are used | Searching the open and closed lists may become slower for large grids. |
| Duplicate open-list entries may occur | A neighbour can be added again when a shorter path is discovered. |
| Grid values are not strictly limited to `0` and `1` | Other numbers may be treated as open cells. |
| Non-integer input may cause an error | Letters, decimal values, or incomplete coordinate input may raise a `ValueError`. |

---

## Possible Improvements

- Use `heapq` as a priority queue for the open list
- Use a set for faster closed-list checking
- Prevent diagonal movement through blocked corners
- Restrict grid values to only `0` and `1`
- Add `try-except` blocks for invalid user input
- Prevent duplicate entries in the open list
- Use different symbols for the start and destination
- Add automated unit testing
- Add a graphical interface
- Allow the user to run multiple searches without restarting the program

---

## Conclusion

The A* Search Algorithm successfully finds the shortest valid path between a selected starting cell and destination cell. The program calculates movement and heuristic costs, checks neighbouring cells, avoids blocked areas, reconstructs the final path, and displays the result in both visual and coordinate formats.

The implementation demonstrates the use of heuristic search, two-dimensional grids, lists, sets, object attributes, input validation, path reconstruction, and testing with normal and edge cases.
