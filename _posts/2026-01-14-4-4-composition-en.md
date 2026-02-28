---
title: "4.4 Composition of Transformations"
date: 2026-01-14 00:00:00 +0900
categories: [Linear Algebra, Linear Transformations]
tags: [linear algebra, mathematics, linear transformations]
math: true
lang: en
hreflang_ko: /posts/4-4-composition/
---


## Introduction

"First rotate 90 degrees to the right, then stretch by a factor of 2 in the x-direction."
"First stretch by a factor of 2 in the x-direction, then rotate 90 degrees to the right."

Do these two sequences produce the same result? **No, they do not.**

Matrix multiplication is not commutative -- swapping the order generally changes the outcome. This is not a bug; it is a fundamental property of how transformations work. When you program a robot arm or design keyframes in a 3D animation, getting the order wrong means getting a completely different motion. Understanding **composition of transformations** is one of the core skills of linear algebra.

---

## Definition of Composition

Given transformations $T_1 : \mathbb{R}^n \to \mathbb{R}^m$ and $T_2 : \mathbb{R}^m \to \mathbb{R}^k$, the **composite transformation** applies them in sequence:

$$T_2 \circ T_1 : \mathbb{R}^n \to \mathbb{R}^k, \quad (T_2 \circ T_1)(\vec{x}) = T_2(T_1(\vec{x}))$$

$T_1$ is applied **first**, and $T_2$ is applied **second**.

![Transformation composition visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_4_TransformComposition.gif)

---

## Matrix Representation

If $T_1(\vec{x}) = A\vec{x}$ and $T_2(\vec{x}) = B\vec{x}$, then

$$(T_2 \circ T_1)(\vec{x}) = B(A\vec{x}) = (BA)\vec{x}$$

The matrix of the composite transformation is $BA$ -- **the matrix of the transformation applied last goes on the left**.

This convention may feel backwards at first, but it follows naturally from how matrix-vector multiplication works: you read from right to left.

---

## Order Matters: $AB \neq BA$

**Example:** Let $R$ be the 45-degree rotation matrix and $M$ the reflection across the x-axis.

$$R = R_{45°} = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \end{pmatrix}, \quad M = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Case 1 -- Rotate first, then reflect:** The composite matrix is $MR$.

$$MR = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \end{pmatrix} = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ -\tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \end{pmatrix}$$

**Case 2 -- Reflect first, then rotate:** The composite matrix is $RM$.

$$RM = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \end{pmatrix}$$

$MR \neq RM$ -- different order, different result.

![Composition order difference visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_4_CompositionOrder.gif)

---

## Inverse Transformations

The **inverse** of a linear transformation $T(\vec{x}) = A\vec{x}$ is

$$T^{-1}(\vec{y}) = A^{-1}\vec{y}$$

The matrix of the inverse transformation is simply the inverse of the original matrix.

For the inverse to exist, $A$ must be invertible: $\det(A) \neq 0$.

**Inverse of a composition:**

$$(T_2 \circ T_1)^{-1} = T_1^{-1} \circ T_2^{-1}$$

In matrix form:

$$(BA)^{-1} = A^{-1}B^{-1}$$

The order reverses -- just like socks and shoes: you put on socks first and shoes second, but you take off shoes first and socks second.

---

## Worked Example: 45-Degree Rotation Followed by x-Axis Reflection

Apply both transformations to the vector $\vec{x} = (1, 0)^\top$.

**Step 1:** Rotate by 45 degrees.

$$R_{45°}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}\tfrac{\sqrt{2}}{2}\\\tfrac{\sqrt{2}}{2}\end{pmatrix}$$

**Step 2:** Reflect across the x-axis.

$$M_x\begin{pmatrix}\tfrac{\sqrt{2}}{2}\\\tfrac{\sqrt{2}}{2}\end{pmatrix} = \begin{pmatrix}\tfrac{\sqrt{2}}{2}\\-\tfrac{\sqrt{2}}{2}\end{pmatrix}$$

Computing with the composite matrix $M_x R_{45°}$ in one step produces the same result.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|-----------------------|
| Composition | $(T_2 \circ T_1)(\vec{x}) = T_2(T_1(\vec{x}))$ |
| Composite matrix | $T_1 \to A$, $T_2 \to B$ gives composite matrix $BA$ |
| Order convention | The matrix of the later transformation goes on the left |
| Non-commutativity | In general, $AB \neq BA$ |
| Inverse transformation | Matrix of $T^{-1}$ is $A^{-1}$ |
| Inverse of a composition | $(BA)^{-1} = A^{-1}B^{-1}$ (order reverses) |
| Existence of inverse | Requires $\det(A) \neq 0$ |

> In the next post, we explore **vector spaces -- subspaces and span**.
