#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Inria
# SPDX-License-Identifier: Apache-2.0

"""GHFFA01 problem.

This problem is inspired by "Geometric and numerical aspects of redundancy",
Wieber, Escande, Dimitrov and Sherikov (2017).

See https://github.com/qpsolvers/qpbenchmark/issues/25
"""

from os import path

import numpy as np
from qpbenchmark.problem import Problem


def get_problem(name: str, alpha: float):
    """Get problem instance.

    Args:
        alpha: Inverse condition number of the problem.
    """
    return Problem(
        P=np.eye(2),
        q=np.zeros(2),
        G=None,
        h=None,
        A=np.array([1.0, alpha]).reshape((1, 2)),
        b=np.array([1.0]),
        lb=None,
        ub=None,
        name=name,
    )


if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    data_dir = path.realpath(path.join(script_dir, "../data"))
    for i, alpha in enumerate([1e-2, 1e-4, 1e-6, 1e-8, 1e-10]):
        name = f"GNAR{i}"
        problem = get_problem(name, alpha)
        save_path = f"{data_dir}/{name}.npz"
        print(f"Writing {name} problem to {save_path}...")
        problem.save(save_path)
