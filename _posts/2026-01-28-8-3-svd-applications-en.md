---
image: https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_3_SVDApplications.gif
title: "8.3 Applications of SVD"
date: 2026-01-28 00:00:00 +0900
categories: [Linear Algebra, SVD]
tags: [linear algebra, mathematics, SVD]
math: true
lang: en
hreflang_ko: /posts/8-3-svd-applications/
---


## Introduction

When studying linear algebra, it is natural to wonder: "Where is this actually used?" For the SVD, the answer is: everywhere. Netflix's movie recommendation engine, medical image compression, Google's search algorithm, facial recognition systems, GPS error correction -- the SVD plays a central role in all of them.

In this post, we take a systematic tour of the major applications of SVD: low-rank approximation and image compression, the connection to PCA, the pseudoinverse and least squares, and the condition number. All of these flow naturally from a single factorization: $A = U\Sigma V^T$. The SVD is not just a mathematical tool -- it is the foundational language of modern data science.

---

## Low-Rank Approximation

### The Outer Product Expansion

The SVD can be written as a sum of rank-one matrices:

$$A = U\Sigma V^T = \sum_{i=1}^{r} \sigma_i \vec{u}_i \vec{v}_i^T$$

Each term $\sigma_i \vec{u}_i \vec{v}_i^T$ is a **rank-1 matrix**. The first term captures the most "important" information in $A$, while subsequent terms add progressively finer details.

![Low-rank approximation -- matrix reconstruction using different numbers of singular values](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_3_LowRankApproximation.gif)

### The Rank-$k$ Approximation

Keeping only the first $k$ terms gives the **rank-$k$ approximation**:

$$A_k = \sum_{i=1}^{k} \sigma_i \vec{u}_i \vec{v}_i^T = U_k \Sigma_k V_k^T$$

Here $U_k$ consists of the first $k$ columns of $U$, $\Sigma_k$ is the $k \times k$ diagonal matrix of the top $k$ singular values, and $V_k$ consists of the first $k$ columns of $V$.

### The Eckart-Young Theorem

**$A_k$ is the closest rank-$k$ matrix to $A$.**

$$\min_{\text{rank}(B) \leq k} \|A - B\|_2 = \|A - A_k\|_2 = \sigma_{k+1}$$

$$\min_{\text{rank}(B) \leq k} \|A - B\|_F = \|A - A_k\|_F = \sqrt{\sigma_{k+1}^2 + \cdots + \sigma_r^2}$$

This theorem guarantees that the approximation provided by the SVD is theoretically optimal.

---

## Image Compression

### A Grayscale Image Is a Matrix

An $m \times n$ pixel image is naturally an $m \times n$ matrix $A$, where each entry is a brightness value (0--255).

**Storage cost comparison:**

- Original matrix $A$: $m \times n$ numbers
- Rank-$k$ approximation $A_k$: $k(m + n + 1)$ numbers (storing $U_k$, $\Sigma_k$, and $V_k$)

**Compression ratio** = $\dfrac{k(m+n+1)}{mn}$

When $k \ll \min(m,n)$, the savings are substantial.

**Example:** A $1000 \times 1000$ image with $k = 50$

- Original: $10^6$ numbers
- Compressed: $50 \times 2001 \approx 100{,}050$ numbers
- Compression ratio $\approx$ 10x

Because the largest singular values carry the vast majority of the image's information, choosing an appropriate $k$ yields visually near-lossless compression.

![SVD applications -- PCA, image compression, and pseudoinverse visualization](https://cdn.jsdelivr.net/gh/rse112/math-animations@main/media/gifs/8_3_SVDApplications.gif)

---

## Connection to PCA

### Principal Component Analysis

Consider a data matrix $X \in \mathbb{R}^{m \times n}$ where each row is a data point and each column is a feature. The **covariance matrix** is:

$$C = \frac{1}{m-1} X^T X \quad (\text{assuming the data is centered})$$

Using the SVD $X = U\Sigma V^T$:

$$C = \frac{1}{m-1}(V\Sigma U^T)(U\Sigma V^T) = \frac{1}{m-1}V\Sigma^2 V^T$$

Therefore:
- **Principal component directions** = the right singular vectors $\vec{v}_1, \vec{v}_2, \ldots$ of $X$ (ordered by decreasing variance)
- **Variance along each principal component** = $\dfrac{\sigma_i^2}{m-1}$
- **Dimensionality reduction to $k$ dimensions**: $X \approx U_k\Sigma_k V_k^T$, using $XV_k$ as the new coordinates

**Explained Variance Ratio (EVR):**

$$\text{EVR}_k = \frac{\sum_{i=1}^k \sigma_i^2}{\sum_{i=1}^r \sigma_i^2}$$

---

## The Pseudoinverse

### $A^+ = V\Sigma^+ U^T$

For matrices that have no inverse (rectangular matrices, or singular square matrices), we define the **Moore-Penrose pseudoinverse**:

$$A^+ = V\Sigma^+ U^T$$

$\Sigma^+$ is formed by taking the reciprocal of each nonzero diagonal entry of $\Sigma$ and then transposing:

$$\Sigma^+ = \begin{pmatrix} 1/\sigma_1 & & \\ & \ddots & \\ & & 1/\sigma_r \end{pmatrix}^T \quad (\text{zeros remain zero})$$

### Properties of the Pseudoinverse

$A^+$ satisfies the four Moore-Penrose conditions:
1. $AA^+A = A$
2. $A^+AA^+ = A^+$
3. $(AA^+)^T = AA^+$
4. $(A^+A)^T = A^+A$

### Least Squares and the Pseudoinverse

The least squares solution of $A\vec{x} = \vec{b}$ with **minimum norm** is:

$$\hat{x} = A^+\vec{b} = V\Sigma^+U^T\vec{b}$$

This can be computed in a numerically stable way using the SVD.

---

## The Condition Number

### A Measure of Numerical Stability

The **condition number** of a matrix $A$:

$$\kappa(A) = \|A\|_2 \cdot \|A^{-1}\|_2 = \frac{\sigma_{\max}}{\sigma_{\min}} = \frac{\sigma_1}{\sigma_r}$$

The condition number tells you how much a small error in the input can be amplified in the output.

- $\kappa(A) \approx 1$: numerically stable (well-conditioned)
- $\kappa(A) \gg 1$: numerically unstable (ill-conditioned)

**Example:** If $\kappa(A) = 10^{10}$ and the input data has errors on the order of $10^{-16}$ (the floating-point precision limit), the solution could have errors as large as $10^{-6}$.

---

## Summary of SVD Applications

| Application | How SVD Is Used | Key Formula / Concept |
|------------|----------------|----------------------|
| Low-rank approximation | Keep top $k$ singular values/vectors | $A_k = \sum_{i=1}^k \sigma_i\vec{u}_i\vec{v}_i^T$ |
| Eckart-Young theorem | Optimal rank-$k$ approximation guaranteed | $\min_{\text{rank}(B)\leq k}\|A-B\|_F = \sqrt{\sum_{i>k}\sigma_i^2}$ |
| Image compression | Store the rank-$k$ approximation | Storage cost: $k(m+n+1)$ |
| PCA | Principal components = right singular vectors | $X = U\Sigma V^T$; PCs are columns of $V$ |
| Dimensionality reduction | Project onto top $k$ principal components | $XV_k$ = reduced coordinates |
| Pseudoinverse | Minimum-norm least squares solution | $A^+ = V\Sigma^+U^T$ |
| Least squares | Numerically stable computation | $\hat{x} = A^+\vec{b}$ |
| Condition number | Assess numerical stability | $\kappa(A) = \sigma_1/\sigma_r$ |
| Rank determination | Count nonzero singular values | $\text{rank}(A) = r$ |
| Matrix norms | Frobenius and spectral norms | $\|A\|_F = \sqrt{\sum\sigma_i^2}$, $\|A\|_2 = \sigma_1$ |

---

## Closing Thoughts: The Culmination of Linear Algebra

When you first learn linear algebra, the focus is on computation: vectors, matrices, determinants, solving systems of equations. But as you reach eigenvalues, orthogonality, and finally the SVD, the true power of the subject reveals itself.

The SVD is the capstone of this journey. Every matrix decomposes as $A = U\Sigma V^T$, and this single factorization lays bare all of the matrix's structural information -- its rank, its dimensions, its most important directions, its numerical stability. From data compression to noise removal, from dimensionality reduction to optimization and the foundations of machine learning, the SVD is a tool you will encounter everywhere.

"Every linear transformation is a rotation, a stretch, and another rotation." This simple fact is what makes linear algebra so powerful and so beautiful.

> Throughout these chapters, we have explored eigenvalues and eigenvectors, orthogonality, the Gram-Schmidt process, least squares, and the singular value decomposition. These concepts are deeply interconnected, and together they form the language of modern mathematics and engineering.
