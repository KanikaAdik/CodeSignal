"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
"""

def solution(inputArray):
    #inputArray = [3, 6, -2, -5, 7, 3]
    pd =[]
    for  i in range (len(inputArray)-1):
        pd.append(inputArray[i] * inputArray[i+1])
    print(pd)
    return (max(pd))



