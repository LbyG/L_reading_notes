import heapq
from collections import defaultdict
import sys

def read_input():
    return sys.stdin.readline().strip()

def find_kth_max_weight(graph, n, a, b, k):
    # 使用优先队列存储路径
    # 每个元素为 (最小边权值, 当前顶点, 已访问顶点集合, 路径上的边权值列表)
    pq = []
    # 初始状态：从起点开始，最小边权值为无穷大
    start_state = (float('inf'), a, frozenset([a]), [])
    heapq.heappush(pq, (-float('inf'), start_state))
    
    # 记录已处理的状态，避免重复访问
    visited_states = set()
    
    while pq:
        _, (min_weight, curr, visited, weights) = heapq.heappop(pq)
        
        # 如果到达目标顶点且路径长度足够
        if curr == b and len(weights) >= k:
            # 对边权值排序并返回第k大的值
            sorted_weights = sorted(weights, reverse=True)
            return sorted_weights[k-1]
        
        state = (curr, min_weight, visited)
        if state in visited_states:
            continue
        visited_states.add(state)
        
        # 遍历所有相邻边
        for next_vertex, weight in graph[curr]:
            if next_vertex not in visited:
                new_visited = visited | {next_vertex}
                new_weights = weights + [weight]
                new_min_weight = min(min_weight, weight)
                new_state = (new_min_weight, next_vertex, new_visited, new_weights)
                # 使用负的最小边权值作为优先级，这样最大的路径会先被处理
                heapq.heappush(pq, (-new_min_weight, new_state))
    
    return -1  # 如果没有找到满足条件的路径

def solve():
    # 读取输入
    n, m, q = map(int, read_input().split())
    
    # 构建图
    graph = defaultdict(list)
    for _ in range(m):
        v, u, w = map(int, read_input().split())
        graph[v].append((u, w))
        graph[u].append((v, w))
    
    # 处理查询
    for _ in range(q):
        a, b, k = map(int, read_input().split())
        result = find_kth_max_weight(graph, n, a, b, k)
        print(result)

def main():
    t = int(read_input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main() 