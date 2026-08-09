# attributes of the cells
class cell:
    def __init__(self, a=0, b=0, blocked=False):
        self.a = a  # row
        self.b = b  # column
        self.pa = -1  # parent row
        self.pb = -1  # parent column

        self.g = float("inf")  # distance from start
        self.h = 0  # heuristic distance to end
        self.f = float("inf")  # total cost

        self.blocked = blocked


# to find distance to destination cell
def Heuristic(a, b):

    return ((a.a - b.a) ** 2 + (a.b - b.b) ** 2) ** 0.5


def Check_valid_positive_integer(value):

    if value <= 0:
        print("\nvalue cannot be 0 or less\n")
        return False

    else:
        return True


def Create_path(start_cell, current):

    # construct a path from the cells in the closed list
    path = []
    while current.pa != -1 and current.pb != -1:
        path.append((current.a, current.b))
        current = cells[current.pa][current.pb]

    path.append((start_cell.a, start_cell.b))
    path.reverse()

    # show path movement on grid
    col_header = " ".join(str(c) for c in range(cols))
    print(f"column: {col_header}")
    print("-" * (len(col_header) + 10))

    path_set = set(path)

    # replaces path walked with symbol x
    for r in range(rows):
        row_display = []
        for c in range(cols):
            # Check if this cell coordinate is part of the path
            if (r, c) in path_set:
                row_display.append("X")
            elif cells[r][c].blocked:
                row_display.append("0")  # Wall
            else:
                row_display.append("1")  # Open path

        row_str = " ".join(row_display)
        print(f"row {r}:  {row_str}")

    print("Path:" + " --> ".join(str(p) for p in path))
    return


def failed_path(closed_list):

    col_header = " ".join(str(c) for c in range(cols))
    print(f"column: {col_header}")
    print("-" * (len(col_header) + 10))

    path_set = set(closed_list)

    # replaces path walked with symbol x
    for r in range(rows):
        row_display = []
        for c in range(cols):
            # Check if this cell coordinate is part of the path
            if (r, c) in path_set:
                row_display.append("X")
            elif cells[r][c].blocked:
                row_display.append("0")  # Wall
            else:
                row_display.append("1")  # Open path

        row_str = " ".join(row_display)
        print(f"row {r}:  {row_str}")

    print("there is no valid path from start to destination")
    return


# main function
def A_star():

    start_cell = cells[start[0]][start[1]]
    end_cell = cells[dest[0]][dest[1]]

    # initialize lists
    open_list = []
    closed_list = []

    # start cell attribute values
    start_cell.g = 0
    start_cell.h = Heuristic(start_cell, end_cell)
    start_cell.f = start_cell.g + start_cell.h

    # insert start cell to open list
    open_list.append(start_cell)

    # loop till reach destination if there is valid path
    while open_list:

        # find the cell with the lowest 'f' cost
        current = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current.f:
                current = item
                current_index = index

        # Remove it from the open_list
        open_list.pop(current_index)

        # checks if current cell is in closed list
        if (current.a, current.b) in closed_list:
            continue

        # put the cells that are already used
        closed_list.append((current.a, current.b))

        # if current cell is at destination = end loop
        if current.a == end_cell.a and current.b == end_cell.b:
            print("Found!")
            Create_path(start_cell, end_cell)
            return

        # neighbour directions
        directions = [
            # 4 directions
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
            # 4 more directions, remove if you want
            ,
            (-1, -1),
            (1, -1),
            (-1, 1),
            (1, 1),
        ]

        # checks every direction from current cell
        for da, db in directions:

            na = current.a + da
            nb = current.b + db

            # cannot be less then row or column, cannot be more then the row or column
            if na < 0 or nb < 0 or na >= rows or nb >= cols:
                continue

            neighbour = cells[na][nb]

            # if already in closed list or is blocked
            if neighbour.blocked or (na, nb) in closed_list:
                continue

            new_g = current.g + Heuristic(current, neighbour)

            # changes neighbour into current based on distance from start
            if new_g < neighbour.g:

                neighbour.pa = current.a
                neighbour.pb = current.b

                neighbour.g = new_g
                neighbour.h = Heuristic(neighbour, end_cell)
                neighbour.f = neighbour.g + neighbour.h

                open_list.append(neighbour)

    # when no more items in open list
    if not open_list:
        failed_path(closed_list)


# Program start
# Get grid dimensions from user

while True:

    rows = int(input("Enter number of rows: "))

    if Check_valid_positive_integer(rows) == True:
        break

while True:

    cols = int(input("Enter number of columns: "))

    if Check_valid_positive_integer(cols) == True:
        break

# show grid layout (1 for unblocked, 0 for blocked)
print(
    f"\nEnter the grid row by row (use spaces between numbers, 1 for open path, 0 for wall)."
)
print(f"Example of row: 1 1 0 1 ...")

# Create a list that resembles a grid
cells = []
for r in range(rows):
    while True:
        row_input = list(map(int, input(f"Row {r}: ").strip().split()))

        if len(row_input) == cols:
            # val == 0 = True, means cell is blocked
            row_cells = [
                cell(r, c, blocked=(val == 0)) for c, val in enumerate(row_input)
            ]
            cells.append(row_cells)
            break
        else:
            print(f"Error: Please enter exactly {cols} numbers.")

# Get start and destination coordinates
while True:
    print("\nEnter coordinates separated by a space (e.g., 0 2)")
    print("*rows and columns start from 0")
    start_r, start_c = map(int, input("\nEnter Start cell (row col): ").split())
    start = [start_r, start_c]

    # only accepts valid integer inputs
    if start_r < 0 or start_r >= rows or start_c < 0 or start_c >= cols:
        print(f"\nError: Please enter a valid coordinate")

    elif (cells[start_r][start_c]).blocked == True:
        print(f"\nError: Please enter a coordinate that is not blocked")

    else:
        break

while True:
    dest_r, dest_c = map(int, input("Enter Destination cell (row col): ").split())

    # only accepts valid integer inputs
    if dest_r < 0 or dest_r >= rows or dest_c < 0 or dest_c >= cols:
        print(f"\nError: Please enter a valid coordinate")

    elif (cells[dest_r][dest_c]).blocked == True:
        print(f"\nError: Please enter a coordinate that is not blocked")

    else:
        dest = [dest_r, dest_c]
        break

# Run the algorithm
print("\nCalculating path...\n")
A_star()
