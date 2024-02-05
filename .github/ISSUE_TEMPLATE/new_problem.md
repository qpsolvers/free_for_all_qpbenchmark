---
name: Submit a new problem
about: Propose a new problem for the free-for-all test set
title: ''
labels: ''
assignees: ''
---

### Problem

I propose to add the following problem to the free-for-all test set:

- [ ] **Option 1:** my problem is in a file that I have [saved via qpsolvers](https://qpsolvers.github.io/qpsolvers/quadratic-programming.html#qpsolvers.problem.Problem.save): [zip your ``.npz`` file then drag-and-drop it here]

- [ ] **Option 2:** here is working code to generate the problem:

<details>
<summary>Click here to expand a code template.</summary>

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Make sure you fill out all <FIELDS> below:
#
# - COPYRIGHT_HOLDER: you or your employer.
# - DESCRIPTION: Describe your problem for interested readers.
# - PROBLEM_CODE: Name your problem in up to eight capital letters.
#
# Copyright 2023 <COPYRIGHT_HOLDER>
# SPDX-License-Identifier: Apache-2.0

"""<DESCRIPTION>"""

from os import path

from qpbenchmark.problem import Problem

# Cost: 1/2 x^T P x + q^T x
P = ...
q = ...

# Linear inequalities (None to disable): G x <= h
G = ...
h = ...

# Linear equalities (None to disable): A x == b
A = ...
b = ...

# Box inequalities (None to disable): lb <= x <= ub
lb = ...
ub = ...

if __name__ == "__main__":
    problem = Problem(P, q, G, h, A, b, lb, ub, name="<PROBLEM_CODE>")
    script_dir = path.dirname(path.abspath(__file__))
    data_dir = path.realpath(path.join(script_dir, "../data"))
    problem.save(f"{data_dir}/{problem.name}.npz")
```

</details>

### Context

<!-- How did this problem arise? Why is it interesting to add it to the benchmark? -->

This problem is interesting because...

### References

<!-- If the problem is detailed in a report or research paper, put the relevant references here. -->

1. [Title](link), Foo Bar *et al.*, venue, year.
