"""
Problem: Find the first duplicate element in an array
Approach:
- Use a set to track elements already seen
- Traverse the array and check if an element exists in the set
- The first element found again is the duplicate

Time Complexity: O(n)
Space Complexity: O(n)
"""

lst=[1,2,3,4,5]
def duplicate(lst):
    if lst:
     return None
    duplicate_val=None
    seen=set()
    for num in lst:
        if num in seen:
            duplicate_val=num
            return duplicate_val
        seen.add(num)
    
print(duplicate(lst))
        