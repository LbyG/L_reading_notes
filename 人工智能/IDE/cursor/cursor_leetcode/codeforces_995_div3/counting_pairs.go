package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type BIT struct {
	tree []int
	size int
}

func NewBIT(size int) *BIT {
	return &BIT{
		tree: make([]int, size+1),
		size: size,
	}
}

func (b *BIT) add(idx, val int) {
	for idx <= b.size {
		b.tree[idx] += val
		idx += idx & (-idx)
	}
}

func (b *BIT) sum(idx int) int {
	total := 0
	for idx > 0 {
		total += b.tree[idx]
		idx -= idx & (-idx)
	}
	return total
}

func (b *BIT) sumRange(left, right int) int {
	if right < left {
		return 0
	}
	return b.sum(right) - b.sum(left-1)
}

func findIdx(values []int64, target int64) int {
	left, right := 0, len(values)-1
	result := 0
	for left <= right {
		mid := left + (right-left)/2
		if values[mid] <= target {
			result = mid + 1
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return result
}

func solveTestCase(n int, x, y int64, nums []int64) int {
	// 离散化处理
	values := make([]int64, 0)
	valueMap := make(map[int64]bool)
	for _, num := range nums {
		if !valueMap[num] {
			values = append(values, num)
			valueMap[num] = true
		}
	}
	sort.Slice(values, func(i, j int) bool {
		return values[i] < values[j]
	})

	// 创建值到索引的映射
	valueToIdx := make(map[int64]int)
	for i, val := range values {
		valueToIdx[val] = i + 1
	}

	// 计算原始序列的总和
	var total int64
	for _, num := range nums {
		total += num
	}
	count := 0

	// 使用树状数组维护前面的元素出现次数
	bit := NewBIT(len(values))

	// 从前往后遍历j
	for j := 0; j < n; j++ {
		// 对于每个位置j，计算移除j后的和
		sumWithoutJ := total - nums[j]

		// 计算需要查找的范围
		leftVal := sumWithoutJ - y
		rightVal := sumWithoutJ - x

		// 找到对应的索引范围
		leftIdx := findIdx(values, leftVal-1)  // 严格大于leftVal的第一个位置
		rightIdx := findIdx(values, rightVal)   // 小于等于rightVal的最后一个位置的下一个位置

		// 计算这个范围内的数的个数
		count += bit.sumRange(leftIdx+1, rightIdx)

		// 将当前数加入树状数组
		bit.add(valueToIdx[nums[j]], 1)
	}

	return count
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)

	for t > 0 {
		var n int
		var x, y int64
		fmt.Fscan(in, &n, &x, &y)

		nums := make([]int64, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(in, &nums[i])
		}

		result := solveTestCase(n, x, y, nums)
		fmt.Fprintln(out, result)

		t--
	}
} 