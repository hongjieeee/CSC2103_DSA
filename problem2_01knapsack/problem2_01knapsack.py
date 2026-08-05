"""0/1 Knapsack solver with a simple command-line interface."""


def knapsack_tabulation(capacity, val, wt):
    """Build the DP table. tab[i][w] = best value using first i items, capacity w."""
    n = len(val)
    tab = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if wt[i - 1] <= w:
                include_item = val[i - 1] + tab[i - 1][w - wt[i - 1]]
                exclude_item = tab[i - 1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i - 1][w]

    return tab


def find_chosen_items(tab, capacity, wt):
    """Walk backwards through the table to see which items were actually taken."""
    chosen = []
    w = capacity

    for i in range(len(wt), 0, -1):
        # If the value changed when item i became available, item i was used.
        if tab[i][w] != tab[i - 1][w]:
            chosen.append(i - 1)
            w -= wt[i - 1]

    chosen.reverse()
    return chosen


def print_table(tab):
    width = max(len(str(cell)) for row in tab for cell in row) + 2
    header = "".join(str(w).rjust(width) for w in range(len(tab[0])))
    print("     " + header)
    for i, row in enumerate(tab):
        label = f"i={i}".ljust(5)
        print(label + "".join(str(cell).rjust(width) for cell in row))


def ask_int(prompt, minimum=0):
    """Keep asking until we get a whole number that's >= minimum."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  That's not a whole number, try again.")
            continue

        if value < minimum:
            print(f"  Please enter a number of at least {minimum}.")
            continue

        return value


def ask_yes_no(prompt):
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  Please answer y or n.")


def main():
    print("=" * 40)
    print("  0/1 Knapsack Solver")
    print("=" * 40)

    capacity = ask_int("\nPlease add capacity: ", minimum=0)

    values = []
    weights = []
    item_number = 1

    while True:
        print(f"\n--- Item {item_number} ---")
        value = ask_int("Please add value: ", minimum=0)
        weight = ask_int("Please add weight: ", minimum=1)

        
        values.append(value)
        weights.append(weight)
        item_number += 1

        if not ask_yes_no("\nDo you want to add another item? (y/n): "):
            break

    tab = knapsack_tabulation(capacity, values, weights)
    best = tab[len(values)][capacity]
    chosen = find_chosen_items(tab, capacity, weights)

    
    print("\n" + "=" * 40)
    print("Results")
    print("=" * 40)
    print("DP Table")
    print_table(tab)
    print()
    print(f"Capacity: {capacity}")
    print(f"Items entered: {len(values)}")

    if chosen:
        print("\nItems to take:")
        for i in chosen:
            print(f"  Item {i + 1}: weight={weights[i]}, value={values[i]}")
        print(f"\nWeight used: {sum(weights[i] for i in chosen)} / {capacity}")
    else:
        print("\nNo items fit in the knapsack.")

    print(f"Maximum value in Knapsack = {best}")


if __name__ == "__main__":
    main()