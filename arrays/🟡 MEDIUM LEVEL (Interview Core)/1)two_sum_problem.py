"""
Problem: Two Sum
Approach:
- Traverse the array once
- For each element, check if (target - element) exists in a hashmap
- If found, return the indices
- Insert the current element into the hashmap only after checking

Time Complexity: O(n)
Space Complexity: O(n)
"""

lst=[2,2]
target=4
def two_sum(lst,target):
    if not lst:
        return []
    n=len(lst)
    hashmap={}
    for i,key in enumerate(lst):
        if target-key in hashmap:
            return [hashmap[target-key],i]
        hashmap[key]=i
        
   
print(two_sum(lst,target))


