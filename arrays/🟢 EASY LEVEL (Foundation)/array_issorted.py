"""Problem: Check if an array is sorted in ascending order
Approach:
- Traverse the array and compare each element with the next one
- If any next element is smaller than the current, the array is not sorted
- If traversal completes without violation, the array is sorted

Time Complexity: O(n)
Space Complexity: O(1)
"""
lst=[1,2,7,4]

def is_sorted(lst):
 if lst:
  n=len(lst)
  for i in range(n-1):
    if lst[i+1]<lst[i]:
        return False
  return True
 else:
   return False

result = is_sorted(lst)
if result:
    print("array is sorted")
else:
    print("array is not sorted or Empty")
 
