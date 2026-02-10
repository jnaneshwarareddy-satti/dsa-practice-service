"""
Problem: Count the frequency of each element in an array
Approach:
- Use a dictionary to store element counts
- Traverse the array and update the frequency of each element

Time Complexity: O(n)
Space Complexity: O(n)
"""

lst=[1,1,2,2,3,4,5,5]
if lst:
 freq={}
 for num in lst:
    freq[num]=freq.get(num,0)+1
 print(freq)
else:
  print("list is empty")