---
title: "7.1 Orthogonal Vectors and Orthogonal Matrices"
date: 2026-01-23 00:00:00 +0900
categories: [Linear Algebra, Orthogonality]
tags: [linear algebra, mathematics, orthogonality]
math: true
lang: en
hreflang_ko: /posts/7-1-orthogonal-vectors-matrices/
---


## Introduction

On a map, north and east are completely independent directions. Moving north does not change your east coordinate at all. This orthogonal coordinate system is what makes map reading, GPS calculations, and building design so straightforward. In much the same way, a coordinate system built from mutually perpendicular vectors dramatically simplifies computation in linear algebra.

This idea is formalized through **orthogonal vectors** and **orthogonal matrices**. Far from being mere mathematical abstractions, orthogonal matrices are the backbone of rotation transforms in computer graphics, Fourier transforms in signal processing, and unitary transforms in quantum mechanics. Orthogonality is also a key property that guarantees **numerical stability** in scientific computing.

---

## Orthogonal Vectors

### Definition: Zero Inner Product

Two vectors $\vec{u}$ and $\vec{v}$ are **orthogonal** if their inner product (dot product) is zero:

$$\vec{u} \cdot \vec{v} = \vec{u}^T\vec{v} = \sum_{i=1}^{n} u_i v_i = 0$$

Geometrically, this means the two vectors meet at a 90-degree angle (assuming both are nonzero).

![Visualization of orthogonal vectors -- two vectors with zero dot product](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/7_1_OrthogonalVectors.gif)

### Example

$$\vec{u} = \begin{pmatrix}1\\2\\3\end{pmatrix}, \quad \vec{v} = \begin{pmatrix}1\\1\\-1\end{pmatrix}$$

$$\vec{u} \cdot \vec{v} = (1)(1) + (2)(1) + (3)(-1) = 1 + 2 - 3 = 0 \checkmark$$

So $\vec{u}$ and $\vec{v}$ are orthogonal.

### The Pythagorean Theorem Generalized

The Pythagorean theorem extends naturally to orthogonal vectors:

$$\|\vec{u} + \vec{v}\|^2 = \|\vec{u}\|^2 + \|\vec{v}\|^2 \quad (\text{when } \vec{u} \perp \vec{v})$$

**Proof:**

$$\|\vec{u} + \vec{v}\|^2 = (\vec{u}+\vec{v})\cdot(\vec{u}+\vec{v}) = \|\vec{u}\|^2 + 2\underbrace{\vec{u}\cdot\vec{v}}_{=0} + \|\vec{v}\|^2 = \|\vec{u}\|^2 + \|\vec{v}\|^2$$

---

## Orthonormal Sets

### Orthogonal + Unit Length

A set of vectors $\{\vec{u}_1, \vec{u}_2, \ldots, \vec{u}_k\}$ is called **orthonormal** if it satisfies two conditions:

1. **Orthogonality**: $\vec{u}_i \cdot \vec{u}_j = 0$ whenever $i \neq j$
2. **Normalization**: $\|\vec{u}_i\| = 1$ for every $i$

These two conditions can be written compactly as:

$$\vec{u}_i \cdot \vec{u}_j = \delta_{ij} = \begin{cases} 1 & (i = j) \\ 0 & (i \neq j) \end{cases}$$

where $\delta_{ij}$ is the **Kronecker delta**.

### Orthogonal Sets Are Linearly Independent

Any orthogonal set (that does not contain the zero vector) is automatically **linearly independent**. This is what makes orthonormal bases so convenient for representing coordinates.

**Proof sketch:** Suppose $c_1\vec{u}_1 + c_2\vec{u}_2 + \cdots + c_k\vec{u}_k = \vec{0}$. Taking the inner product of both sides with $\vec{u}_i$ immediately gives $c_i = 0$.

---

## Orthogonal Matrices

### Definition

A square matrix $Q$ is an **orthogonal matrix** if:

$$Q^T Q = Q Q^T = I$$

In other words, the inverse of $Q$ is simply its transpose:

$$Q^{-1} = Q^T$$

The columns of an orthogonal matrix form an orthonormal set, and so do its rows.

![Orthogonal matrix -- a transformation that preserves lengths and angles](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/7_1_OrthogonalMatrix.gif)

### Key Properties of Orthogonal Matrices

**Length preservation:**

$$\|Q\vec{x}\| = \|\vec{x}\| \quad \text{for all } \vec{x}$$

**Proof:**

$$\|Q\vec{x}\|^2 = (Q\vec{x})^T(Q\vec{x}) = \vec{x}^T Q^T Q \vec{x} = \vec{x}^T I \vec{x} = \|\vec{x}\|^2$$

**Angle preservation:**

$$\cos\theta = \frac{(Q\vec{x}) \cdot (Q\vec{y})}{\|Q\vec{x}\|\|Q\vec{y}\|} = \frac{\vec{x}^TQ^TQ\vec{y}}{\|\vec{x}\|\|\vec{y}\|} = \frac{\vec{x}\cdot\vec{y}}{\|\vec{x}\|\|\vec{y}\|}$$

In other words, an orthogonal matrix is an **isometry** -- it preserves the shape and size of geometric objects.

**Determinant:**

$$\det(Q) = \pm 1$$

When $\det(Q) = 1$, the matrix represents a pure rotation. When $\det(Q) = -1$, it includes a reflection.

---

## Example: 2D Rotation Matrix

The matrix representing rotation by angle $\theta$:

$$Q = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

Verifying it is orthogonal:

$$Q^T Q = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

$$= \begin{pmatrix} \cos^2\theta + \sin^2\theta & 0 \\ 0 & \sin^2\theta + \cos^2\theta \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \checkmark$$

$\det(Q) = \cos^2\theta + \sin^2\theta = 1$ (a pure rotation, as expected).

---

## Column Conditions for Orthogonal Matrices

Writing $Q = [\vec{q}_1 \; \vec{q}_2 \; \cdots \; \vec{q}_n]$, the condition $Q^TQ = I$ is equivalent to:

$$\vec{q}_i^T \vec{q}_j = \delta_{ij}$$

That is, the columns form an orthonormal set.

---

## Summary

| Concept | Formula / Description |
|---------|----------------------|
| Orthogonal vectors | $\vec{u} \cdot \vec{v} = 0$ |
| Orthonormal set | Orthogonal + unit length: $\vec{u}_i \cdot \vec{u}_j = \delta_{ij}$ |
| Orthogonal matrix | $Q^T Q = Q Q^T = I$ |
| Easy inverse | $Q^{-1} = Q^T$ |
| Length preservation | $\|Q\vec{x}\| = \|\vec{x}\|$ |
| Angle preservation | Inner products are preserved |
| Determinant | $\det(Q) = \pm 1$ |
| Rotation matrix | An orthogonal matrix with $\det(Q) = 1$ |
| Column condition | Columns form an orthonormal set |

> In the next post, we explore the **Gram-Schmidt process**, a systematic procedure for constructing an orthonormal basis from any set of linearly independent vectors.
