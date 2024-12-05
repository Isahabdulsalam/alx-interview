# Island Perimeter Project

## Overview

This project, **Island Perimeter**, is part of the ALX software engineering program. The goal is to develop an algorithm to calculate the perimeter of a single island within a grid represented by a 2D array of integers. The project will test your understanding of 2D arrays, conditional logic, and Python programming skills.

## Concepts Needed

### 2D Arrays (Matrices)

- Accessing and iterating over elements in a 2D array.
- Navigating through adjacent cells (horizontally and vertically).

### Conditional Logic

- Applying conditions to determine whether a cell contributes to the perimeter of the island.

### Counting Techniques

- Developing a method to count the edges that contribute to the island’s perimeter.

### Problem-Solving Strategies

- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

### Python Programming

- Using nested loops for iterating over grid cells.
- Applying conditional statements to check the status of adjacent cells.

## Resources

### Python Official Documentation

- **Nested Lists**: Understanding how to work with lists within lists in Python.

### GeeksforGeeks Articles

- **Python Multi-dimensional Arrays**: A guide to working with 2D arrays in Python effectively.

### TutorialsPoint

- **Python Lists**: Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.

### YouTube Tutorials

- **Python 2D arrays and lists**

## Additional Resources

- **Mock Technical Interviews**

## Requirements

- **Editors Allowed**: vi, vim, emacs
- **Python Version**: Python 3.4.3 on Ubuntu 20.04 LTS
- **File Endings**: All files should end with a new line.
- **Shebang Line**: The first line of all your files should be exactly `#!/usr/bin/python3`.
- **Code Style**: Your code should use the PEP 8 style (version 1.7).
- **Module Import**: You are not allowed to import any module.
- **Documentation**: All modules and functions must be documented.
- **File Executability**: All your files must be executable.

## Task

### 0. Island Perimeter

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of lists of integers:
  - `0` represents water
  - `1` represents land
- Each cell is square, with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- `grid` is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
