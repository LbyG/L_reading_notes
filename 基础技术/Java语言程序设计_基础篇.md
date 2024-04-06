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

- switch语句
    - switch表达式必须能计算出一个char，byte，short或int类型，并且必须要在括号中
    - case后面的类型必须与switch表达式的值类型相同，且是不可变的常量表达式
    - 如果不写break，switch会从匹配到的case一直运行到末尾
    ```java
    switch (switch表达式) {
        case 值1:
            语句组1;
            break;
        case 值2:
            语句组2;
            break;
        ...
        default:
            都不匹配的语句组
    }
    ```
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

#### 第5章 函数方法

- 方法的定义
    ```java
    // 装饰符：public static
    // 返回值类型：int
    // 方法名：max
    // 形式参数：int num, int num
    public static int max(int num, int num) {
        // 方法体
    }
    ```
- 定义在方法头中的变量成为形式参数，调用参数时候传递的值为实际参数
- 当调用带参数的方法时，实参的值传递给形参，这个过程称为通过值传递
- 方法重载：一个类中有多个方法具有相同的名字，但有不同的参数列表。Java编译器会自动根据方法签名决定使用哪个方法
    - 被重载的方法必须具有不同的参数列表，不能基于不同修饰符或返回值类型来重载方法
    - 优势调用一个方法时，会有多个匹配，这时编译器无法进行判断，因此会产生歧义调用
    - 局部变量的作用域从声明的地方开始，到包含该变量的块结束
- 当编写一个大程序时，可以使用分治策略，通过结构图，将大问题分解成小问题。然后自顶向下或自底向上的进行实现。

#### 第6章 一维数组

- 在程序中使用数组，必须声明一个引用数组的变量，并指明数组的元素类型
    - elementType可以是任意数据类型，但所有元素必须具有相同的数据类型
    ```java
    // 元素类型[] 数组引用变量;
    elementType[] arrayRefVar;
    ```
- 声明一个数组变量时并不在内存中给数组分配任何空间，如果没有赋值对数组的引用则该值为null
- 可以用new操作符创建数组，可以在声明数组的同时用new创建数组，并将数组引用赋值给引用数组的变量
    ```java
    // 元素类型[] 数组引用变量 = new 元素类型[数组大小];
    elementType[] arrayRefVar = new elementType[arraySize]
    ```
- 创建数组之后就不能再修改它的大小，并且会被赋予默认值0。
- 数组下标是基于0的，数组中的每个元素都可以使用下面的【下标变量】语法表示
    ```java
    // 数组引用变量[下标];
    arrayRefVar[index];
    ```
- 数组初始化语法如下：
    ```java
    // 元素类型[] 数组引用变量 = {值0，值1，...，值k};
    // elementType[] myList = {value0, value1, ..., valuek};
    double[] myList = {1.9, 2.9, 3.4, 3.5};
    ```
- 数组支持for-each循环，不使用下标变量就可以顺序地遍历整个数组。
    ```java
    /*
    for (elementType element: arrayRefVar) {
        // process the element
    }
    */
    for (double u: myList) {
        System.out.println(u);
    }
    ```
- 数组的赋值是将数组引用赋值给另一个变量，两个变量会指向相同的数组，因此数组作为实参时传递的是引用
- 匿名函数：没有显式地引用变量的数组
    ```java
    // new 数组类型[]{值0，值1，...，值k};
    // elementType[]{value0, value1, ..., valuek};
    printArray(new int[](3, 1, 2, 6, 4, 2))
    ```
- 可变长参数列表，类型相同但个数可变的参数传递给方法。该方法只能指定一个可变参数，该参数必须放到最后一个，使用时当作数组使用
    ```java
    // 类型名...参数名
    // typeName...parameterName
    public static void printMax(double... numbers) {
        double result = numbers[0];
    }
    ```
    

#### 第7章 多维数组
- 多维数组的语法
    ```java
    // 数组类型[][] 数组名;
    int[][] matrix;
    matrix = new int[5][5];
    
    // ok
    int[][] triangleArray = new int[5][]
    // error
    int[][] triangleArray = new int[][]
    ```
- 二维数组中的每一行本身就是一个数组，因此，各行的长度就可以不同
    ```java
    int[][] triangleArray = {
        {1, 2, 3, 4, 5},
        {1, 2, 3, 4},
        {1, 2, 3},
        {1, 2},
        {1},
    };
    ```
- 更高维度的数组同样处理
    ```java
    double[][][] scores = new double[10][24][2];
    ```

#### 第8章 对象和类

- 实例化：从一个【类】中创建【实例】的过程
- Java类使用变量定义数据域，使用方法定义动作。类可以通过调用构造方法创建一个新对象
- 可以把两个类放在同一个文件中，但是文件中只能有一个类时公共的。此外，公共类必须与文件同名。
- 构造方法有如下特殊性，并且可以重载。如果没有定义构造函数，会生成一个默认构造方法
    - 构造方法必须具备和所在类相同的名字
    - 构造方法没有返回类型，甚至连void也没有
        ```java
        class Circle {
            public void Circle() {
                ...
            }
            
            public void Circle(double radius) {
                ...
            }
        }
        ```
    - 构造方法是在创建一个对象使用new操作符时调用的。构造方法的作用是初始化对象。
- 对象是通过对象引用变量来访问的。
    ```java
    // 类名 对象引用变量;
    // ClassName objectRefVar;
    Circle myCircle;
    myCircle = new Circle()
    // 类名 对象引用变量 = new 类名();
    // ClassName objectRefVar = new ClassName();
    Circle myCircle = new Circle();
    ```
- 创建一个对象之后，他的数据和方法可以使用圆点运算符（.）来访问和调用，该运算符也称为对象成员访问运算符
    ```java
    // 引用对象的数据域
    objectRefVar.dataField
    // 调用对象的方法
    objectRefVar.method(参数)
    ```
- Java支持静态方法和静态变量，他们在一个类的所有实例中共享数据。可以通过加上修饰符`static`声明一个静态变量或定义一个静态方法。
    ```java
    class className {
        // 静态变量
        static int numberOfObjects;
        // 类中的常量是被该类的所有对象所共享的
        final static double PI = 3.1415926;
        
        // 静态方法
        static init getNumerObjects() {
            return numberOfObjects;
        }
    }
    ```
- 可见性修饰符
    - 类
        | 修饰符 | 访问限制 |
        |---|---|
        | 没有使用可见性修饰符，默认为包内私有 | 可以被同一个包中的任何类访问 |
        | public | 可以被包外访问，可以被任何其他的类访问 |
    - 方法和数据域
        | 修饰符 | 访问限制 |
        |---|---|
        | 没有使用可见性修饰符，默认为包内私有 | 可以被同一个包中的任何类访问 |
        | public | 可以被包外访问，可以被任何其他的类访问 |
        | private | 只能在它自己的类中被访问 |
- 数据域封装：为了避免对数据域的直接修改，应该使用private修饰符将数据域声明为私有。
    - 通过get方法返回数据域的值
        ```java
        // get方法有如下签名：
        // public returnType getPropertyName()
        public double getRadius() { ... }
        // 如果返回类型是boolean型，习惯上如下定义get方法
        // public boolean isPropertyName()
        public boolean isFilled() { ... }
        ```
    - 通过set方法给数据域设置新值
        ```java
        // set方法有如下签名
        // public void setPropertyName(dataType propertyValue)
        public void setRadius(double radius) { ... }
        ```
- 对象的数组实际上是引用变量的数组，当使用new操作符创建对象数组后，这个数组中的每个元素都是默认值为null的引用变量
    ```java
    // 此时circleArray中的值为null
    Circle[] circleArray = new Circle[10];
    // 创建对象并将引用赋值给对象数组下标
    for (int i = 0; i < circleArray.length; i ++) {
        circleArray[i] = new Circle();
    }
    ```
- UML类图的一些支持
    - 在UML类图中，静态变量和方法都是以下划线标注的
    - `-`号表示私有装饰符
    ```java
    // 数据域表示为：
    // 数据域名：数据域类型
    // dataFieldName: dataFieldType
    radius: double
    // 构造方法可以表示为：
    // 类名（参数名：参数类型）
    // ClassName(parameterName: parameterType)
    Circle()
    Circle(newRadius: double)
    // 方法可以表示为
    // methodName(parameterName: parameterType)
    getArea(): double
    ```