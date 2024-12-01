# Coin Change Problem

## 0. Change Comes From Within

This project tackles the classic coin change problem using dynamic programming and greedy algorithms. The goal is to find the minimum number of coins required to make up a given total amount using a list of coin denominations.

## Concepts Needed

### Greedy Algorithms
- **Understanding Greedy Algorithms**: Learn how greedy algorithms work and why they are suitable for the coin change problem.
- **Limitations of Greedy Algorithms**: Recognize scenarios where greedy algorithms might not provide the optimal solution.

### Dynamic Programming
- **Basic Principles**: Understand the principles of dynamic programming to solve optimization problems.
- **Overlapping Subproblems and Optimal Substructure**: Learn how these concepts apply to the coin change problem.

### Algorithmic Complexity
- **Time and Space Complexity**: Analyze the complexity of algorithms and strive for solutions with lower complexity to meet runtime constraints.

### Problem-Solving Strategies
- **Breaking Down Problems**: Divide the problem into smaller, manageable sub-problems.
- **Iterative vs Recursive Approaches**: Explore different approaches to dynamic programming.

### Python Programming
- **Manipulating Lists**: Use list comprehensions and other techniques to manipulate lists.
- **Efficient Functions**: Implement functions with efficient looping and conditional statements.

## Resources

### Python Official Documentation
- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html): for loops, if statements.

### GeeksforGeeks Articles
- [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
- [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

### YouTube Tutorials
- [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic): A visual and step-by-step explanation of the dynamic programming approach.

By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. Decide whether a greedy algorithm suffices for your particular set of coin denominations or if a dynamic programming approach is necessary to ensure correctness and efficiency. This project tests your algorithmic skills and reinforces the importance of choosing the right strategy based on problem constraints.

## Additional Resources
- Mock Technical Interview

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

### Tasks

#### 0. Change Comes From Within
**Mandatory**
- **Objective**: Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total amount.
- **Prototype**: `def makeChange(coins, total)`
- **Return**: Fewest number of coins needed to meet the total
  - If total is 0 or less, return 0
  - If total cannot be met by any number of coins you have, return -1
  - `coins` is a list of the values of the coins in your possession
  - The value of a coin will always be an integer greater than 0
  - You can assume you have an infinite number of each denomination of coin in the list
- **Evaluation**: Your solution’s runtime will be evaluated in this task
