---
title: "6.2 The Characteristic Equation"
date: 2026-01-20 00:00:00 +0900
categories: [Linear Algebra, Eigenvalues and Eigenvectors]
tags: [linear algebra, mathematics, eigenvalues and eigenvectors]
math: true
lang: en
hreflang_ko: /posts/6-2-characteristic-equation/
---


## Introduction

In the previous post, we learned what eigenvalues and eigenvectors are. The equation $A\vec{v} = \lambda\vec{v}$ tells us that certain special vectors only get scaled by a transformation. But given an actual matrix, how do we find these values? We certainly cannot guess eigenvectors one by one and check.

Fortunately, linear algebra gives us a systematic procedure. The key insight is that rearranging $A\vec{v} = \lambda\vec{v}$ brings the **determinant** into play. Setting that determinant equal to zero produces the **characteristic equation**, and solving it yields the eigenvalues. In this post, we will derive the characteristic equation step by step and work through a complete example.

---

## Deriving the Characteristic Equation

### The Core Idea: When Does a Homogeneous System Have Nontrivial Solutions?

Start from the eigenvalue definition $A\vec{v} = \lambda\vec{v}$ and rearrange:

$$A\vec{v} - \lambda\vec{v} = \vec{0}$$

$$A\vec{v} - \lambda I\vec{v} = \vec{0}$$

$$(A - \lambda I)\vec{v} = \vec{0}$$

This is a homogeneous system with coefficient matrix $(A - \lambda I)$. We need a nontrivial solution ($\vec{v} \neq \vec{0}$). If $(A - \lambda I)$ were invertible, the only solution would be $\vec{v} = (A-\lambda I)^{-1}\vec{0} = \vec{0}$, which is useless. So for eigenvectors to exist, $(A - \lambda I)$ must be **singular** (non-invertible), which happens exactly when its determinant is zero:

$$\det(A - \lambda I) = 0$$

This is the **characteristic equation**.

![Characteristic equation derivation visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_2_CharacteristicEquation.gif)

### The Characteristic Polynomial

Expanding $\det(A - \lambda I)$ as a polynomial in $\lambda$ gives the **characteristic polynomial**. For an $n \times n$ matrix, this polynomial has degree $n$, so (counting multiplicities and allowing complex roots) there are exactly $n$ eigenvalues.

---

## A 2x2 Example: Finding Eigenvalues

### The Matrix

$$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$$

### Step 1: Form $(A - \lambda I)$

$$A - \lambda I = \begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix}$$

### Step 2: Set Up the Characteristic Equation

$$\det(A - \lambda I) = (4-\lambda)(3-\lambda) - (1)(2) = 0$$

$$= 12 - 4\lambda - 3\lambda + \lambda^2 - 2 = 0$$

$$= \lambda^2 - 7\lambda + 10 = 0$$

### Step 3: Factor the Characteristic Polynomial

$$(\lambda - 5)(\lambda - 2) = 0$$

$$\therefore \quad \lambda_1 = 5, \quad \lambda_2 = 2$$

---

## Finding the Eigenvectors for Each Eigenvalue

### Eigenvectors for $\lambda_1 = 5$

Solve $(A - 5I)\vec{v} = \vec{0}$:

$$A - 5I = \begin{pmatrix} 4-5 & 1 \\ 2 & 3-5 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}$$

Row reducing reveals that both rows are proportional (dependent):

$$\begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix} \rightarrow -v_1 + v_2 = 0 \rightarrow v_1 = v_2$$

Setting the free variable $v_2 = t$: $\vec{v} = t\begin{pmatrix}1\\1\end{pmatrix}$

Eigenvector: $\vec{v}_1 = \begin{pmatrix}1\\1\end{pmatrix}$

**Verification:** $A\vec{v}_1 = \begin{pmatrix}4&1\\2&3\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix} = \begin{pmatrix}5\\5\end{pmatrix} = 5\begin{pmatrix}1\\1\end{pmatrix}$ ✓

### Eigenvectors for $\lambda_2 = 2$

Solve $(A - 2I)\vec{v} = \vec{0}$:

$$A - 2I = \begin{pmatrix} 4-2 & 1 \\ 2 & 3-2 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}$$

Row reducing:

$$\begin{pmatrix} 2 & 1 \\ 0 & 0 \end{pmatrix} \rightarrow 2v_1 + v_2 = 0 \rightarrow v_2 = -2v_1$$

Setting the free variable $v_1 = t$: $\vec{v} = t\begin{pmatrix}1\\-2\end{pmatrix}$

Eigenvector: $\vec{v}_2 = \begin{pmatrix}1\\-2\end{pmatrix}$

**Verification:** $A\vec{v}_2 = \begin{pmatrix}4&1\\2&3\end{pmatrix}\begin{pmatrix}1\\-2\end{pmatrix} = \begin{pmatrix}2\\-4\end{pmatrix} = 2\begin{pmatrix}1\\-2\end{pmatrix}$ ✓

---

## Repeated Eigenvalues and Special Cases

### Algebraic and Geometric Multiplicity

When an eigenvalue $\lambda$ appears $k$ times as a root of the characteristic polynomial, its **algebraic multiplicity** is $k$. The number of linearly independent eigenvectors for that eigenvalue is called its **geometric multiplicity**, and it satisfies:

$$1 \leq \text{geometric multiplicity} \leq \text{algebraic multiplicity}$$

### General Formula for 2x2 Matrices

For any $2 \times 2$ matrix $A = \begin{pmatrix}a&b\\c&d\end{pmatrix}$:

$$\det(A - \lambda I) = \lambda^2 - (a+d)\lambda + (ad-bc) = 0$$

$$= \lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$$

Here $\text{tr}(A) = a + d$ is the **trace** and $\det(A) = ad - bc$ is the determinant. This gives two elegant relationships:

$$\lambda_1 + \lambda_2 = \text{tr}(A), \qquad \lambda_1 \cdot \lambda_2 = \det(A)$$

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Derivation | $A\vec{v}=\lambda\vec{v} \Rightarrow (A-\lambda I)\vec{v}=\vec{0}$ |
| Characteristic equation | $\det(A - \lambda I) = 0$ |
| Degree of characteristic polynomial | $n$ for an $n \times n$ matrix |
| Number of eigenvalues | $n$ over the complex numbers (counting multiplicity) |
| 2x2 formula | $\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$ |
| Sum of eigenvalues | $\lambda_1 + \cdots + \lambda_n = \text{tr}(A)$ |
| Product of eigenvalues | $\lambda_1 \cdots \lambda_n = \det(A)$ |
| Finding eigenvectors | For each $\lambda$, solve $(A-\lambda I)\vec{v}=\vec{0}$ |

> Next up: **Diagonalization** -- using eigenvalues and eigenvectors to compute matrix powers efficiently.
