# 向量空间

*向量空间*与*线性变换* 为*线性数学模型*提供框架。对非线性过程也可生成很好的近似。

向量空间例如：
二维实平面，三维实欧几里得空间，量子力学标准模型、信号处理的复向量空间。

可探索向量空间的形式，这种工具仅依靠向量空间的公里及逻辑推论。

## 向量空间定义

包含以下要件：

1. 一个纯量（scalar）域 $\mathbb{F}$, 可以是复数域  $\mathbb{C}$ 或 实数域  $\mathbb{R}$
2. 一组称为Vector的对象的集合 $\Large\nu$
3. 加法*封闭*
4. 纯量乘法*封闭*

## 公理假设

1. 零元：存在唯一的单位元 $\bf{0} \in \Large\nu$ 使得对所有 $\bf{u} \in \Large\nu$, 有 $\bf{0} + \bf{u} = \bf{u}$
2. 向量加法是交换的 $\bf{u} + \bf{v} =  \bf{v} + \bf{u}$
3. 向量加法是结合的
4. 加法的逆元存在且唯一, 存在唯一 $-\bf{u} \rightarrow \bf{u} + (-\bf{u}) = 0$
5. 存在幺元 1, 乘法
6. 向量乘法与纯量乘法相容 ， $a(b\bf{u})  = ( ab )  \bf{u} $
7. 纯量乘法对向量加法满足分配律  $c(\bf{u} + \bf{v})  = c\bf{u} + c \bf{v} $

## 推论定理

1. $c\bf{u} = \bf{0}$ $\Longleftrightarrow  $
   $  c=0,$  or $ \bf{u}=0$
2. $(-1)\bf{u}= -\bf{u}$

## 零向量空间（无用）

若 $\Large\nu  \normalsize= \{\bf{0} \}$ , 为零向量空间；
若 $\Large\nu  \normalsize \neq \{\bf{0} \}$ , 为非零向量空间；

## 域F不是C就是R

### 例子

1. 设 $\Large\nu=  \normalsize \mathbb{F}^n$, 是元素取自 $\mathbb{F}$的 $n \times 1 $ 的矩阵的集合（列向量），通常写为 $\bf{u} = [u_i]$  或 $ \bf{u} = [u_1 , u_2 \cdots, u_n]^T$ 的形式。
2. $\bf{u} = [u_i]$ $\bf{v} = [v_i]$ , 向量加法定义为 

   $$
   \bf{u}+ \bf{v} =[u_i + v_i]
   $$

    , 乘法定义为 
   $$
   c\bf{u} = [cu_i]
   $$

称为 *逐项运算* entrywise operation, 0向量大小可推算时，省略下标

3. 设 $\Large\nu  \normalsize= \bf{M}_{m \times n}(\mathbb{F}) $, 是元素取自 $\mathbb{F}$的 $n \times 1 $

## 子空间

$ \mathbb{F}$ 向量空间 $\Large\nu$ 的 *子空间*subspace ， 是一 $\Large\nu$ 的一个子集 $\Large u$, 也是 $ \mathbb{F}$ 向量空间

1. 如果 $\Large\nu$  是一个 $ \mathbb{F}$ 向量空间 ， 那么 $\{\bf{0} \}$ 与  $\Large\nu$  本身也是 $\Large\nu$  的子空间。
2. 子空间是非空的，包含0向量。
3. 子空间需满足
   3.1 纯量乘法封闭 ，向量加法封闭
   3.2 包含零向量（加法0元），乘法1元
   3.3 包含加法逆元，
4. $\Large\nu$  是一个 $ \mathbb{F}$ 向量空间， $\Large u$ 是  $\Large\nu$ 的非空子集，则：
   $\Large u$ 是  $\Large\nu$ 的子空间, 当且仅当

$$
\bf{u},\bf{v} \in \Large {u} , c\in \mathbb{F}
$$

有 $c\bf{u} + v \in \Large{u}$

5. 子空间必须包含同样的纯量域， $P_5(\mathbb{R} ) $ 是 $P_5(\mathbb{C}) $  的子集但不是子空间。
6. 偶多项式，对所有z有 $p(-z) = p (z) $
7. 奇多项式， 对所有z有 $p(-z) = -p (z) $
8. 常数多项式是偶的（如 p=5），0多项式既是奇又是偶
9. $P_\text{even}$ $P_\text{odd} $ 都是 $P$ 的子空间

## 线性组合与生成空间

定义： 设 $\Large u$ 是  $ \mathbb{F}$ 向量空间 $\Large\nu$ 的非空子集, $\Large u$ 的元素是一个*线性组合* linear combination，是形如

$$
c_1 \bf{\nu}_1 +    c_2 \bf{\nu}_2 + \cdots +  c_r \bf{\nu}_r
$$

的表达式，r是正整数， $\nu \in \Large u$ , $c_1, c_2 \in \mathbb{F}$.

1. c_n 都为0 ， 称平凡的(trivial), 否则为非平凡的。
2. 线性组合是有限多个向量的纯量倍数直和。
3. list 为非空、有限、有序序列。 常用一个希腊字母表示。元素可重复出现。

### 组合空间 span

设 $\Large u$ 是  $ \mathbb{F}$ 向量空间 $\Large\nu$ 的非空子集， $\text{span}\Large u$ 是  $\Large u$ 的元素的线性组合组成的集合。

1. 定义  $\text{span} \space \varnothing = {\bf{0}}$
2. 矩阵的 *列空间 $\text{col} \space A$* 为矩阵的列的生成空间

定理
设 $\Large u$ 是  $ \mathbb{F}$ 向量空间 $\Large\nu$ 的子集
有：

1. $\text{span}\Large u$ 是 $\Large\nu$ 的子空间
2. $ \large u \normalsize \in \text{span} \Large u$
3. $ \large u \normalsize = \text{span} \Large u$  当且仅当  $\Large\nu$ 是 $\Large\nu$ 的子空间
4. $\text{span} （ \text{span}   \Large u   \normalsize     ） =  \text{span}   \Large u$

定理

1. 设 $\Large u$ ， $\Large w$ 是  $ \mathbb{F}$ 向量空间 $\Large\nu$ 的子集, 如果 $ \Large u  \normalsize \subseteq \Large w   $ ,那么  $ \text{span} \Large u  \normalsize \subseteq \text{span} \Large w   $

定义
设 $\Large u$ 是  $ \mathbb{F}$ 向量空间 $\Large\nu$ 的子集，$\beta$ 是 $\Large\nu$ 中的向量列表。

1. 若 $ \text{span} \space \Large u  \normalsize = \Large \nu $, 那么
   $\Large u  $ 生成（span）  $\Large \nu $  ( $\Large u  $ 是生成集spanning set)
2. 若 $ \text{span} \space \beta   \normalsize = \Large \nu $  , 那么
   $\beta  $ 生成（span）  $\Large \nu $  ( $\beta  $ 是一个生成组spanning list)

## 子空间的交、和、直和

1. 子空间的交是子空间
2. 子空间的并不一定是子空间
3. 子空间的并集的生成空间是子空间
4. 子空间的和（sum） 定义为 $\text{span} (\Large u \normalsize \cup \Large w  \normalsize )  = \Large u \normalsize  + \Large w  \normalsize$
5. 复向量空间P中，$P_{\text{even }} + P_{\text{odd }}= P$

### 直和

设 $\Large u$ ， $\Large w$ 是  $ \mathbb{F}$ 向量空间 $\Large\nu$ 的子空间，如果 并集为 {\bf{0}} , uw之和为直和，记为 $\Large u \oplus \Large w$

1. 直和中任何向量关于求和项都有唯一的表示。
2. $\Large u \oplus \Large w$ 中每一个向量都可以用唯一的方式表示成u的向量和w中的向量之和。
3. 向量减法为求交集
4. 交集非0则非直和。

## 线性相关

定义:
$ \mathbb{F}$ 向量空间 $\Large\nu$ 的向量列表 $\beta= \nu_1 + \cdots + \nu_r$ ， 如果存在不全为零的纯量c1... cr 使得 $c_1\nu_1 + \cdots + c_r\nu_r = \bf{0}$, 则称向量列表线性相关(linearly dependent)。

等价于：

$$
\sum_{i=1}^{r}c_i \bf{v}_i = 0
$$

性质：

1. 如果  $\beta$ 线性相关，那么重新排列的任何 *向量列表* 也是线性相关的。
2. 单个向量 $\nu$ 组成的向量组线性相关，当且仅当 $\nu$  是0向量。
3. 两个向量线性相关，当且仅当其中一个向量是另一个向量的纯量倍数。
4. 大于3个向量线性相关，当且仅当其中一个向量是其他向量的线性组合。
5. 包含零向量的任何向量列表都是线性相关的。
6. 包含同一个向量2次的*向量列表*线性相关。

定理

1. 若 $ \mathbb{F}$ 向量空间 $\Large \nu$ 的向量列表 $ v_1 + \cdots + v_r$ 线性相关，那么对任何 $v \in \Large\nu$, 向量组线性相关。

## 线性无关

等价于：
$\sum_{i=1}^{r}c_i \bf{v}_i = 0  $ 只存在平凡解（c均为0）
#$\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$

## 集合的线性相关

1. 对于向量空间 $\Large \nu$ 的子集 $\mathscr{S}$ 中每组向量都线性无关，称  $\mathscr{S}$ *线性无关* 。
2. 对于向量空间 $\Large \nu$ 的子集 $\mathscr{S}$ 中有一组相异向量线性相关，称  $\mathscr{S}$ *线性相关* 。
   相关性质：
3. 向量列表是否线性无关与排列次序无关
4. 由单个向量组成的向量组线性无关，当且仅当$v$不是零向量
5. 两个向量线性无关， 当且仅当其中没有向量是另一个向量的纯量倍数。
6. 至少由三个向量的向量组线性无关，当且仅当其中不存在任何一个向量是其他向量的线性组合。

例子：

1. $A = [\mathbf{a}_{n}] \in \mathbf{M}_{m\times n}(\mathbb{F})$ . 向量组 $\beta= a_1 + \cdots + a_n$ 线性无关，当且仅当使得
   $\sum_{i=1}^{n} x_i\bf{a}_i = 0$ 成立的 $\mathbf{x}=[x_1  \cdots x_n]^T \in \mathbb{F}^n$ 是0向量。

也就是说，$\beta$ 线性无关，当且仅当 $\text{null}\space A= {\mathbf{0}}$

等价于 

$$
A \mathbf{x} = \mathbf{0}
$$


2. 多项式 $P$, 线性组合是零多项式且只存在平凡解(系数均为0)时，向量*线性无关*。
3. 设 $A = [\mathbf{a}_{n}] \in \mathbf{M}_{n}$ 可逆, $\mathbf{x}=x_i \in \mathbb{F}$ 是纯量，使得 $\sum_{i=1}^{n} x_i\bf{a}_i = 0$, 则
   $A\mathbf{x} =\mathbf{0}$ ,从而
   $\mathbf{x}= A^{-1} (A\mathbf{x} ) = A^{-1} \mathbf{0} =  \mathbf{0}$, 推出 $x_i=0$
   推出 $\mathbf{a_i}$ 线性无关。
   得出结论： 任何可逆矩阵的列，线性无关。
4. 单位矩阵可逆，列线性无关。

性质：
线性无关列向量的重要性质： 对于其生成空间中的每一个向量，均给出*唯一*表示

定理：
1. 线性无关向量的= ， 必须每个系数均相等。

在某些情况下，线性无关的向量组可以扩大或缩小，而*生成空间*不变。为了方便可新定义记号。

定理：
1. 如果从一个至少有两个向量的线性无关的向量组中去掉任何一个向量，则剩下的向量依然线性无关。
2. 等价于：线性相关向量组，增加同向量空间的向量后，线性相关。

3. 从大于2的线性无关向量组中去掉1个向量，剩下的向量依然线性无关。反之若剩下的向量组线性相关，则源向量组线性相关。

设 $\beta=\mathbf{v}_1 \cdots \mathbf{v}_r $ 是非零向量空间 $\Large \nu$ 的一列向量。
那么
1. 假设 $\beta$ 线性无关，不生成  $\Large \nu$ ， 如果新项 $\mathbf{v} \in \Large \nu$ , $v \not\in \text{span} \beta$ ,则新向量组线性无关。

（增加不在生成空间内的元素，可组成新的线性无关向量组）

2. 

（线性相关向量组（非平凡线性组合），可去除线性相关元素（该元素可被其他元素的标量倍数表示），变为生成空间一致的线性组合）

