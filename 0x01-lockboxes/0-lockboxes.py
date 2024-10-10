#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""

def canUnlockAll(boxes):
    visited = set()
    queue = [0]  # Start with the first box

    while queue:
        box_index = queue.pop(0)  # BFS: get the first box in the queue
        if box_index not in visited:
            visited.add(box_index)  # Mark this box as visited
            # Add new keys from this box to the queue
            for key in boxes[box_index]:
                if key < len(boxes) and key not in visited:
                    queue.append(key)

    return len(visited) == len(boxes)
