"""
New years day chaos

- each person wears a sticker indicating initial position in the queue from 1 to n
- any person can bribe the person directly in front (current -> prev) but still wear
original sticker
- one person can bribe at most 2 times (current -> prev) 
- determine min number of bribes it took place to get to a given queue order

eg.

q = [1,2,3,4,5,6,7,8] -> q = [1,2,3,5,4,6,7,8]
q = [1,2,5,3,4,6,7,8]
if person 5 bribes person 4
only 1 bribe is required print 1

q = [1,2,3,4] - > bribed: [4,1,2,3]
person 4 bribed 3 times print too chaotic


q = [1,2,3,4,5,6,7,8,9] -> q = [1,3,2,4,7,5,6,8,9]

current[0] - next [1] = 2
-> current -> current[2]

R[7] - R[6] = 2
arr[R] - arr[R-1] = 2

"""
from typing import List


# keep track of how many bribes
bribes = 0


def minimumBribes(q: List[int]) -> None:

    bribes: int = 0
    # 1,2,3,5,4

    for i in range(len(q)):

        # account for element moved more then 2 indexes
        if q[i] - (i + 1) > 2:
            return "Too chaotic"

        # account for at most two bribes for current element
        # start from 2 previous from current to allow for at most 2 bribes
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes +=1

    # total bribes occured within max limit of 2 per person
    return bribes


if __name__ == "__main__":

    test_cases: List[List[int]] = [
        [1, 2, 3, 5, 4, 6, 7, 8],  [1,3,2,4,7,5,6,8,9], [4,3,2,1], [4]
        ]

    for q in test_cases:
        print(f"bribes: {minimumBribes(q)}")