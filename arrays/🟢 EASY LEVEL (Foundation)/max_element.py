"""
Problem: Find the maximum element in an array
Approach: Linear traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""
lst=[1,2,3,7,5,8]
if lst:
 max_val=lst[0]
 for num in lst[1:]:
    if num>max_val:
        max_val=num
 print(max_val)
else:
    print("array is empty")
