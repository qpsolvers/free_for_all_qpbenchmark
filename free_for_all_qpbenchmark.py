#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Inria
# SPDX-License-Identifier: Apache-2.0

"""Free-for-all test set."""

import os
from typing import Iterator

import qpbenchmark
from qpbenchmark.problem import Problem


class FreeForAllQpbenchmark(qpbenchmark.TestSet):
    """Free-for-all test set.

    Note:
        This test set is open to proposals from the community. Feel free to
        `submit a new problem
        <https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/new?template=new_problem.md>`__.
    """

    @property
    def description(self) -> str:
        return "Community-built test set to benchmark QP solvers."

    @property
    def title(self) -> str:
        return "Free-for-all test set"

    @property
    def sparse_only(self) -> bool:
        """This test set is open to sparse and dense matrices."""
        return False

    def __init__(self):
        """Initialize test set."""
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        self.data_dir = data_dir
        self.__add_known_solver_issues()
        self.__add_known_solver_timeouts()

    def __add_known_solver_issues(self):
        """See how this is done in the maros_meszaros_qpbenchmark."""

    def __add_known_solver_timeouts(self):
        """See how this is done in the maros_meszaros_qpbenchmark."""

    def __iter__(self) -> Iterator[Problem]:
        """Iterate over test set problems."""
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".npz"):
                yield Problem.load(os.path.join(self.data_dir, fname))
