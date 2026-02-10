"""
Problem: Find the missing number in an array containing numbers from 1 to n
Approach:
- Use the sum of first n natural numbers formula
- Calculate expected sum and subtract the actual sum of the array
- The difference gives the missing number

Time Complexity: O(n)
Space Complexity: O(1)
"""

lst=[1,2,3,4,6]
def missing_element(lst):
    n=len(lst)+1
    sum_lst=sum(lst)
    sum_n_num=n*(n+1)//2
    missing_ele=sum_n_num-sum_lst
    return missing_ele
print(missing_element(lst))