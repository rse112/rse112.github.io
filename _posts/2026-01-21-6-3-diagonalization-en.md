---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_3_DiagonalizationExample.gif
title: "6.3 Diagonalization"
date: 2026-01-21 00:00:00 +0900
categories: [Linear Algebra, Eigenvalues and Eigenvectors]
tags: [linear algebra, mathematics, eigenvalues and eigenvectors]
math: true
lang: en
hreflang_ko: /posts/6-3-diagonalization/
---


## Introduction

Imagine you need to compute $A^{30}$. Multiplying a matrix by itself 30 times is tedious and error-prone. But what if $A$ were a diagonal matrix? Then $D^{30}$ is trivial -- you just raise each diagonal entry to the 30th power. **Diagonalization** extends this idea to general matrices. By using eigenvalues and eigenvectors, we can treat a complicated matrix as if it were essentially diagonal.

Beyond its mathematical elegance, diagonalization is a workhorse in applications. Solving systems of differential equations, predicting long-run probabilities in Markov chains, analyzing coupled oscillators in physics -- diagonalization turns complex iterative computations into simple ones.

---

## Definition of Diagonalization

### $A = PDP^{-1}$

An $n \times n$ matrix $A$ is **diagonalizable** if it can be factored as:

$$A = PDP^{-1}$$

where:
- $D$ is a diagonal matrix with the eigenvalues on its diagonal
- $P$ is an invertible matrix whose columns are the corresponding eigenvectors
- $P^{-1}$ is the inverse of $P$

![Diagonalization formula A = PDP^{-1} visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_3_DiagonalizationFormula.gif)

$$D = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}, \qquad P = \begin{pmatrix} | & | & & | \\ \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \\ | & | & & | \end{pmatrix}$$

---

## Conditions for Diagonalizability

### $n$ Linearly Independent Eigenvectors

An $n \times n$ matrix $A$ is diagonalizable if and only if it has **$n$ linearly independent eigenvectors**.

When this holds, the matrix $P$ formed by placing these eigenvectors as columns is invertible.

**Sufficient condition:** If $A$ has $n$ distinct eigenvalues, it is automatically diagonalizable. (Eigenvectors corresponding to distinct eigenvalues are always linearly independent.)

However, repeated eigenvalues do not necessarily prevent diagonalization. If the geometric multiplicity equals the algebraic multiplicity for every eigenvalue, the matrix is still diagonalizable. When these multiplicities differ, it is not.

### A Non-Diagonalizable Example

$$B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

Characteristic equation: $(1-\lambda)^2 = 0 \Rightarrow \lambda = 1$ (multiplicity 2)

Solving $(B - I)\vec{v} = \begin{pmatrix}0&1\\0&0\end{pmatrix}\vec{v} = \vec{0}$ gives: $\vec{v} = t\begin{pmatrix}1\\0\end{pmatrix}$

There is only one linearly independent eigenvector, so $B$ is **not diagonalizable**.

---

## A Worked Example

### The Matrix

Let us diagonalize the matrix from Section 6.2:

$$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$$

Eigenvalues: $\lambda_1 = 5$, $\lambda_2 = 2$

Eigenvectors: $\vec{v}_1 = \begin{pmatrix}1\\1\end{pmatrix}$, $\vec{v}_2 = \begin{pmatrix}1\\-2\end{pmatrix}$

### Constructing $P$, $D$, and $P^{-1}$

$$P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}, \qquad D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}$$

Computing $P^{-1}$: $\det(P) = (1)(-2) - (1)(1) = -3$

$$P^{-1} = \frac{1}{-3}\begin{pmatrix} -2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2/3 & 1/3 \\ 1/3 & -1/3 \end{pmatrix}$$

### Verification: $A = PDP^{-1}$

$$PDP^{-1} = \begin{pmatrix}1&1\\1&-2\end{pmatrix}\begin{pmatrix}5&0\\0&2\end{pmatrix}\begin{pmatrix}2/3&1/3\\1/3&-1/3\end{pmatrix}$$

$$= \begin{pmatrix}5&2\\5&-4\end{pmatrix}\begin{pmatrix}2/3&1/3\\1/3&-1/3\end{pmatrix} = \begin{pmatrix}4&1\\2&3\end{pmatrix} = A \checkmark$$

![Diagonalization calculation example visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_3_DiagonalizationExample.gif)

---

## The Power of Diagonalization: Matrix Powers

### $A^k = PD^kP^{-1}$

The most powerful application of diagonalization is computing matrix powers efficiently:

$$A^k = (PDP^{-1})^k = PD^kP^{-1}$$

To see why, observe how the middle terms telescope:

$$A^2 = (PDP^{-1})(PDP^{-1}) = PD(P^{-1}P)DP^{-1} = PD^2P^{-1}$$

$$A^k = PD^kP^{-1}$$

And raising a diagonal matrix to the $k$-th power is trivial -- just raise each diagonal entry:

$$D^k = \begin{pmatrix} \lambda_1^k & 0 & \cdots & 0 \\ 0 & \lambda_2^k & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n^k \end{pmatrix}$$

### Example: Computing $A^{10}$

$$A^{10} = PD^{10}P^{-1} = \begin{pmatrix}1&1\\1&-2\end{pmatrix}\begin{pmatrix}5^{10}&0\\0&2^{10}\end{pmatrix}\begin{pmatrix}2/3&1/3\\1/3&-1/3\end{pmatrix}$$

$5^{10} = 9{,}765{,}625$, $2^{10} = 1{,}024$

Instead of multiplying the matrix 30 times, we get the answer in just a few computations.

---

## Diagonalization and Linear Recurrences

### Application to the Fibonacci Sequence

The Fibonacci recurrence $F_{n+2} = F_{n+1} + F_n$ can be expressed in matrix form:

$$\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix}$$

Diagonalizing this matrix leads to a closed-form formula for $F_n$.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Diagonalization definition | $A = PDP^{-1}$ |
| Columns of $P$ | Linearly independent eigenvectors $\vec{v}_1, \ldots, \vec{v}_n$ |
| Diagonal of $D$ | Corresponding eigenvalues $\lambda_1, \ldots, \lambda_n$ |
| Diagonalizability condition | $n \times n$ matrix must have $n$ linearly independent eigenvectors |
| Sufficient condition | $n$ distinct eigenvalues |
| Matrix powers | $A^k = PD^kP^{-1}$ |
| Computing $D^k$ | Raise each diagonal entry to the $k$-th power |
| Not diagonalizable | Fewer than $n$ linearly independent eigenvectors |

> Next up: **The Geometric Meaning of Eigenvalues** -- a deeper look at what eigenvalues reveal about transformations, including symmetric matrices and the spectral decomposition.
