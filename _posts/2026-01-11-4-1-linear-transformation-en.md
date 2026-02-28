---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_1_LinearTransformGrid.gif
title: "What Is a Linear Transformation? Definition and Examples"
date: 2026-01-11 00:00:00 +0900
categories: [Linear Algebra, Linear Transformations]
tags: [linear algebra, mathematics, linear transformations]
math: true
lang: en
hreflang_ko: /posts/4-1-linear-transformation/
---


## Introduction

Imagine grabbing a map and stretching it, or rotating a sheet of paper so it faces a different direction. Every point on the surface moves **simultaneously** and **according to a consistent rule**. That intuition is exactly what a **linear transformation** captures.

A linear transformation is a function that reshapes a vector space without bending it. Straight lines stay straight, the origin stays fixed, and parallel lines remain parallel. From computer graphics and physics simulations to the layers of a neural network, linear transformations are one of the most fundamental tools in mathematics.

---

## Definition

A **linear transformation** is a function between two vector spaces,

$$T : \mathbb{R}^n \to \mathbb{R}^m$$

that satisfies the following two conditions.

**Condition 1 -- Additivity:**

$$T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})$$

**Condition 2 -- Homogeneity (scalar multiplication is preserved):**

$$T(c\vec{u}) = c\,T(\vec{u})$$

These two conditions can be combined into a single statement:

$$T(c_1\vec{u} + c_2\vec{v}) = c_1\,T(\vec{u}) + c_2\,T(\vec{v})$$

This property is called **linearity**.

![Linear transformation grid visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_1_LinearTransformGrid.gif)

### A Non-Example

The function $f(x) = x + 3$ is **not** a linear transformation. Since $f(0) = 3 \neq 0$, the origin does not map to the origin.

Every linear transformation must satisfy $T(\vec{0}) = \vec{0}$.

---

## Matrix Representation

Every linear transformation $T : \mathbb{R}^n \to \mathbb{R}^m$ can be represented **completely** by a matrix:

$$T(\vec{x}) = A\vec{x}$$

where $A$ is an $m \times n$ matrix.

This is a remarkably powerful fact. All the information about the transformation is packed into a single matrix.

---

## Images of the Basis Vectors

Recall the standard basis vectors of $\mathbb{R}^2$:

$$\hat{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \hat{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

Apply the linear transformation $T$ to each basis vector:

$$T(\hat{e}_1) = \begin{pmatrix} a \\ c \end{pmatrix}, \quad T(\hat{e}_2) = \begin{pmatrix} b \\ d \end{pmatrix}$$

Then the matrix of the transformation is simply:

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

In other words, **the columns of the matrix are the images of the basis vectors**.

For an arbitrary vector $\vec{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$:

$$T(\vec{x}) = x_1\,T(\hat{e}_1) + x_2\,T(\hat{e}_2) = x_1 \begin{pmatrix} a \\ c \end{pmatrix} + x_2 \begin{pmatrix} b \\ d \end{pmatrix} = A\vec{x}$$

![Basis vector transformation visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/4_1_LinearTransformBasis.gif)

---

## Example: Transforming the Unit Square

The unit square has vertices at

$$\begin{pmatrix}0\\0\end{pmatrix},\quad \begin{pmatrix}1\\0\end{pmatrix},\quad \begin{pmatrix}1\\1\end{pmatrix},\quad \begin{pmatrix}0\\1\end{pmatrix}$$

Apply the matrix $A = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$:

$$\begin{pmatrix}0\\0\end{pmatrix} \to \begin{pmatrix}0\\0\end{pmatrix},\quad \begin{pmatrix}1\\0\end{pmatrix} \to \begin{pmatrix}2\\0\end{pmatrix},\quad \begin{pmatrix}1\\1\end{pmatrix} \to \begin{pmatrix}3\\1\end{pmatrix},\quad \begin{pmatrix}0\\1\end{pmatrix} \to \begin{pmatrix}1\\1\end{pmatrix}$$

The square has been transformed into a **parallelogram**. Straight lines remain straight, and parallel sides remain parallel -- this is the geometric essence of linearity.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|-----------------------|
| Linear transformation | $T : \mathbb{R}^n \to \mathbb{R}^m$, preserves addition and scalar multiplication |
| Additivity | $T(\vec{u}+\vec{v}) = T(\vec{u})+T(\vec{v})$ |
| Homogeneity | $T(c\vec{u}) = c\,T(\vec{u})$ |
| Origin condition | $T(\vec{0}) = \vec{0}$ (necessary condition) |
| Matrix representation | $T(\vec{x}) = A\vec{x}$ (every linear transformation has a matrix) |
| Columns = images of basis | Each column of $A$ is $T(\hat{e}_i)$ |
| Geometric meaning | Lines map to lines, parallel lines stay parallel, squares become parallelograms |

> In the next post, we look at specific types of **2D linear transformations -- rotation, reflection, shear, and scaling**.
