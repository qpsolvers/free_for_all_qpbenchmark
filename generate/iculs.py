#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Ill-conditioned unconstrained least squares (ICULS) problem.

See: https://github.com/qpsolvers/qpbenchmark/issues/29
"""

from os import path

import numpy as np
from qpbenchmark.problem import Problem


def get_problem(n: int, name: str):
    """Get problem instance.

    Args:
        n: Number of optimization variables.
    """
    M = np.array(range(n * n), dtype=float).reshape((n, n))
    P = np.dot(M.T, M)  # this is a positive definite matrix
    q = np.dot(np.ones(n, dtype=float), M)
    return Problem(
        P=P,
        q=q,
        G=None,
        h=None,
        A=None,
        b=None,
        lb=None,
        ub=None,
        name=name,
    )


if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    data_dir = path.realpath(path.join(script_dir, "../data"))
    for i, n in enumerate([100, 1000]):
        problem = get_problem(n, name=f"ICULS{i}")
        problem.save(f"{data_dir}/{problem.name}.npz")
