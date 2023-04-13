n,s = map(int,input().split())
nums = list(map(int,input().split()))
prefixSum = [ 0 for _ in range(n+1)]
if sum(nums)<s:
    print(0)
    exit()
for i in range(0,n):
    prefixSum[i+1] += nums[i] + prefixSum[i]
answer = 0
#print(prefixSum)
mid = n//2
left = 0
right = n+1
while left + 1 < right:
    #print(left,right,mid)
    mid = (left+right)//2
    isPosiblle = False
    for i in range(mid,n+1):
        #print(prefixSum[i] - prefixSum[i-mid])
        tmpSum = prefixSum[i] - prefixSum[i-mid]
        if tmpSum >= s:
            isPosiblle = True
            break
    if isPosiblle:
        right = mid 
        answer = mid
    else:
        left = mid 
print(answer)
'''
10 11
1 1 1 1 1 1 1 1 1 1
'''
