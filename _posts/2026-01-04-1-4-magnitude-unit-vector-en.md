---
title: "1.4 Magnitude and Unit Vectors"
date: 2026-01-04 00:00:00 +0900
categories: [Linear Algebra, Vectors]
tags: [linear algebra, mathematics, vectors]
math: true
lang: en
hreflang_ko: /posts/1-4-magnitude-unit-vector/
---


## Introduction

Think about what a GPS tells you: "Your destination is 500 meters away, to the northeast." Two pieces of information -- **distance** (500 m) and **direction** (northeast) -- and you need both for the navigation to be useful.

Vectors work the same way. Given a vector like $\vec{v} = (3, 4)$, we can ask two separate questions: "How long is it?" and "Which direction does it point?" The **magnitude** answers the first question (via the Pythagorean theorem), and the **unit vector** answers the second. Mastering these two concepts gives you much finer control over vectors.

---

## Vector Magnitude (Norm)

### Definition

The magnitude (also called the **norm** or **length**) of a 2D vector $\vec{v} = (v_1, v_2)$ is the distance from the origin to the tip of the vector. It is computed using the **Pythagorean theorem**:

$$\|\vec{v}\| = \sqrt{v_1^2 + v_2^2}$$

Geometrically, $v_1$ is the horizontal leg, $v_2$ is the vertical leg, and the magnitude is the hypotenuse of the right triangle they form.

### Example

For $\vec{v} = (3, 4)$:

$$\|\vec{v}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

This is the classic 3-4-5 right triangle, which makes the result easy to verify by intuition.

More examples:

- $\vec{u} = (1, 1)$: $\|\vec{u}\| = \sqrt{1+1} = \sqrt{2} \approx 1.414$
- $\vec{w} = (-5, 0)$: $\|\vec{w}\| = \sqrt{25+0} = 5$

The magnitude is **always non-negative**. It equals zero if and only if $\vec{v} = \vec{0}$ (the zero vector).

![Vector magnitude (norm) visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_4_VectorMagnitude.gif)

### Magnitude in 3D

For a 3D vector $\vec{v} = (v_1, v_2, v_3)$, we apply the Pythagorean theorem twice:

$$\|\vec{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$$

**Example:** For $\vec{v} = (1, 2, 2)$:

$$\|\vec{v}\| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$

The formula generalizes to $n$ dimensions:

$$\|\vec{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} = \sqrt{\sum_{i=1}^{n} v_i^2}$$

---

## Unit Vectors

### Definition

A **unit vector** is a vector with magnitude exactly 1. It encodes **direction only**, with the magnitude information stripped away.

To find the unit vector $\hat{v}$ in the direction of $\vec{v}$, divide $\vec{v}$ by its magnitude:

$$\hat{v} = \frac{\vec{v}}{\|\vec{v}\|}$$

Verification: $\|\hat{v}\| = \left\|\frac{\vec{v}}{\|\vec{v}\|}\right\| = \frac{\|\vec{v}\|}{\|\vec{v}\|} = 1$ $\checkmark$

### Example

For $\vec{v} = (3, 4)$ with $\|\vec{v}\| = 5$:

$$\hat{v} = \frac{(3, 4)}{5} = \left(\frac{3}{5},\ \frac{4}{5}\right) = (0.6,\ 0.8)$$

Verification: $\|\hat{v}\| = \sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = \sqrt{1} = 1$ $\checkmark$

**Important:** The zero vector $\vec{0}$ has no unit vector, because dividing by zero is undefined.

![Unit vector (normalization) visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_4_UnitVector.gif)

---

## Standard Basis Vectors

The unit vectors that point along the coordinate axes are called **standard basis vectors** (or **standard unit vectors**).

### In 2D

$$\hat{i} = (1,\ 0), \qquad \hat{j} = (0,\ 1)$$

- $\hat{i}$: unit vector in the positive $x$-direction
- $\hat{j}$: unit vector in the positive $y$-direction

### In 3D

$$\hat{i} = (1, 0, 0), \qquad \hat{j} = (0, 1, 0), \qquad \hat{k} = (0, 0, 1)$$

- $\hat{i}$: along the $x$-axis
- $\hat{j}$: along the $y$-axis
- $\hat{k}$: along the $z$-axis

Each standard basis vector has magnitude 1:

$$\|\hat{i}\| = \sqrt{1^2} = 1, \quad \|\hat{j}\| = \sqrt{1^2} = 1, \quad \|\hat{k}\| = \sqrt{1^2} = 1$$

---

## Decomposing a Vector into Magnitude and Direction

Every vector can be decomposed as the **product of its magnitude and its direction**:

$$\vec{v} = \|\vec{v}\| \cdot \hat{v}$$

- $\|\vec{v}\|$: a scalar (how large the vector is)
- $\hat{v}$: a unit vector (which direction it points)

**Example:** For $\vec{v} = (3, 4)$:

$$\vec{v} = 5 \cdot \left(\frac{3}{5},\ \frac{4}{5}\right)$$

This decomposition is used constantly in practice -- in physics to separate the magnitude of a force from its direction, and in computer graphics to perform normalization.

Using the standard basis vectors, any 2D vector can also be written as:

$$\vec{v} = (v_1, v_2) = v_1\hat{i} + v_2\hat{j}$$

---

## Key Takeaways

| Concept | Description |
|---------|-------------|
| Magnitude (2D) | $\|\vec{v}\| = \sqrt{v_1^2 + v_2^2}$ (Pythagorean theorem) |
| Magnitude (3D) | $\|\vec{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$ |
| Magnitude Properties | Always $\|\vec{v}\| \geq 0$; equals $0$ iff $\vec{v}=\vec{0}$ |
| Unit Vector | $\hat{v} = \vec{v} / \|\vec{v}\|$; a vector of magnitude 1 |
| Standard Basis (2D) | $\hat{i}=(1,0)$, $\hat{j}=(0,1)$ |
| Standard Basis (3D) | $\hat{i}=(1,0,0)$, $\hat{j}=(0,1,0)$, $\hat{k}=(0,0,1)$ |
| Magnitude-Direction Decomposition | $\vec{v} = \|\vec{v}\| \cdot \hat{v}$ |
| Classic Example | $\vec{v}=(3,4) \Rightarrow \|\vec{v}\|=5$, $\hat{v}=(0.6, 0.8)$ |

> In the next post, we will explore the **dot product** -- an operation that measures the angle between two vectors.
