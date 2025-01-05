import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.ans = 0        # 区间内的最大便利度
        self.max_minus = float('-inf')  # ai-i的最大值
        self.min_minus = float('inf')   # ai-i的最小值
        self.max_plus = float('-inf')   # ai+i的最大值
        self.min_plus = float('inf')    # ai+i的最小值

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [Node() for _ in range(4 * n)]
    
    def merge(self, left: Node, right: Node) -> Node:
        """合并两个节点的信息"""
        res = Node()
        # 合并ai-i的信息
        res.max_minus = max(left.max_minus, right.max_minus)
        res.min_minus = min(left.min_minus, right.min_minus)
        # 合并ai+i的信息
        res.max_plus = max(left.max_plus, right.max_plus)
        res.min_plus = min(left.min_plus, right.min_plus)
        
        # 计算最大便利度：
        # 1. 左子区间的最大便利度
        # 2. 右子区间的最大便利度
        # 3. 右边最大值减左边最小值的情况
        # 4. 左边最大值减右边最小值的情况
        res.ans = max(
            left.ans,
            right.ans,
            right.max_minus - left.min_minus,  # 右边减左边(ai-i)
            left.max_plus - right.min_plus     # 左边减右边(ai+i)
        )
        return res
    
    def update(self, pos, val, node=0, node_l=0, node_r=None):
        if node_r is None:
            node_r = self.n - 1
        
        if node_l == node_r:
            # 叶子节点，直接更新值
            self.tree[node].max_minus = val - pos
            self.tree[node].min_minus = val - pos
            self.tree[node].max_plus = val + pos
            self.tree[node].min_plus = val + pos
            self.tree[node].ans = 0
            return
        
        mid = (node_l + node_r) // 2
        if pos <= mid:
            self.update(pos, val, 2*node+1, node_l, mid)
        else:
            self.update(pos, val, 2*node+2, mid+1, node_r)
        
        # 合并子节点的信息
        self.tree[node] = self.merge(self.tree[2*node+1], self.tree[2*node+2])

def solve_test_case():
    # 读取n和q
    n, q = map(int, input().split())
    
    # 读取初始尺码
    sizes = list(map(int, input().split()))
    
    # 初始化线段树
    tree = SegmentTree(n)
    
    # 填充线段树
    for i in range(n):
        tree.update(i, sizes[i])
    
    # 输出初始状态的最大便利度
    sys.stdout.write(f"{tree.tree[0].ans}\n")
    
    # 处理每次改变
    for _ in range(q):
        p, x = map(int, input().split())
        p -= 1
        sizes[p] = x
        tree.update(p, x)
        sys.stdout.write(f"{tree.tree[0].ans}\n")

def main():
    t = int(input())
    for _ in range(t):
        solve_test_case()

if __name__ == "__main__":
    main() 