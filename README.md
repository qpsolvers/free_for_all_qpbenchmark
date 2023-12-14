# Free-for-all test set for QP solvers

This repository contains quadratic programs (QPs) in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). It is [free-for-all](https://en.wiktionary.org/wiki/free-for-all#Noun), open to problems from all fields, hard and easy. Here is the report produced by the benchmarking tool:

<p align=center>
  📈 <a href="results/free_for_all_qpbenchmark_ref.md"><strong>Free-for-all test set results</strong></a>
</p>

## Installation

The recommended process is to install the benchmark and all solvers in an isolated environment using ``conda``:

```console
conda env create -f environment.yaml
conda activate qpbenchmark
```

It is also possible to install ``qpbenchmark`` [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

```
qpbenchmark ./free_for_all_qpbenchmark.py run
```

The outcome, written to the `results/` directory, is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/free_for_all_qpbenchmark/discussions/categories/results).

## Contributions

The problems in this test set have been contributed by:

| Problems | Contributor | Details |
|----------|-------------|---------|
| ``ICULS*`` | [@stephane-caron](https://github.com/stephane-caron) | Proposed in [#1](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/1) |
| ``GNAR*`` | [@stephane-caron](https://github.com/stephane-caron) | Proposed in [#2](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/2) and [#3](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/3), details in [this paper](https://hal.inria.fr/hal-01418462/document) |
| ``QUADCMPC*`` | [@paLeziart](https://github.com/paLeziart) | Proposed in [mpc\_qpbenchmark#1](https://github.com/qpsolvers/mpc_qpbenchmark/issues/1), details in [this thesis](https://laas.hal.science/tel-03936109/document) |

## Citation

If you use `qpbenchmark` in your scientific works, please cite it *e.g.* as follows:

```bibtex
@software{qpbenchmark2023,
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin},
  license = {Apache-2.0},
  month = dec,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  url = {https://github.com/qpsolvers/qpbenchmark},
  version = {2.0.0},
  year = {2023}
}
```

You can also click on ``Cite this repository`` at the top-right of the [repository page](https://github.com/qpsolvers/qpbenchmark/).
