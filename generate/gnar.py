#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""GHFFA01 problem.

This problem is inspired by "Geometric and numerical aspects of redundancy",
Wieber, Escande, Dimitrov and Sherikov (2017).

See https://github.com/qpsolvers/qpbenchmark/issues/25
"""

from os import path

import numpy as np
from qpbenchmark.problem import Problem


def get_problem_1(name: str, alpha: float):
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


def get_problem_2(alpha: float):
    """Get problem instance.

    Args:
        alpha: Inverse condition number of the problem.
    """
    return Problem(
        P=np.eye(2),
        q=np.zeros(2),
        G=None,
        h=None,
        A=np.array([[1.0, 0.0], [1.0, alpha]]),
        b=np.array([0.0, 1.0]),
        lb=None,
        ub=None,
        name=f"GHFFA02_{alpha=}",
    )


def save_problem(problem: Problem) -> None:
    script_dir = path.dirname(path.abspath(__file__))
    data_dir = path.realpath(path.join(script_dir, "../data"))
    save_path = f"{data_dir}/{problem.name}.npz"
    print(f"Writing {problem.name} problem to {save_path}...")
    problem.save(save_path)


if __name__ == "__main__":
    for i, alpha in enumerate([1e-2, 1e-4, 1e-6, 1e-8, 1e-10]):
        problem_1 = get_problem_1(f"GNAR1{i}", alpha)
        problem_2 = get_problem_2(f"GNAR2{i}", alpha)
        save_problem(problem_1)
        save_problem(problem_2)
