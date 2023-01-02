#!/usr/bin/python3
"""
Pascal Triangle exercise file
"""

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def pascal_triangle(n):
    result = []
    if n > 0:
        for i in range(n):
            new_list = []
            for j in range(i+1):
                new_list.append(int((fact(i)/(fact(i-j)*fact(j)))))
            result.append(new_list)

    return result
