N = int(input())
result = 0

for i in range(1, N+1):
    sample=i+sum(map(int, str(i)))
    if sample==N:
        result=i
        break

print(result)



# N=int(input())

# check=0
# result=[]

# for i in range(1,N):
#     sum=i
#     str_i=str(i)
#     for j in range(len(str_i)):
#         sum+=int(str_i[j])
#     if N==sum:
#         result.append(i)
#         check=1
#         break

# if check==0:
#     print(0)
# else:
#     print(min(result))
