---
title: "Conditional Probability"
date: 2024-10-08 00:00:00 +0900
categories: [Probability and Statistics]
tags: [probability, statistics, conditional probability, Bayes]
math: true
lang: en
hreflang_ko: /posts/조건부확률/
---

### What Is Conditional Probability?

**Conditional probability** is the probability of an event occurring *given that* another event has already occurred.

The conditional probability of event $A$ given event $B$ is written $P(A \mid B)$ and read as "the probability of $A$ given $B$."

The formula is:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Here, $P(A \cap B)$ is the probability that both $A$ and $B$ occur, and $P(B)$ is the probability that $B$ occurs (which must be nonzero for the expression to be defined).

The intuition is straightforward: once we know that $B$ has happened, $B$ becomes our new "universe." We then ask what fraction of that universe also belongs to $A$.

---

### Example

At a certain university, 60% of students are male and 40% are female. Among male students, 30% major in engineering; among female students, 20% major in engineering.

**Question:** A student is randomly selected from the engineering majors. What is the probability that this student is male?

---

### Solution

**Step 1: Find the overall proportion of engineering students.**

$$P(\text{Engineering}) = (0.6 \times 0.3) + (0.4 \times 0.2) = 0.18 + 0.08 = 0.26$$

So 26% of all students are engineering majors.

**Step 2: Apply the conditional probability formula.**

We want $P(\text{Male} \mid \text{Engineering})$:

$$P(\text{Male} \mid \text{Engineering}) = \frac{P(\text{Male} \cap \text{Engineering})}{P(\text{Engineering})} = \frac{0.6 \times 0.3}{0.26} = \frac{0.18}{0.26} \approx 0.692$$

Therefore, the probability that a randomly selected engineering student is male is approximately **69%**.

---

### Connection to Bayes' Theorem

Notice that in the example above, we effectively used **Bayes' theorem** without naming it explicitly. Bayes' theorem provides a systematic way to "reverse" conditional probabilities:

$$P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}$$

In our example:
- $A$ = the student is male
- $B$ = the student is an engineering major
- $P(B \mid A) = 0.3$ (probability of engineering given male)
- $P(A) = 0.6$ (probability of being male)
- $P(B) = 0.26$ (total probability of engineering)

Plugging in:

$$P(A \mid B) = \frac{0.3 \times 0.6}{0.26} = \frac{0.18}{0.26} \approx 0.692$$

Bayes' theorem is one of the most important results in probability and statistics, with applications ranging from medical diagnosis to spam filtering to machine learning.
