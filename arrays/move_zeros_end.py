"""
Problem: Move all zeros to the end of the array
Approach:
- First find the index of the first zero
- Traverse the remaining array
- Whenever a non-zero element is found, swap it with the zero position
- Increment the zero pointer after each swap

Time Complexity: O(n)
Space Complexity: O(1)
"""

lst=[0,1,0,3,12]
def move_zeros(lst):
 if lst:
  n=len(lst)
  i=0
  while i<n and lst[i]!=0:
    i+=1  
  for j in range(i+1,n):
    if lst[j]>0:
      lst[i],lst[j]=lst[j],lst[i]
      i+=1

  print(lst) 
 else:
    print("Array is empty")
move_zeros(lst)


