import time

class SudokuSolver:
    def __init__(self, grid):
        self.grid = [row[:] for row in grid]
        self.rows = [0] * 9
        self.cols = [0] * 9
        self.boxes = [0] * 9
        
        # Initialize bitmasks
        for r in range(9):
            for c in range(9):
                val = self.grid[r][c]
                if val != 0:
                    mask = 1 << (val - 1)
                    self.rows[r] |= mask
                    self.cols[c] |= mask
                    box_idx = (r // 3) * 3 + (c // 3)
                    self.boxes[box_idx] |= mask

    def get_options(self, r, c):
        # Returns a bitmask of available options for cell (r, c)
        box_idx = (r // 3) * 3 + (c // 3)
        used = self.rows[r] | self.cols[c] | self.boxes[box_idx]
        # Invert used mask, keep only first 9 bits
        return ~used & 0x1FF

    def count_set_bits(self, n):
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

    def find_best_empty_cell(self):
        # MRV Heuristic: Find empty cell with fewest options
        min_options = 10
        best_cell = None
        
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    options = self.get_options(r, c)
                    count = self.count_set_bits(options)
                    if count == 0:
                        return (-1, -1) # Dead end
                    if count < min_options:
                        min_options = count
                        best_cell = (r, c)
                        if count == 1: # Can't do better than 1
                            return best_cell
        return best_cell

    def solve(self):
        cell = self.find_best_empty_cell()
        if cell is None:
            return True # No empty cells left, puzzle solved
        
        r, c = cell
        if r == -1:
            return False # Dead end found
            
        options = self.get_options(r, c)
        
        # Try numbers 1-9
        for num in range(1, 10):
            mask = 1 << (num - 1)
            if options & mask:
                # Place number
                self.grid[r][c] = num
                self.rows[r] |= mask
                self.cols[c] |= mask
                box_idx = (r // 3) * 3 + (c // 3)
                self.boxes[box_idx] |= mask
                
                if self.solve():
                    return True
                
                # Backtrack
                self.grid[r][c] = 0
                self.rows[r] &= ~mask
                self.cols[c] &= ~mask
                self.boxes[box_idx] &= ~mask
                
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

solver = SudokuSolver(grid)

start_time = time.perf_counter()
if solver.solve():
    end_time = time.perf_counter()
    print("Solution found:")
    for row in solver.grid:
        print(' '.join(map(str, row)))
    print(f"\nTime taken: {end_time - start_time:.6f} seconds")
else:
    print("No solution for this Sudoku puzzle")
