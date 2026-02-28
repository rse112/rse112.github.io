---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_3_DimensionExamples.gif
title: "5.3 Dimension"
date: 2026-01-17 00:00:00 +0900
categories: [Linear Algebra, Vector Spaces]
tags: [linear algebra, mathematics, vector spaces]
math: true
lang: en
hreflang_ko: /posts/5-3-dimension/
---


## Introduction

One dimension is a line, two dimensions is a plane, three dimensions is the space we live in -- everyone has an intuitive sense of this. But how do we define "dimension" rigorously in mathematics?

Dimension is the **minimum number of independent directions** needed to describe a space. In linear algebra, this number is precisely the number of vectors in a basis.

Here is the remarkable fact: no matter which basis you choose for a given vector space, **the number of basis vectors is always the same**. This is the theorem that makes dimension a well-defined concept.

---

## Definition of Dimension

The **dimension** of a vector space $V$ is the number of vectors in any basis for $V$:

$$\dim(V) = \text{(number of vectors in a basis)}$$

This number does not depend on which basis you choose.

**Special case:** The zero space $\{\vec{0}\}$ has the empty set as its basis, so

$$\dim(\{\vec{0}\}) = 0$$

---

## Familiar Examples

### $\mathbb{R}^1$ -- The Number Line

Basis: $\{1\}$ (or any single nonzero real number)
$$\dim(\mathbb{R}^1) = 1$$

### $\mathbb{R}^2$ -- The Plane

Basis: $\{\hat{e}_1, \hat{e}_2\} = \{(1,0)^\top, (0,1)^\top\}$
$$\dim(\mathbb{R}^2) = 2$$

Another valid basis: $\{(1,1)^\top, (1,-1)^\top\}$ -- these vectors are linearly independent and span $\mathbb{R}^2$, so they form a legitimate basis.

### $\mathbb{R}^3$ -- Three-Dimensional Space

Basis: $\{\hat{e}_1, \hat{e}_2, \hat{e}_3\}$
$$\dim(\mathbb{R}^3) = 3$$

![Dimension examples visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_3_DimensionExamples.gif)

---

## Dimension Table

| Space | Example Basis | Dimension |
|-------|---------------|-----------|
| $\{\vec{0}\}$ | Empty set $\emptyset$ | $0$ |
| Line through the origin | One vector along the line | $1$ |
| Plane through the origin | Two non-parallel vectors | $2$ |
| $\mathbb{R}^2$ | $\{\hat{e}_1, \hat{e}_2\}$ | $2$ |
| $\mathbb{R}^3$ | $\{\hat{e}_1, \hat{e}_2, \hat{e}_3\}$ | $3$ |
| $\mathbb{R}^n$ | $\{\hat{e}_1, \ldots, \hat{e}_n\}$ | $n$ |

---

## The Dimension Theorem

**Theorem:** Every basis for a finite-dimensional vector space $V$ contains the same number of vectors.

Without this theorem, the very definition of dimension would be ambiguous. The key idea behind the proof: assuming two bases of different sizes leads to a contradiction.

**Corollaries:**
- Any set of $\dim(V)$ linearly independent vectors in $V$ is automatically a basis.
- Any set of $\dim(V)$ vectors that spans $V$ is automatically a basis.

---

## Dimension of Subspaces

If $W$ is a subspace of $V$, then

$$\dim(W) \leq \dim(V)$$

Equality holds if and only if $W = V$.

**Example:** Subspaces of $\mathbb{R}^3$:

| Subspace | Geometric Meaning | Dimension |
|----------|-------------------|-----------|
| $\{\vec{0}\}$ | The origin | $0$ |
| $\text{span}\{\vec{v}\}$ | Line through the origin | $1$ |
| $\text{span}\{\vec{v}_1, \vec{v}_2\}$ | Plane through the origin | $2$ |
| $\mathbb{R}^3$ itself | Full 3D space | $3$ |

---

## Extending and Reducing to a Basis

**Basis extension theorem:** A basis $\mathcal{B}_W$ for a subspace $W$ can always be extended to a basis $\mathcal{B}_V$ for the full space $V$.

**Extending a linearly independent set:** You can keep adding vectors to a linearly independent set (while preserving independence) until you reach a basis.

**Reducing a spanning set:** You can keep removing redundant vectors from a spanning set (while preserving the span) until you arrive at a basis.

---

## Intuitive Understanding

Think of dimension as the number of **degrees of freedom**.

- To specify a point on a line (1D space), you need **one** number.
- To specify a point on a plane (2D space), you need **two** numbers.
- To specify a point in $n$-dimensional space, you need **$n$** numbers.

Number of basis vectors = number of independent numbers needed to describe the space = dimension.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Definition of dimension | $\dim(V)$ = number of vectors in a basis |
| Dimension of the zero space | $\dim(\{\vec{0}\}) = 0$ |
| Dimension of $\mathbb{R}^n$ | $\dim(\mathbb{R}^n) = n$ |
| Dimension theorem | Every basis has the same number of vectors |
| Subspace dimension | $\dim(W) \leq \dim(V)$ |
| Intuition | Dimension = number of numbers needed to specify a point in the space |

> Next up: **Null Space and Column Space** -- when does the matrix equation $A\vec{x}=\vec{b}$ have a solution?
