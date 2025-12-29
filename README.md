# Sudoku Solver

This project contains Python implementations of a Sudoku solver, demonstrating the evolution from a basic backtracking algorithm to a highly optimized version using heuristic search and bitwise operations.

## Files

- `sudoku_solver.py`: The main solver script, featuring the latest optimizations (Bitmasking + MRV Heuristic).
- `original_solver.py`: The initial basic backtracking implementation. Kept for benchmarking and educational comparison.
- `improved_solver.py`: The development version of the optimized solver.

## Evolution & Improvements

The current solver (`sudoku_solver.py`) introduces significant performance optimizations over the original implementation (`original_solver.py`):

1.  **Bitmasking**:
    -   Replaced list-based lookups with bitmasks for tracking used numbers in rows, columns, and 3x3 boxes.
    -   Allows for O(1) constraint checking and updates.

2.  **Minimum Remaining Values (MRV) Heuristic**:
    -   Instead of solving cells in a fixed order (left-to-right, top-to-bottom), the solver now dynamically selects the empty cell with the fewest possible legal moves.
    -   This drastically reduces the search space by identifying bottlenecks early (fail-fast).

3.  **Class-Based Structure**:
    -   Refactored the code into a `SudokuSolver` class for better state management and encapsulation.

## Usage

You can run the main solver:

```bash
python sudoku_solver.py
```

To compare performance with the original baseline:

```bash
python original_solver.py
```

Both scripts include a sample Sudoku grid to solve and will output the solution along with the execution time.
