#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""
=======
"""          
>>>>>>> faa2a2d276d5eebc01eb45e6c31b0d2726131c02
=======
"""
>>>>>>> 9f112973edb7d6637a3cabd7f51822f21ee25db8
Calculates the minimum number of operations to achieve 'n' 'H' characters
"""


def minOperations(n):
<<<<<<< HEAD
<<<<<<< HEAD
    """
    The minimum number of operations needed to achieve 'n' 'H' characters

    Args:
        n (int): The target number of 'H' characters

    Returns:
        int: The minimum number of operations needed
    """
    if n <= 1:
        return 0
    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n / op)) + op
=======
    """           
=======
    """
>>>>>>> 9f112973edb7d6637a3cabd7f51822f21ee25db8
    The minimum number of operations needed to achieve 'n' 'H' characters

    Args:
        n (int): The target number of 'H' characters

    Returns:
        int: The minimum number of operations needed
    """
    if n <= 1:
        return 0
    for op in range(2, n + 1):
<<<<<<< HEAD
      if n % op == 0:
        return minOperations(int(n / op)) + op
>>>>>>> faa2a2d276d5eebc01eb45e6c31b0d2726131c02
=======
        if n % op == 0:
            return minOperations(int(n / op)) + op
>>>>>>> 9f112973edb7d6637a3cabd7f51822f21ee25db8