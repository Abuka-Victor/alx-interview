#!/usr/bin/python3
"""
Lockboxes file
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    :param boxes:
    :return: True if box can be opened and false if not
    """
    all_keys = []
    for i in boxes:
        for j in i:
            if j:
                all_keys.append(j)
        print(all_keys)
        next_index = boxes.index(i) + 1
        print(f"The next index is: {next_index}")
        if next_index != 0 and next_index not in all_keys and next_index < len(boxes):
            return False
        print("end")
    return True
