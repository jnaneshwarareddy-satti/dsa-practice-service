"""
Problem: Reverse an array in-place
Approach:
- Use two pointers: one from the start and one from the end
- Swap elements while moving pointers towards the center
- No extra space is used

Time Complexity: O(n)
Space Complexity: O(1)
"""

lst=[1,2,3,4]
if lst:
 right=-1
 for left in range (len(lst)//2):
    lst[left],lst[right]=lst[right],lst[left]
    right-=1
 print(lst)
else:
  print("lst is empty")

