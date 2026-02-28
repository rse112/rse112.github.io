---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_2_Rotation2D.gif
title: "4.2 2D Linear Transformations"
date: 2026-01-12 00:00:00 +0900
categories: [Linear Algebra, Linear Transformations]
tags: [linear algebra, mathematics, linear transformations]
math: true
lang: en
hreflang_ko: /posts/4-2-2d-transformations/
---


## Introduction

Think about rotating an image on your phone, or flipping a game sprite so a character faces the opposite direction. Movie special effects, CAD software, map rotations on your screen -- behind all of these lies **2D linear transformations**.

Every 2D linear transformation is captured by a single $2 \times 2$ matrix. Change the four numbers in that matrix, and every point in the plane moves to a new position. In this post, we examine the four most common transformations.

---

## Rotation

The matrix that rotates every point **counterclockwise** by an angle $\theta$ about the origin is

$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

**Derivation:** Rotate the basis vector $\hat{e}_1 = (1, 0)^\top$ by $\theta$ to get $(\cos\theta, \sin\theta)^\top$. Rotate $\hat{e}_2 = (0, 1)^\top$ to get $(-\sin\theta, \cos\theta)^\top$. Place these as columns, and you obtain $R_\theta$.

**Example:** For $\theta = 90°$,

$$R_{90°} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$

The vector $(1, 0)^\top$ maps to $(0, 1)^\top$ -- exactly a 90-degree counterclockwise turn.

**Properties of the rotation matrix:**
- $\det(R_\theta) = \cos^2\theta + \sin^2\theta = 1$ (area is preserved).
- $R_\theta^{-1} = R_{-\theta} = R_\theta^\top$ (the inverse is simply rotation in the opposite direction).

![2D rotation visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_2_Rotation2D.gif)

---

## Reflection

**Reflection across the x-axis** -- flips the y-coordinate:

$$M_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Reflection across the y-axis** -- flips the x-coordinate:

$$M_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$$

**Reflection across the line $y = x$** -- swaps x and y coordinates:

$$M_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

A key property of every reflection matrix: $\det(M) = -1$. Area is preserved, but the orientation is reversed (like looking in a mirror).

![2D reflection visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_2_Reflection2D.gif)

---

## Shear

**Horizontal shear** -- each point slides in the x-direction by an amount proportional to its y-coordinate:

$$S_H = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$$

The point $(x, y)^\top$ maps to $(x + ky,\; y)^\top$. A square tilts into a parallelogram -- think of a stack of cards pushed sideways.

**Vertical shear:**

$$S_V = \begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}$$

A notable property of shear transformations: $\det(S) = 1$, so areas are unchanged.

![2D shear visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_2_Shear2D.gif)

---

## Scaling

Stretching or compressing by a factor of $s_x$ in the x-direction and $s_y$ in the y-direction:

$$S = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$$

**Special cases:**

| Condition | Meaning |
|-----------|---------|
| $s_x = s_y = s$ | Uniform (isotropic) scaling |
| $s_x = -1, s_y = 1$ | Reflection across the y-axis |
| $s_x = 1, s_y = -1$ | Reflection across the x-axis |
| $0 < s < 1$ | Shrinking |
| $s > 1$ | Enlarging |

The determinant is $\det(S) = s_x \cdot s_y$, so the area changes by a factor of $|s_x \cdot s_y|$.

---

## Comparison of Transformations

| Transformation | Matrix | Determinant | Area change |
|----------------|--------|-------------|-------------|
| Rotation by $\theta$ | $\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ | $1$ | Preserved |
| Reflection (x-axis) | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | $-1$ | Preserved (orientation flipped) |
| Reflection (y-axis) | $\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ | $-1$ | Preserved (orientation flipped) |
| Horizontal shear $k$ | $\begin{pmatrix}1&k\\0&1\end{pmatrix}$ | $1$ | Preserved |
| Scaling | $\begin{pmatrix}s_x&0\\0&s_y\end{pmatrix}$ | $s_xs_y$ | Scaled by $\|s_xs_y\|$ |

---

## Key Takeaways

| Concept | Description / Formula |
|---------|-----------------------|
| Rotation matrix | $R_\theta = \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$ |
| Inverse of rotation | $R_\theta^{-1} = R_{-\theta} = R_\theta^\top$ |
| Reflection (x-axis) | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$, $\det = -1$ |
| Reflection (y-axis) | $\begin{pmatrix}-1&0\\0&1\end{pmatrix}$, $\det = -1$ |
| Horizontal shear | $\begin{pmatrix}1&k\\0&1\end{pmatrix}$, $\det = 1$ |
| Scaling | $\begin{pmatrix}s_x&0\\0&s_y\end{pmatrix}$, $\det = s_xs_y$ |
| Determinant and area | $|\det(A)|$ is the area scaling factor; the sign indicates orientation |

> In the next post, we explore **3D linear transformations -- rotations about the x, y, and z axes, and homogeneous coordinates**.
