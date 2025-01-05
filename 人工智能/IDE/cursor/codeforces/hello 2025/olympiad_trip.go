package main

import (
	"bufio"
	"fmt"
	"os"
)

// 获取数字的二进制长度
func getBinaryLength(n int64) int64 {
	if n == 0 {
		return 0
	}
	var length int64
	for n > 0 {
		length++
		n >>= 1
	}
	return length
}

// 解决单个测试用例
func solveTestCase(l, r int64) (int64, int64, int64) {
	// 如果范围太小，直接返回
	if r-l < 2 {
		return r, r - 1, l
	}

	// 获取l和r的二进制长度
	maxBit := getBinaryLength(r) - 1

	// 从高位到低位，找到第一个l和r不同的位
	var diffBit int64 = -1
	var samePrefix int64 = 0
	for bit := maxBit; bit >= 0; bit-- {
		lBit := (l >> bit) & 1
		rBit := (r >> bit) & 1
		if lBit != rBit {
			diffBit = bit
			break
		}
		if lBit == 1 { // 记录相同的高位前缀
			samePrefix |= (1 << bit)
		}
	}

	// 如果没有找到不同的位，说明l=r，返回保底方案
	if diffBit == -1 {
		return r, r - 1, l
	}

	// 构造掩码
	lowMask := (int64(1) << diffBit) - 1 // 低位全1

	// 构造第一个数：在不同位取1，低位取0
	num1 := samePrefix | (int64(1) << diffBit)

	// 构造第二个数：在不同位取0，低位取1
	num2 := samePrefix | lowMask

	// 尝试构造第三个数：在不同位取1，低位取0，但在某个低位取1
	var num3 int64
	if diffBit > 0 {
		num3 = samePrefix | (int64(1) << diffBit) | 1
		// 如果超出范围，改用另一种构造方式
		if num3 > r {
			num3 = samePrefix | (lowMask & ^int64(1)) // 低位全1除了最低位
		}
	} else {
		// 如果diffBit是0，使用备选方案
		num3 = samePrefix | (lowMask & ^int64(1))
	}

	// 确保所有数都在范围内
	if num1 > r || num2 < l || num3 < l || num3 > r {
		return r, r - 1, l
	}

	// 确保三个数互不相同
	if num1 == num2 || num2 == num3 || num1 == num3 {
		return r, r - 1, l
	}

	return num1, num2, num3
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var t int
	fmt.Fscan(reader, &t)

	for i := 0; i < t; i++ {
		var l, r int64
		fmt.Fscan(reader, &l, &r)
		a, b, c := solveTestCase(l, r)
		fmt.Fprintln(writer, a, b, c)
	}
} 