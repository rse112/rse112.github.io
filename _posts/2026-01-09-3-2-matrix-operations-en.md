---
title: "3.2 Matrix Operations"
date: 2026-01-09 00:00:00 +0900
categories: [Linear Algebra, Matrices]
tags: [linear algebra, mathematics, matrices]
math: true
lang: en
hreflang_ko: /posts/3-2-matrix-operations/
---


## Introduction

When you use a map app, you might rotate the view by 30 degrees and then zoom in by a factor of 2. You could apply these two operations one after the other, but what if you could combine them into a single operation -- "rotate, then zoom" -- all at once? That is exactly what **matrix multiplication** does. It lets you encode the composition of two transformations into a single matrix.

Matrix operations include addition, scalar multiplication, and matrix multiplication. Among these, matrix multiplication follows rules that differ from ordinary multiplication of numbers, and understanding these differences is foundational to all of linear algebra.

---

## Matrix Addition and Subtraction

### Definition

Two matrices can be added or subtracted only when they have the **same dimensions**. The operation is performed entry by entry.

$$(A + B)_{ij} = a_{ij} + b_{ij}$$
$$(A - B)_{ij} = a_{ij} - b_{ij}$$

### Example

$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}$$

![Matrix addition visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_2_MatrixAddition.gif)

### Properties

$$A + B = B + A \quad \text{(commutativity)}$$
$$(A + B) + C = A + (B + C) \quad \text{(associativity)}$$
$$A + O = A \quad \text{(additive identity)}$$
$$A + (-A) = O \quad \text{(additive inverse)}$$

---

## Scalar Multiplication

### Definition

Multiplying a scalar (a real number) $c$ by a matrix $A$ means multiplying every entry of $A$ by $c$.

$$(cA)_{ij} = c \cdot a_{ij}$$

### Example

$$3 \begin{pmatrix} 1 & -2 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 3 & -6 \\ 0 & 12 \end{pmatrix}$$

### Properties

$$c(A + B) = cA + cB$$
$$(c + d)A = cA + dA$$
$$(cd)A = c(dA)$$
$$1 \cdot A = A$$

---

## Matrix Multiplication

### Size Requirement

If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, then the product $AB$ is defined only when **the number of columns of $A$ equals the number of rows of $B$**. The result is an $m \times p$ matrix.

$$\underbrace{A}_{m \times n} \cdot \underbrace{B}_{n \times p} = \underbrace{AB}_{m \times p}$$

### Definition

The entry $(AB)_{ij}$ is the **dot product** of the $i$-th row of $A$ and the $j$-th column of $B$.

$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{in}b_{nj}$$

### Example

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

$$AB = \begin{pmatrix} 1\cdot5+2\cdot7 & 1\cdot6+2\cdot8 \\ 3\cdot5+4\cdot7 & 3\cdot6+4\cdot8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

![Matrix multiplication visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_2_MatrixMultiplication.gif)

---

## Properties of Matrix Multiplication

### Associativity (holds)

$$(AB)C = A(BC)$$

This means that when composing three transformations in sequence, it does not matter which pair you group first -- the result is the same.

### Distributivity (holds)

$$A(B + C) = AB + AC$$
$$(A + B)C = AC + BC$$

### Multiplication by the Identity

$$AI = IA = A$$

### Commutativity (does NOT hold in general)

$$AB \neq BA \quad \text{(in general)}$$

This is the single most important property to remember about matrix multiplication. For ordinary numbers, $ab = ba$ always. For matrices, it almost never holds.

**Counterexample:**

$$A = \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 1 \\ 0 & 2 \end{pmatrix}$$

$$AB = \begin{pmatrix} 0 & 5 \\ 0 & 0 \end{pmatrix}, \quad BA = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$

Clearly $AB \neq BA$.

### Zero Divisors Exist

For ordinary numbers, if $ab = 0$ then $a = 0$ or $b = 0$. For matrices, it is possible that $AB = O$ even when neither $A$ nor $B$ is the zero matrix.

In the counterexample above, $BA = O$ yet $A \neq O$ and $B \neq O$.

---

## Geometric Meaning of Matrix Multiplication

Applying $B$ to a vector $\vec{x}$ and then applying $A$ to the result gives:

$$(AB)\vec{x} = A(B\vec{x})$$

In other words, the matrix $AB$ represents the **composite transformation**: "first apply $B$, then apply $A$."

---

## Key Takeaways

| Concept | Description / Formula |
|---------|-----------------------|
| Matrix addition | Defined only for same-size matrices; entry-wise addition |
| Scalar multiplication | Multiply every entry by the scalar |
| Size requirement for product | $m \times n$ times $n \times p$ yields $m \times p$ |
| Product entry formula | $(AB)_{ij} = \sum_k a_{ik} b_{kj}$ |
| Associativity | $(AB)C = A(BC)$ holds |
| Commutativity | $AB \neq BA$ in general |
| Distributivity | $A(B+C) = AB + AC$ holds |
| Geometric meaning | Matrix product = composition of linear transformations |

> In the next post, we explore the **inverse matrix and the determinant** -- the essential tools for solving the matrix equation $A\vec{x}=\vec{b}$.
