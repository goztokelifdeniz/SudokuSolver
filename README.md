# Sudoku Step-by-Step Solver

## Description
This project is a Python program that solves a given Sudoku puzzle step by step and prints each step in a structured format. It follows a naive brute-force approach to determine the correct numbers for empty cells in a logical manner.

## Usage
To execute the program, run the following command:
```sh
python3 sudoku.py input.txt output.txt
```
- `input.txt`: The file containing the initial Sudoku board.
- `output.txt`: The file where the solution steps will be saved.

## Input Format
- The input consists of a 9×9 grid.
- Each number (1-9) represents a filled cell.
- Empty cells are represented by 0.
- Numbers are separated by spaces.

### Example Input:
```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## Output Format
- Each step is structured as follows:
  ```
  ------------------
  Step <SN> - <VAL> @ R<ROW>C<COL>
  ------------------
  ```
- After each step, the updated Sudoku grid is displayed.

### Example Output:
```
------------------
Step 1 - 4 @ R1C3
------------------
5 3 4 0 7 0 0 0 0
...
```

## Solution Approach
- The program selects the first available empty cell (topmost, leftmost).
- It determines the valid number for the cell based on Sudoku rules.
- The process repeats until the grid is completely filled.

## Requirements
- Python 3.6.8
