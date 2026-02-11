lst=[1,2,-3,-4,5,6]
"""
Problem: Rearrange array in alternating positive and negative order

Approach:
- Separate positive and negative numbers into two lists
- Alternate elements depending on starting element
- Append remaining elements if counts are unequal

Time Complexity: O(n)
Space Complexity: O(n)
"""

def rearrange(lst):
    if not lst:
        return
    positive=[]
    negative=[]
    result=[]
    for num in lst:
        if num>0:
            positive.append(num)
        else:
            negative.append(num)
    #adding to result
    is_positive=lst[0]>0
        
    p_num=n_num=0
    while p_num<len(positive) and n_num<len(negative):
        if is_positive:
            result.append(positive[p_num])
            result.append(negative[n_num])
        else:
            result.append(negative[n_num])
            result.append(positive[p_num])
        p_num+=1
        n_num+=1
           
      # Add remaining elements
    result.extend(positive[p_num:])
    result.extend(negative[n_num:])
    return result
print(rearrange(lst))

                