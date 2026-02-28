---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/2_2_VectorProjection.gif
title: "Vector Projection Formula - How to Project One Vector onto Another"
date: 2026-01-06 00:00:00 +0900
categories: [Linear Algebra, Dot and Cross Product]
tags: [linear algebra, mathematics, projection]
math: true
lang: en
hreflang_ko: /posts/2-2-projection/
---


## Introduction

On a sunny afternoon, plant a stick vertically in the ground. When the sun is directly overhead, the shadow is just a dot. As the sun dips toward the horizon, the shadow stretches longer and longer. The length and direction of that shadow depend on the stick's length and the angle of the sunlight. Computing the "shadow" that one vector casts onto another is precisely what **vector projection** does.

This idea shows up far more often than you might expect. In physics, you decompose a force along a ramp. In signal processing, you extract a specific frequency component. In machine learning, you reduce the dimensionality of data. At its core, vector projection is the tool for **isolating the component of a vector that points in a particular direction**.

---

## Scalar Projection

### Definition

The **scalar projection** of $\vec{v}$ onto $\vec{u}$ is the signed length of the shadow that $\vec{v}$ casts in the direction of $\vec{u}$. It is denoted $\text{comp}_{\vec{u}}\vec{v}$.

Starting from the geometric definition of the dot product, $\vec{v} \cdot \vec{u} = \|\vec{v}\| \|\vec{u}\| \cos\theta$:

$$\text{comp}_{\vec{u}}\vec{v} = \|\vec{v}\| \cos\theta = \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}$$

Using the unit vector $\hat{u} = \dfrac{\vec{u}}{\|\vec{u}\|}$, this simplifies to:

$$\text{comp}_{\vec{u}}\vec{v} = \vec{v} \cdot \hat{u}$$

The scalar projection carries a sign: it is positive when $\theta < 90°$ and negative when $\theta > 90°$.

### Example

For $\vec{v} = (3, 4)$ and $\vec{u} = (1, 0)$ (the unit vector along the $x$-axis):

$$\text{comp}_{\vec{u}}\vec{v} = \frac{(3)(1) + (4)(0)}{\sqrt{1^2 + 0^2}} = \frac{3}{1} = 3$$

The shadow of $(3, 4)$ onto the $x$-axis has length 3, which matches our intuition.

---

## Vector Projection

### Definition

The scalar projection tells us the **length** of the shadow, but we often need the shadow as a **vector**. To get it, multiply the scalar projection by the unit vector in the direction of $\vec{u}$:

$$\text{proj}_{\vec{u}}\vec{v} = \left(\frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}\right)\hat{u} = \left(\frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}\right)\frac{\vec{u}}{\|\vec{u}\|} = \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\,\vec{u}$$

This vector is **parallel** to $\vec{u}$ and represents the component of $\vec{v}$ that lies along $\vec{u}$.

### Example

For $\vec{v} = (2, 3)$ and $\vec{u} = (4, 0)$:

$$\frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2} = \frac{(2)(4) + (3)(0)}{16} = \frac{8}{16} = \frac{1}{2}$$

$$\text{proj}_{\vec{u}}\vec{v} = \frac{1}{2}(4, 0) = (2, 0)$$

![Vector projection visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/2_2_VectorProjection.gif)

---

## The Perpendicular Component

Any vector $\vec{v}$ can be **decomposed** into a component along $\vec{u}$ and a component perpendicular to $\vec{u}$:

$$\vec{v} = \underbrace{\text{proj}_{\vec{u}}\vec{v}}_{\text{component along } \vec{u}} + \underbrace{(\vec{v} - \text{proj}_{\vec{u}}\vec{v})}_{\text{component perpendicular to } \vec{u}}$$

Writing the perpendicular component as $\vec{v}_\perp$:

$$\vec{v}_\perp = \vec{v} - \text{proj}_{\vec{u}}\vec{v} = \vec{v} - \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\,\vec{u}$$

Let us verify that $\vec{v}_\perp$ is indeed orthogonal to $\vec{u}$:

$$\vec{v}_\perp \cdot \vec{u} = \left(\vec{v} - \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\vec{u}\right) \cdot \vec{u} = \vec{v} \cdot \vec{u} - \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}(\vec{u} \cdot \vec{u}) = \vec{v} \cdot \vec{u} - \vec{v} \cdot \vec{u} = 0 \checkmark$$

---

## Applications

### Physics: Work

When a force $\vec{F}$ acts on an object that moves along a displacement $\vec{d}$, only the component of $\vec{F}$ in the direction of $\vec{d}$ does work:

$$W = \vec{F} \cdot \hat{d} \cdot \|\vec{d}\| = \vec{F} \cdot \vec{d}$$

### Shadow Length

If parallel light shines in the direction $\hat{n}$, the length of the shadow cast by a vector $\vec{v}$ is the absolute value of its scalar projection: $|\text{comp}_{\hat{n}}\vec{v}|$.

### The Gram-Schmidt Process

Given a set of vectors that are not mutually orthogonal, you can convert them into an orthogonal (or orthonormal) basis by repeatedly subtracting projections. At each step, you remove the component that lies along the previously processed vectors. This procedure is known as **Gram-Schmidt orthogonalization**, and vector projection is its core operation.

---

## Key Takeaways

| Concept | Formula / Description |
|---------|----------------------|
| Scalar Projection | $\text{comp}_{\vec{u}}\vec{v} = \dfrac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}$ |
| Vector Projection | $\text{proj}_{\vec{u}}\vec{v} = \dfrac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\,\vec{u}$ |
| Perpendicular Component | $\vec{v}_\perp = \vec{v} - \text{proj}_{\vec{u}}\vec{v}$ |
| Vector Decomposition | $\vec{v} = \text{proj}_{\vec{u}}\vec{v} + \vec{v}_\perp$ |
| Unit Vector Form | $\text{comp}_{\vec{u}}\vec{v} = \vec{v} \cdot \hat{u}$, $\text{proj}_{\vec{u}}\vec{v} = (\vec{v} \cdot \hat{u})\hat{u}$ |
| Orthogonality Check | $\vec{v}_\perp \cdot \vec{u} = 0$ |

> In the next post, we will study the **cross product** -- an operation defined only in three dimensions that produces a new vector perpendicular to both inputs.
