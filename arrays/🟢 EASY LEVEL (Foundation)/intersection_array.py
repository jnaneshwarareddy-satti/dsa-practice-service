"""
Problem: Find the intersection of two arrays
Approach:
- Convert the second array into a set for fast lookup
- Traverse the first array and check if each element exists in the set
- Add common elements to the result list
- Preserves the order of elements from the first array

Time Complexity: O(n + m)
Space Complexity: O(m)
"""

lst1=[1,2,3,4]
lst2=[4,3,5]
def intersection(lst1,lst2):
 if lst1 and lst2:
    result=[]
    seen=set(lst2)
    for i in lst1:
        if i in seen:
            result.append(i)
    return result
 else:
    return "one or both lists are empty"
print(intersection(lst1,lst2))
 