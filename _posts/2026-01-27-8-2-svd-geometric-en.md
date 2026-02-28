---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_2_SVDGeometric.gif
title: "SVD Geometric Interpretation - Visualizing Singular Value Decomposition"
date: 2026-01-27 00:00:00 +0900
categories: [Linear Algebra, SVD]
tags: [linear algebra, mathematics, SVD]
math: true
lang: en
hreflang_ko: /posts/8-2-svd-geometric/
---


## Introduction

Even the most complex machine is ultimately a combination of simple parts. An engine decomposes into combustion, piston motion, and rotary motion. A lever decomposes into a change of force direction and a change of magnitude. Linear transformations work the same way. No matter how complicated a linear transformation may be, the SVD breaks it down into **three simple geometric operations performed in sequence**.

Given $A = U\Sigma V^T$, applying $A$ to a vector $\vec{x}$ proceeds as:

$$A\vec{x} = U\Sigma V^T \vec{x}$$

Reading from right to left: first apply $V^T$ (a rotation), then apply $\Sigma$ (axis-aligned stretching), and finally apply $U$ (another rotation). These three steps capture the essence of every linear transformation. In this post, we will walk through each step and build geometric intuition by watching the unit circle transform into an ellipse.

---

## The Three Geometric Steps

### Overview

$$A\vec{x} = \underbrace{U}_{\text{3. Rotate}} \underbrace{\Sigma}_{\text{2. Stretch}} \underbrace{V^T}_{\text{1. Rotate}} \vec{x}$$

### Step 1: $V^T$ -- Rotation in the Input Space

$V^T$ is an orthogonal matrix, so it is an **isometry** that preserves lengths and angles. Specifically, $V^T$ rotates the coordinate system so that the columns of $V$ (the right singular vectors $\vec{v}_1, \vec{v}_2, \ldots$) become aligned with the standard axes.

$$\vec{x} \xrightarrow{V^T} V^T\vec{x}$$

After this step, the coordinate axes are aligned with the right singular vectors $\vec{v}_i$.

### Step 2: $\Sigma$ -- Stretching Along Each Axis

$\Sigma$ is a diagonal matrix that scales each axis independently. The $i$-th axis is scaled by a factor of $\sigma_i$:

$$V^T\vec{x} \xrightarrow{\Sigma} \Sigma V^T\vec{x}$$

$$\text{$i$-th component} \rightarrow \sigma_i \times \text{$i$-th component}$$

- Since $\sigma_1 \geq \sigma_2 \geq \cdots$, the first direction gets stretched the most
- If $\sigma_i = 0$, that direction collapses to zero -- a loss of dimension
- This is the only step that changes the **shape** of a figure (lengths change here)

### Step 3: $U$ -- Rotation in the Output Space

Finally, $U$ rotates the stretched vectors so they align with the left singular vectors $\vec{u}_i$:

$$\Sigma V^T\vec{x} \xrightarrow{U} U\Sigma V^T\vec{x} = A\vec{x}$$

This step also preserves lengths and angles. Only the $\Sigma$ step alters sizes.

![Geometric meaning of SVD -- the unit circle transforming into an ellipse](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_2_SVDGeometric.gif)

---

## How the Unit Circle Becomes an Ellipse

### The Key Result

When you apply $A$ to the $n$-dimensional unit sphere, the result is an **ellipse** (or ellipsoid) whose:

- **Semi-axis directions** are the left singular vectors $\vec{u}_1, \vec{u}_2, \ldots$
- **Semi-axis lengths** are the singular values $\sigma_1, \sigma_2, \ldots$

$$\{A\vec{x} : \|\vec{x}\| = 1\} = \text{an ellipse with semi-axes of length } \sigma_i \text{ in direction } \vec{u}_i$$

### A 2D Example

$$A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$$

Computing the SVD of this matrix yields singular values $\sigma_1$ and $\sigma_2$. Each point on the unit circle $\vec{x} = (\cos\theta, \sin\theta)$ maps under $A$ to a point on an ellipse.

Step by step:
1. $V^T$: rotates the unit circle (it is still a circle)
2. $\Sigma$: stretches by $\sigma_1$ in the $x$-direction and $\sigma_2$ in the $y$-direction, producing an ellipse
3. $U$: rotates the ellipse so its axes align with $\vec{u}_1$ and $\vec{u}_2$

---

## The Intuition: Every Linear Transformation = Rotate-Stretch-Rotate

### Why Is This So Powerful?

The fact that any linear transformation can be reduced to three simple operations is remarkable. Here is what it means:

1. **There exists a "most important direction."** The right singular vector $\vec{v}_1$ corresponding to the largest singular value $\sigma_1$ is the direction along which the transformation has its greatest effect.

   $$\max_{\|\vec{x}\|=1} \|A\vec{x}\| = \sigma_1, \quad \text{achieved at } \vec{x} = \vec{v}_1$$

2. **There is also a "least important direction."** The direction corresponding to the smallest nonzero singular value $\sigma_r$ is where the transformation has its weakest effect.

3. **Dimensionality reduction arises naturally.** Directions with $\sigma_i \approx 0$ nearly vanish after the transformation, so the directions corresponding to the large singular values carry the "essential information."

### Comparing the Geometric Effects

| Transformation | Geometric Effect |
|---------------|-----------------|
| $V^T$ (orthogonal, $\det=1$) | Pure rotation |
| $V^T$ (orthogonal, $\det=-1$) | Rotation with reflection |
| $\Sigma$ (diagonal) | Axis-aligned scaling |
| $U$ (orthogonal) | Rotation (possibly with reflection) |
| $A = U\Sigma V^T$ | Composition of all three |

---

## Maximum and Minimum Stretch Ratios

### The Spectral Norm

The **spectral norm** (operator 2-norm) of a matrix is its largest singular value:

$$\|A\|_2 = \sigma_1 = \max_{\vec{x} \neq 0} \frac{\|A\vec{x}\|}{\|\vec{x}\|}$$

This is the maximum factor by which $A$ can stretch any unit vector, achieved at the first right singular vector $\vec{v}_1$.

### The Frobenius Norm and SVD

$$\|A\|_F = \sqrt{\sum_{i,j} a_{ij}^2} = \sqrt{\sigma_1^2 + \sigma_2^2 + \cdots + \sigma_r^2}$$

The SVD makes it possible to express many different matrix norms in terms of the singular values.

---

## Summary

| Concept | Formula / Description |
|---------|----------------------|
| Three steps of SVD | $V^T$ (rotate) $\to$ $\Sigma$ (scale) $\to$ $U$ (rotate) |
| Unit sphere image | An ellipse with semi-axis lengths $\sigma_i$ and directions $\vec{u}_i$ |
| Maximum stretch direction | $\vec{v}_1$ (first right singular vector) |
| Maximum stretch ratio | $\sigma_1$ (first singular value) |
| Spectral norm | $\|A\|_2 = \sigma_1$ |
| Frobenius norm | $\|A\|_F = \sqrt{\sum \sigma_i^2}$ |
| Core intuition | Every linear transformation = rotate-stretch-rotate |
| Dimensionality reduction | Directions with $\sigma_i \approx 0$ are "unimportant" |

> In the next post, we explore the **applications of SVD** -- low-rank approximation, image compression, the connection to PCA, the pseudoinverse, and more.
