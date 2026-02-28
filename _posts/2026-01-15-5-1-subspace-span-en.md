---
title: "5.1 Subspaces and Span"
date: 2026-01-15 00:00:00 +0900
categories: [Linear Algebra, Vector Spaces]
tags: [linear algebra, mathematics, vector spaces]
math: true
lang: en
hreflang_ko: /posts/5-1-subspace-span/
---


## Introduction

Imagine drawing a line through the origin on a 2D plane. Now collect every point (vector) that lies on that line into a set. This set has a remarkable property: if you add any two vectors from it, the result is still on the line. If you multiply any vector in it by any scalar, the result is still on the line.

A set like this is called a **subspace**. A subspace is essentially a "smaller vector space" living inside a larger one. And the set of all possible linear combinations you can form from a given collection of vectors is called the **span** of those vectors. Together, these two concepts are the fundamental tools for answering the question: "Starting from these vectors, where can we reach?"

---

## What Is a Vector Space?

A set $V$ is a **vector space** if it is equipped with two operations -- addition $\vec{u} + \vec{v}$ and scalar multiplication $c\vec{v}$ -- that satisfy the following properties:

**Key axioms:**
- Closure under addition: $\vec{u}, \vec{v} \in V \Rightarrow \vec{u} + \vec{v} \in V$
- Closure under scalar multiplication: $\vec{v} \in V, c \in \mathbb{R} \Rightarrow c\vec{v} \in V$
- Contains the zero vector: $\vec{0} \in V$
- Commutativity and associativity of addition, existence of additive inverses, distributive laws, etc.

The most familiar example is $\mathbb{R}^n$ itself.

---

## Subspaces: Definition and Conditions

A subset $W$ of a vector space $V$ is a **subspace** if it satisfies three conditions:

**Condition 1 -- Contains the zero vector:**

$$\vec{0} \in W$$

**Condition 2 -- Closed under addition:**

$$\vec{u}, \vec{v} \in W \Rightarrow \vec{u} + \vec{v} \in W$$

**Condition 3 -- Closed under scalar multiplication:**

$$\vec{v} \in W,\; c \in \mathbb{R} \Rightarrow c\vec{v} \in W$$

Conditions 2 and 3 together mean: $W$ is closed under all linear combinations.

### A Non-Example

In $\mathbb{R}^2$, the first quadrant $W = \{(x, y) : x \geq 0, y \geq 0\}$ is **not** a subspace. The vector $(1, 1)$ belongs to $W$, but $-1 \cdot (1, 1) = (-1, -1) \notin W$. It fails closure under scalar multiplication.

---

## Span

The **span** of vectors $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k \in \mathbb{R}^n$ is the set of all possible linear combinations of those vectors:

$$\text{span}\{\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k\} = \{c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k \mid c_1, c_2, \ldots, c_k \in \mathbb{R}\}$$

**Key property:** The span is always a subspace. Setting all $c_i = 0$ gives $\vec{0}$, and sums and scalar multiples of linear combinations are themselves linear combinations.

---

## 1D Span -- A Line

The span of a single nonzero vector $\vec{v}$:

$$\text{span}\{\vec{v}\} = \{c\vec{v} \mid c \in \mathbb{R}\}$$

This is a **line** through the origin in the direction of $\vec{v}$.

For example, if $\vec{v} = \begin{pmatrix}2\\1\end{pmatrix}$, then $\text{span}\{\vec{v}\}$ is the line through the origin with slope $\tfrac{1}{2}$.

![1D Span visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_1_Span1D.gif)

---

## 2D Span -- A Plane

If two vectors $\vec{v}_1$ and $\vec{v}_2$ are not parallel to each other, then:

$$\text{span}\{\vec{v}_1, \vec{v}_2\}$$

forms a **2-dimensional plane** containing the origin.

In $\mathbb{R}^3$, if $\vec{v}_1 = (1, 0, 0)^\top$ and $\vec{v}_2 = (0, 1, 0)^\top$, then $\text{span}\{\vec{v}_1, \vec{v}_2\}$ is the entire $xy$-plane.

![2D Span visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_1_Span2D.gif)

---

## The Relationship Between Span and Subspaces

| Set of Vectors | Span | Geometric Meaning |
|----------------|------|-------------------|
| $\{\vec{0}\}$ | $\{\vec{0}\}$ | A point (0-dimensional) |
| $\{\vec{v}\}$ ($\vec{v} \neq \vec{0}$) | A line | 1-dimensional subspace |
| $\{\vec{v}_1, \vec{v}_2\}$ (not parallel) | A plane | 2-dimensional subspace |
| $\{\vec{v}_1, \vec{v}_2, \vec{v}_3\}$ (independent) | $\mathbb{R}^3$ | The full 3-dimensional space |

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Vector space | A set closed under addition and scalar multiplication |
| Subspace (3 conditions) | Contains $\vec{0}$, closed under addition, closed under scalar multiplication |
| Span | $\text{span}\{\vec{v}_1,\ldots,\vec{v}_k\}$ = the set of all linear combinations |
| Span is always a subspace | Sums and scalar multiples of linear combinations are still linear combinations |
| 1D span | One vector produces a line through the origin |
| 2D span | Two non-parallel vectors produce a plane through the origin |

> Next up: **Linear Independence and Basis** -- how to determine whether vectors truly point in "different" directions.
