import copy
from os import name

"""
a = {"name": "ray",
      "age": 25,
      "kid": ["1st_kid", "2nd_kid"],
      "relatives": {"name": "John", "name": "Doe"}}

print(a)
print(a["name"])
print(a["age"])
print(a["relatives"]["name"])
"""

"""
c = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "$id": "https://example.com/employee.schema.json",
    "title": "Record of employee",
    "description": "This document records the details of an employee",
    "type": "object",
    "properties": {
        "id": {
            "description": "A unique identifier for an employee",
            "type": "number"
        },
        "name": {
            "description": "Full name of the employee",
            "type": "string"
        },
        "age": {
            "description": "Age of the employee",
            "type": "number"
        },
        "hobbies": {
            "description": "Hobbies of the employee",
            "type": "object",
            "properties": {
                "indoor": {
                    "type": "array",
                    "items": {
                        "description": "List of indoor hobbies",
                        "type": "string"
                    }
                },
                "outdoor": {
                    "type": "array",
                    "items": {
                        "description": "List of outdoor hobbies",
                        "type": "string"
                    }
                }
            }
        }
    }
}

print(c['properties']['hobbies']['properties']['outdoor']['items']['description'])
"""

"""
while True:
    num = input("Enter a number: ")
    if num < 0:
        print("Negative number entered. Exiting the loop.")
        break
    if num == 2 or num == 1:
        print("Yes Prime")
    elif num == 0:
        print("Not Prime")
    else:
        is_prime = True
        for i in range(1 , num):
            if num % i == 0:
                print("Not Prime")
                is_prime = False
                break
            if is_prime:
                print("Yes Prime")
"""

"""
def grades():
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")

print(grades())
"""

def min_path_sum_recursive(grid):
    rows,cols = len(grid[0])


# base case: if we reach the bottom-right cell, return its value
    if rows == 1 and cols == 1:
        return grid[0][0]

# if we go out of bounds 
    if rows <= 0 or cols <= 0:
        return float('inf')

    # recursively calculate the minimum path sum from the current cell
    right = min_path_sum_recursive([row[1:] for row in grid])
    down = min_path_sum_recursive(grid[1:])

    return grid[0][0] + min(right, down)

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(min_path_sum_recursive(grid))  