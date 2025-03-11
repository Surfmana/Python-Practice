# 区间 DP, 前缀和
# 题干用人话就是 “只可以进行一次区间反转，统计反转后整体数组 ai == bi 的数量，输出全部可能数量的 cnt”
# 用区间 DP 维护修改：反转 [l, r] 区间内的匹配数量
# 用前缀和维护区间外原本的匹配数量
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = [0] * (n + 1)
dp = [[0] * n for _ in range(n)]
# 前缀和
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + (1 if a[i] == b[i] else 0)

sum_base = prefix[-1]

# 初始化：区间 DP
for i in range(n):
    dp[i][i] = 1 if a[i] == b[i] else 0
    ans[sum_base] += 1

# 区间 DP 的外层 len 递增，内层 ij 维护
for length in range(2, n + 1):
    for j in range(length - 1, n):
        i = j - length + 1
        dp[i][j] = (dp[i + 1][j - 1] +
                    (1 if a[i] == b[j] else 0) +
                    (1 if a[j] == b[i] else 0))
        # 最终数量是：区间内数量 + 原本总数量 - 区间内原本数量
        ans[dp[i][j] + sum_base - (prefix[j + 1] - prefix[i])] += 1
for out in ans:
    print(out)
