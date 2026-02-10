"""
Problem: Right rotate an array by one position
Approach:
- Store the last element
- Shift all elements one position to the right
- Place the last element at index 0

Time Complexity: O(n)
Space Complexity: O(1)
"""

lst=[1,2,3,4]
def right_rotate_one(lst):
    n=len(lst)
    if not lst or n==1:
        print("array is empty or not possible to rotate")
        return
    else:
        for i in range(-1,-n,-1):
            lst[i],lst[i-1]=lst[i-1],lst[i]
        print(lst)
right_rotate_one(lst)