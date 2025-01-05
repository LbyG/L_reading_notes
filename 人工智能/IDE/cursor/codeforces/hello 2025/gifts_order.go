package main

import (
	"bufio"
	"fmt"
	"os"
)

// Node 表示线段树的节点
type Node struct {
	ans      int64 // 区间内的最大便利度
	maxMinus int64 // ai-i的最大值
	minMinus int64 // ai-i的最小值
	maxPlus  int64 // ai+i的最大值
	minPlus  int64 // ai+i的最小值
}

// SegmentTree 表示线段树
type SegmentTree struct {
	n    int
	tree []Node
}

// NewSegmentTree 创建一个新的线段树
func NewSegmentTree(n int) *SegmentTree {
	return &SegmentTree{
		n:    n,
		tree: make([]Node, 4*n),
	}
}

// merge 合并两个节点的信息
func (st *SegmentTree) merge(left, right Node) Node {
	res := Node{
		maxMinus: max(left.maxMinus, right.maxMinus),
		minMinus: min(left.minMinus, right.minMinus),
		maxPlus:  max(left.maxPlus, right.maxPlus),
		minPlus:  min(left.minPlus, right.minPlus),
	}

	// 计算最大便利度
	res.ans = max(
		max(left.ans, right.ans),
		max(
			right.maxMinus-left.minMinus, // 右边减左边(ai-i)
			left.maxPlus-right.minPlus,   // 左边减右边(ai+i)
		),
	)
	return res
}

// update 更新线段树中的值
func (st *SegmentTree) update(pos int, val int64, node int, nodeL int, nodeR int) {
	if nodeL == nodeR {
		// 叶子节点，直接更新值
		posInt64 := int64(pos)
		st.tree[node].maxMinus = val - posInt64
		st.tree[node].minMinus = val - posInt64
		st.tree[node].maxPlus = val + posInt64
		st.tree[node].minPlus = val + posInt64
		st.tree[node].ans = 0
		return
	}

	mid := (nodeL + nodeR) / 2
	if pos <= mid {
		st.update(pos, val, 2*node+1, nodeL, mid)
	} else {
		st.update(pos, val, 2*node+2, mid+1, nodeR)
	}

	// 合并子节点的信息
	st.tree[node] = st.merge(st.tree[2*node+1], st.tree[2*node+2])
}

// Update 对外的更新接口
func (st *SegmentTree) Update(pos int, val int64) {
	st.update(pos, val, 0, 0, st.n-1)
}

func solveTestCase(reader *bufio.Reader, writer *bufio.Writer) {
	// 读取n和q
	var n, q int
	fmt.Fscan(reader, &n, &q)

	// 读取初始尺码
	sizes := make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &sizes[i])
	}

	// 初始化线段树
	tree := NewSegmentTree(n)

	// 填充线段树
	for i := 0; i < n; i++ {
		tree.Update(i, sizes[i])
	}

	// 输出初始状态的最大便利度
	fmt.Fprintln(writer, tree.tree[0].ans)

	// 处理每次改变
	for i := 0; i < q; i++ {
		var p int
		var x int64
		fmt.Fscan(reader, &p, &x)
		p--
		sizes[p] = x
		tree.Update(p, x)
		fmt.Fprintln(writer, tree.tree[0].ans)
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var t int
	fmt.Fscan(reader, &t)

	for i := 0; i < t; i++ {
		solveTestCase(reader, writer)
	}
}

// 辅助函数：返回两个int64中的最大值
func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

// 辅助函数：返回两个int64中的最小值
func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
} 