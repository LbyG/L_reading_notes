import sys
from collections import Counter
input = sys.stdin.readline

def solve_test_case(n: int, k: int, arr: list) -> int:
    """
    解决单个测试用例
    返回经过最多k次替换操作后，能达到的f(a)的最小值
    
    贪心思路：
    1. 统计每个数字出现的次数
    2. 将出现次数较少的数字通过k次操作改成出现次数最多的数字
    3. 最后结果为剩余不同数字的个数
    """
    if k >= n - 1:
        return 1
        
    # 统计每个数字出现的次数
    counter = Counter(arr)
    
    # 按照出现次数从小到大排序
    freq = sorted(counter.values())
    
    # 从出现次数最少的开始，尽可能将它们变成出现次数最多的数
    remaining_changes = k
    distinct_nums = len(freq)  # 不同数字的个数
    
    # 从出现次数最少的数开始处理
    i = 0
    while i < len(freq) and remaining_changes > 0:
        if remaining_changes >= freq[i]:
            # 可以完全改变这个数字
            remaining_changes -= freq[i]
            distinct_nums -= 1
        else:
            # 不能完全改变这个数字，停止处理
            break
        i += 1
    
    return max(1, distinct_nums)

def main():
    # 读取测试用例数量
    t = int(input())
    
    # 处理每个测试用例
    for _ in range(t):
        # 读取n和k
        n, k = map(int, input().split())
        # 读取数组
        arr = list(map(int, input().split()))
        # 输出结果
        sys.stdout.write(f"{solve_test_case(n, k, arr)}\n")

if __name__ == "__main__":
    main() 