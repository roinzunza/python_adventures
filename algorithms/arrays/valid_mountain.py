""" 
Given an array determine if its a valid mountain.

It is a mountain if the array contains 3 elements or more
it is a mountain if the array starts increasing then has a subsequence that decreases

valid = [1,2,3,2]
invalid = [1]
invalid = [1,2,3,3]

first check if there are 3 or more elemenets

- iterate through the array to go through increasing sequenec and stop once you get to decreasing
- check that you havent went through the entire arr or that you have even moved through the array
- iterate through the decreasing sequence

"""
from typing import List

def is_mountain(arr: List[int]):
    """ time complexity
    
    both while loops O(N)

    space: O(1)
    """
    if len(arr) < 3:
        return False 

    L : int = 1

    # increasing sequence
    # iterates as long as current is greater than previus
    while  L < len(arr) and arr[L] > arr[L- 1]:
        L +=1

    # another case check
    # check that we have moved through arr or that we havent moved through entire array
    # this accounts if the array is only increasing
    if L == 1 or L == len(arr):
        return False
    
    # decreasing sequence
    # iterates through array as long as the current is smaller than previous
    while L < len(arr) and arr[L] < arr[L - 1]:
        L+=1

    # return as true if L gets to the end of the array
    return L==len(arr)



if __name__ == "__main__":
    arr =[1,2,3,2]
    print(is_mountain(arr))

