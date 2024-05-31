"""
Given n non-negative integers where each integer represetns the hiegh of a vertical line on a chat
- find two lines which together with x - axis forms a container, that holds the most amount of water
- return the area of that water

eg.
        0  1  2  3  4  5  6  7  8
arr = [ 1, 8, 6, 2, 5, 4, 8, 3, 7]

area = width * Length

length = difference of two indexes that will be the miiddle part of the container
width = the max height without overflowing the container

Left index = 1 value: 8
Right index = 8 value = 7

length = 8 - 1 = 7
width = 7 since left index is 8 and right is 7 we cannot exceed 7 or else it will overflow

"""

from typing import List



def two_pointers(arr: List[int]) -> int:
    """ two pointer approach that finds all possibilities """
    L: int= 0
    R: int = L + 1

    max_area : int = 0

    while L < len(arr) -1:

        this_area: int = min(arr[L], arr[R]) * abs(L - R)
        # update max area
        max_area: int = max(max_area, this_area)

        # move R to the right
        R +=1
        # once R hits the end of the array Move L to the right onec and reset R to be one ahead of L
        if  R == len(arr):
            L += 1
            R = L + 1

    return max_area


def two_pointer_2(arr: List[int]) -> int:
    """ two pointer approach that will have less iterations """
    L: int= 0
    R: int = len(arr) -1

    max_area : int = 0

    while (L < R):
        # area = length * height
        this_area: int = min(arr[L], arr[R]) * (R - L)
        max_area: int = max(max_area, this_area)

        """ find the biggest element in arr
        L will continue to move Right until its bigger than R
        goal is to find the biggest on left since it will hold the most area
        """
        if arr[L] < arr[R]:
            L += 1
        else:
            R -= 1
    return max_area

def brute_force(arr: List[int]) -> int:
    max_area = 0

    for p1 in range(len(arr)):
        for p2 in range(p1 + 1,len(arr)):
            this_area: int  = min(arr[p1], arr[p2]) * abs(p1 - p2)
            max_area: int = max(max_area, this_area)

    return max_area


if __name__ == "__main__":

    arr: List[int] = [ 1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(f"max area using two pointers: {two_pointers(arr)}")
    print(f"max area using two pointers method 2: {two_pointers(arr)}")
    print(f"max area using brute force {brute_force(arr)}")

