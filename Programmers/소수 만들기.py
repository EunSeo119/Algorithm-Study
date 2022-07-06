def solution(nums):
    result=[]
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                A=nums[i]+nums[j]+nums[k]
                no=0
                for z in range(2,A//2):
                    if A%z==0:
                        no+=1
                        break
                if no==0:
                    result.append(A)

    return len(result)
