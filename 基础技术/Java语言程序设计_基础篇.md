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
        | (default) | 可以被同一个包中的任何类访问 |
        | public | 可以被包外访问，可以被任何其他的类访问 |
    - 方法和数据域
        | 修饰符 | 访问限制 |
        |---|---|
        | private | 只能在它自己的类中被访问 |
        | (default) | 可以被同一个包中的任何类访问 |
        | protected | 1.允许同一个包内访问; 2.允许子类访问定义在父类的数据域和方法 |
        | public | 可以被包外访问，可以被任何其他的类访问 |
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

#### 第9章 字符串与文本I/O

- 在Java中，字符串是一个对象，可以使用如下方法构造一个字符串
    ```java
    // 从字符串直接量创建一个字符串
    // String newString = new String(stringLiteral);
    String message = new String("Welcome to Java");
    // Java将字符串直接量看作String对象
    String message = "Welcome to Java";
    // 用字符数组创建一个字符串
    char[] charArray = {'G', 'o', 'o', 'd'};
    String message = new String(charArray);
    ```
- String对象是不可变的，它的内容不能改变的。Java虚拟机对具有相同字符串序列的字符串直接量使用同一个实例
    ```java
    // s1 == s2   result is false
    // s1 == s3   result is true
    String s1 = "Welcome to Java";  // 指向内置字符串对象"Welcome to Java"
    String s2 = new String("Welcome to Java");  // 指向新创建的字符串对象
    String s3 = "Welcome to Java";  // 指向内置字符串对象"Welcome to Java"
    ```
- 字符串比较：运算符`==`只能检测两个字符串是否指向同一个对象，不能判断两个字符串变量的内容是否相同，应该使用`equals`方法判断两个字符串是否相同
    ```java
    // 如果这个字符串等于字符串s1则返回true
    +equals(s1: String): boolean
    // 判断这个字符串的前缀是否是prefix
    +startsWith(prefix: String): boolean
    // 判断这个字符串的后缀是否是suffix
    +endsWith(suffix: String): boolean
    ```
- 字符串的基础方法
    ```java
    String s = new String("test");
    // 返回字符串长度
    // +length(): int
    int length = s.length();    // 4
    // 返回指定下标处的字符串
    // +charAt(index: int): char
    char c = s.charAt(0);   // 't'
    // 将这个字符串与s1字符串拼接构造新的字符串，并将其引用返回
    // +concat(s1: String): String
    String newStr = s.concat(" concat");    // "test concat"
    ```
- 获取子串的方法：返回会构造一个新的字符串
    ```java
    String s = new String("test");
    // 返回从下标beginIndex开始的子串
    // +substring(beginIndex: int): String
    String subStr1 = s.substring(1);    // "est"
    // 返回从下标beginIndex到beginIndex-1的子串
    // +substring(beginIndex: int, endIndex: int): String
    String subStr2 = s.substring(1, 3); // "es"
    ```
- 字符串的转换，替换和分隔：返回会构造一个新的字符串
    ```java
    String s = new String(" Hello World\n");
    // 字符串转全小写
    String lowerStr = s.toLowerCase();  // " hello world\n"
    // 字符串转全大写
    String upperStr = s.toUpperCase();  // " HELLO WORLD\n"
    // 去掉两遍的空白字符
    String trimStr = s.trim();          // "Hello World"
    // 字符替换
    String replaceChrStr = s.replace('l', 'k');     // " Hekko Workd\n"
    // 替换首个匹配成功的字符串
    String replaceFirstStr = s.replaceFirst("l", "jk"); // " Hejklo World\n"
    // 替换全部匹配成功的字符串
    String replaceAllStr = s.replaceAll("l", "jk"); // " Hejkjko Worjkd\n"
    // 通过分隔符，将字符串分割成字符串数组
    String[] splitStrList = s.split("o");   // {" Hell", " W", "rld\n"}
    ```
- 查找字符串中某个字符或某个字符串的位置
    ```java
    String s = new String("test test!");
    // 查找第一个匹配成功的下标，如果没有匹配到，则返回-1
    // +indexOf(ch: char): int
    // +indexOf(ch: char, fromIndex: int): int
    // +indexOf(s: String): int
    // +indexOf(s: String, fromIndex: int): int
    int firstIndex = s.indexOf("es");   // 1
    // 查找最后一个匹配成功的下标，如果没有匹配到，则返回-1
    // +lastIndexOf(ch: char): int
    // +lastIndexOf(ch: char, fromIndex: int): int
    // +lastIndexOf(s: String): int
    // +lastIndexOf(s: String, fromIndex: int): int
    int lastIndex = s.lastIndexOf("es");   // 6
    ```
- 可以通过`toCharAarry`方法，将字符串转化为字符数组
    ```java
    char[] chars = "test".toCharArray();    // {'t', 'e', 's', 't'}
    ```
- 可以通过`valueOf`方法，将基础类型`char, char[], double, float, int, long, boolean`转化为字符串
    ```
    double doubleValue = 5.44;
    String s = String.valueOf(doubleValue);     // "5.44"
    ```
- `StringBuilder/StringBuffer`:支持添加，插入或追加的字符串处理方案
    ```java
    StringBuilder stringBuilder = new StringBuilder("Hello");
    // 追加一个char数组或字符串到StringBuilder生成器
    // +append(data: char[]): StringBuilder
    // +append(s: String): StringBuilder
    stringBuilder.append("World");      // "HelloWorld"
    // 从字符串生成器StringBuilder返回一个字符串对象
    // +toString(): String
    String s = StringBuilder.toString();    // "HelloWorld"
    ```
- `File`类提供了一种抽象，用以不依赖机器的方式来处理文件
    - 用相对路径，不要用绝对路径，绝对路径会有window/linux系统命名问题
    ```java
    // 为特定路径名创建一个File对象，路径可以是目录，也可以是一个文件
    // +File(pathname: String)
    File file = File("image/test.txt");
    // 判断是否存在
    // +exists(): boolean
    boolean isExist = file.exist();
    // 判断是否为文件
    // +isDirectory(): boolean
    boolean isDir = file.isDirectory(); // false
    // 判断是否为目录（文件夹）
    // +isFile(): boolean
    boolean isFile = file.isFile();     // true
    ```
- `PrintWriter`写数据到文件
    ```java
    // 从File类构造
    // +PrintWriter(file: File)
    File file = File("image/test.txt");
    PrintWriter writer1 = new PrintWriter(file);
    // 从文件路径构造
    // +PrintWriter(filename: String)
    PrintWriter writer2 = new PrintWriter("image/test.txt");
    // 写基础类型数据，char数组，字符串到文件
    // +print(data: dataType): void
    writer2.print("test\n");
    writer2.print(1);
    writer2.print(3.14);
    ```
- `Scanner`从文件读取数据
    ```java
    // 从File类构造
    // +Scanner(source: File)
    Scanner systemInInput = new Scanner(System.in);
    Scanner fileInput = new Scanner(new File("image/test.txt"));
    // 判断是否还有可读的数据
    // +hasNext(): boolean
    boolean hasNext = fileInput.hasNext();
    // 读取下一个数据
    // +next(): String  读取到下一个分隔符，默认分隔符为空格
    // +nextLine(): String  读取到下一个换行符，不同系统的换行符不一样
    // +nextInt(): int  读取下一个标志作为int值
    // ...
    String line = fileInput.nextLine();
    int intValue = fileInput.nextInt();
    // 设置支持正则表达式的分隔符，与next()搭配使用
    // +useDelimiter(pattern: String)
    Scanner s = new fileInput.useDelimiter("\\s*fish\\s*");
    // 关闭扫描器
    // +close()
    systemInInput.close();
    fileInput.close();
    ```

#### 第10章 关于对象的思考

- this指向调用对象本身的引用名
    ```java
    public class Circle {
        private double radius = 5;
        
        public Circle(double radius) {
            // 调用私有数据域
            this.radius = radius;
        }
        
        public Circle() {
            // 调用同一个类的另一个构造方法
            this(1.0);
        }
    }
    ```
- 面向对象与面向过程的区别
    - 面向过程
        - 重在设计方法
        - 数据和数据上的操作是分离的
    - 面向对象
        - 将数据和方法都组合在对象中，重在对象和对象的操作
        - 数据和对他们的操作都放在一个对象中
- 类的设计原则
    - 内聚性
        - 类应该描述一个单一的实体，而所有的类操作应该在逻辑上相互配合，支持一个连贯性的目标。
    - 一致性
        - 一般来说，应该提供一个公共无参的构造方法
        - 如果不想让用户创建类，可以声明一个私有的构造方法
        - 命名要保持一致，类，数据域和方法选择有信息量的名字
        - 数据声明置于构造方法之前，构造函数至于方法之前
    - 封装性
        - 一个类应该用private修饰符隐藏其数据，以免用户直接访问它，而是通过`get`和`set`进行读取和设置
    - 清晰性
        - 不应该声明一个可以由其他数据获得的数据
        - 类的使用目的和使用时间没有限制
    - 完整性
        - 一个类应该通过属性和方法提供多种方案以适应用户的不同需求
- 静态变量和方法的使用注意事项
    - 用类名（而不是引用变量）引用静态变量和方法，以增强可读性并避免错误
    - 不要从构造方法初始化静态数据，要使用set改变

#### 第11章 继承与多态

- Java支持继承，可以从已有的类`C1`派生出新类`C2`，`C1`为父类，`C2`为子类。
- 子类使用下面的语法拓展父类，继承的注意事项：
    - 子类无法访问父类的私有数据域
    - 不是所有`is-a`都该用继承来建模
    - 继承是用来为`is-a`建模的，而不是为了重用
    - Java只支持单一继承，不允许多重继承，一个Java类只能继承自一个父类
    ```java
    public class ChildClass extends ParentClass {
        ...
    }
    ```
- 父类的构造方法必须使用关键字`super`，而且这个调用必须是构造方法的第一条语句，父类的构造方法不被子类继承。
    - 如果子类没有显式调用父类构造函数，编译器会自动将`super()`作为构造方法的第一条语句
    - 构造方法链：构造一个类的实例时，会沿着继承链调用所有父类的构造方法
    ```java
    class ChildClass extend ParentClass {
        public ChildClass() {
            super() or super(parameters);
            // ... ChildClass数据域初始化
        }
    }
    ```
- 关键词`super`还可以引用父类的方法
    - Java不支持`super.super.func()`调用父类的父类
    ```java
    class ChildClass extend ParentClass {
        public void func() {
            super.func();
            // ...
        }
    }
    ```
- **多态**：是指父类型的变量可以引用子类型的对象
    ```java
    ChildClass childClass = new ParentClass();
    ```
- **动态绑定**：是指Java中调用哪个函数是由变量的实际类型决定的
    - 声明类型：一个变量必须被声明为某种类型，变量的这个类型称为声明类型。如下面代码中的`Object`
    - 实际类型：变量的实际类型是被变量引用的对象的实际类。如下面代码中的`String`
    ```java
    Object o = new String();
    ```
- Java支持在继承体系结构中，将一个类转化为另一个类
    ```java
    // 子类转换父类支持隐式转换
    ParentClass parent = new ChildClass();
    // 父类转子类需要显式转换，为确保转换成功，可以利用运算符instanceof
    if (parent instanceof ChildClass) {
        ChildClass child = (ChildClass)parent;
    }
    ```
- `==`运算符检测两个引用变量是否指向同一个对象。如果要检测内容是否相同，需要子类覆盖`Object`类的`equals`方法
    ```java
    public boolean equals(Object o) {
        ...
    }
    object1.equals(object2);
    ```
- ArrayList类支持存储不限定个数的对象
    ```java
    // 初始化
    ArrayList list = new ArrayList();
    // 添加一个元素
    list.add("test1");              // {"test1"}
    list.add("test2");              // {"test1", "test2"}
    // 返回大小
    list.size();                    // 2
    // 更新元素
    list.set(1, "update test2");    // {"test1", "update test2"}
    // 引用元素
    list.get(1);                    // "update test2"
    // 删除一个元素
    list.remove(0);                 // {"update test2"}
    // 删除所有元素
    list.clear();                   // {}
    ```
- `final`修饰符表明一个类是终极的，是不能作为父类的。或者修饰一个函数是不能被覆盖的
    ```java
    // 无法作为父类
    public final class ClassName {
        // ...
    }
    
    public class Test {
        // 无法被覆盖
        public final void func() {
            // ...
        }
    }
    ```

#### 第13章 异常处理

- Java支持抛出异常和捕获异常
    ```java
    void funcToThrowException() throws Exception {
        // 抛出异常
        throw new Exception("test exception")
    }
    
    void funcToCatchException() {
        try {
            // 语句组
            funcToThrowException();
            // 语句组
        }
        catch (ArithmeticException ex) {
            // 处理异常ArithmeticException
        }
        catch (Exception ex) {
            // 处理异常Exception
        }
        finally {
            // 会处理的代码块，即使try开始到finally之前，触发了return，finally块还是会执行
            // 一般用于处理资源的释放
        }
    }
    ```
- `RuntimeException`, `Error`以及他们的子类称为**免检异常**，其他为**必检异常**。
    - 大多数情况下，免检异常都会反映出程序设计上不可恢复的逻辑错误。Java语言不允许编写代码捕获和声明免检异常
    - `RuntimeException`：由Java虚拟机抛出的系统错误
    - `Error`：程序设计错误导致的运行时异常，比如数组越界，类型转换错误
- 每个方法都必须声明它可能抛出的必检异常的类型
    ```java
    // 声明单个异常
    public void myMethod() throws IOException {
        // ...
    }
    // 声明多个异常
    public void myMethod() throws Exception1, Exception2, ..., ExceptionN {
        // ...
    }
    ```
- Java强迫程序员处理必检异常，由如下两种处理方法
    ```java
    // public void p2() throws IOException
    
    // 在try-catch块中调用它
    void p1() {
        try {
            p2();
        }
        catch (IOException ex) {
            ...
        }
    }
    
    // 在调用方法中声明要抛出异常
    void p1 throws IOException {
        p2();
    }
    ```
- 处理异常的逻辑
    - 仅当必须处理不可预料的错误状况时应该使用它。例如：文件无法进行I/O
    - 不要用`try-catch`处理简单的，可预料的情况。例如：null的处理。
- 重新抛出**链式异常**
    ```java
    try {
        ...
    }
    catch (Exception ex) {
        throw new Exception("new info ...", ex);
    }
    ```