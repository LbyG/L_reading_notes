import sys
input = sys.stdin.readline

def solve_test_case(n: int, m: int) -> int:
    """
    解决单个测试用例
    对于 n×m 的表格，返回最大可能的MEX和
    """
    return max(n, m) + 1

def main():
    # 读取测试用例数量
    t = int(input())
    
    # 处理每个测试用例
    for _ in range(t):
        # 读取每个测试用例的 n 和 m
        n, m = map(int, input().split())
        # 输出结果
        sys.stdout.write(f"{solve_test_case(n, m)}\n")

if __name__ == "__main__":
    main()