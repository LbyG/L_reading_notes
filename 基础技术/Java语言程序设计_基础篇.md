## Java语言程序设计（基础篇）

#### 第1章 计算机，程序和Java概述

- 编译器会生成一个拓展名为.class的字节码文件，字节码类似于机器指令，但它是体系结构中立的，是可以在任何带Java虚拟机（JVM）的平台上运行。虚拟机是一个解释Java字节码的程序，因此Java字节码可以在不同的硬件平台和操作系统上运行。

#### 第2章 基本程序设计
- 简单的程序
    ```java
    public class A {
        public static void(String[] args) {
            // ...
        }
    }
    ```
- 方法中声明的变量在使用之前必须被赋值
    ```java
    int i = 1, j = 2;
    ```
- 定名常量
    ```java
    final datatype CNSTANTNAME = VALUE;
    ```
- 数值类型

    | 类型名 | 存储大小 |
    |---|---|
    | byte | 8 bit,1 byte |
    | short | 16 bit,2 byte |
    | int | 32 bit,4 byte |
    | long | 64 bit,8 byte |
    | float | 32 bit,4 byte |
    | double | 64 bit,8 byte |

- 统一码（Unicode）为2个字节，用以\u开头的4位十六进制表示，范围从`\u0000`到`\uFFFF`；ASCII码为1个字节
- String实际上与System类一样，都是一个Java库中预定的类。String类型不是基本类型，而是引用类型。
- 注释风格
    ```java
    // 行注释
    
    /*
    块注释
    */
    
    /**
    Java文档注释
    */
    ```
- 命名习惯
    - 变量和函数按照，首字母小写驼峰命名，如`myVaribale`, `myFunc`
    - 类名按照，首字母大写驼峰命名，如`MyClass`
    - 常量用全大写蛇形，如`API`和`MAX_VALUE`

#### 第3章 选择

- if语句
    ```java
    if (bool expression)
        单个语句
    else
        单个语句
    
    if (bool expression) {
        ...
    }
    else if (bool expression) {
        ...
    }
    else {
        ...
    }
    ```
- 逻辑运算符

    | 运算符 | 名称 |
    |---|---|
    | ! | 非 |
    | && | 与 |
    | || | 或 |
    | ^ | 异或 |

- 条件表达式：`boolean-expression ? expression 1 : expression 2`; 
    - 如：`y = (x > 0) ? 1 : -1`

#### 第4章 循环

- while 循环
    ```java
    while (循环继续条件) {
        // 循环体
    }
    ```
- do-while循环
    ```java
    do {
        // 循环体
    } while (循环继续条件);
    ```
- for循环
    ```java
    for (i = initialValue; i < endValue; i ++) {
        // loop body
    }
    ```

