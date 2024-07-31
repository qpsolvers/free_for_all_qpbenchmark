#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2023-2024 Inria

"""Dense subset of the Free-for-all test set."""

import os
from typing import Iterator

from qpbenchmark.benchmark import main
from qpbenchmark.problem import Problem

from free_for_all import FreeForAll


class FreeForAllDense(FreeForAll):
    """Subset of dense problems from the Free-for-all test set.

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
        return "Free-for-all dense subset"

    @property
    def sparse_only(self) -> bool:
        """This test set is open to sparse and dense matrices."""
        return False

    def __iter__(self) -> Iterator[Problem]:
        """Iterate on test set problems."""
        for problem in super().__iter__():
            if "CONT" in problem.name:
                continue
            yield problem.to_dense()


if __name__ == "__main__":
    main(test_set_path=os.path.abspath(__file__))
