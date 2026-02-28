---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_4_EigendecompGeometric.gif
title: "6.4 The Geometric Meaning of Eigenvalues"
date: 2026-01-22 00:00:00 +0900
categories: [Linear Algebra, Eigenvalues and Eigenvectors]
tags: [linear algebra, mathematics, eigenvalues and eigenvectors]
math: true
lang: en
hreflang_ko: /posts/6-4-geometric-meaning/
---


## Introduction

So far we have treated eigenvalues and eigenvectors algebraically -- computing them through characteristic equations and diagonalization. Now let us step back and ask: "What does all of this mean geometrically?" At its heart, finding eigenvalues and eigenvectors is about discovering the **principal axes** of a linear transformation. Just as an ellipse has a major axis and a minor axis, a linear transformation has preferred directions along which it simply stretches or compresses.

This geometric perspective is not just for visualization. Principal Component Analysis (PCA) in data science, resonance modes in vibrating systems, and structural analysis in graph theory all rest on the geometric meaning of eigenvalues.

---

## Geometric Interpretation: Stretching, Shrinking, and Flipping

### What the Eigenvalue Tells You About Each Direction

An eigenvector $\vec{v}$ marks a direction that the transformation $A$ preserves. The eigenvalue $\lambda$ tells you exactly what happens along that direction:

| Eigenvalue Range | Geometric Effect |
|------------------|-----------------|
| $\lambda > 1$ | Stretching along that direction |
| $\lambda = 1$ | No change in that direction |
| $0 < \lambda < 1$ | Shrinking along that direction |
| $\lambda = 0$ | That direction collapses to the origin |
| $\lambda < 0$ | Direction reversal, scaled by $\|\lambda\|$ |

![Geometric meaning of eigenvalues -- the unit circle transforms into an ellipse](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/6_4_EigendecompGeometric.gif)

### The Intuitive Picture

In two dimensions, suppose a matrix $A$ has two eigenvectors $\vec{v}_1$ and $\vec{v}_2$ pointing in different directions. Applying $A$:

- Stretches (or shrinks) by a factor of $\lambda_1$ along the $\vec{v}_1$ direction
- Stretches (or shrinks) by a factor of $\lambda_2$ along the $\vec{v}_2$ direction

If you apply $A$ to the unit circle, it becomes an **ellipse**. The semi-axis lengths are $|\lambda_1|$ and $|\lambda_2|$, and the semi-axes point in the eigenvector directions.

---

## Special Properties of Symmetric Matrices

### Real Eigenvalues and Orthogonal Eigenvectors

A symmetric matrix ($A = A^T$) has two remarkable properties:

1. **All eigenvalues are real** -- no complex eigenvalues ever appear.
2. **Eigenvectors for distinct eigenvalues are orthogonal** to each other.

That is, if $\lambda_i \neq \lambda_j$, then $\vec{v}_i \cdot \vec{v}_j = 0$.

Here is the proof. Suppose $A\vec{v}_i = \lambda_i \vec{v}_i$ and $A\vec{v}_j = \lambda_j \vec{v}_j$. Then:

$$\lambda_i (\vec{v}_i \cdot \vec{v}_j) = (A\vec{v}_i)^T \vec{v}_j = \vec{v}_i^T A^T \vec{v}_j = \vec{v}_i^T A \vec{v}_j = \lambda_j (\vec{v}_i \cdot \vec{v}_j)$$

$$(\lambda_i - \lambda_j)(\vec{v}_i \cdot \vec{v}_j) = 0$$

Since $\lambda_i \neq \lambda_j$, we must have $\vec{v}_i \cdot \vec{v}_j = 0$. Orthogonality is proven.

### The Spectral Theorem

Every real symmetric matrix $A$ is diagonalizable, and moreover it can be diagonalized using an orthogonal matrix $Q$:

$$A = QDQ^T = QDQ^{-1}$$

where $Q^T = Q^{-1}$ (the defining property of an orthogonal matrix).

---

## The Spectral Decomposition

### Decomposing a Matrix into Rank-1 Pieces

Given a symmetric matrix $A$ with normalized eigenvectors $\vec{u}_1, \vec{u}_2, \ldots, \vec{u}_n$ and corresponding eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_n$:

$$A = \sum_{i=1}^{n} \lambda_i \vec{u}_i \vec{u}_i^T$$

Each term $\lambda_i \vec{u}_i \vec{u}_i^T$ is a **rank-1 matrix** -- the projection onto $\vec{u}_i$ scaled by $\lambda_i$.

This decomposition expresses $A$ as a sum of simple, primitive transformations. Each one acts along a single direction, and $A$ is just the aggregate of all of them.

### A Worked Example

$$A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$$

Characteristic equation: $\lambda^2 - 6\lambda + 8 = 0 \Rightarrow \lambda_1 = 4, \lambda_2 = 2$

Normalized eigenvectors:

$$\vec{u}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}, \quad \vec{u}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}$$

Spectral decomposition:

$$A = 4 \cdot \frac{1}{2}\begin{pmatrix}1\\1\end{pmatrix}\begin{pmatrix}1&1\end{pmatrix} + 2 \cdot \frac{1}{2}\begin{pmatrix}1\\-1\end{pmatrix}\begin{pmatrix}1&-1\end{pmatrix}$$

$$= 2\begin{pmatrix}1&1\\1&1\end{pmatrix} + 1\begin{pmatrix}1&-1\\-1&1\end{pmatrix} = \begin{pmatrix}3&1\\1&3\end{pmatrix} \checkmark$$

---

## What Eigenvalues Reveal About a Matrix

### Matrix Properties from Eigenvalues

| Matrix Property | Eigenvalue Condition |
|-----------------|---------------------|
| Invertible | All eigenvalues $\neq 0$ |
| Positive definite | All eigenvalues $> 0$ |
| Positive semidefinite | All eigenvalues $\geq 0$ |
| Orthogonal matrix | All eigenvalues have absolute value $= 1$ |
| Trace | $\text{tr}(A) = \sum \lambda_i$ |
| Determinant | $\det(A) = \prod \lambda_i$ |

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Geometric meaning | Eigenvector directions = principal axes of the transformation |
| $\|\lambda\| > 1$ | Stretching along that direction |
| $\|\lambda\| < 1$ | Shrinking along that direction |
| $\lambda < 0$ | Direction reversal |
| Symmetric matrix properties | Real eigenvalues + orthogonal eigenvectors |
| Spectral theorem | $A = QDQ^T$ for symmetric matrices |
| Spectral decomposition | $A = \sum \lambda_i \vec{u}_i\vec{u}_i^T$ |
| $\text{tr}(A)$ | Sum of eigenvalues |
| $\det(A)$ | Product of eigenvalues |

> Next up: **Orthogonal Vectors and Orthogonal Matrices** -- exploring why orthogonality is so important for numerical computation.
