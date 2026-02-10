"""
Problem: Left rotate an array by one position
Approach:
- Iterate through the array
- Swap each element with the next element
- The first element moves to the last position

Time Complexity: O(n)
Space Complexity: O(1)
"""

lst=[1,2,3,4]
def left_rotate_one(lst):
 n=len(lst)
 if not lst or n==1:
    print("List is Empty or not possible to rotate")
    return
 else:
    for i in range(n-1):
        lst[i],lst[i+1]=lst[i+1],lst[i]
left_rotate_one(lst)
print(lst)