import sys
input = sys.stdin.readline

def get_binary_length(n: int) -> int:
    """获取数字的二进制长度"""
    return n.bit_length()

def solve_test_case(l: int, r: int) -> tuple[int, int, int]:
    """
    贪心解法：
    1. 找到l和r第一个不同的二进制位
    2. 在这一位上，构造三个数使异或和最大
    3. 其他位根据l,r的范围填充
    """
    # 如果范围太小，直接返回
    if r - l < 2:
        return (r, r-1, l)
        
    # 获取l和r的二进制长度
    max_bit = get_binary_length(r) - 1
    
    # 从高位到低位，找到第一个l和r不同的位
    diff_bit = -1
    same_prefix = 0
    for bit in range(max_bit, -1, -1):
        l_bit = (l >> bit) & 1
        r_bit = (r >> bit) & 1
        if l_bit != r_bit:
            diff_bit = bit
            break
        if l_bit == 1:  # 记录相同的高位前缀
            same_prefix |= (1 << bit)
    
    # 如果没有找到不同的位，说明l=r，返回保底方案
    if diff_bit == -1:
        return (r, r-1, l)
    
    # 构造三个数
    # num1: 相同前缀 + 1 + 全0
    # num2: 相同前缀 + 0 + 全1
    # num3: 相同前缀 + 1 + 全0 + 1（如果超出范围则改为 0 + 全1 + 0）
    
    # 构造掩码
    low_mask = (1 << diff_bit) - 1  # 低位全1
    
    # 构造第一个数：在不同位取1，低位取0
    num1 = same_prefix | (1 << diff_bit)
    
    # 构造第二个数：在不同位取0，低位取1
    num2 = same_prefix | low_mask
    
    # 尝试构造第三个数：在不同位取1，低位取0，但在某个低位取1
    if diff_bit > 0:
        num3 = same_prefix | (1 << diff_bit) | 1
        # 如果超出范围，改用另一种构造方式
        if num3 > r:
            num3 = same_prefix | (low_mask & ~1)  # 低位全1除了最低位
    else:
        # 如果diff_bit是0，使用备选方案
        num3 = same_prefix | (low_mask & ~1)
    
    # 确保所有数都在范围内
    if num1 > r or num2 < l or num3 < l or num3 > r:
        return (r, r-1, l)
    
    # 确保三个数互不相同
    if len(set([num1, num2, num3])) < 3:
        return (r, r-1, l)
    
    return (num1, num2, num3)

def main():
    # 读取测试用例数量
    t = int(input())
    
    # 处理每个测试用例
    for _ in range(t):
        # 读取l和r
        l, r = map(int, input().split())
        
        # 计算结果
        a, b, c = solve_test_case(l, r)
        
        # 输出结果
        sys.stdout.write(f"{a} {b} {c}\n")

        # # 计算异或结果
        # print((a^b)+(b^c)+(c^a))

if __name__ == "__main__":
    main() 