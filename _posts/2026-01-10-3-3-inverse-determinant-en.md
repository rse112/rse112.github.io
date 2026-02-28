---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_3_Determinant2x2.gif
title: "3.3 The Inverse Matrix and the Determinant"
date: 2026-01-10 00:00:00 +0900
categories: [Linear Algebra, Matrices]
tags: [linear algebra, mathematics, matrices]
math: true
lang: en
hreflang_ko: /posts/3-3-inverse-determinant/
---


## Introduction

To solve the scalar equation $ax = b$, you multiply both sides by $a^{-1} = \frac{1}{a}$ (provided $a \neq 0$) and get $x = a^{-1}b$. Could we do the same thing with a matrix equation $A\vec{x} = \vec{b}$? If there exists a "matrix version of the reciprocal" for $A$, we could multiply both sides by it and immediately find $\vec{x}$. That matrix is the **inverse matrix**, and the idea is exactly this simple.

But just as $\frac{1}{0}$ does not exist for scalars, some matrices have no inverse either. The tool that tells us whether an inverse exists is the **determinant**.

---

## Definition of the Inverse Matrix

### Definition

For an $n \times n$ square matrix $A$, the **inverse matrix** $A^{-1}$ is the matrix satisfying

$$A A^{-1} = A^{-1} A = I$$

A matrix that has an inverse is called **invertible** (or **non-singular**). A matrix without an inverse is called **singular**.

### Uniqueness

If an inverse exists, it is unique. Suppose both $B$ and $C$ are inverses of $A$. Then:

$$B = BI = B(AC) = (BA)C = IC = C$$

### Properties of the Inverse

$$(A^{-1})^{-1} = A$$
$$(AB)^{-1} = B^{-1}A^{-1} \quad \text{(note the reversal!)}$$
$$(A^T)^{-1} = (A^{-1})^T$$
$$(cA)^{-1} = \frac{1}{c}A^{-1} \quad (c \neq 0)$$

---

## The 2x2 Inverse Formula

### Formula

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

This works only when $ad - bc \neq 0$.

### How to Remember It

Swap the diagonal entries ($a \leftrightarrow d$), flip the signs of the off-diagonal entries ($b \to -b$, $c \to -c$), and divide by $ad - bc$.

### Example

$$A = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$$

$$\det A = 3 \cdot 2 - 1 \cdot 5 = 6 - 5 = 1$$

$$A^{-1} = \frac{1}{1}\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$$

Verification: $AA^{-1} = \begin{pmatrix}3&1\\5&2\end{pmatrix}\begin{pmatrix}2&-1\\-5&3\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$ $\checkmark$

![2x2 inverse matrix visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_3_InverseMatrix2x2.gif)

---

## The Determinant

### The 2x2 Determinant

$$\det A = \det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

This is also written as $|A|$.

### Geometric Meaning -- Area Scaling Factor

In two dimensions, the **absolute value** of the determinant equals the area of the parallelogram spanned by the column vectors of $A$. More generally, $A$ scales the area of every shape by a factor of $|\det A|$.

- $|\det A| > 1$: areas are enlarged.
- $|\det A| = 1$: areas are preserved (an area-preserving transformation).
- $|\det A| = 0$: areas collapse to zero -- the plane is squished onto a line (or a point).
- $\det A < 0$: the orientation is flipped.

![Geometric meaning of the 2x2 determinant](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/3_3_Determinant2x2.gif)

### The 3x3 Determinant

$$\det\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = a_{11}(a_{22}a_{33}-a_{23}a_{32}) - a_{12}(a_{21}a_{33}-a_{23}a_{31}) + a_{13}(a_{21}a_{32}-a_{22}a_{31})$$

This is called the **Laplace expansion** (or cofactor expansion) along the first row.

---

## Properties of the Determinant

### Determinant of a Product

$$\det(AB) = \det(A) \cdot \det(B)$$

This is an extremely powerful property. The determinant of a product equals the product of the determinants.

### Determinant of the Transpose

$$\det(A^T) = \det(A)$$

### Determinant of the Inverse

$$\det(A^{-1}) = \frac{1}{\det(A)}$$

This follows from $\det(AA^{-1}) = \det(I) = 1$, so $\det(A)\det(A^{-1}) = 1$.

### Determinant of a Scalar Multiple

$$\det(cA) = c^n \det(A) \quad (n \times n \text{ matrix})$$

---

## The Invertibility Condition

$$\boxed{A^{-1} \text{ exists} \quad \Leftrightarrow \quad \det A \neq 0}$$

This is the fundamental test. If $\det A = 0$, then $A$ is singular and has no inverse.

Geometrically, $\det A = 0$ means the transformation collapses space into a lower dimension. Information is lost, so there is no way to reverse the transformation and recover the original vectors.

$$A\vec{x} = \vec{b} \text{ has a unique solution} \quad \Leftrightarrow \quad \det A \neq 0 \quad \Leftrightarrow \quad \vec{x} = A^{-1}\vec{b}$$

---

## Key Takeaways

| Concept | Description / Formula |
|---------|-----------------------|
| Inverse definition | $AA^{-1} = A^{-1}A = I$ |
| 2x2 inverse | $A^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| $(AB)^{-1}$ | $B^{-1}A^{-1}$ (order reversal) |
| 2x2 determinant | $\det A = ad - bc$ |
| Geometric meaning | Area (volume) scaling factor $= |\det A|$ |
| Determinant of product | $\det(AB) = \det A \cdot \det B$ |
| Invertibility condition | $\det A \neq 0$ |
| Solving linear systems | If $\det A \neq 0$, then $\vec{x} = A^{-1}\vec{b}$ |

> In the next post, we explore **linear transformations** -- how matrices transform vector spaces, and what that looks like geometrically.
