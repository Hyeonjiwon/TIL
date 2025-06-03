import sys
# 평범한 배낭

result = -100000
flag = False

def dfs(L, weight_sum, value_sum, wl, vl):
    # print(L , ": ", weight_sum[L], value_sum[L])
    print(L, weight_sum, value_sum)
    
    if weight_sum > k: 
        print("111")
        return False # 무게가 k 보다 큰 경우 함수 종료
    if L==n:
        # 완성된 부분집합의 weight_sum 의 최대값을 찾아야 함
        result = max(result, value_sum)
        print("222", result)
    else:
        print("333")
        dfs(L + 1, weight_sum + wl[L], value_sum + vl[L], wl, vl) # 물건 넣는 경우 
        dfs(L + 1, weight_sum, value_sum, wl, vl) # 물건 안넣는 경우
        # 물건을 담는 조합 경우의 부분집합 하나 완성  -> 누적해서 sum 완성
        

n, k =  map(int, sys.stdin.readline().split())
weight_list = []
value_list = []
for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    weight_list.append(weight)
    value_list.append(value)

result = 0    
dfs(0, 0, 0, weight_list, value_list)
print(result)