"""
Problem: Maximum Subarray Sum (Kadane’s Algorithm)

Approach:
- Traverse the array once while maintaining two variables:
    1. current_sum → Maximum subarray sum ending at current index
    2. max_sum → Maximum subarray sum found so far
- At each element, decide whether to:
    • Start a new subarray from the current element
    • Or extend the previous subarray
- Update max_sum whenever current_sum becomes larger

Time Complexity: O(n)
Space Complexity: O(1)
"""

#brute force approach
'''lst=[-2,1,-3,4]
n=len(lst)
max_value=lst[0]
for i in range (n):
    sum_value=0
    for j in range(i,n):
        sum_value+=lst[j]
        if sum_value>max_value:
            max_value=sum_value
print(max_value)'''
lst=[-2,1,-3,4]
def max_sum(lst):
    if not lst:
        return
    n=len(lst)
    max_val=lst[0]
    current_sum=lst[0]
    for i in range(1,n):
        current_sum=max(lst[i],current_sum+lst[i])
        max_val=max(current_sum,max_val)
    return max_val
print(max_sum(lst))
