---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_1_MatrixIntro.gif
title: "3.1 What is a Matrix?"
date: 2026-01-08 00:00:00 +0900
categories: [Linear Algebra, Matrices]
tags: [linear algebra, mathematics, matrices]
math: true
lang: en
hreflang_ko: /posts/3-1-what-is-matrix/
---


## Introduction

Imagine you run a store that sells three products: A, B, and C. You need to keep track of each product's price, inventory, and sales figures. The most natural approach? Arrange the data in a table -- rows for the products, columns for the attributes. At a glance, you can see everything.

In mathematics, this rectangular arrangement of numbers is called a **matrix**. But a matrix is far more than a data table. Write a system of equations in matrix form, and you can solve it systematically. Represent rotation, scaling, or reflection as a single matrix, and you can transform entire spaces with one multiplication. Matrices are the universal language of modern mathematics, physics, computer science, and machine learning.

---

## Definition of a Matrix

### Basic Definition

An **$m \times n$ matrix** is a rectangular array of numbers with $m$ rows and $n$ columns.

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$

The entry $a_{ij}$ sits in the $i$-th row and $j$-th column. A useful mnemonic: the row index always comes first, then the column index -- just like how you say "Row $i$, Column $j$."

![Matrix dimension visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_1_MatrixDimension.gif)

### Connection to Systems of Equations

Consider the following system of linear equations:

$$\begin{cases} 2x + 3y = 5 \\ x - y = 1 \end{cases}$$

Collect the coefficients into a matrix:

$$A = \begin{pmatrix} 2 & 3 \\ 1 & -1 \end{pmatrix}, \quad \vec{x} = \begin{pmatrix} x \\ y \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$$

Now the entire system collapses into a single matrix equation:

$$A\vec{x} = \vec{b}$$

![Matrix introduction visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_1_MatrixIntro.gif)

---

## Special Matrices

### Zero Matrix

A matrix whose entries are all zero. It serves as the additive identity.

$$O = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$

For any matrix $A$ of the same size, $A + O = A$.

### Identity Matrix

A **square matrix** with ones on the main diagonal and zeros everywhere else. It serves as the multiplicative identity.

$$I_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix}$$

For any matrix $A$ of compatible size, $AI = IA = A$.

### Square Matrix

A matrix with the same number of rows and columns, i.e., an $n \times n$ matrix. Many important concepts -- such as the inverse and the determinant -- are defined only for square matrices.

### Diagonal Matrix

A square matrix where every off-diagonal entry is zero.

$$D = \begin{pmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{pmatrix}$$

Multiplying two diagonal matrices is especially easy: just multiply the corresponding diagonal entries.

---

## The Transpose

### Definition

The **transpose** of a matrix $A$, written $A^T$, is the matrix obtained by swapping rows and columns. In other words, $(A^T)_{ij} = A_{ji}$.

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \implies A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

If $A$ is $m \times n$, then $A^T$ is $n \times m$.

### Properties of the Transpose

$$\left(A^T\right)^T = A$$
$$(A + B)^T = A^T + B^T$$
$$(cA)^T = cA^T$$
$$(AB)^T = B^T A^T \quad \text{(note the reversal of order!)}$$

---

## Symmetric Matrices

A square matrix that equals its own transpose is called a **symmetric matrix**.

$$A^T = A \quad \Leftrightarrow \quad a_{ij} = a_{ji}$$

Symmetric matrices look the same on either side of the main diagonal. They appear everywhere in practice: covariance matrices in statistics, adjacency matrices of undirected graphs, and many more.

$$S = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 4 \\ 3 & 4 & 6 \end{pmatrix}$$

Conversely, a matrix satisfying $A^T = -A$ is called a **skew-symmetric matrix**.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| $m \times n$ matrix | Rectangular array with $m$ rows, $n$ columns; entries $a_{ij}$ |
| Zero matrix | All entries are 0; $A + O = A$ |
| Identity matrix | Diagonal entries are 1, rest 0; $AI = IA = A$ |
| Square matrix | Row count = column count ($n \times n$) |
| Diagonal matrix | All off-diagonal entries are 0 |
| Transpose | $(A^T)_{ij} = A_{ji}$; $(AB)^T = B^T A^T$ |
| Symmetric matrix | $A^T = A$, i.e., $a_{ij} = a_{ji}$ |

> In the next post, we explore **matrix operations** -- addition, subtraction, scalar multiplication, and the rules of matrix multiplication.
