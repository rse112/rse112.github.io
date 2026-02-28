---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_3_RotationMatrices3D.gif
title: "3D Linear Transformations - Rotation Matrices and Scaling"
date: 2026-01-13 00:00:00 +0900
categories: [Linear Algebra, Linear Transformations]
tags: [linear algebra, mathematics, linear transformations]
math: true
lang: en
hreflang_ko: /posts/4-3-3d-transformations/
---


## Introduction

In a 3D game, a character turns their head. In an animated film, a robot arm bends at the elbow. A drone tilts in mid-air; a spacecraft adjusts its attitude along three axes. Every one of these motions is described by a **3D linear transformation**.

In three dimensions, there are three independent rotation axes (x, y, z), which makes the landscape of transformations far richer than in 2D. And when you need to handle **translation** (moving objects from one place to another) within the same framework, you turn to **homogeneous coordinates**. Let us explore the world of 3D transformations.

---

## Rotation About the x-Axis

Fix the x-axis and rotate the yz-plane counterclockwise by $\theta$:

$$R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}$$

The x-coordinate stays unchanged; the y and z coordinates mix together exactly like a 2D rotation. In aviation, this is called **roll** -- tilting the wings of an airplane.

---

## Rotation About the y-Axis

Fix the y-axis and rotate the xz-plane by $\theta$:

$$R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}$$

Watch the signs carefully: unlike $R_x$ and $R_z$, the $\sin\theta$ terms appear in different positions. This asymmetry comes from the right-hand rule for the y-axis. In aviation terminology, this is **pitch** -- raising or lowering the nose of the aircraft.

---

## Rotation About the z-Axis

Fix the z-axis and rotate the xy-plane counterclockwise by $\theta$:

$$R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

The upper-left $2 \times 2$ block is identical to the familiar 2D rotation matrix. The z-coordinate is left untouched. In aviation, this is **yaw** -- turning left or right.

![3D rotation matrices visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_3_RotationMatrices3D.gif)

---

## 3D Scaling

Scale by factors of $s_x$, $s_y$, and $s_z$ along each axis:

$$S = \begin{pmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{pmatrix} = \text{diag}(s_x,\, s_y,\, s_z)$$

The volume scaling factor is $|\det(S)| = |s_x \cdot s_y \cdot s_z|$.

![3D scaling matrix visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_3_ScalingMatrix3D.gif)

---

## Comparing the Three Rotations

| Rotation axis | Matrix size | Fixed coordinate | Aviation term |
|---------------|-------------|------------------|---------------|
| x-axis $R_x(\theta)$ | $3\times3$ | x unchanged | Roll |
| y-axis $R_y(\theta)$ | $3\times3$ | y unchanged | Pitch |
| z-axis $R_z(\theta)$ | $3\times3$ | z unchanged | Yaw |

All three rotation matrices satisfy $\det = 1$ and $R^{-1} = R^\top$ (they are orthogonal matrices).

---

## Homogeneous Coordinates

A linear transformation $T(\vec{x}) = A\vec{x}$ always fixes the origin. Therefore, **translation** -- $\vec{x} \mapsto \vec{x} + \vec{t}$ -- is not a linear transformation.

To work around this, we use **homogeneous coordinates**. Embed each 3D point $(x, y, z)$ as a 4D vector:

$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} \longrightarrow \begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix}$$

Now translation can be expressed as a $4 \times 4$ matrix:

$$T_{\vec{t}} = \begin{pmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

With this trick, rotation, scaling, and translation can all be unified as $4 \times 4$ matrix multiplications. This is the standard approach used by graphics APIs like OpenGL and DirectX.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|-----------------------|
| x-axis rotation | $R_x(\theta)$: rotates the yz-plane, Roll |
| y-axis rotation | $R_y(\theta)$: rotates the xz-plane, Pitch (watch the signs) |
| z-axis rotation | $R_z(\theta)$: rotates the xy-plane, Yaw |
| 3D scaling | $\text{diag}(s_x, s_y, s_z)$; volume scales by $\|s_xs_ys_z\|$ |
| Orthogonal matrices | Rotation matrices satisfy $R^{-1} = R^\top$, $\det = 1$ |
| Homogeneous coordinates | Extend 3D points to 4D; express translation as matrix multiplication |
| 4x4 translation matrix | Place the translation vector $\vec{t}$ in the last column |

> In the next post, we examine **composition of transformations -- why the order in which you apply two transformations matters**.
