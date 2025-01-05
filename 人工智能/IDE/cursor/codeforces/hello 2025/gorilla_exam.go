package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func solveTestCase(n, k int, arr []int) int {
	// 如果可以替换n-1个或更多元素，可以让所有数相同
	if k >= n-1 {
		return 1
	}

	// 统计每个数字出现的次数
	counter := make(map[int]int)
	for _, num := range arr {
		counter[num]++
	}

	// 将出现次数收集到切片中并排序
	freq := make([]int, 0, len(counter))
	for _, count := range counter {
		freq = append(freq, count)
	}
	sort.Ints(freq)

	// 从出现次数最少的开始，尽可能将它们变成出现次数最多的数
	remainingChanges := k
	distinctNums := len(freq) // 不同数字的个数

	// 从出现次数最少的数开始处理
	for i := 0; i < len(freq) && remainingChanges > 0; i++ {
		if remainingChanges >= freq[i] {
			// 可以完全改变这个数字
			remainingChanges -= freq[i]
			distinctNums--
		} else {
			// 不能完全改变这个数字，停止处理
			break
		}
	}

	if distinctNums < 1 {
		return 1
	}
	return distinctNums
}

func main() {
	// 设置快速I/O
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	// 读取测试用例数量
	var t int
	fmt.Fscan(reader, &t)

	// 处理每个测试用例
	for i := 0; i < t; i++ {
		// 读取n和k
		var n, k int
		fmt.Fscan(reader, &n, &k)

		// 读取数组
		arr := make([]int, n)
		for j := 0; j < n; j++ {
			fmt.Fscan(reader, &arr[j])
		}

		// 计算并输出结果
		result := solveTestCase(n, k, arr)
		fmt.Fprintln(writer, result)
	}
} 