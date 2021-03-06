## 4.2 规范
函数的规范定义了函数编写者与使用者之间的约定。我们将函数使用者称为客户。可以认为约定包括以下两部分。
 假设：客户使用函数时必须满足的前提条件，通常是对实参的限制。它几乎总是限定每个参数可以接受的变量类型，偶尔对一个或多个参数的取值添加限制条件。例如，函数
findRoot的文档字符串前两行描述了客户必须满足的假设。
 保证：调用方法满足条件时，函数应当实现的功能。函数findRoot的文档字符串后两行描述了函数必须实现的结果保证。

函数通过分解和抽象的功能，大大提高了编程的便捷性。

分解实现了程序结构化。它允许我们将程序分成多个逻辑上独立的部分，并可以通过各种设定实现重用。
抽象隐藏了细节。它允许我们将一段代码当作黑箱使用。所谓黑箱，是指那些我们不能看见、不需看见甚至根本不想看见内部细节的东西。①抽象的精髓在于，在具体背景之下，保留那些该保留的，忽略那些该忽略的。在编程中有效使用抽象的关键在于，找到一个对于抽象创建者和抽象潜在使用者都很合适的相关性表示。这才是真正的程序设计艺术。
抽象归根结底就是忽略。有很多方式可以对此形象地进行解释，例如，多数年轻人的听觉器官。
抽象是个多对一的过程。

## 4.3 递归
一般情况下，递归定义包括两部分。其中至少有一种**基本情形**可以直接得出某种**特定情形**的结果（如上面例子中的第一种情况），还至少有一种**递归情形**（或称归纳情形）定义了该问题在**其他情形**下的结果，其他情形通常是同样问题的简化版本。

找到某种抽象方式表示问题的解，常常是编程过程中最困难的部分。
### 4.3.1 斐波那契数列
### 4.3.2 回文
这种对isPalindrome的实现是分治策略的典型例子。（这种原则与分治算法密切相关，但又有点不一样，我们会在第10章进行讨论。）这种解决问题的原则就是，将一个困难问题分解成一组子问题逐个解决。分解出来的子问题具有以下特性：
 子问题比初始问题更容易解决；
 子问题的解决方案可以组合起来解决初始问题。

本例（回文算法）中，我们将初始问题分解为一个更简单的情形（检查一个更短的字符串是否是回文字符串）和一个我们可以解决的简单情形（比较单个字符），然后使用and将这两个问题的解组合起来。
