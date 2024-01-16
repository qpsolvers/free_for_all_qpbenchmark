#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Small least-squares problem from the qpsolvers documentation.

See: https://qpsolvers.github.io/qpsolvers/least-squares.html
"""

from os import path

import numpy as np
from qpbenchmark.problem import Problem

R = np.array([[1.0, 2.0, 0.0], [-8.0, 3.0, 2.0], [0.0, 1.0, 1.0]])
s = np.array([3.0, 2.0, 3.0])
G = np.array([[1.0, 2.0, 1.0], [2.0, 0.0, 1.0], [-1.0, 2.0, -1.0]])
h = np.array([3.0, 2.0, -2.0]).reshape((3,))
P = R.T @ R
q = -(s.T @ R)

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    data_dir = path.realpath(path.join(script_dir, "../data"))
    problem = Problem(
        P=P, q=q, G=G, h=h, A=None, b=None, lb=None, ub=None, name="DOCSLS"
    )
    problem.save(f"{data_dir}/{problem.name}.npz")
