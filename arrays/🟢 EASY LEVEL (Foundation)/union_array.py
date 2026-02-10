"""
Problem: Find the union of two arrays
Approach:
- Traverse both arrays
- Use a set to track already seen elements
- Add elements to the result list only if they are not seen
- Preserves insertion order

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

lst1 = [1, 2, 3]
lst2 = [5, 3, 4]
def union_arrays(lst1, lst2):
 if lst1 and lst2:
    seen=set()
    result=[]
    for num in lst1+lst2:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
 else:
    return "Either lists are empty or one of the lists are empty"
print(union_arrays(lst1, lst2))