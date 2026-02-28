---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/7_2_GramSchmidtProcess.gif
title: "Gram-Schmidt Process - Orthogonalization Step by Step"
date: 2026-01-24 00:00:00 +0900
categories: [Linear Algebra, Orthogonality]
tags: [linear algebra, mathematics, orthogonality]
math: true
lang: en
hreflang_ko: /posts/7-2-gram-schmidt/
---


## Introduction

Imagine reorganizing a set of crooked, tangled shelves so that they all sit perfectly at right angles to one another. You want to preserve the space they span while making the arrangement as clean as possible. The **Gram-Schmidt process** does exactly this for vectors. Given a set of linearly independent vectors that are not necessarily orthogonal, it systematically produces an orthonormal basis spanning the same subspace.

Developed by the mathematicians Jorgen Gram and Erhard Schmidt in the 1800s, this procedure is foundational to numerical analysis, signal processing, and machine learning -- it is the engine behind the **QR decomposition**. With an orthonormal basis, coordinate calculations reduce to simple dot products, and computations become far more numerically stable.

---

## The Core Idea: Subtract the Projection

### A Quick Review of Projection

The orthogonal projection of a vector $\vec{a}$ onto a unit vector $\vec{e}$ is:

$$\text{proj}_{\vec{e}}\vec{a} = (\vec{a} \cdot \vec{e})\vec{e}$$

The idea behind Gram-Schmidt is beautifully simple: from each new vector, subtract the components along all previously processed directions. What remains is orthogonal to everything that came before.

---

## The Algorithm

### Input: Linearly independent vectors $\vec{a}_1, \vec{a}_2, \ldots, \vec{a}_k$

### Output: Orthonormal vectors $\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_k$

**Step 1: Normalize the first vector**

$$\vec{e}_1 = \frac{\vec{a}_1}{\|\vec{a}_1\|}$$

**Step 2: Remove the component along $\vec{e}_1$ from the second vector, then normalize**

$$\vec{u}_2 = \vec{a}_2 - (\vec{a}_2 \cdot \vec{e}_1)\vec{e}_1$$

$$\vec{e}_2 = \frac{\vec{u}_2}{\|\vec{u}_2\|}$$

**Step 3: Remove the components along $\vec{e}_1$ and $\vec{e}_2$ from the third vector, then normalize**

$$\vec{u}_3 = \vec{a}_3 - (\vec{a}_3 \cdot \vec{e}_1)\vec{e}_1 - (\vec{a}_3 \cdot \vec{e}_2)\vec{e}_2$$

$$\vec{e}_3 = \frac{\vec{u}_3}{\|\vec{u}_3\|}$$

**General step $k$:**

$$\vec{u}_k = \vec{a}_k - \sum_{j=1}^{k-1} (\vec{a}_k \cdot \vec{e}_j)\vec{e}_j$$

$$\vec{e}_k = \frac{\vec{u}_k}{\|\vec{u}_k\|}$$

![Step-by-step visualization of the Gram-Schmidt process](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/7_2_GramSchmidtProcess.gif)

---

## A Worked Example

### Three Vectors in 3D

$$\vec{a}_1 = \begin{pmatrix}1\\1\\0\end{pmatrix}, \quad \vec{a}_2 = \begin{pmatrix}1\\0\\1\end{pmatrix}, \quad \vec{a}_3 = \begin{pmatrix}0\\1\\1\end{pmatrix}$$

**Step 1:**

$$\|\vec{a}_1\| = \sqrt{1+1+0} = \sqrt{2}$$

$$\vec{e}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix}$$

**Step 2:**

$$\vec{a}_2 \cdot \vec{e}_1 = \frac{1}{\sqrt{2}}(1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0) = \frac{1}{\sqrt{2}}$$

$$\vec{u}_2 = \begin{pmatrix}1\\0\\1\end{pmatrix} - \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix} = \begin{pmatrix}1\\0\\1\end{pmatrix} - \frac{1}{2}\begin{pmatrix}1\\1\\0\end{pmatrix} = \begin{pmatrix}1/2\\-1/2\\1\end{pmatrix}$$

$$\|\vec{u}_2\| = \sqrt{1/4 + 1/4 + 1} = \sqrt{3/2} = \frac{\sqrt{6}}{2}$$

$$\vec{e}_2 = \frac{2}{\sqrt{6}}\begin{pmatrix}1/2\\-1/2\\1\end{pmatrix} = \frac{1}{\sqrt{6}}\begin{pmatrix}1\\-1\\2\end{pmatrix}$$

**Step 3:**

$$\vec{a}_3 \cdot \vec{e}_1 = \frac{1}{\sqrt{2}}(0+1+0) = \frac{1}{\sqrt{2}}, \quad \vec{a}_3 \cdot \vec{e}_2 = \frac{1}{\sqrt{6}}(0-1+2) = \frac{1}{\sqrt{6}}$$

$$\vec{u}_3 = \begin{pmatrix}0\\1\\1\end{pmatrix} - \frac{1}{2}\begin{pmatrix}1\\1\\0\end{pmatrix} - \frac{1}{6}\begin{pmatrix}1\\-1\\2\end{pmatrix} = \begin{pmatrix}-2/3\\2/3\\2/3\end{pmatrix}$$

$$\vec{e}_3 = \frac{1}{\sqrt{4/3}} \begin{pmatrix}-2/3\\2/3\\2/3\end{pmatrix} = \frac{1}{\sqrt{3}}\begin{pmatrix}-1\\1\\1\end{pmatrix}$$

---

## QR Decomposition

### $A = QR$

When the Gram-Schmidt process is organized in matrix form, it yields the **QR decomposition**. For a matrix $A = [\vec{a}_1 \; \vec{a}_2 \; \cdots \; \vec{a}_n]$:

$$A = QR$$

- $Q = [\vec{e}_1 \; \vec{e}_2 \; \cdots \; \vec{e}_n]$: a matrix whose columns are orthonormal
- $R$: an upper triangular matrix with entries $R_{ij} = \vec{a}_j \cdot \vec{e}_i$ (for $i \leq j$)

$$R = \begin{pmatrix} \vec{a}_1\cdot\vec{e}_1 & \vec{a}_2\cdot\vec{e}_1 & \vec{a}_3\cdot\vec{e}_1 \\ 0 & \vec{a}_2\cdot\vec{e}_2 & \vec{a}_3\cdot\vec{e}_2 \\ 0 & 0 & \vec{a}_3\cdot\vec{e}_3 \end{pmatrix}$$

QR decomposition is widely used for solving linear systems, least squares problems, and eigenvalue computation (the QR algorithm).

---

## Numerical Stability

### Modified Gram-Schmidt

In theory, the classical Gram-Schmidt process works perfectly. In practice, however, floating-point rounding errors accumulate and can gradually destroy the orthogonality of the output vectors. The **Modified Gram-Schmidt** algorithm addresses this by re-orthogonalizing against each previously computed vector immediately, which suppresses the buildup of numerical error. In production numerical libraries, Modified Gram-Schmidt or **Householder reflections** are used to produce more stable QR decompositions.

---

## Summary

| Concept | Formula / Description |
|---------|----------------------|
| Goal | Linearly independent vectors $\to$ orthonormal basis |
| Projection | $\text{proj}_{\vec{e}}\vec{a} = (\vec{a}\cdot\vec{e})\vec{e}$ |
| Orthogonalization | $\vec{u}_k = \vec{a}_k - \sum_{j<k}(\vec{a}_k\cdot\vec{e}_j)\vec{e}_j$ |
| Normalization | $\vec{e}_k = \vec{u}_k / \|\vec{u}_k\|$ |
| QR decomposition | $A = QR$ ($Q$: orthonormal columns, $R$: upper triangular) |
| Entries of $R$ | $R_{ij} = \vec{a}_j \cdot \vec{e}_i$ (for $i \leq j$) |
| Numerical stability | Use Modified Gram-Schmidt or Householder reflections |

> In the next post, we explore **Least Squares**, a method for finding the best approximate solution when a linear system has no exact solution.
