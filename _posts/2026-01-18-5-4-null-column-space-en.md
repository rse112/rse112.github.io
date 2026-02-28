---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_4_ColumnSpaceViz.gif
title: "Null Space and Column Space - How to Find Them"
date: 2026-01-18 00:00:00 +0900
categories: [Linear Algebra, Vector Spaces]
tags: [linear algebra, mathematics, vector spaces]
math: true
lang: en
hreflang_ko: /posts/5-4-null-column-space/
---


## Introduction

When you encounter a system of equations $A\vec{x} = \vec{b}$, the very first question is: **"Does a solution exist? And if so, how many solutions are there?"**

There are three possible outcomes: no solution, exactly one solution, or infinitely many solutions. What determines which case you are in? The answer lies in two fundamental subspaces associated with the matrix $A$:

- **Column space:** Determines whether $\vec{b}$ is "reachable" -- that is, whether a solution exists at all.
- **Null space:** Determines how many solutions there are.

Once you understand these two spaces and the relationship between their dimensions, the entire structure of $A\vec{x} = \vec{b}$ becomes transparent.

---

## The Null Space

The **null space** of a matrix $A$ is the set of all vectors that $A$ maps to the zero vector:

$$N(A) = \{\vec{x} \in \mathbb{R}^n \mid A\vec{x} = \vec{0}\}$$

**The null space is a subspace.** Here is the verification:
- $A\vec{0} = \vec{0}$, so $\vec{0} \in N(A)$.
- If $A\vec{u} = \vec{0}$ and $A\vec{v} = \vec{0}$, then $A(\vec{u}+\vec{v}) = \vec{0}$. (Closed under addition.)
- If $A\vec{u} = \vec{0}$, then $A(c\vec{u}) = c\vec{0} = \vec{0}$. (Closed under scalar multiplication.)

The dimension of the null space is called the **nullity**:

$$\text{nullity}(A) = \dim(N(A))$$

![Null space visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_4_NullSpaceViz.gif)

---

## Null Space Example

$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$$

Solving $A\vec{x} = \vec{0}$:

$$x_1 + 2x_2 = 0 \implies x_1 = -2x_2$$

Let the free variable $x_2 = t$:

$$\vec{x} = t\begin{pmatrix}-2\\1\end{pmatrix}, \quad t \in \mathbb{R}$$

$$N(A) = \text{span}\left\{\begin{pmatrix}-2\\1\end{pmatrix}\right\}, \quad \text{nullity}(A) = 1$$

The null space is a line through the origin.

---

## The Column Space

The **column space** of a matrix $A$ is the span of its column vectors.

If the columns of $A$ are $\vec{a}_1, \vec{a}_2, \ldots, \vec{a}_n$, then

$$C(A) = \text{span}\{\vec{a}_1, \vec{a}_2, \ldots, \vec{a}_n\}$$

The column space is the set of all vectors that $A$ can produce -- the **range** (or image) of $A$:

$$C(A) = \{A\vec{x} \mid \vec{x} \in \mathbb{R}^n\} = \text{Range}(A)$$

**The column space is a subspace** because it is a span.

The dimension of the column space is called the **rank**:

$$\text{rank}(A) = \dim(C(A))$$

![Column space visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/5_4_ColumnSpaceViz.gif)

---

## Existence of Solutions

**Key theorem:** $A\vec{x} = \vec{b}$ has a solution if and only if $\vec{b} \in C(A)$.

The reason is straightforward:

$$A\vec{x} = x_1\vec{a}_1 + x_2\vec{a}_2 + \cdots + x_n\vec{a}_n$$

So $A\vec{x}$ is always a linear combination of the columns of $A$. A solution exists precisely when $\vec{b}$ can be written as such a combination -- that is, when $\vec{b}$ lies in the column space.

---

## The Rank-Nullity Theorem

For an $m \times n$ matrix $A$:

$$\text{rank}(A) + \text{nullity}(A) = n$$

This is known as the **Rank-Nullity Theorem** (also called the Dimension Theorem).

**Intuitive meaning:**
- $n$ is the dimension of the input space $\mathbb{R}^n$.
- $\text{rank}(A)$ counts the dimensions that "survive" the transformation -- the directions that actually contribute to the output.
- $\text{nullity}(A)$ counts the dimensions that "collapse" to zero -- the directions that get crushed.
- These two always add up to the total input dimension $n$.

---

## Verifying the Theorem with an Example

$$A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

**Column space:** Column 1, $(1,0,0)^\top$, and Column 2, $(0,1,0)^\top$, are linearly independent. Column 3 = Column 1 + Column 2.

$$C(A) = \text{span}\left\{\begin{pmatrix}1\\0\\0\end{pmatrix}, \begin{pmatrix}0\\1\\0\end{pmatrix}\right\}, \quad \text{rank}(A) = 2$$

**Null space:** Solving $A\vec{x} = \vec{0}$ with free variable $x_3 = t$ gives $x_1 = -t$, $x_2 = -t$.

$$N(A) = \text{span}\left\{\begin{pmatrix}-1\\-1\\1\end{pmatrix}\right\}, \quad \text{nullity}(A) = 1$$

**Verification:** $\text{rank}(A) + \text{nullity}(A) = 2 + 1 = 3 = n$. The theorem checks out.

---

## Key Takeaways

| Concept | Description / Formula |
|---------|----------------------|
| Null space | $N(A) = \{\vec{x} : A\vec{x} = \vec{0}\}$, a subspace |
| Nullity | $\text{nullity}(A) = \dim(N(A))$ |
| Column space | $C(A) = \text{span}\{\text{column vectors}\} = \{A\vec{x}\}$, a subspace |
| Rank | $\text{rank}(A) = \dim(C(A))$ |
| Existence of solutions | $A\vec{x}=\vec{b}$ has a solution $\iff$ $\vec{b} \in C(A)$ |
| Rank-Nullity Theorem | $\text{rank}(A) + \text{nullity}(A) = n$ |
| Unique solution condition | $\text{nullity}(A) = 0$ (null space = $\{\vec{0}\}$) |

> Next up: **Eigenvalues and Eigenvectors** -- the special vectors whose direction is preserved by a linear transformation.
