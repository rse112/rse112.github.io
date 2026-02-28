---
title: "6.1 What Are Eigenvalues and Eigenvectors?"
date: 2026-01-19 00:00:00 +0900
categories: [Linear Algebra, Eigenvalues and Eigenvectors]
tags: [linear algebra, mathematics, eigenvalues and eigenvectors]
math: true
lang: en
hreflang_ko: /posts/6-1-definition/
---


## Introduction

Stand in front of a mirror and raise your arm. Your reflection raises its arm too -- but the mirror flips left and right. Most transformations change the direction of vectors. Yet some special vectors survive the transformation with their direction intact. The transformation only scales them, making them longer or shorter (or perhaps flipping them to point the opposite way). These special vectors are called **eigenvectors**, and the scaling factor is called the **eigenvalue**.

This is far more than a mathematical curiosity. Resonance frequencies of vibrating structures, Google's PageRank algorithm, facial recognition technology, energy states in quantum mechanics -- eigenvalues and eigenvectors form the backbone of modern science and engineering. In this post, we will build an intuitive understanding of their definition and geometric meaning.

---

## Definition of Eigenvalues and Eigenvectors

### The Core Definition

For a square matrix $A$, if there exists a nonzero vector $\vec{v}$ and a scalar $\lambda$ such that

$$A\vec{v} = \lambda\vec{v}, \quad \vec{v} \neq \vec{0}$$

then $\lambda$ is called an **eigenvalue** of $A$, and $\vec{v}$ is called an **eigenvector** corresponding to $\lambda$.

Unpacking this equation: when you apply the linear transformation $A$ to $\vec{v}$, the result is simply $\vec{v}$ scaled by the constant $\lambda$. The direction stays the same (or flips exactly), and the magnitude changes by a factor of $|\lambda|$.

![Eigenvector visualization -- a vector whose direction is preserved](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_1_EigenvectorVisualization.gif)

### Why Do We Require $\vec{v} \neq \vec{0}$?

The zero vector always satisfies $A\vec{0} = \lambda\vec{0} = \vec{0}$ for every $\lambda$. This tells us nothing useful, so we exclude it from the definition.

---

## Geometric Meaning

### Vectors That Stay on Their Line

The geometric interpretation of eigenvectors is beautifully simple. When you transform the vector $\vec{v}$ by the matrix $A$, the result $A\vec{v}$ lies on the **same line** as the original $\vec{v}$.

- $\lambda > 0$: The vector stretches (or shrinks) in the same direction by a factor of $\lambda$.
- $\lambda < 0$: The vector flips to the opposite direction and scales by $|\lambda|$.
- $\lambda = 1$: The vector is completely unchanged by the transformation (a fixed point).
- $\lambda = 0$: The vector collapses to the zero vector (that direction gets "crushed").

$$\vec{v} \xrightarrow{A} \lambda\vec{v}$$

### The Eigenspace

For a given eigenvalue $\lambda$, the collection of all eigenvectors (together with the zero vector) forms a subspace called the **eigenspace**:

$$E_\lambda = \ker(A - \lambda I) = \{\vec{v} : A\vec{v} = \lambda\vec{v}\}$$

---

## Example: Eigenvalues of a Diagonal Matrix

### Diagonal matrices make eigenvalues obvious

Consider the diagonal matrix $D = \begin{pmatrix} 3 & 0 \\ 0 & 5 \end{pmatrix}$.

Apply it to the standard basis vectors $\vec{e}_1 = \begin{pmatrix}1\\0\end{pmatrix}$ and $\vec{e}_2 = \begin{pmatrix}0\\1\end{pmatrix}$:

$$D\vec{e}_1 = \begin{pmatrix} 3 & 0 \\ 0 & 5 \end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}3\\0\end{pmatrix} = 3\vec{e}_1$$

$$D\vec{e}_2 = \begin{pmatrix} 3 & 0 \\ 0 & 5 \end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\5\end{pmatrix} = 5\vec{e}_2$$

The eigenvalues of a diagonal matrix are simply its **diagonal entries**, and the eigenvectors are the **standard basis vectors**.

In general, for an $n \times n$ diagonal matrix $D = \text{diag}(d_1, d_2, \ldots, d_n)$, the eigenvalues are $\lambda_i = d_i$.

![Eigenvalue equation visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_1_EigenvalueEquation.gif)

### A 3x3 Diagonal Example

$$D = \begin{pmatrix} -2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \end{pmatrix}$$

Eigenvalues: $\lambda_1 = -2$, $\lambda_2 = 1$, $\lambda_3 = 4$

Corresponding eigenvectors:
- $\lambda_1 = -2$: $\vec{v}_1 = \begin{pmatrix}1\\0\\0\end{pmatrix}$ (the $x$-direction gets flipped and doubled)
- $\lambda_2 = 1$: $\vec{v}_2 = \begin{pmatrix}0\\1\\0\end{pmatrix}$ (the $y$-direction is unchanged)
- $\lambda_3 = 4$: $\vec{v}_3 = \begin{pmatrix}0\\0\\1\end{pmatrix}$ (the $z$-direction is stretched by a factor of 4)

---

## Scalar Multiples of Eigenvectors

If $\vec{v}$ is an eigenvector for eigenvalue $\lambda$, then any nonzero scalar multiple $c\vec{v}$ is also an eigenvector for the same $\lambda$:

$$A(c\vec{v}) = c(A\vec{v}) = c(\lambda\vec{v}) = \lambda(c\vec{v})$$

This is why eigenvectors represent **directions** rather than specific vectors. When reporting eigenvectors, we typically choose a convenient representative -- often a unit vector or one with simple integer components.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Eigenvector definition | $A\vec{v} = \lambda\vec{v}$, $\vec{v} \neq \vec{0}$ |
| Eigenvalue $\lambda$ | The scaling factor after transformation |
| Eigenvector $\vec{v}$ | A vector whose direction is preserved by the transformation |
| Geometric meaning | The transformed vector stays on the same line |
| $\lambda > 1$ | Stretching in that direction |
| $0 < \lambda < 1$ | Shrinking in that direction |
| $\lambda < 0$ | Direction reversal plus scaling |
| $\lambda = 0$ | That direction collapses to the origin |
| Diagonal matrix eigenvalues | Simply the diagonal entries |
| Eigenspace | $E_\lambda = \ker(A - \lambda I)$ |

> Next up: **The Characteristic Equation** -- a systematic method for finding eigenvalues of any matrix.
