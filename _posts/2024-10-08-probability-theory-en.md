---
title: "Probability Theory: Axioms and Set Operations"
date: 2024-10-08 00:00:00 +0900
categories: [Probability and Statistics]
tags: [probability, statistics, probability axioms, set theory]
math: true
lang: en
hreflang_ko: /posts/확률이론/
---

Just as arithmetic begins with addition and subtraction, probability theory begins with basic set operations. Before we can talk about how probability works, we need to understand **unions** and **intersections** -- the building blocks from which all probability calculations are constructed.

---

## Union

The **union** of two or more sets is the set of elements that belong to *at least one* of the sets (with duplicates removed).

The union is denoted by $\cup$. For two sets $A$ and $B$, their union is written $A \cup B$.

**Example:**

If $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$, then $A \cup B = \{1, 2, 3, 4\}$.

For a (possibly infinite) sequence of sets, we write:

$$\bigcup_{n=1}^{\infty} A_n = A_1 \cup A_2 \cup A_3 \cup \cdots$$

---

## Intersection

The **intersection** of two or more sets is the set of elements that belong to *all* of the sets simultaneously.

The intersection is denoted by $\cap$. For two sets $A$ and $B$, their intersection is written $A \cap B$.

**Example:**

If $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$, then $A \cap B = \{2, 3\}$.

For a (possibly infinite) sequence of sets:

$$\bigcap_{n=1}^{\infty} A_n = A_1 \cap A_2 \cap A_3 \cap \cdots$$

---

## The Axioms of Probability

For a function $P$ to qualify as a **probability measure**, it must satisfy three axioms:

### Axiom 1: Total Probability Is 1

The probability of the entire sample space is 1:

$$P(\Omega) = 1$$

where $\Omega$ denotes the sample space. In other words, *something* must happen.

### Axiom 2: Non-Negativity

The probability of any event is between 0 and 1:

$$0 \leq P(A_n) \leq 1$$

Probabilities cannot be negative, and they cannot exceed 1.

### Axiom 3: Countable Additivity

If $A_1, A_2, A_3, \ldots$ are **mutually exclusive** events (meaning no two of them can occur at the same time), then:

$$P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n)$$

In plain language: the probability that *at least one* of a collection of mutually exclusive events occurs is the sum of their individual probabilities.

---

## Why These Axioms Matter

These three axioms, known as the **Kolmogorov axioms**, are the foundation of all probability theory. Every theorem about probability -- from the law of large numbers to Bayes' theorem -- is ultimately derived from these three simple rules.

A function $P$ defined on events that satisfies all three axioms is called a **probability measure**, and the events $A_n$ are properly called **random events** (or simply **events**) within this framework.
