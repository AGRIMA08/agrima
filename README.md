# agrima
# Python Programming Portfolio

This repository showcases my Python programming skills through various algorithmic solutions, data processing scripts, game logic implementations, and object-oriented programming.

## About Me

Second year student with a passion for problem-solving and algorithm development. Experienced in Python programming,Java algorithms, data structures, algorithms, puzzle solving, and software design patterns.

## Projects Overview

### 1. CSV Data Processing & Error Detection (`CSV.py`)
- **Description:** Automated error detection system for educational data management
- **Features:**
  - Reads CSV files containing student and teacher data
  - Validates presence of teachers for all classes (6A-12C)
  - Identifies missing judges for grade levels
  - Generates comprehensive error reports
- **Technologies:** Python, CSV module
- **Use Case:** Quality assurance for educational management systems

### 2. Grid Expansion & Distance Calculator (`GRID1.py`)
- **Description:** Cosmic expansion simulation for astronomical calculations
- **Features:**
  - Expands 2D grid based on empty rows/columns (inspired by astronomical problems)
  - Calculates minimum and maximum distances between celestial objects (#)
  - Handles coordinate transformations after expansion
- **Technologies:** Python, Mathematical algorithms
- **Key Concepts:** 2D array manipulation, distance calculations, coordinate geometry

### 3. Maximum Square Detector (`GRID2.py`)
- **Description:** Dynamic programming solution to find largest square submatrix
- **Features:**
  - Identifies the largest square of 1s in a binary matrix
  - Returns both size and top-left coordinates of the square
  - Optimized O(n×m) time complexity using dynamic programming
- **Technologies:** Python, Dynamic Programming
- **Applications:** Image processing, pattern recognition, optimization problems

### 4. Library Management System (`OOPS.py`)
- **Description:** Object-oriented library book management system
- **Features:**
  - Complete book lifecycle management (check-out, renewal, return)
  - Borrower tracking and status monitoring
  - Renewal count tracking with validation
  - Interactive command-line interface
- **Technologies:** Python, Object-Oriented Programming
- **Key Concepts:** Classes, encapsulation, state management

### 5. Merge Sort Implementation (`SORTING.py`)
- **Description:** Efficient sorting algorithm with k-th element finder
- **Features:**
  - Recursive merge sort implementation
  - Finds k-th smallest element in array
  - O(n log n) time complexity
  - Clean, readable divide-and-conquer approach
- **Technologies:** Python, Algorithms
- **Applications:** Data sorting, order statistics, algorithm optimization

### 6. Sudoku Validator (`SUDOKU.py`)
- **Description:** Complete Sudoku puzzle validation system
- **Features:**
  - Validates 9x9 Sudoku grid completeness and correctness
  - Checks row, column, and 3x3 box constraints
  - Robust input validation with error handling
  - Returns True/False for valid/invalid puzzles
- **Technologies:** Python, Set operations, Input validation
- **Key Concepts:** Constraint satisfaction, data validation, mathematical logic

### 7. Tic-Tac-Toe Game Engine (`TICTACTOE.py`)
- **Description:** Advanced tic-tac-toe game state analyzer and move predictor  
- **Features:**
  - Validates game state integrity and move sequences
  - Detects winning conditions across rows, columns, and diagonals
  - Generates all possible winning scenarios from incomplete states
  - Handles complex game logic with state exploration
- **Technologies:** Python, Game Logic, Combinatorics
- **Key Concepts:** State validation, recursive exploration, set operations

## Technical Skills Demonstrated

### Programming Concepts
- **Object-Oriented Programming:** Class design, encapsulation, method implementation
- **Data Structures:** Arrays, lists, sets, tuples, matrices, 2D grids
- **Algorithms:** Sorting (merge sort), dynamic programming, recursive algorithms
- **File I/O:** CSV processing, file reading/writing operations
- **Game Logic:** State validation, rule enforcement, move generation

### Problem-Solving Approaches
- **Dynamic Programming:** Optimal substructure solutions (largest square problem)
- **Divide and Conquer:** Recursive problem decomposition (merge sort)
- **Constraint Satisfaction:** Sudoku validation, game rule checking
- **State Space Exploration:** Tic-tac-toe move generation
- **Data Validation:** Input sanitization and error detection

### Mathematical & Logical Skills
- **Coordinate Geometry:** Distance calculations, grid transformations
- **Combinatorics:** Game state enumeration, possibility counting
- **Set Theory:** Duplicate detection, constraint validation
- **Matrix Operations:** 2D array manipulation, pattern recognition

### Code Quality
- **Robust Error Handling:** Input validation and edge case management
- **Efficient Algorithms:** Optimized time and space complexity
- **Clean Architecture:** Readable, well-structured implementations
- **Comprehensive Testing:** Multiple scenario handling

## How to Run the Programs

### Prerequisites
```bash
python 3.x
```

### Running Individual Programs

**CSV Error Detection:**
```bash
python CSV.py
# Requires: generated_data.csv in the same directory
# Output: errors.txt with detected issues
```

**Grid Expansion Calculator:**
```bash
python GRID1.py
# Input: 10 lines of grid data via stdin
# Output: minimum and maximum distances
```

**Maximum Square Finder:**
```bash
python GRID2.py
# Input: matrix dimensions and binary matrix
# Output: largest square size and coordinates
```

**Library Management System:**
```bash
python OOPS.py
# Input: book title and author, then interactive commands
# Commands: check_out, renew, return, status?, etc.
```

**Merge Sort with K-th Element:**
```bash
python SORTING.py
# Input: array size, array elements, k value
# Output: k-th smallest element
```

**Sudoku Validator:**
```bash
python SUDOKU.py
# Input: 9x9 grid of numbers (1-9)
# Output: "True" if valid Sudoku, "False" otherwise
```

**Tic-Tac-Toe Game Engine:**
```bash
python TICTACTOE.py
# Input: 9 positions (X, O, or -1 for empty)
# Output: Number of possible winning scenarios
```

## Sample Input/Output Examples

### CSV Error Detection
```
Input: CSV with missing teachers/judges
Output: 
Class 6A: Error TEACHER not found.
Class 7: Error JUDGE not found.
```

### Maximum Square Detector
```
Input:
4 4
1 1 1 0
1 1 1 0
1 1 1 0
0 0 0 0

Output:
3
0 0
```

## Project Structure
```
portfolio/
├── README.md
├── CSV.py                    # Data processing & validation
├── GRID1.py                 # Grid expansion algorithms  
├── GRID2.py                 # Dynamic programming solution
├── OOPS.py                  # Object-oriented design
├── SORTING.py               # Sorting algorithms
├── SUDOKU.py                # Sudoku puzzle validator
├── TICTACTOE.py             # Tic-tac-toe game engine
└── sample_data/             # Test data files
    └── generated_data.csv
```

## Learning Outcomes

Through these projects, I have demonstrated proficiency in:
- **Algorithm Design:** Implementing efficient solutions for complex computational problems
- **Data Processing:** Handling CSV files, validation, and automated error detection  
- **Object-Oriented Design:** Creating maintainable, reusable code structures
- **Mathematical Programming:** Solving geometric, optimization, and logical puzzles
- **Game Development:** Implementing rule-based systems with comprehensive state validation
- **Puzzle Solving:** Creating validators for classic games (Sudoku, Tic-Tac-Toe)
- **Performance Optimization:** Writing efficient algorithms with optimal time complexity


---

*These projects showcase practical Python programming skills applicable to software development, data analysis, and algorithmic problem-solving roles.*
