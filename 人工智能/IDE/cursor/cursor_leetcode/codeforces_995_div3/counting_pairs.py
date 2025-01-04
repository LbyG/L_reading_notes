import sys
input = sys.stdin.readline
 
class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def add(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)
    
    def sum(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total
    
    def sum_range(self, left, right):
        if right < left:
            return 0
        return self.sum(right) - self.sum(left - 1)
 
def find_idx(values, target):
    left, right = 0, len(values) - 1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if values[mid] <= target:
            result = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return result
 
def solve_test_case(n: int, x: int, y: int, nums: list) -> int:
    # 离散化处理
    values = sorted(set(nums))
    value_to_idx = {val: i + 1 for i, val in enumerate(values)}
    
    # 计算原始序列的总和
    total = sum(nums)
    count = 0
    
    # 使用树状数组维护前面的元素出现次数
    bit = BIT(len(values))
    
    # 从前往后遍历j
    for j in range(n):
        # 对于每个位置j，计算移除j后的和
        sum_without_j = total - nums[j]
        
        # 计算需要查找的范围
        # 如果移除i位置的数后，剩余和要在[x,y]范围内
        # sum_without_j - nums[i] ∈ [x,y]
        # nums[i] ∈ [sum_without_j-y, sum_without_j-x]
        left_val = sum_without_j - y
        right_val = sum_without_j - x
        
        # 找到对应的索引范围
        left_idx = find_idx(values, left_val - 1)  # 严格大于left_val的第一个位置
        right_idx = find_idx(values, right_val)    # 小于等于right_val的最后一个位置的下一个位置
        
        # 计算这个范围内的数的个数
        count += bit.sum_range(left_idx + 1, right_idx)
        
        # 将当前数加入树状数组
        bit.add(value_to_idx[nums[j]], 1)
    
    return count
 
def main():
    input_lines = sys.stdin.read().strip().split('\n')
    pos = 0
    
    t = int(input_lines[pos])
    pos += 1
    
    for _ in range(t):
        n, x, y = map(int, input_lines[pos].split())
        pos += 1
        nums = list(map(int, input_lines[pos].split()))
        pos += 1
        
        result = solve_test_case(n, x, y, nums)
        sys.stdout.write(str(result) + '\n')
 
if __name__ == "__main__":
    main() 