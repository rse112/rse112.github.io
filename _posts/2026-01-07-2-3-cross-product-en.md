---
title: "2.3 The Cross Product"
date: 2026-01-07 00:00:00 +0900
categories: [Linear Algebra, Dot and Cross Product]
tags: [linear algebra, mathematics, cross product]
math: true
lang: en
hreflang_ko: /posts/2-3-cross-product/
---


## Introduction

Think about tightening a screw with a screwdriver. You grip the handle and apply a force that rotates it. The direction of your applied force, the axis of the screwdriver, and the resulting rotational effect are all mutually perpendicular. If you curl the fingers of your right hand from the first vector toward the second, your thumb points in the direction of the result. This is the **right-hand rule**.

While the dot product takes two vectors and produces a **scalar**, the **cross product** takes two vectors and produces a new **vector**. That resulting vector is perpendicular to both inputs. This property makes the cross product indispensable in 3D applications -- from computing torque in physics to finding surface normals in computer graphics.

---

## Defining the Cross Product

### The Determinant Formula

For two 3D vectors $\vec{u} = (u_1, u_2, u_3)$ and $\vec{v} = (v_1, v_2, v_3)$, the cross product is defined via the following determinant:

$$\vec{u} \times \vec{v} = \det\begin{pmatrix} \hat{i} & \hat{j} & \hat{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix}$$

Expanding along the first row (cofactor expansion):

$$\vec{u} \times \vec{v} = \hat{i}(u_2 v_3 - u_3 v_2) - \hat{j}(u_1 v_3 - u_3 v_1) + \hat{k}(u_1 v_2 - u_2 v_1)$$

Written in component form:

$$\vec{u} \times \vec{v} = (u_2 v_3 - u_3 v_2,\ u_3 v_1 - u_1 v_3,\ u_1 v_2 - u_2 v_1)$$

![Cross product formula visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/2_3_CrossProductFormula.gif)

### Example

For $\vec{u} = (1, 2, 3)$ and $\vec{v} = (4, 5, 6)$:

$$\vec{u} \times \vec{v} = (2 \cdot 6 - 3 \cdot 5,\ 3 \cdot 4 - 1 \cdot 6,\ 1 \cdot 5 - 2 \cdot 4) = (12-15,\ 12-6,\ 5-8) = (-3, 6, -3)$$

Let us verify that the result is perpendicular to both inputs using the dot product:

$$(-3,6,-3) \cdot (1,2,3) = -3 + 12 - 9 = 0 \checkmark$$
$$(-3,6,-3) \cdot (4,5,6) = -12 + 30 - 18 = 0 \checkmark$$

---

## Magnitude of the Cross Product

### Geometric Meaning -- Area of a Parallelogram

$$\|\vec{u} \times \vec{v}\| = \|\vec{u}\| \|\vec{v}\| \sin\theta$$

where $\theta$ is the angle between the two vectors ($0 \leq \theta \leq \pi$). This value equals the **area of the parallelogram** formed by $\vec{u}$ and $\vec{v}$:

$$\text{Area of parallelogram} = \|\vec{u} \times \vec{v}\|$$

The area of the triangle they span is half of that:

$$\text{Area of triangle} = \frac{1}{2}\|\vec{u} \times \vec{v}\|$$

When two vectors are parallel, $\sin\theta = 0$, so the cross product is the zero vector. When they are perpendicular, $\sin 90° = 1$, and the magnitude of the cross product reaches its maximum.

![Cross product and parallelogram area](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/2_3_CrossProductArea.gif)

---

## Properties of the Cross Product

### Anti-commutativity

$$\vec{v} \times \vec{u} = -(\vec{u} \times \vec{v})$$

Swapping the order of the operands **reverses the direction** of the result. This is why the cross product does not obey commutativity -- order matters.

### Cross Product with Itself

$$\vec{u} \times \vec{u} = \vec{0}$$

Since $\sin 0° = 0$, any vector crossed with itself gives the zero vector.

### Distributivity

$$\vec{u} \times (\vec{v} + \vec{w}) = \vec{u} \times \vec{v} + \vec{u} \times \vec{w}$$

### Scalar Factoring

$$(c\vec{u}) \times \vec{v} = c(\vec{u} \times \vec{v}) = \vec{u} \times (c\vec{v})$$

### Cross Products of Standard Basis Vectors

$$\hat{i} \times \hat{j} = \hat{k}, \quad \hat{j} \times \hat{k} = \hat{i}, \quad \hat{k} \times \hat{i} = \hat{j}$$

Reversing the cyclic order flips the sign: $\hat{j} \times \hat{i} = -\hat{k}$.

---

## Applications

### Normal Vectors

Given two vectors $\vec{u}$ and $\vec{v}$ that lie in a plane, the **normal vector** (perpendicular to that plane) is simply their cross product:

$$\vec{n} = \vec{u} \times \vec{v}$$

This is essential in computer graphics for lighting calculations, collision detection, and rendering.

### Torque

In physics, **torque** (rotational force) $\vec{\tau}$ is the cross product of the position vector $\vec{r}$ and the applied force $\vec{F}$:

$$\vec{\tau} = \vec{r} \times \vec{F}$$

The magnitude is $\|\vec{r}\|\|\vec{F}\|\sin\theta$, and the direction follows the right-hand rule.

### Volume Calculation (Scalar Triple Product)

The volume of the parallelepiped spanned by three vectors $\vec{u}$, $\vec{v}$, and $\vec{w}$ is given by the **scalar triple product**:

$$V = |\vec{u} \cdot (\vec{v} \times \vec{w})|$$

---

## Key Takeaways

| Concept | Formula / Description |
|---------|----------------------|
| Cross Product Definition | $\vec{u} \times \vec{v} = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\u_1&u_2&u_3\\v_1&v_2&v_3\end{pmatrix}$ |
| Magnitude | $\|\vec{u} \times \vec{v}\| = \|\vec{u}\|\|\vec{v}\|\sin\theta$ |
| Direction | Perpendicular to both input vectors (right-hand rule) |
| Anti-commutativity | $\vec{v} \times \vec{u} = -\vec{u} \times \vec{v}$ |
| Parallelogram Area | $\|\vec{u} \times \vec{v}\|$ |
| Triangle Area | $\frac{1}{2}\|\vec{u} \times \vec{v}\|$ |
| Key Applications | Normal vectors, torque, area and volume calculations |

> In the next post, we will explore **matrices** -- a powerful tool for organizing multiple vectors and systems of equations into a single structured table.
