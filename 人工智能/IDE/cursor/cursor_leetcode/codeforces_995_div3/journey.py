import sys
input = sys.stdin.readline

def solve_test_case(n: int, a: int, b: int, c: int) -> int:
    # 每三天的循环中能走的总距离
    cycle_distance = a + b + c
    
    # 完整的循环次数
    complete_cycles = (n - 1) // cycle_distance
    
    # 剩余需要走的距离
    remaining = n - complete_cycles * cycle_distance
    
    # 已经走过的天数（完整循环）
    days = complete_cycles * 3
    
    # 处理剩余距离
    if remaining <= 0:
        return days
    
    current_distance = 0
    distances = [a, b, c]  # 每天可以走的距离
    
    # 一天一天地走，直到达到目标
    for i in range(3):
        current_distance += distances[i]
        if current_distance >= remaining:
            return days + i + 1
            
    return days + 3

def main():
    # 为了加快输入输出速度
    input_lines = sys.stdin.read().strip().split('\n')
    pos = 0
    
    # 读取测试用例数量
    t = int(input_lines[pos])
    pos += 1
    
    # 处理每个测试用例
    for _ in range(t):
        n, a, b, c = map(int, input_lines[pos].split())
        pos += 1
        
        # 计算并输出结果
        result = solve_test_case(n, a, b, c)
        sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    main() 