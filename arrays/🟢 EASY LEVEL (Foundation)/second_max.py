"""
Problem: Find the second largest element in an array
Approach:
- Maintain two variables: max_val and second_max
- Traverse the array once and update both values accordingly
- Ignore duplicate values of the maximum element

Time Complexity: O(n)
Space Complexity: O(1)
"""
lst=[1,1]
if lst and len(lst)>1:
 second_max=None
 max_val=lst[0]
 for num in lst:
    if num>max_val:
        second_max=max_val
        max_val=num
 print(second_max)
else:
   print("Array is Empty")