---
title: "Random Variables"
date: 2024-10-08 00:00:00 +0900
categories: [Probability and Statistics]
tags: [probability, statistics, random variable, sample space]
math: true
lang: en
hreflang_ko: /posts/확률변수/
---

Before diving into mathematical statistics, let us first understand one of its most fundamental concepts: the **random variable**.

---

## What Is a Random Variable?

A **random variable** is a function that assigns a numerical value to each outcome of a random experiment. More precisely, given a sample space $C$ associated with a random experiment, a random variable is a function that maps each element of $C$ to exactly one real number.

But to fully grasp this definition, we need to unpack two key terms: **random experiment** and **sample space**.

---

## Random Experiments

A **random experiment** is an experiment that can be repeated under the same conditions, but whose outcome cannot be predicted with certainty before it is performed. The critical feature is *unpredictability* -- even though the conditions are identical each time, the result may differ.

Think of rolling a standard six-sided die. Each time you roll, you get one of the numbers 1 through 6, but you cannot know in advance which one it will be. This is a random experiment.

By contrast, rolling a die whose faces are all labeled "1" would *not* be a random experiment, because the result is perfectly predictable every time.

---

## Sample Spaces

A **sample space** is the set of all possible outcomes of a random experiment.

For example, suppose you roll a standard die **twice**. Each roll can produce any number from 1 to 6, so the sample space consists of all ordered pairs:

$$C = \{(i, j) : i, j \in \{1, 2, 3, 4, 5, 6\}\}$$

Writing these out explicitly:

$$\{(1,1), (1,2), \ldots, (1,6)\}$$

$$\{(2,1), (2,2), \ldots, (2,6)\}$$

$$\vdots$$

$$\{(6,1), (6,2), \ldots, (6,6)\}$$

That gives a total of $6 \times 6 = 36$ possible outcomes. The sample space for rolling a die twice is:

$$C = \{(1,1), (1,2), \ldots, (6,6)\}$$

---

## Putting It Together

Now we can return to the definition of a random variable with full clarity. A random variable takes each outcome in the sample space and assigns it a real number. For instance, if our random experiment is rolling two dice, we might define a random variable $X$ to be the sum of the two rolls:

$$X\big((i, j)\big) = i + j$$

This function maps each of the 36 outcomes to a number between 2 and 12. The randomness of $X$ comes from the randomness of the experiment itself -- we do not know which outcome will occur, so we do not know what value $X$ will take.

This simple but powerful idea -- turning random outcomes into numbers -- is the starting point for all of probability theory and statistics.
