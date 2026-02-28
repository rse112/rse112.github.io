---
title: "1.1 What Is a Vector?"
date: 2026-01-01 00:00:00 +0900
categories: [Linear Algebra, Vectors]
tags: [linear algebra, mathematics, vectors]
math: true
lang: en
hreflang_ko: /posts/1-1-what-is-vector/
---


## Introduction

Imagine someone gives you directions: "Walk 500 meters." Is that enough to get you where you need to go? Probably not. But if they say "Walk 500 meters north," now you have something useful. The first instruction only tells you **how far** -- that is **magnitude**. The second tells you both **how far** and **which way** -- that is magnitude and **direction**.

This distinction is fundamental in mathematics. A quantity that has only magnitude is called a **scalar**. A quantity that has both magnitude and direction is called a **vector**.

---

## Defining Vectors and Scalars

### Scalars

A scalar is a quantity that is **fully described by a single number**.

- Temperature: $37°C$
- Mass: $5\text{kg}$
- Time: $3\text{s}$

One number tells you everything you need to know.

### Vectors

A vector is a quantity that carries both **magnitude and direction**.

- Velocity: $60\text{km/h}$, heading **east**
- Force: $10\text{N}$, pointing **upward**
- Displacement: $3\text{m}$, toward the **northeast**

![Scalar vs. Vector visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_1_ScalarVsVector.gif)

### Notation

Vectors are typically written in one of these forms:

- Arrow notation: $\vec{v}$
- Boldface notation: $\mathbf{v}$
- Component notation: $(v_1, v_2)$ or $\begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$

The magnitude (length) of a vector is denoted $|\vec{v}|$ or $\|\vec{v}\|$.

---

## Representing Vectors

### Vectors in a Coordinate System

To work with vectors concretely, we need a **coordinate system**. In a 2D coordinate plane, a vector is drawn as an arrow from an **initial point** (tail) to a **terminal point** (tip).

For example, the vector $\vec{AB}$ from point $A(1, 1)$ to point $B(4, 3)$ is:

$$\vec{AB} = B - A = (4-1,\ 3-1) = (3, 2)$$

![Vector in a coordinate system](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_1_VectorInCoordinate.gif)

### Position Vectors

A **position vector** is a vector whose tail is at the origin $O(0, 0)$. The position vector of a point $P(3, 2)$ is simply:

$$\vec{OP} = (3, 2)$$

Position vectors let us represent any vector as a neat pair of coordinates.

### Free Vectors

Vectors are fundamentally **free vectors**. This means that **two vectors are considered identical if they have the same magnitude and direction**, regardless of where they start. Whether a vector begins at the origin or at the point $(2, 3)$, as long as it points the same way and has the same length, it is the same vector.

---

## 2D and 3D Vectors

### 2D Vectors

A two-dimensional vector has two components:

$$\vec{v} = (v_1, v_2)$$

- $v_1$: the component along the $x$-axis
- $v_2$: the component along the $y$-axis

**Example:** $\vec{v} = (3, 2)$ represents a displacement of 3 units in the $x$-direction and 2 units in the $y$-direction.

Its magnitude:

$$|\vec{v}| = \sqrt{v_1^2 + v_2^2} = \sqrt{9 + 4} = \sqrt{13}$$

### 3D Vectors

A three-dimensional vector extends to three components:

$$\vec{w} = (w_1, w_2, w_3)$$

**Example:** $\vec{w} = (1, 2, 3)$

Its magnitude:

$$|\vec{w}| = \sqrt{w_1^2 + w_2^2 + w_3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}$$

---

## Key Takeaways

| Concept | Description |
|---------|-------------|
| Scalar | A quantity with magnitude only (e.g., temperature, mass) |
| Vector | A quantity with both magnitude and direction (e.g., velocity, force) |
| Position Vector | A vector starting from the origin |
| Free Vector | Vectors with the same magnitude and direction are equal, regardless of starting point |
| Vector Notation | $\vec{v} = (v_1, v_2)$ or $\mathbf{v}$ |
| Vector Magnitude | $\|\vec{v}\| = \sqrt{v_1^2 + v_2^2}$ |

> In the next post, we will explore **vector addition and subtraction**.
