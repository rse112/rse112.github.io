---
title: "2.1 The Dot Product"
date: 2026-01-05 00:00:00 +0900
categories: [Linear Algebra, Dot and Cross Product]
tags: [linear algebra, mathematics, dot product]
math: true
lang: en
hreflang_ko: /posts/2-1-dot-product/
---


## Introduction

When you push an object, how much of your effort actually moves it? If you push in exactly the direction the object moves, all of your force goes into useful work. But if you push at an angle -- say, sideways while the object slides forward -- only part of your force contributes to the motion. In physics, **work** captures this relationship:

$$W = \|\vec{F}\|\|\vec{d}\|\cos\theta$$

where $\theta$ is the angle between the force vector $\vec{F}$ and the displacement vector $\vec{d}$. The smaller the angle (the more aligned the vectors), the more work gets done. The operation at the heart of this formula is the **dot product**. It takes two vectors and returns a single number that measures how much they point in the same direction.

---

## Defining the Dot Product

### Algebraic Definition

For $n$-dimensional vectors $\vec{u} = (u_1, u_2, \ldots, u_n)$ and $\vec{v} = (v_1, v_2, \ldots, v_n)$, the dot product is the sum of the products of corresponding components:

$$\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n = \sum_{k=1}^{n} u_k v_k$$

**Example** -- For 2D vectors $\vec{u} = (3, 4)$ and $\vec{v} = (1, 2)$:

$$\vec{u} \cdot \vec{v} = 3 \times 1 + 4 \times 2 = 3 + 8 = 11$$

Notice that the result is a **scalar** (a single number), not a vector. The dot product takes two vectors as input and produces a number as output.

![Algebraic definition of the dot product](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/2_1_DotProductAlgebraic.gif)

### Geometric Definition

Using the angle $\theta$ between two vectors ($0 \leq \theta \leq \pi$), the dot product can also be expressed as:

$$\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$$

where $\|\vec{u}\|$ is the magnitude of $\vec{u}$. These two definitions are completely equivalent -- you can derive one from the other using the law of cosines.

![Geometric definition of the dot product](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/2_1_DotProductGeometric.gif)

---

## Properties of the Dot Product

### Commutativity

$$\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$$

Since multiplication of real numbers is commutative, the order of the component products does not matter.

### Distributivity

$$\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}$$

The dot product distributes over vector addition, which means you can expand and factor dot product expressions just like ordinary algebra.

### Dot Product with Itself -- The Square of the Magnitude

$$\vec{v} \cdot \vec{v} = v_1^2 + v_2^2 + \cdots + v_n^2 = \|\vec{v}\|^2$$

This gives us a clean way to express magnitude in terms of the dot product:

$$\|\vec{v}\| = \sqrt{\vec{v} \cdot \vec{v}}$$

### Scalar Factoring

For a scalar $c$:

$$(c\vec{u}) \cdot \vec{v} = c(\vec{u} \cdot \vec{v}) = \vec{u} \cdot (c\vec{v})$$

---

## The Orthogonality Condition

Two vectors are **orthogonal** (perpendicular) when $\theta = 90°$. Since $\cos 90° = 0$:

$$\vec{u} \cdot \vec{v} = 0 \quad \Leftrightarrow \quad \vec{u} \perp \vec{v}$$

This condition appears throughout linear algebra. For instance, the standard basis vectors are mutually orthogonal:

$$\hat{i} \cdot \hat{j} = (1,0,0) \cdot (0,1,0) = 0$$

By convention, the zero vector $\vec{0}$ is considered orthogonal to every vector.

---

## Computing the Angle Between Vectors

Rearranging the geometric definition for $\cos\theta$ gives us a formula for the angle between any two vectors:

$$\cos\theta = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$

$$\theta = \arccos\!\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}\right)$$

**Example** -- For $\vec{u} = (1, 0)$ and $\vec{v} = (1, 1)$:

$$\cos\theta = \frac{1 \cdot 1 + 0 \cdot 1}{\sqrt{1} \cdot \sqrt{2}} = \frac{1}{\sqrt{2}} \implies \theta = 45°$$

Even without computing the exact angle, the **sign** of the dot product reveals the directional relationship at a glance:

| Dot Product Value | Angle Range | Interpretation |
|-------------------|-------------|----------------|
| $> 0$ | $0° \leq \theta < 90°$ | Vectors share a common direction |
| $= 0$ | $\theta = 90°$ | Vectors are orthogonal |
| $< 0$ | $90° < \theta \leq 180°$ | Vectors point in opposing directions |

---

## Key Takeaways

| Concept | Formula / Description |
|---------|----------------------|
| Algebraic Definition | $\vec{u} \cdot \vec{v} = \sum_{k=1}^{n} u_k v_k$ |
| Geometric Definition | $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$ |
| Commutativity | $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$ |
| Relation to Magnitude | $\vec{v} \cdot \vec{v} = \|\vec{v}\|^2$ |
| Orthogonality Test | $\vec{u} \cdot \vec{v} = 0 \Leftrightarrow \vec{u} \perp \vec{v}$ |
| Angle Formula | $\cos\theta = \dfrac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$ |
| Physical Meaning | A scalar that measures how much two vectors point in the same direction |

> In the next post, we will study **vector projection** -- using the dot product to "cast the shadow" of one vector onto another.
