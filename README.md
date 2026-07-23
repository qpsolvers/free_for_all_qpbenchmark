# Free-for-all test set for QP solvers

This repository contains quadratic programs (QPs) in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). It is [free-for-all](https://en.wiktionary.org/wiki/free-for-all#Noun), open to problems from all fields, hard and easy. Here are the reports produced by the benchmarking tool:

- 📈 <a href="results/free_for_all.md"><strong>Free-for-all test set results</strong></a>
- 📈 [Dense subtest results](https://github.com/qpsolvers/free_for_all_qpbenchmark/blob/main/results/free_for_all_dense.md)

The methodology and limitations of the benchmark are described in the [qpbenchmark readme](https://github.com/qpsolvers/qpbenchmark/).

## Installation

The recommended process is to install the benchmark and all solvers using [pixi](https://pixi.prefix.dev/):

```console
pixi install
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

```console
pixi run free_for_all         # full test set
pixi run free_for_all_dense   # dense subset
```

The outcome, written to the `results/` directory, is a standardized report comparing all available solvers against the different benchmark metrics. You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/free_for_all_qpbenchmark/discussions/categories/results).

## Contributing

Do you have quadratic programs to share? Join the benchmark by submitting it to this test set: open a PR (preferred), or complete the submission form:

- 🙌 **[Submit a new problem](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/new?template=new_problem.md)**

You can also contribute by running the benchmark on your machine and posting your results to the [Results forum](https://github.com/qpsolvers/free_for_all_qpbenchmark/discussions/categories/results).

## Problems

Here are all problems in this test set:

| Problem name  | Source and details |
|---------------|--------------------|
| ``CONT-*``    | [Maros-Meszaros test set](https://www.cuter.rl.ac.uk/Problems/marmes.shtml) |
| ``DOCSLS``    | From [this issue](https://github.com/qpsolvers/qpsolvers/issues/278) |
| ``GNAR*``     | Proposed in [#2](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/2) and [#3](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/3), details in [this paper](https://hal.inria.fr/hal-01418462/document) |
| ``ICULS*``    | Proposed in [#1](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/1) |
| ``LIPMWALK*`` | Proposed in [#3](https://github.com/qpsolvers/mpc_qpbenchmark/issues/3), details in [this paper](https://inria.hal.science/inria-00390462) |
| ``QUADCMPC*`` | Proposed in [mpc\_qpbenchmark#1](https://github.com/qpsolvers/mpc_qpbenchmark/issues/1), details in [this thesis](https://laas.hal.science/tel-03936109/document) |
| ``WHLIPBAL*`` | Proposed in [#4](https://github.com/qpsolvers/mpc_qpbenchmark/issues/4), details in [this paper](https://inria.hal.science/hal-04198663/) |

These problems have been contributed by:

- [@paLeziart](https://github.com/paLeziart): QUADCMPC
- [@stephane-caron](https://github.com/stephane-caron): LIPMWALK, WHLIPBAL

## Citation

This test set is run using `qpbenchmark`. If you use it in your works, you can refer to it using [this citation](https://github.com/qpsolvers/qpbenchmark#citation).

## See also

Related test sets that may be relevant to your use cases:

- [Maros-Meszaros test set](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/): a standard test set with problems designed to be difficult.
- [Model predictive control](https://github.com/qpsolvers/mpc_qpbenchmark): model predictive control problems arising e.g. in robotics.
