---
title: "5.2 Linear Independence and Basis"
date: 2026-01-16 00:00:00 +0900
categories: [Linear Algebra, Vector Spaces]
tags: [linear algebra, mathematics, vector spaces]
math: true
lang: en
hreflang_ko: /posts/5-2-linear-independence-basis/
---


## Introduction

Picture yourself holding a hiking map. "East" and "North" are two genuinely different directions -- no matter how far you walk east, you will never move north. These two directions are independent.

Now consider "East" and "Northeast." Northeast is just $\frac{1}{\sqrt{2}}$ East $+$ $\frac{1}{\sqrt{2}}$ North. It does not give you a new direction; it is merely a combination of directions you already have.

This idea of vectors pointing in "genuinely different" directions is captured by the concept of **linear independence**. And a set of vectors that is both linearly independent and spans the entire space is called a **basis**.

---

## Definition of Linear Independence

Vectors $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k$ are **linearly independent** if the equation

$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{0}$$

has only the trivial solution $c_1 = c_2 = \cdots = c_k = 0$.

In other words, the only way to combine these vectors to produce the zero vector is to use all-zero coefficients.

**Practical test:** Form the matrix $A = [\vec{v}_1 \mid \vec{v}_2 \mid \cdots \mid \vec{v}_k]$ with the vectors as columns. If the only solution to $A\vec{c} = \vec{0}$ is $\vec{c} = \vec{0}$, the vectors are linearly independent.

---

## Definition of Linear Dependence

Vectors are **linearly dependent** if they are not linearly independent. This means there exist scalars $c_1, \ldots, c_k$, not all zero, such that

$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{0}$$

Equivalently, at least one vector can be written as a **linear combination** of the others. For instance, if $c_1 \neq 0$, then

$$\vec{v}_1 = -\frac{c_2}{c_1}\vec{v}_2 - \cdots - \frac{c_k}{c_1}\vec{v}_k$$

So $\vec{v}_1$ is redundant -- it does not contribute any new direction.

![Linear dependence visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_2_LinearDependence.gif)

---

## Examples

**Linearly independent:**

$$\vec{v}_1 = \begin{pmatrix}1\\0\end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix}0\\1\end{pmatrix}$$

If $c_1\begin{pmatrix}1\\0\end{pmatrix} + c_2\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}$, then we must have $c_1 = 0$ and $c_2 = 0$. Linearly independent.

**Linearly dependent:**

$$\vec{v}_1 = \begin{pmatrix}1\\2\end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix}2\\4\end{pmatrix}$$

Since $\vec{v}_2 = 2\vec{v}_1$, we have $2\vec{v}_1 - \vec{v}_2 = \vec{0}$. The coefficients $(2, -1)$ are not all zero, so the vectors are linearly dependent.

---

## Basis

A **basis** for a vector space $V$ is a set of vectors satisfying two conditions simultaneously:

1. **Linearly independent:** No vector in the set is redundant.
2. **Spans $V$:** Every vector in $V$ can be expressed as a linear combination of the basis vectors.

A basis is the "minimal amount of information" needed to describe the entire space.

---

## The Standard Basis

The **standard basis** for $\mathbb{R}^n$ consists of the unit vectors along each coordinate axis:

$$\hat{e}_1 = \begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},\quad \hat{e}_2 = \begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix},\quad \ldots,\quad \hat{e}_n = \begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}$$

Any vector $\vec{x} = (x_1, x_2, \ldots, x_n)^\top$ can be written **uniquely** as

$$\vec{x} = x_1\hat{e}_1 + x_2\hat{e}_2 + \cdots + x_n\hat{e}_n$$

![Standard basis visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_2_StandardBasis.gif)

---

## Basis and Uniqueness of Coordinates

Given a basis $\mathcal{B} = \{\vec{b}_1, \ldots, \vec{b}_n\}$, every vector $\vec{v}$ in $V$ can be expressed **uniquely** as

$$\vec{v} = c_1\vec{b}_1 + c_2\vec{b}_2 + \cdots + c_n\vec{b}_n$$

The scalars $(c_1, c_2, \ldots, c_n)$ are called the **coordinates** of $\vec{v}$ with respect to $\mathcal{B}$.

Because this representation is unique, a basis acts as a **coordinate system**. Just like GPS coordinates, once you fix a basis, every point in the space corresponds to exactly one tuple of numbers.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Linear independence | $c_1\vec{v}_1+\cdots+c_k\vec{v}_k=\vec{0} \Rightarrow$ all $c_i=0$ |
| Linear dependence | There exist nonzero $c_i$ such that the linear combination equals $\vec{0}$ |
| Meaning of dependence | At least one vector is a linear combination of the others |
| Basis conditions | Linearly independent + spans the space (both at once) |
| Standard basis | $\{\hat{e}_1, \ldots, \hat{e}_n\}$, unit vectors with a 1 in the $i$-th entry |
| Uniqueness of coordinates | Given a basis, every vector has a unique representation |

> Next up: **Dimension** -- why every basis for the same space always has the same number of vectors.
