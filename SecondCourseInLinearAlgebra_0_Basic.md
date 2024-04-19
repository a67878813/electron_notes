## 函数

设$\mathscr{X}$ $\mathscr{Y}$ 是集合

记号$f:\mathscr{X}\rightarrow\mathscr{Y}$为函数。
其中

1. $\mathscr{X}$是定义域
2. $\mathscr{Y}$是上域
3. ran f 是值域
4. $\begin{aligned}    ran\space f  &= \{  f(x):    x \in \mathscr{X}       \} \\ &= \{  y \in \mathscr{Y} :y = f(x)           \} \end{aligned}          $
5. 值域是$\mathscr{Y}$的子onto集， 称函数是映上的（onto）
6. 值域和上域相等，成函数是一对一的(one to one)
7. $f(x_1) = f(x_2) \implies   x_1 =x_2   $ 则f是一对一的
8. $f(x_1) \neq f(x_2) \implies   x_1 \neq x_2   $ 则集合x是一对一的
9. 对任意 $i \neq j,\space i,j \in\{ 1,2,...,k\} \implies x_i \neq x_j$ 则集合元素x_1,x2,...相异（distinct）

## 纯量

实数 $\mathbb{R}$

复数 $\mathbb{C}$

## 矩阵

mxn的矩阵指由实数或复数组成的举行阵列。行列式

$A=[a_{ij}]= $

下标i行，j列。

1. 若两个举着你有同样的行数列数，且对应元素均相等，则两个矩阵相等（equal）
2. $n \times n $ 的矩阵成为方阵（square matrix）
3. 元素为复数的所有 $m\times n $ 的矩阵的集合，记为 $\bf{M}_{m \times n}(\mathbb{C})$
4. 如果上条的m=n,可简写为 $\bf{M}_{n}(\mathbb{C})$, 也可简写为 $\bf{M}_{n}$
5. $\bf{M}_{m \times n}(\mathbb{C})$ 简写为 $\bf{M}_{m \times n}$
6. 实数元素矩阵必须标明。$\bf{M}_{m \times n}(\mathbb{R}) $

### 行与列

矩阵 $A= [a_{ij}]$

1. 行i是 $1\times n$  矩阵

   $$
   \begin{bmatrix} a_{i1} & a_{i2} ... & a_{in} \end{bmatrix}
   $$
2. 列j 是 $m \times 1 $ 矩阵 $\bf{a}_j \begin{bmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{mj}   \end{bmatrix}$
3. 单列矩阵简写为 $\bf{a}_j$
4. 矩阵可简写为 $1\times n$的阵列形式：

   $$
   A=\begin{bmatrix} \bf{a}_1 & \bf{a}_2 & \cdots & \bf{a}_n \end{bmatrix}
   $$

### 加法与纯量乘法

若 $ A=[a_{ij}] $ 与  $ B=[b_{ij}] $的size都为 $m\times n$,

则：

1. A+B 的size 为 $m\times n$。
2. A+B 在位置 $(i,j)$处的元素是 $a_{ij}+ b_{ij}$。

若 $A \in \bf{M}_{m\times n}$ , c是纯量，则：

1. $ cA = [ca_{ij}]    $

零矩阵， 是元素全为零的 $m\times n $ 矩阵，可用0表示零矩阵。也可加下标指出0矩阵的大小。

设 $A,B \in \bf{M}_{m \times n}$ ,c,d 是纯量，则：

1. A+B = B+A
2. A +(B+C) = (A+B) +C
3. A +0 = A = 0+ A
4. c(A+B)= cA +cB
5. c(dA) = (cd) A = d(cA)
6. (c+d)A = cA +dA

### 乘法

如果 $A=[a_{ij}] \in \bf{M}_{m \times r} $, $B=[b_{ij}] \in \bf{M}_{r \times n} $,则：

1. 乘积  $AB=[c_{ij}] \in   \bf{M}_{m \times n} $ 位于 $(i,j)$处的元素是

$$
c_{ij} = \sum_{k=1}^{r}a_{ik}b_{kj}
$$

(for k=1 ; k<r ; ++k)

这个元素包含了A的第i行元素和B的第j列元素。A的列数=B的行数。

2. 如果把B写成列组成的 $1 \times n$阵列，阵列 $B = [ \bf{b}_1, \bf{b}_2  \cdots \bf{b}_n]$,则

$$
AB = [A\bf{b}_1,A\bf{b}_2  \cdots A\bf{b}_n ]
$$

3. 如果$AB =BA$, 则称$A,B \in \bf{M}_{n} $ 可交换。
4. $\bf{M}_{n}$ (复方阵)中的某些 __矩阵对__ 是不可交换的。
5. AB=AC 不能推出B=C
6. 设A,B，C是适当大小的矩阵，c是纯量，那么：
   6.1 $  A(BC)=(AB)C     $
   6.2 $  A(B+C)=AB+AC     $
   6.3 $  (A+C)C = AC + BC     $
   6.4 $  (cA)B = c(AB) = A(cB)     $

### 单位阵

$$
\mathbb{I}_n = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} 
\in  \bf{M}_{n}
$$

是 $n \times n$ 单位阵（identity matrix）

即 $I_n=[\delta _{ij}]$,其中

$$
\delta _{ij} =      \begin{cases}  1,\text{ if} \space i=j \\ 0, \text{ if}  \space i\neq j   \end{cases}
$$

1. 如果能明确知道单位阵的大小，可简写单位阵为 $I$.
2. 对每个 $A \in \bf{M}_{m \times n}$ 有

$$
AI_n = A = I_m A
$$

### 三角阵

$A = [a_{ij}] \in \bf{M}_{n}$ (复方阵)

1. 若i>j 有 $a_{ij}=0$, 称A是上三角的。（右上角不为0）
2. 若i<j 有 $a_{ij}=0$, 称A是上三角的。（左下角不为0）

### 对角阵  diagonal matrix

$A = [a_{ij}] \in \bf{M}_{n}$ (复方阵)

1. 若 $i\neq j$ 有 $a_{ij}=0$, 称A是对角的.

A的任何非零元素都在A的*主对角线*(main diagonal )上（左上右下）

2. *主对角线* 由*对角线元素*(diagonal entry)组成，$a_{11} ,\cdots $；
3. $i \neq j$ 对应的元素 $ a_{ij}$称为 A *对角线之外的元素*(off-diagonal entry)
4. $\text{diag}(\lambda_1 ,\lambda_2, \cdots, \lambda_n )$ 表示 $n\times n$对角矩阵
5. 纯量矩阵(scalar matrix)指 形如 $\text{diag}(c ,c,c, c )=cI$的对角阵，c为某个纯量
6. 大小相等的对角阵都 __可交换__（AB= BA）

### 超对角线， 次对角线

$A = [a_{ij}] \in \bf{M}_{n}$ (复方阵)

1. 超对角线（superdiagonal） 包含 $a_{12},a_{23},\cdots, a_{n-1,n}$ 的集合。对角线平行右上方。
2. 次对角线， 主对角线平行左下方。

### 三对角阵，双对角阵。

$A = [a_{ij}] \in \bf{M}_{n}$ (复方阵)

1. 若对任意 $|i-j| \geq 2$ 有$a_{ij}=0$ ,称三对角的（tridiagonal）。
2. 如果三对角阵的超对角线或此对角线的元素只有0，称双对角的（bidiagonal）

### 子矩阵

$A = [a_{ij}] \in \bf{M}_{m\times n}$

1. A 的子矩阵由A特定的行与列的交点处的元素组成的阵列。
2. A 的 $k\times k$ 主子矩阵（principal submatrix）i+1~ i+k 行，与i+1~ i+k列组成的。
3. 首主子矩阵(leading principal submatrix) ，1~k行，1~k列。
4. 尾主子矩阵(trailing principal submatrix)是 n-k+1 ~  n行， n-k+1 ~ n列交点处的元素组成的。

### 逆矩阵

对$A = [a_{ij}] \in \bf{M}_{n}$ (复方阵)

1. 如存在 $B \in \bf{M}_{n} $, 使得

   $$
   AB= I_n = BA
   $$

   , 称B为A的逆（inverse）
2. 如果A没有逆， 则称A是不可逆的(noninvertible)
3. 不是每个方阵都有逆。
4. 一个方阵至多只有一个逆。
5. 如果A可逆， 用$A^{-1}$表示A的逆。
6. A的逆满足

   $$
   AA^{-1}=I=A^{-1}A
   $$
7. .  对 $ad-bc \neq 0$ 的二方阵

   $$
   \begin{bmatrix}
   a & b  \\
   c & d  
   \end{bmatrix}^{-1}  =\frac{1}{ad-bc} \begin{bmatrix}
   d & -b  \\
   -c & a  
   \end{bmatrix}
   $$
8. 对于方阵A，　定义 $A^0=I$
9. 定义 $ A^k = AAAAA\text{(k个A)}$
10. 对于可逆的A，对于正整数ｋ，定义 $ A^{-k}= (A^{-1})^k$
11. 对A B是矩阵，j,k是整数,c是纯量，有

a. $ A^jA^k = A^{j+k} = A^kA^j      $
a. $  (A^{-1})^{-1} = A     $
a. $  (A^{j})^{-1} =A^{-j}    $
a. 若 $c\neq 0$, $(cA)^{-1}=c^{-1}A^{-1}       $
a. $ (AB)^{-1} = B^{-1}A^{-1}      $
a. $       $
a. $       $
a. $       $
a. $       $

### 转置矩阵

$A = [a_{ij}] \in \bf{M}_{m\times n}$ 的转置transpos,是矩阵 $A^T\in \bf{M}_{m\times n} $,位于$(i,j)$处的元素是$a_{ji}$.

设A，B为矩阵，c是纯量，有

1. $  (A^{T})^{T} = A     $
2. $  (A\pm B)^{T} = A^T \pm B^T      $
3. $ (cA)^T = cA^T      $
4. $  (AB)^T = B^TA^T     $
5. 若A可逆 $ (A^T)^{-1} = (A^{-1})^T       $

### 共轭矩阵

$A = [a_{ij}] \in \bf{M}_{m\times n}$ 的共轭（conjugate）是矩阵 $\overline A = [\overline a_{ij}] \in \bf{M}_{m\times n}$, 每个元素都是 $a_{ij}$ 的共轭复数 $\overline{ a_{ij}}$

有以下性质

1. $ \overline{(\overline A)}    =A   $
2. $  \overline{A+B} =\overline{A} + \overline{B}         $
3. $   \overline{AB} = \overline{A} \space \overline{B}        $
4. 如A的元素均为实数 $  \overline{A} = A          $
5. $           $
6. $           $

### 共轭转置矩阵

$A = [a_{ij}] \in \bf{M}_{m\times n}$  的共轭转置（conjugate transpose ） 是

$$
A^* = \overline{A^T}  = (\overline{A})^T  \in \bf{M}_{n\times m}
$$

A* 位于 $(i,j)$ 的元素是 $\overline{a_{ji}} $

1. 若A的元素均为实数, 则 $A^* = A^T$
2. 矩阵的共轭转置也称 *矩阵的伴随* （adjoint）

令A，B为矩阵， c为纯量， 有

1. $ I_n^* = In  $
2. $  0_{m \times n}^* = 0_{n \times m}         $
3. $ (A^*)^* =A           $
4. $  (A \pm B)^* = A^* \pm B^*         $
5. $  (cA)^* = \bar{ c}  A^*         $
6. $ (AB)^* = B^* A^*          $
7. 若A可逆 $  (A^*)^{-1}= (A^{-1})^* = A^{-*}   $ ,记为 $   A^{-*}= (A^{_1})^*      $

### 特殊矩阵

1. 若 $A^*=A$ ,则A是 Hermite(Hermitian)
2. 若 $A^*=-A$ ,则A是斜Hermite (skew Hermitian)
3. 若 $A^T=A$ 则A是对称的(symmetric); $A^T=-A$ ,A 是斜对称的。
4. 若 $A^* A=I　$ ，则A是酉的（unitary）;
5. 若 A 是实矩阵， $A^T A=I　$ , 则A是实正交的（real orthogonal）
6. 若 $A^* A=A A^*　$ , 则A是正规的(normal)
7. 若 $A^2=I　$ , 则A对合（involution）
8. 若 $A^2=A　$ ,则A幂等（imdepotent）
9. 若 k正整数 $A^k=0   $ ， 则A幂零（nilpotent）

### 迹

$A = [a_{ij}] \in \bf{M}_{n}$ 的迹（trace） ， 是A的主对角元素之和。

$$
\text{tr}\space A = \sum_{i=1}^{n}a_{ii}
$$

1. $   \text{tr}\space (  )      $
2. $   \text{tr}\space ( cA \pm B ) = c \text{tr}\space ( A)   \pm  \text{tr}\space ( B   )   $
3. $   \text{tr}\space (  A^T  ) =    \text{tr}\space ( A )      $
4. $ \text{tr}\space ( \overline{A}  )= \overline{ \text{tr}\space ( A )    }  $
5. $ \text{tr}\space ( A^*  )= \overline{ \text{tr}\space ( A )    }  $
6. A B 可乘， 则 $ \text{tr}\space ( AB  )  =  \text{tr}\space ( BA ) $
7. tr() 确保单方向相等， $ \text{tr}\space (ABC  ) =  \text{tr}\space ( CAB ) =  \text{tr}\space ( BCA )  $

## 线性方程组（system of linear equations）

一个$m \times n $的线性方程组，含有关于n个变量$x_1, \cdots, x_n$的m个线性方程,纯量$a_{ij}$是方程组的系数,纯量$b_i$是常数项.

1. 无解，称 *不相容* inconsistent.
2. 至少1组解， 称 *相容* consistent
3. 无穷多解

### 齐次方程组

常数项均为0 ， $b_i=0$

1. 每个其次方程组都有一组平凡解(trivial solution) $x_i=0$, 其他解称为非平凡解(nontrivial solution).
2. 齐次方程组只有两种可能： 无穷多解；只有平凡解。
3. 未知数个数>方程个数，有无穷多解。

### 线性方程组的矩阵表示

写成 $A \mathbf{x} x = \bf{b}$,
$A=[a_{mn}]$, $\mathbf{x} = [x_n]$ $\mathbf{b} = [b_m]$
粗体字母为*列向量*，形状 $\mathbf{M}_{n \times 1}$.

1. $\mathbb{C}^n $ 是 $\mathbf{M}_{n \times 1}(\mathbb{C}   ) $的简写
2. $\mathbb{R}^n $ 是 $\mathbf{M}_{n \times 1}(\mathbb{R}   ) $的简写
3. 列向量需排成行时， 记为 $\mathbf{x} = [x_1, x_2 , x_n ]^T$, 不写成竖直形式。
4. $m \times n$ 的齐次线性方程组可写为 $A\mathbf{x } = \mathbf{0}_m$ ,其中 $A\in \bf{M}_{m \times n}$, 如果可知尺寸,则简写为$\bf{0} $

### 简化的行梯矩阵

1. 三种出等运算解线性方程组：
   1.1 非0常数乘方程
   1.2 交换2个方程
   1.3 将方程的倍数加到另一方程
2. 方程组可写成 *增广矩阵* augmented matrix

$$
[A \space \bf{b}]
$$

3. 用初等运算后进行， 行的简化 （row reduce），成为简化的行梯形阵(reduced row echelon form)

### 初等矩阵

若对 $I_n$ 进行简单匀速那可得到的 $n\times n$ 的矩阵为*初等矩阵*(elementary matrix)

1. 初等矩阵可逆，它的逆也是初等矩阵
2. 某矩阵*左乘*一个*初等矩阵*，等同与对矩阵进行初等*行运算*

2.1 非0常数乘一行；

$$
\begin{bmatrix}
k & 0  \\
0 & 1  
\end{bmatrix} 
\begin{bmatrix}
a_{11} & a_{12}  \\
a_{21} & a_{22}  
\end{bmatrix}=
\begin{bmatrix}
ka_{11} & ka_{12}  \\
a_{21} & a_{22}  
\end{bmatrix}\\
$$

2.2 交换两行；

$$
\begin{bmatrix}
0 & 1  \\
1 & 0  
\end{bmatrix} 
\begin{bmatrix}
a_{11} & a_{12}  \\
a_{21} & a_{22}  
\end{bmatrix}=
\begin{bmatrix}
a_{21} & a_{22} \\
a_{11} & a_{12}  
 
\end{bmatrix}\\
$$

2.2 一行的非0倍数加到另一行；

$$
\begin{bmatrix}
1 & k  \\
0 & 1  
\end{bmatrix} 
\begin{bmatrix}
a_{11} & a_{12}  \\
a_{21} & a_{22}  
\end{bmatrix}=
\begin{bmatrix}
a_{11}+ka_{21} & a_{12}+ka_{12}  \\
a_{21} & a_{22}  
 
\end{bmatrix}\\
$$

## 行列式函数（入矩阵，输出标量）

$\text{det}: \bf{M}_N(\mathbb{C})\rightarrow \mathbb{C}$

数值应用优先，避免计算很大的行列式

### Laplace展开

可把 $n\times n $ 矩阵的行列式的计算归结为计算若干个（n-1）x(n-1)矩阵的行列式之和.

定义
$ \text{det}\space [a_{11}] = a_{11}$ 设 $n \geq 2 , A \in \bf{M}_{n}$

$A_{ij} \in \bf{M}_{n-1}$表示A中去掉第i行和第j列之后得到的 $(n-1)\times (n-1)$ 的矩阵,
则：
对于n内的整数ij，有：

$$
\text{det}\space A = \sum_{k=1}^{n} (-1)^{i+k} a_{ij} \space  \text{det}\space A_{ik}
$$

行加或列加均可。

量$\text{det}\space A_{ij} $ 称为  $A(i,j)$ 的 子式（minor）

$(-1)^{i+j} a_{ij} \space  \text{det}\space A_{ij}  $ 则成为 $A(i,j)$的 代数余子式(cofactor)

### 行列式与逆阵

$A \in \bf{M}_{n}$, 则A的*转置伴随阵*(adjugate)是 nxn矩阵

$$
\text{adj}\space A= [ (-1)^{i+j}  \text{det}\space   A_{ji}            ]
$$

adj A 是*代数余子式的矩阵*的*转置* 。满足:

$$
A  \space \text{adj}\space A  =  (  \text{adj}\space A) A =   (\text{det}\space A) \space I
$$

### 行列式的性质

设$A,B \in \bf{M}_n$,c是纯量，则：

1. $ \text{det}\space I  =1        $
2. $\text{det}\space A  \neq 0 \Longleftrightarrow   $ A可逆
3. $ \text{det}\space AB = (\text{det}\space A )(\text{det}\space B ) $
4. $ \text{det}\space AB =\text{det}\space BA  $
5. $ \text{det}\space (cA) = c^n \text{det}\space A  $
6. $ \text{det}\space \overline A   = \overline{ \text{det}\space A }$
7. $ \text{det}\space A^T = \text{det}\space A  $
8. $ \text{det}\space A^* = \overline{ \text{det}\space A }$
9. A可逆，$  \text{det}\space A^{-1} =  (\text{det}\space A)^{-1}$, detA 的倒数
10. 若 $A = [a_{ij}] \in \bf{M}_{n} $ 是上三角或下三角的，$ \text{det}\space A = a_{11}a_{22}\cdots a_{nn}$
11. 若 $A  \in \bf{M}_{n}(\mathbb{R})  $,则 $\text{det}\space A \in \mathbb{R}$
12. $ $
13. $ $

### 行列式的简化

### 置换与行列式

置换 permutation ，是一对一的函数。

1. 数列{1，-n} 的不同置换有 $n!$个
2. 对换 ，只交换数列的2个元素,其他元素不变，称对换（transpositino ）（swap in c++）
3. 置换可表示为对换的复合，其中含有的对换个数奇偶性只与置换有关。
4. 所需的对换的个数是偶数或奇数，称置换 $\sigma $ 是偶的（even） , 或奇的(odd)
5. $$
   \text{sgn}\space \sigma =  \begin{cases}  1,\text{ if } \space \sigma \text{ is even} \\ -1, \text{ if}  \space \sigma \text{ is odd}   \end{cases}
   $$
6. . $A = [a_{ij}] \in \bf{M}_{n}$ 的行列式可表示成：

$$
\text{det}\space A =  \sum_{\sigma}( \text{sgn} \space  \prod_{i=1}^{n}  a_{i\sigma(i)}      )
$$

其中求和取遍所有$n!$个置换

### 行列式、面积与体积

若 $ A = [\bf{a}_1,\bf{a}_2 ] \in \bf{M}_{2}(\mathbb{R}) $,
则：

1. $\left | \text{det}\space A    \right|  $ 是以 $\bf{a}_1  $， $\bf{a}_2$ 组成的平行四边形面积。

若 $ B = [\bf{b}_1,\bf{b}_2,\bf{b}_3 ] \in \bf{M}_{3}(\mathbb{R}) $,
则：

1. $\left | \text{det}\space B    \right|  $ 是以 $\bf{b}_1  $， $\bf{b}_2$， $\bf{b}_3$ 组成的平行六面体面积

## 数学归纳法

1. 若S1为真
2. Sn为真，则Sn+1为真

均为真，则n>=1 ,Sn为真。 是归纳假设(induction hypothesis).

1为base case ， 2. 为归纳步骤（induction step）

## 多项式

$c_0 , \cdots, c_k$是复数，次数为$k \geq 0$ 的复多项式，
形如：

$$
p(z) = c_kz^k + c_{k-1}z^{k+1} + \cdots + c_1 z + c_0, c_k\neq 0
$$

的函数。
纯量c是p的系数。
我们用 $\text{deg} \space p$ 记录 p的次数.

1. 如果所有的系数都是实数，则p是实多项式。零多项式是$p(z)=0$.约定零多项式的次数为 $-\infty$
2. 若ck=1 ,为*首1多项式*monic.
3. 实多项式是特殊的*复多项式*，默认指复多项式
4. $p(z)/c_k$是首1的
5. 若p,q是多项式， c是纯量，则，cp,p+q,pq 都是多项式。

### 零点与根

设 $\lambda $ 是一个复数，$ p $是一个多项式。

若 $p(\lambda)=0 $,称 $\lambda $ 是方程 $p(z)=0$的根。

1. 实多项式可能没有实的零点。如 $p(z)=z^2+1$ 无实零点，但有$\pm i$的复零点

定理，每个非常数的多项式在  $\mathbb{C}$ 中有一个零点。

### 辗转相除法

多项式形式的*带余数* 的长除法成为 *辗转相除法*（division algorithm ）

1. 如果多项式f,g, 满足 $ 1\leq \text{deg} \space g \leq \text{deg} \space f$ , 则：
   1.1 存在唯一多项式 q,r，使得 $ f=gq+r$, 且 $\text{deg} \space r < \text{deg} \space g $
   1.2 f被除式dividend  ， g除式divisor ， q商quotient ，r余式remainder

### 因式分解与零点的重数

对于多项式p可分解为

$$
p(z)= c_k(z-\lambda_1)(z-\lambda_2)\cdots(z-\lambda)_k
$$

其中的复数$\lambda_n$是p的零点。分解后最高的指数$n_i$ ,是p的零点$\mu_i$的重数（multiplicity）
从而n1 + ... nn = deg p

### 多项式恒等定理

设f,g 为多项式，假设 $\text{deg} \space f=n \geq 1$, 则:

1. f的零点的*重数*之和等于n
2. f至多有n个相异的零点
3. 零多项式判据
4. 多项式相等判据
5. g(z)=0 ,g 是0多项式
6. 如果fg是零多项式，那么g是零多项式。

### Lagrange插值

定理（Lagrange插值）。令 $n \geq 1$,设 $z_1 ... z_n$是相异的复数，设$w_1,w_n \in \mathbb{C}$,
则 ：

1. 存在唯一一个次数至多为 $n-1$ 的多项式p, 使得对1， n ,有

$$
(z_i) = w_i\mathscr{L}_i
$$

。
如果z,w 均为实，则p是实多项式。

2. 使用方法：
   小l函数(n>=2)

$$
\mathscr{l}_j(z) = \prod_{k=1, 跳过 k=j        }^{n}   \frac{z-z_k } {z_j-z_k}
$$

2.1 根据数据点，写出n个小l，拟合n-1次p(z)
四对数据（w1,z1; w2,z2; w3,z3; w4,z4）
形式如
若n=4

$$
\mathscr{l}_1(z) =  \frac{z-z_2 } {z_1-z_2} \frac{z-z_3 } {z_1-z_3} \frac{z-z_4 } {z_1-z_4}
$$

$$
\mathscr{l}_2(z) =  \frac{z-z_1 } {z_2-z_1} \frac{z-z_3 } {z_2-z_3} \frac{z-z_4 } {z_2-z_4}
$$

$$
\mathscr{l}_3(z) =  \frac{z-z_1 } {z_3-z_1} \frac{z-z_2 } {z_3-z_2} \frac{z-z_4 } {z_3-z_4}
$$

$$
\mathscr{l}_4(z) =  \frac{z-z_1 } {z_4-z_1} \frac{z-z_2 } {z_4-z_2} \frac{z-z_3 } {z_4-z_3}
$$

2.2 带入

$$
p(z_k)=\sum_{j=i}^{n} w_jl_j(z) =w_k
$$

展开

$$
p(z_1) = w_1l_1(z_1) +w_2l_2(z_1)  +w_3l_3(z_1) + +w_4l_4(z_1)   = w_1
$$

$$
p(z_2) = w_1l_1(z_2) +w_2l_2(z_2)  +w_3l_3(z_2) + +w_4l_4(z_2)   = w_2
$$

$$
p(z_3) = w_1l_1(z_3) +w_2l_2(z_3)  +w_3l_3(z_3) + +w_4l_4(z_3)   = w_3
$$

$$
p(z_4) = w_1l_1(z_4) +w_2l_2(z_4)  +w_3l_3(z_4) + +w_4l_4(z_4)   = w_4
$$

解出(w1,w2,w3,w4)
带入得出拟合多项式$p(z) $

---

**Lagrange插值**

n个数对， 2n个方程，拟合最高次（n-1）的多项式,

---
  
### 多项式与矩阵
若$A  \in \bf{M}_{n}$
定义 $$p(A) = c_kA^k +c_{k-1}A^{k-1} + \cdots + c_1A + c_0 I $$

若p,q 为多项式，有
1. $p(A) + q(A ) = (p+q)(A)$
2. $p(A) q(A ) = (pq)(A) = (qp)(A) = q(A) p(A ) $

对于对角阵（除主对角线元素外，均为0）: $\Lambda= \text{diag}( \lambda_1 + \cdots + \lambda_n         )$，有
$p(\Lambda)=\text{diag}( p(\lambda_1), p(\lambda_2) ,\cdots ,  p(\lambda_n)           )   $

### 缠绕

设 $A\in \bf{M}_{m }, B\in \bf{M}_{n }, X\in \bf{M}_{m \times n }$, 若 $AX=XB$ ,称X缠绕（intertwine）AB


1. 若X方阵且可逆  ($X X^{-1}= I$)  $\Longleftrightarrow A=XBX^{-1}$

2. 若AX=XB ，则对任意多项式$p$, 有$$p(A)X=Xp(B)$$. 此外，A与p(A)可交换 ？？


### 相似(等尺寸方阵)

设 $A, B, X\in \bf{M}_{n }$,
$XX^{-1}=I$  , p是多项式.
若 $A=XBX^{-1}$  那么$AX=XB$
1. $p(A)X=Xp(B)       $ $\Longrightarrow$
2. $p(A)=Xp(B)X^{-1}     $
3. 对于对角阵（除主对角线元素外，均为0）: $B = \Lambda= \text{diag}( \lambda_1 + \cdots + \lambda_n         )$，有
$p(A) = Xp(\Lambda)X^{-1}=X\text{diag}( p(\lambda_1), p(\lambda_2) ,\cdots ,  p(\lambda_n)           ) X^{-1}  $

4. 若 $p(z)=z+c $,(多项式为首1的1次多项式)， 有平移性质(shift property)
$A=XBX^{-1}$ $\Longrightarrow$ 
$$        A +cI = X(B+cI) X^{-1}$$