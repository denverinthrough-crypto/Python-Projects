def grid_to_string(grid):
    """Conver 2D Sudoku grid to a single string."""
    return ''.join(str(cell) if cell != 0 else '.' for row in grid for cell in row)

def string_to_grid(s):
    """Convert string representation to 2D grid."""
    grid = []
    s = s.replace('\n', '').replace('','')
    for i in range(0, 81, 9):
        row = [int(c) if c.isdigit() and c != '0' else 0 for c in s[i:i+9]]
        grid.append(row)

    return grid

def print_grid(grid):
    """Pretty print Sudoku gird."""

    for i, row in enumerate(grid):
        print(" ".join(str(num) if num != 0 else '.' for num in row))
        if i % 3 == 2 and i != 8:
            print("-"*21)


#---------------------------
# Sudoku Solver (Backtrcking)
#---------------------------

def find_empty(grid):
    """Find an empty cell in the grid. Returns (row, col) or None if full."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    """Check if num can be placed at pos (row, col)."""
    row, col = pos

    # Check now
    if num in grid[row]:
        return False
    
    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num:
                return False
            
    return True

def solve(grid):
    """Solve the Sudoku using backtracking."""
    empty = find_empty(grid)
    if not empty:
        return True # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0 # Rest if not valid (backtrack)

    return False # Trigger backtracking

# --------------------------
# Example usage
# --------------------------
if __name__ == "__main__":
    sample_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Grid: ")
    print_grid(sample_grid)

    # Convert to string
    s = grid_to_string(sample_grid)
    print("\nConverted to string: ")
    print(s)

    # Convert back to grid
    grid_back = string_to_grid(s)
    print("\nConverted back to grid: ")
    print_grid(grid_back)

    # Solve the puzzle
    if solve(grid_back):
        print("\nSolved Sudoku: ")
        print_grid(grid_back)
    else:
        print("\nNo solution found!")
        