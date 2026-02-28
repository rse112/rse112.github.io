---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_3_ScalarMultiplication.gif
title: "1.3 Scalar Multiplication"
date: 2026-01-03 00:00:00 +0900
categories: [Linear Algebra, Vectors]
tags: [linear algebra, mathematics, vectors]
math: true
lang: en
hreflang_ko: /posts/1-3-scalar-multiplication/
---


## Introduction

Picture yourself riding a bicycle eastward at $10\text{km/h}$. If you **double** your speed, you are now going $20\text{km/h}$ east. If you cut your speed **in half**, you are going $5\text{km/h}$ east. The direction stays the same; only the magnitude changes. Now, if you slam on the brakes and reverse, you are traveling $10\text{km/h}$ **west** -- the direction has flipped.

The operation of **multiplying a vector by a scalar (a number)** to stretch, shrink, or reverse it is called **scalar multiplication**. Together with addition, it forms the backbone of vector algebra.

---

## Definition of Scalar Multiplication

For a scalar $c \in \mathbb{R}$ and a vector $\vec{v} = (v_1, v_2)$, scalar multiplication is defined by **multiplying each component by the scalar**:

$$c\vec{v} = (cv_1,\ cv_2)$$

In three dimensions:

$$c\vec{v} = (cv_1,\ cv_2,\ cv_3)$$

**Example:** For $c = 3$ and $\vec{v} = (2, -1)$:

$$3\vec{v} = (3 \cdot 2,\ 3 \cdot (-1)) = (6, -3)$$

![Scalar multiplication visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_3_ScalarMultiplication.gif)

---

## Geometric Interpretation

Let us see how different values of $c$ transform a vector geometrically.

### $c > 1$: Scaling Up (Same Direction)

$$c = 2,\quad \vec{v} = (1, 2) \Rightarrow 2\vec{v} = (2, 4)$$

The direction is preserved, and the magnitude is multiplied by $c$.

### $0 < c < 1$: Scaling Down (Same Direction)

$$c = \frac{1}{2},\quad \vec{v} = (4, 2) \Rightarrow \frac{1}{2}\vec{v} = (2, 1)$$

The direction is preserved, and the magnitude shrinks by a factor of $c$.

### $c < 0$: Direction Reversal

$$c = -1,\quad \vec{v} = (3, 1) \Rightarrow -\vec{v} = (-3, -1)$$

The magnitude becomes $|c|$ times the original, and the direction **flips to the opposite**. The special case $c = -1$ gives the additive inverse.

![Negative scalar multiplication reversing direction](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_3_NegativeScalar.gif)

### $c = 0$: The Zero Vector

$$0 \cdot \vec{v} = (0, 0) = \vec{0}$$

Multiplying any vector by zero collapses it to the **zero vector**.

---

## Properties of Scalar Multiplication

For scalars $c, d \in \mathbb{R}$ and vectors $\vec{u}, \vec{v}$, the following properties hold.

### Distributivity over Scalar Addition

$$(c + d)\vec{v} = c\vec{v} + d\vec{v}$$

**Example:** $(2 + 3)\vec{v} = 5\vec{v} = 2\vec{v} + 3\vec{v}$

### Distributivity over Vector Addition

$$c(\vec{u} + \vec{v}) = c\vec{u} + c\vec{v}$$

Scalar multiplication **distributes** over vector addition.

### Associativity

$$(cd)\vec{v} = c(d\vec{v})$$

Multiplying the scalars first and then applying the product to the vector gives the same result as applying them one at a time.

### Multiplicative Identity

$$1 \cdot \vec{v} = \vec{v}$$

The scalar $1$ leaves the vector unchanged.

---

## Linear Combinations

When we combine scalar multiplication with vector addition, we arrive at one of the most powerful ideas in linear algebra: the **linear combination**.

Given vectors $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n$ and scalars $c_1, c_2, \ldots, c_n$, a linear combination is:

$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n$$

**Example:** Let $\vec{v}_1 = (1, 0)$, $\vec{v}_2 = (0, 1)$, $c_1 = 3$, $c_2 = 2$:

$$3(1, 0) + 2(0, 1) = (3, 0) + (0, 2) = (3, 2)$$

Linear combinations are a central theme throughout linear algebra. The key question is always: can a given vector be expressed as a linear combination of other vectors? If so, what are the coefficients? The answers to these questions reveal the structure of vector spaces.

In particular, using the standard basis vectors $\hat{i} = (1, 0)$ and $\hat{j} = (0, 1)$, **every** vector in the 2D plane can be written as a linear combination:

$$\vec{v} = (v_1, v_2) = v_1\hat{i} + v_2\hat{j}$$

---

## Key Takeaways

| Concept | Description |
|---------|-------------|
| Scalar Multiplication | $c\vec{v} = (cv_1,\ cv_2)$; multiply each component by the scalar |
| $c > 1$ | Stretches the vector (same direction) |
| $0 < c < 1$ | Shrinks the vector (same direction) |
| $c < 0$ | Reverses direction (magnitude scaled by $\|c\|$) |
| $c = 0$ | Produces the zero vector $\vec{0}$ |
| Distributivity (scalar) | $(c+d)\vec{v} = c\vec{v} + d\vec{v}$ |
| Distributivity (vector) | $c(\vec{u}+\vec{v}) = c\vec{u} + c\vec{v}$ |
| Associativity | $(cd)\vec{v} = c(d\vec{v})$ |
| Identity | $1 \cdot \vec{v} = \vec{v}$ |
| Linear Combination | $c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n$ |

> In the next post, we will study **vector magnitude and unit vectors**.
