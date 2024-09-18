"""
In the assembly line, the factory assembles three parts 'a' 'b' 'c' 
of a triangle toy. A valid toy is one where the two shorter sides 
added together are greater in length than the longest side.
There are two forms of valid triangles to identify.
- If 2 parts are of equal length, the form is 'Isosceles'
- If all 3 parts are of equal length, the form is 'Equilateral
If a toy is not valid or is not one of those 2 forms, 
it is 'None of these.
Example
triangleToy = ["221", "333", "345", "113"]
- First triangle valid Isoceles
- Second Triangel valid Equilateral
- Third is a valid triangle but not the specific form
- Fourth is not a valid triangle
"""

from typing import List


def toyTriangle(triangles:List[str]):
    res = []

    for triangle in triangles:
        a, b, c = triangle[0], triangle[1], triangle[2]

        if (a + b > c) and (a + c > b) and (b + c > a):
            if (a == b) and (b == c):
                res.append("Equilateral")
            elif (a == b) or (a == c) or (b == c):
                res.append("Isoceles")
            else:
                res.append("None of these")
        else:
            res.append("None of these")
    
    return res


#Test Case 
print("Test Case 1:", toyTriangle(["221", "333", "345", "113"]))






