import sys
input = sys.stdin.readline

def solve_test_case(n: int, m: int, k: int, missing_nums: list, known_answers: list) -> str:
    # 将已知答案转换为集合
    known = set(known_answers)
    
    # 计算未知答案的题目数量
    unknown_count = n - len(known)
    
    # 情况1：所有题目都知道答案
    if unknown_count == 0:
        return '1' * m
        
    # 情况2：只有一道题不知道答案
    if unknown_count == 1:
        unknown_question = set(range(1, n+1)) - known
        unknown_question = unknown_question.pop()  # 获取唯一的未知题目编号
        return ''.join('1' if missing == unknown_question else '0' for missing in missing_nums)
        
    # 情况3：有两道或更多题不知道答案
    return '0' * m

def main():
    # 为了加快输入输出速度
    input_lines = sys.stdin.read().strip().split('\n')
    pos = 0
    
    # 读取测试用例数量
    t = int(input_lines[pos])
    pos += 1
    
    # 处理每个测试用例
    for _ in range(t):
        # 读取n, m, k
        n, m, k = map(int, input_lines[pos].split())
        pos += 1
        
        # 读取缺失的问题编号
        missing_nums = list(map(int, input_lines[pos].split()))
        pos += 1
        
        # 读取已知答案的问题编号
        known_answers = list(map(int, input_lines[pos].split()))
        pos += 1
        
        # 计算并输出结果
        result = solve_test_case(n, m, k, missing_nums, known_answers)
        sys.stdout.write(result + '\n')

if __name__ == "__main__":
    main() 