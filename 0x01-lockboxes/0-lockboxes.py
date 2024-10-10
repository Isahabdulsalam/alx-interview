#!/usr/bin/python3
"""
This module contains a function that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is a list containing
                               keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is initially unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)

if __name__ == "__main__":
    # Example usage
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 2, 3], [4], [], [2, 3], [0]]
    print(canUnlockAll(boxes))  # Should print: False
