import sys
input = sys.stdin.readline

def solve_test_case(n: int, a: list, b: list) -> int:
    # 从后往前考虑每一天是否训练
    # 如果在第i天训练，会得到a[i]分，但会导致Stereocarp在第i+1天得到b[i+1]分
    
    if n == 1:
        return a[0]  # 特殊情况，只有一天
    
    # 记录Monocarp和Stereocarp的得分
    mono_score = 0
    stereo_score = 0
    
    # 从后往前遍历
    for i in range(n-1, -1, -1):
        # 计算如果这天训练的收益
        gain = a[i]  # Monocarp在第i天训练获得的分数
        if i < n-1:
            # 如果不是最后一天，训练会导致Stereocarp在第i+1天训练
            cost = b[i+1]  # Stereocarp在第i+1天训练的得分
        else:
            cost = 0  # 最后一天训练没有代价
            
        # 如果收益大于等于代价，就在这天训练
        if gain >= cost:
            mono_score += gain
            if i < n-1:  # 如果不是最后一天
                stereo_score += b[i+1]  # Stereocarp在第i+1天的得分
            
    return mono_score - stereo_score

def main():
    # 为了加快输入输出速度
    input_lines = sys.stdin.read().strip().split('\n')
    pos = 0
    
    # 读取测试用例数量
    t = int(input_lines[pos])
    pos += 1
    
    # 处理每个测试用例
    for _ in range(t):
        n = int(input_lines[pos])
        pos += 1
        a = list(map(int, input_lines[pos].split()))
        pos += 1
        b = list(map(int, input_lines[pos].split()))
        pos += 1
        
        # 计算并输出结果
        result = solve_test_case(n, a, b)
        sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    main() 