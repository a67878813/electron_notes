# 基与相似性
生成一个向量空间的线性无关向量组有特殊重要性。它们在向量空间这个抽象的世界与矩阵这个具体的世界之间提供了一座链接的桥梁。
允许我们定义向量空间的位数，并有道产生出*矩阵相似性*的概念。
在秩与矩阵的零度之间的关系中，它们处于中心的地位。

## 基 basis
设 $\Large u$ 是  $ \mathbb{F}$ 向量空间 $\Large\nu$ ，n是正整数 $\beta=\mathbf{v}_1 \cdots \mathbf{v}_r $ 称为是 $\Large \nu$ 的一组*基*（basis）， 如果 $\text{span}\space \beta=\Large\nu$，且 $\beta$ 线性无关。

例子
1. 设 $\Large u$ 是  $ \mathbb{R}^2$ 向量空间 ,向量组 
$$
\beta=
\left[ \begin{array}{ccc}
2 & 1 
\end{array} 
\right ]^T , 
\left[ \begin{array}{ccc}
1 & 1 
\end{array} 
\right ]^T
$$
令 $A =\beta$ 则 $\beta $ 的生成空间形如


$$


x_1 
\left[ \begin{array}{ccc}
2 \\ 1
\end{array} 
\right ]
+
x_2 
\left[ \begin{array}{ccc}
1\\ 1
\end{array} 
\right ]
=
\left[ \begin{array}{ccc}
2& 1 \\
1&1
\end{array} 
\right ]
\left[ \begin{array}{ccc}
x_1\\ x_2
\end{array} 
\right ]
=
A\mathbb{x}



$$
的向量组成.
计算给出：
$$A^{-1} = \left[ \begin{array}{}
1& -1 \\
-1& 2
\end{array} 
\right ] $$
于是，任何 $\mathbf{y}= \left[ \begin{array}{}y_1 & y_2\end{array}\right ]^T \in \mathbb{R}^2$ 都可以用唯一的方式表示称 $\mathbf{y}=A\mathbf{x}$,
其中
$$ \mathbf{x} =A^{-1}\mathbf{y}=
\left[ \begin{array}{}
y_1  -y_2 \\
-y_1  + 2y_2
\end{array}\right ]

$$

以上证明了 $\text{span}\space \beta = \mathbb{R}^2$ ,且$\beta$线性无关。
从而 $\beta$ 是 $\mathbb{R}^2$ 的一组基。

**定理**
1. 设 $A= \left[ \begin{array}{} \mathbf{a}_1 \mathbf{a}_2 \cdots  \mathbf{a}_2n \end{array}\right ] \in \mathbf{M}_n(\mathbb{F})  $ 可逆，又设 $\beta = \mathbf{a}_1 ,\cdots, \mathbf{a}_n$ . 
那么 ，$\beta$ 是 $\mathbb{F}^n$ （n行1列）的一组基。

理解：
$\mathbf{M}_n(\mathbb{F}) $中的任何可逆矩阵的列都生成 $\mathbb{F}^n$ 且是线性无关的。

引理：
1. （替换引理）
设 $\Large \nu$ 是 非零 $ \mathbb{F}$ 向量空间 ，r是正整数 $\beta=\mathbf{u}_1 \cdots \mathbf{u}_r $ 称为是 $\Large \nu$ ,生成  $\Large \nu$ 。
设 $\mathbf{v} \in \Large\nu$ 是非零向量。
令 
$$
\mathbf{v} = \sum_{i=1}^{r} c_i\mathbf{u}_i
$$ 
那么：
- 1.1    （非零向量系数非平凡） 对于某个 $j \in \{ 1,2, \cdots, r\}$ 有 $c_j \not= 0$
- 1.2  （换基） 如果  $c_j \not= 0$ ， 那么
$$
\mathbf{v}, \mathbf{u}_1 , \mathbf{u}_2 \cdots,  \hat{\mathbf{u}}_j \cdots,  \mathbf{u}_r
$$
是 $\Large \nu$ 的一组基。

- 1.3   1.2是一组基
- 1.4 如果 $r \geq 2 $ 且 $\beta $ 是 $\Large \nu$ 的一组基
且对某个 $k \in \{1,2, \cdots , r-1 \}$ 有 $\mathbf{v}\not\in \text{span}\space \{\mathbf{u}_1,\cdots ,\mathbf{u}_k \}$ ,
那么存在一个指标 $j \in \{ k+1, k+2 \cdots , r \}$, 使得
$$
\mathbf{v},\mathbf{u}_1,\mathbf{u}_2,\cdots,\mathbf{u}_k,\mathbf{u}_{k+1},\hat{\mathbf{u}}_j,\cdots,\mathbf{u}_r
$$
是 $\Large \nu$ 的一组基。
（在V内不在(1-k的基)的生成空间内的 v, 存在(k~ r)的v和戴帽u_j(k~ r)）的一组基生成V。

定理
1.1 V的基中元素个数是V的任何线性无关向量组中元素个数的上界。

1.1 设 $\Large \nu$ 是 非零 $ \mathbb{F}$ 向量空间 ，r,n是正整数 。如果 $\beta=\mathbf{u}_1 \cdots \mathbf{u}_n$ 是 $\Large \nu$ 的一组基，而 $\gamma=\mathbf{v}_1 \cdots \mathbf{v}_r$ 是 $\Large \nu$  线性无关， 那么 $r\leq n$ 。
如果 $r=n$ ， 那么 $\gamma$ 是 $\Large \nu$ 的一组基。

（beta向量组减u加v，新gamma是大nu的基）

推论 
1.2 设r,n 是正整数， 如果 $\mathbf{v}_1 \cdots \mathbf{v}_n$ ，  $\mathbf{w}_1 \cdots \mathbf{w}_r$ 都是 $ \mathbb{F}$ 向量空间  $\Large \nu$  的基，则r=n
证明,上一定理保证 $r\leq n$ , $n\leq r$



## 维数

定义 1.1 设 $\Large \nu$ 是 非零 $ \mathbb{F}$ 向量空间,n是正整数 。如果存在一列向量  $\mathbf{v}_1 \cdots \mathbf{v}_r$ 是 $\Large \nu$ 的一组基，那么称：
 $\Large \nu$ 是n维的。(n-dimensional)
 零向量空间的维数为0（dimension zero）.
如果对某个非负整数n， $\Large \nu$ 的维数为n， 那么称 $\Large \nu$ 是 *有限维的*（finite dimensional）;反之则称 $\Large \nu$ 是 *无限维的* （infinite dimensional）。
如果 $\Large \nu$ 是有限维的， 就记它的维数为 $\text{dim}\space \Large \nu$ .

例
向量  $\mathbf{e}_1 \cdots \mathbf{e}_n$ 线性无关，且它们的生成空间是 $\mathbb{F}^n$  . 它们构成  $\mathbb{F}^n$ 的标准基（standard basis）. 这组基里有n个向量，所以  $\text{dim}\space \mathbb{F}^n =n$ .

例
对 $1 \leq p \leq m$ ,  $1 \leq q \leq n$ , 在 $\mathbb{F}-$ 向量空间 $\mathbf{M}_{m \times n}(\mathbb{F})$  中考虑矩阵 $\mathbf{E}_{pq}$ , 定义如下
 $\mathbf{E}_{pq}$  位于 $(i,j)$ 处的元素当 $(i,j)=(p,q)$ 时取值为1， 反之则取值为零。 mn个矩阵  $\mathbf{E}_{pq}$ （次序随意排列） 构成一组基， 所以 $\text{dim}\space \mathbf{M}_{m \times n}(\mathbb{F})= mn$.

例
n无线==>大nu无限。

定义：
设 $A = [\mathbf{a}_n] \in \mathbf{M}_{m\times n}(\mathbb{F})$ , 又设 $\beta = \mathbf{a}_n$ 是   $\mathbb{F}^m$ 中的一向量列表。 
那么 $\text{dim} \space \text{span}\beta  = \text{dim} \space \text{col} A   $ 称为A的*秩*(rank).

（矩阵A的秩，　指的是（矩阵列向量的生成空间）的维度  ）    （可以比矩阵大小更低）
*满秩*、*欠秩*，  rand(A)   r(A).

结论
1. 生成  $\Large \nu$ 的任何有限集合都包含一个子集，该子集的元素构成一组基； 、
（生成空间为大nu的有限集合均包含*可构成基的子集*）
2. 如果  $\Large \nu$ 是有限维的，那么任何线性无关向量组都可以被扩充成一组基。
2. 假设  $\Large \nu$ 是有限维的 ， 且 $\text{dim} \space \Large\nu \normalsize =n \geq r $ ,如果  $\mathbf{v}_1 \cdots \mathbf{v}_r$  线性无关，那么：
存在 $n-r$ 个向量   $\mathbf{w}_1 \cdots \mathbf{w}_{n-r} \in \Large\nu $ ,使得 $\mathbf{v}_1 \cdots \mathbf{v}_r , \mathbf{w}_1 \cdots \mathbf{w}_{n-r} $ 是  $\Large \nu$ 的一组基。

基： *极大线性无关组*(maximal linearly independent list) , 或
*极小生成向量组*(minimal spanning list)

推论 2.2.8 设 n是正整数，  $\Large \nu$ 是 n维 $\mathbb{F}$  向量空间。 设 $\beta=\mathbf{v}_1 \cdots \mathbf{v}_n \in \Large\nu $
1. 如果   $\beta$  生成 $\Large \nu$ ，那么它是一组基
2. 如果   $\beta$  线性无关，那么它是一组基

定理 2.2.9 设 $\Large u$ 是 n维 $\mathbb{F}$  向量空间 $\Large \nu$ 的一个子空间。那么 $\Large \nu$ 是有限维的，且 $\text{dim}\space \Large u\normalsize \leq n$
,其中的等式成立当且仅当 $ \Large u\normalsize = \Large \nu$ 
