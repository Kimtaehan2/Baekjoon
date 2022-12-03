import sys
nums=[1,1,1]
result=[]
while sum(nums)!=0:
  nums=list(map(int,sys.stdin.readline().split()))
  nums.sort()
  if nums[0]**2+nums[1]**2==nums[2]**2:
    result.append('right')
  else: result.append('wrong')
result.pop()
print('\n'.join(result))