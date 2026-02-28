---
title: "1.2 Vector Addition and Subtraction"
date: 2026-01-02 00:00:00 +0900
categories: [Linear Algebra, Vectors]
tags: [linear algebra, mathematics, vectors]
math: true
lang: en
hreflang_ko: /posts/1-2-vector-addition-subtraction/
---


## Introduction

Suppose you start at an intersection and walk 3 km east, then turn and walk 4 km north. Where do you end up relative to where you started? You are 3 km east and 4 km north of your starting point. Combining those two displacements into one is exactly what **vector addition** does.

Vector subtraction is equally intuitive. If your friend is at position $B$ and you are at position $A$, then the relative displacement from you to your friend is $\vec{B} - \vec{A}$. The difference of two position vectors gives you the direction and distance between two points.

---

## Vector Addition

### Component-wise Addition

Given two vectors $\vec{u} = (u_1, u_2)$ and $\vec{v} = (v_1, v_2)$, their sum is computed by **adding corresponding components**:

$$\vec{u} + \vec{v} = (u_1 + v_1,\ u_2 + v_2)$$

In three dimensions:

$$\vec{u} + \vec{v} = (u_1 + v_1,\ u_2 + v_2,\ u_3 + v_3)$$

**Example:** For $\vec{u} = (3, 1)$ and $\vec{v} = (1, 4)$:

$$\vec{u} + \vec{v} = (3+1,\ 1+4) = (4, 5)$$

![Tip-to-Tail vector addition](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_2_VectorAddition.gif)

### Geometric Interpretation: The Tip-to-Tail Rule

The first way to visualize vector addition is the **tip-to-tail method**:

1. Draw $\vec{u}$ starting from any point.
2. Place the **tail** of $\vec{v}$ at the **tip** of $\vec{u}$.
3. The arrow from the tail of $\vec{u}$ to the tip of $\vec{v}$ is the sum $\vec{u} + \vec{v}$.

Think of it as chaining two trips together -- the result is your net displacement.

### Geometric Interpretation: The Parallelogram Law

The second method is the **parallelogram law**:

1. Draw both $\vec{u}$ and $\vec{v}$ from the **same starting point**.
2. Complete the **parallelogram** using the two vectors as adjacent sides.
3. The **diagonal** of the parallelogram is $\vec{u} + \vec{v}$.

![Parallelogram law visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_2_ParallelogramRule.gif)

Both methods always give the same result.

---

## Properties of Addition

For vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ and the zero vector $\vec{0} = (0, 0)$, the following properties hold.

### Commutativity

$$\vec{u} + \vec{v} = \vec{v} + \vec{u}$$

The parallelogram picture makes this obvious: it does not matter which side you draw first -- the diagonal is the same.

### Associativity

$$(\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})$$

The order in which you group three vectors does not affect the final sum.

### Zero Vector (Additive Identity)

The zero vector $\vec{0} = (0, 0)$ is the **additive identity**:

$$\vec{v} + \vec{0} = \vec{0} + \vec{v} = \vec{v}$$

### Additive Inverse

For every vector $\vec{v} = (v_1, v_2)$, there exists an **additive inverse** $-\vec{v} = (-v_1, -v_2)$:

$$\vec{v} + (-\vec{v}) = \vec{0}$$

The additive inverse has the **same magnitude** as $\vec{v}$ but points in the **opposite direction**.

---

## Vector Subtraction

### Definition

Vector subtraction is defined as **adding the additive inverse**:

$$\vec{u} - \vec{v} = \vec{u} + (-\vec{v})$$

In terms of components:

$$\vec{u} - \vec{v} = (u_1 - v_1,\ u_2 - v_2)$$

**Example:** For $\vec{u} = (5, 3)$ and $\vec{v} = (2, 1)$:

$$\vec{u} - \vec{v} = (5-2,\ 3-1) = (3, 2)$$

### Geometric Meaning of Subtraction

When $\vec{u}$ and $\vec{v}$ are drawn from the same starting point, the vector $\vec{u} - \vec{v}$ points **from the tip of $\vec{v}$ to the tip of $\vec{u}$**.

In other words, $\vec{u} - \vec{v}$ represents the relative displacement from the position of $\vec{v}$ to the position of $\vec{u}$. This is how subtraction is used to find the vector between two points.

**Tip-to-tail verification:** Draw $-\vec{v}$ first, then attach $\vec{u}$ at its tip -- you get the same result.

![Geometric meaning of vector subtraction](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/1_2_VectorSubtraction.gif)

---

## Key Takeaways

| Concept | Description |
|---------|-------------|
| Vector Addition (components) | $\vec{u} + \vec{v} = (u_1+v_1,\ u_2+v_2)$ |
| Tip-to-Tail Rule | Place the tail of $\vec{v}$ at the tip of $\vec{u}$ to find the sum |
| Parallelogram Law | The diagonal of the parallelogram formed by $\vec{u}$ and $\vec{v}$ is the sum |
| Commutativity | $\vec{u} + \vec{v} = \vec{v} + \vec{u}$ |
| Associativity | $(\vec{u}+\vec{v})+\vec{w} = \vec{u}+(\vec{v}+\vec{w})$ |
| Zero Vector | $\vec{v} + \vec{0} = \vec{v}$ |
| Additive Inverse | $\vec{v} + (-\vec{v}) = \vec{0}$; same magnitude, opposite direction |
| Vector Subtraction | $\vec{u} - \vec{v} = \vec{u} + (-\vec{v}) = (u_1-v_1,\ u_2-v_2)$ |
| Geometric Meaning of Subtraction | The vector from the tip of $\vec{v}$ to the tip of $\vec{u}$ |

> In the next post, we will explore **scalar multiplication**.
