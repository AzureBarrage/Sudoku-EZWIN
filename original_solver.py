import time

def is_valid_move(grid, row, col, number):
    if number in grid[row]:  # Check row
        return False

    if number in [grid[r][col] for r in range(9)]:  # Check column
        return False

    # Check 3x3 box
    box_row, box_col = row - row % 3, col - col % 3
    for r in range(3):
        for c in range(3):
            if grid[box_row + r][box_col + c] == number:
                return False

    return True


def solve_sudoku(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False


grid = [[0, 4, 0, 6, 0, 1, 0, 0, 3],
        [3, 0, 1, 0, 2, 7, 5, 8, 0],
        [0, 0, 7, 8, 0, 0, 9, 0, 1],
        [7, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 9, 0, 6, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 5],
        [5, 0, 2, 0, 0, 8, 1, 0, 0],
        [0, 6, 9, 2, 4, 0, 8, 0, 7],
        [4, 0, 0, 3, 0, 9, 0, 5, 0]]

start_time = time.perf_counter()
if solve_sudoku(grid, row=0, col=0):
    end_time = time.perf_counter()
    print("Solution found:")
    for row in grid:
        print(' '.join(map(str, row)))
    print(f"\nTime taken: {end_time - start_time:.6f} seconds")
else:
    print("No solution for this Sudoku puzzle")
