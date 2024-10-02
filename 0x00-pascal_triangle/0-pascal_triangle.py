#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal’s triangle of n.
    
    Args:
        n (int): The number of rows in Pascal's triangle.
        
    Returns:
        list: A list of lists containing integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    res = []
    
    # Return empty list for non-positive input
    if n <= 0:
        return res
    
    for i in range(n):
        level = []
        C = 1
        
        for j in range(i + 1):
            level.append(C)
            C = C * (i - j) // (j + 1)  # Calculate next coefficient
        
        res.append(level)
    
    return res
