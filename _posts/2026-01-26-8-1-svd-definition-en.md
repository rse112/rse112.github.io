---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_1_SVDFormula.gif
title: "Singular Value Decomposition (SVD) - Definition and Computation"
date: 2026-01-26 00:00:00 +0900
categories: [Linear Algebra, SVD]
tags: [linear algebra, mathematics, SVD]
math: true
lang: en
hreflang_ko: /posts/8-1-svd-definition/
---


## Introduction

In the world of matrix factorizations, the SVD (Singular Value Decomposition) stands alone as the most powerful and versatile tool. Eigenvalue decomposition only applies to square matrices. Diagonalization fails for many matrices. QR decomposition is specialized for certain equation-solving tasks. But the SVD applies to **every matrix** -- rectangular or square, invertible or singular, no exceptions.

The essential idea behind the SVD is beautiful: any linear transformation, no matter how complicated, can be decomposed into three simple operations -- **rotate, stretch along the axes, rotate again**. This decomposition reveals hidden structure in a matrix (its rank, condition number, and most important directions) with striking clarity. In modern data science, image compression, recommendation systems, and natural language processing, the SVD is an indispensable core tool.

---

## Definition of the SVD

### $A = U\Sigma V^T$

For any real matrix $A \in \mathbb{R}^{m \times n}$, there exists a decomposition:

$$A = U\Sigma V^T$$

![Visualization of the SVD formula $A = U\Sigma V^T$](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_1_SVDFormula.gif)

Here is what each piece does:

| Matrix | Size | Property | Meaning |
|--------|------|----------|---------|
| $U$ | $m \times m$ | Orthogonal ($U^TU = I$) | Left singular vectors |
| $\Sigma$ | $m \times n$ | Diagonal entries are the singular values | Scaling information |
| $V$ | $n \times n$ | Orthogonal ($V^TV = I$) | Right singular vectors |

The structure of $\Sigma$ (where $r = \text{rank}(A)$):

$$\Sigma = \begin{pmatrix} \sigma_1 & & & & \\ & \sigma_2 & & & \\ & & \ddots & & \\ & & & \sigma_r & \\ & & & & 0 \end{pmatrix}$$

The singular values are arranged in descending order: $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots$

---

## The Meaning and Computation of Singular Values

### $\sigma_i = \sqrt{\lambda_i(A^TA)}$

The singular values $\sigma_i$ are the positive square roots of the eigenvalues of $A^TA$:

$$\sigma_i = \sqrt{\lambda_i(A^TA)}, \quad \lambda_1 \geq \lambda_2 \geq \cdots \geq 0$$

Why does this work? The matrix $A^TA$ is always a **symmetric positive semidefinite** matrix, so all of its eigenvalues are $\geq 0$.

**Proof sketch:**

Let $\vec{v}_i$ be the eigenvectors of $A^TA$ (so that $A^TA\vec{v}_i = \lambda_i \vec{v}_i$). Then:

$$\sigma_i = \sqrt{\lambda_i}, \quad \vec{u}_i = \frac{1}{\sigma_i}A\vec{v}_i \quad (\text{when } \sigma_i \neq 0)$$

One can verify that the matrices constructed this way satisfy $A = U\Sigma V^T$.

---

## Example: SVD of a 2x3 Matrix

### Worked Example

$$A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}$$

**Step 1: Compute $A^TA$**

$$A^TA = \begin{pmatrix}3&2\\2&3\\2&-2\end{pmatrix}\begin{pmatrix}3&2&2\\2&3&-2\end{pmatrix} = \begin{pmatrix}13&12&2\\12&13&-2\\2&-2&8\end{pmatrix}$$

**Step 2: Find eigenvalues of $A^TA$ (squares of the singular values)**

Solving the characteristic equation gives: $\lambda_1 = 25$, $\lambda_2 = 9$, $\lambda_3 = 0$

Singular values: $\sigma_1 = 5$, $\sigma_2 = 3$

**Step 3: Construct $V$ (eigenvectors of $A^TA$)**

$$\vec{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix}, \quad \vec{v}_2 = \frac{1}{\sqrt{18}}\begin{pmatrix}1\\-1\\4\end{pmatrix}, \quad \vec{v}_3 = \frac{1}{3}\begin{pmatrix}2\\-2\\-1\end{pmatrix}$$

**Step 4: Construct $U$**

$$\vec{u}_1 = \frac{1}{\sigma_1}A\vec{v}_1 = \frac{1}{5} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}5\\5\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$$

$$\vec{u}_2 = \frac{1}{\sigma_2}A\vec{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}$$

$$\Sigma = \begin{pmatrix}5&0&0\\0&3&0\end{pmatrix}$$

![Visualization of the SVD components $U$, $\Sigma$, $V$](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_1_SVDComponents.gif)

---

## SVD and Rank

### Rank = Number of Nonzero Singular Values

$$\text{rank}(A) = r = \#\{\sigma_i : \sigma_i > 0\}$$

This is one of the most important properties of the SVD. The singular values tell you the "effective dimensionality" of the matrix.

### The Four Fundamental Subspaces via SVD

The SVD reveals the four fundamental subspaces of linear algebra with crystal clarity:

| Subspace | Basis from SVD |
|----------|---------------|
| Column space $C(A)$ | First $r$ columns of $U$: $\vec{u}_1, \ldots, \vec{u}_r$ |
| Null space $N(A)$ | Last $n-r$ columns of $V$: $\vec{v}_{r+1}, \ldots, \vec{v}_n$ |
| Row space $C(A^T)$ | First $r$ columns of $V$: $\vec{v}_1, \ldots, \vec{v}_r$ |
| Left null space $N(A^T)$ | Last $m-r$ columns of $U$: $\vec{u}_{r+1}, \ldots, \vec{u}_m$ |

---

## Existence of the SVD

The fact that every real matrix has an SVD is a major theorem in linear algebra. It follows from the spectral theorem: since $A^TA$ is always symmetric and positive semidefinite, it can always be orthogonally diagonalized, which provides the starting point for constructing the full SVD.

---

## Summary

| Concept | Formula / Description |
|---------|----------------------|
| SVD definition | $A = U\Sigma V^T$ |
| $U$ | $m \times m$ orthogonal matrix, left singular vectors |
| $\Sigma$ | $m \times n$ diagonal matrix, singular values $\sigma_1 \geq \cdots \geq 0$ |
| $V$ | $n \times n$ orthogonal matrix, right singular vectors |
| Singular value formula | $\sigma_i = \sqrt{\lambda_i(A^TA)}$ |
| Rank | $r$ = number of nonzero singular values |
| Existence | Every real (or complex) matrix has an SVD |
| Column space basis | First $r$ columns of $U$ |
| Null space basis | Last $n-r$ columns of $V$ |

> In the next post, we explore the **geometric meaning of the SVD** and develop an intuitive understanding of how any linear transformation decomposes into "rotate -- stretch -- rotate."
