# Free-for-all test set for QP solvers

This repository contains quadratic programs (QPs) in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). It is [free-for-all](https://en.wiktionary.org/wiki/free-for-all#Noun), open to problems from all fields, hard and easy. Here is the report produced by the benchmarking tool:

- 📈 <a href="results/free_for_all_qpbenchmark_ref.md"><strong>Free-for-all test set results</strong></a>

Are you working on a QP right now? Join the benchmark by submitting it to this test set:

- **[Submit a new problem](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/new?template=new_problem.md)**

## Installation

The recommended process is to install the benchmark and all solvers in an isolated environment using ``conda``:

```console
conda env create -f environment.yaml
conda activate qpbenchmark
```

It is also possible to install the benchmark individually by ``pip install qpbenchmark``.

## Usage

Run the test set as follows:

```
python free_for_all_qpbenchmark.py run
```

The outcome, written to the `results/` directory, is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/free_for_all_qpbenchmark/discussions/categories/results).

## Problems

Here are all problems in this test set:

| Problem name  | CUTE [classification](https://www.cuter.rl.ac.uk//Problems/classification.shtml) | Source and details |
|---------------|-------------|-----------------------------------|
| ``CONT-050``  | QLR2-AN-2597-2401 | [Maros-Meszaros test set](https://www.cuter.rl.ac.uk/Problems/marmes.shtml) |
| ``CONT-100``  | QLR2-AN-10197-9801 | ↑ |
| ``CONT-101``  | QLR2-AN-10197-10098 | ↑ |
| ``CONT-200``  | QLR2-AN-40397-39601 | ↑ |
| ``CONT-201``  | QLR2-AN-40397-40198 | ↑ |
| ``CONT-300``  | QLR2-AN-90597-90298 | ↑ |
| ``DOCSLS``    | QLR2-AN-3-3 | From [this issue](https://github.com/qpsolvers/qpsolvers/issues/278) |
| ``GNAR0``     | QLR2-AN-2-1 | Proposed in [#2](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/2) and [#3](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/3), details in [this paper](https://hal.inria.fr/hal-01418462/document) |
| ``GNAR1``     | QLR2-AN-2-1 | ↑ |
| ``GNAR2``     | QLR2-AN-2-1 | ↑ |
| ``GNAR3``     | QLR2-AN-2-1 | ↑ |
| ``GNAR4``     | QLR2-AN-2-1 | ↑ |
| ``ICULS0``    | QLR2-AN-1000-0 | Proposed in [#1](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/1) |
| ``ICULS1``    | QLR2-AN-1000-0 | ↑ |
| ``LIPMWALK0`` | QLR2-RN-16-32 | Proposed in [#3](https://github.com/qpsolvers/mpc_qpbenchmark/issues/3), details in [this paper](https://inria.hal.science/inria-00390462) |
| ``LIPMWALK1`` | QLR2-RN-16-32 | ↑ |
| ``LIPMWALK2`` | QLR2-RN-16-32 | ↑ |
| ``LIPMWALK3`` | QLR2-RN-16-32 | ↑ |
| ``LIPMWALK4`` | QLR2-RN-16-32 | ↑ |
| ``QUADCMPC1`` | QLR2-RN-768-896 | Proposed in [mpc\_qpbenchmark#1](https://github.com/qpsolvers/mpc_qpbenchmark/issues/1), details in [this thesis](https://laas.hal.science/tel-03936109/document) |
| ``QUADCMPC2`` | QLR2-RN-768-896 | ↑ |
| ``QUADCMPC3`` | QLR2-RN-768-896 | ↑ |
| ``QUADCMPC4`` | QLR2-RN-768-896 | ↑ |
| ``WHLIPBAL0`` | QLR2-RN-50-100 | Proposed in [#4](https://github.com/qpsolvers/mpc_qpbenchmark/issues/4), details in [this paper](https://inria.hal.science/hal-04198663/) |
| ``WHLIPBAL1`` | QLR2-RN-50-100 | ↑ |
| ``WHLIPBAL2`` | QLR2-RN-50-100 | ↑ |
| ``WHLIPBAL3`` | QLR2-RN-50-100 | ↑ |
| ``WHLIPBAL4`` | QLR2-RN-50-100 | ↑ |

These problems have been contributed by:

- [@paLeziart](https://github.com/paLeziart): QUADCMPC
- [@stephane-caron](https://github.com/stephane-caron): LIPMWALK, WHLIPBAL

## Contributing

New problems are welcome: open a PR (preferred), or complete the **[submission form](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/new?template=new_problem.md)** and we will add them to the test set. You can also contribute by running the benchmark on your machine and posting your results to the [Results forum](https://github.com/qpsolvers/free_for_all_qpbenchmark/discussions/categories/results).

## Citation

If you use `qpbenchmark` in your scientific works, please cite it *e.g.* as follows:

```bibtex
@software{qpbenchmark2024,
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin},
  license = {Apache-2.0},
  month = jan,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  url = {https://github.com/qpsolvers/qpbenchmark},
  version = {2.2.0},
  year = {2024}
}
```

## See also

Related test sets that may be relevant to your use cases:

- [Maros-Meszaros test set](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/): a standard test set with problems designed to be difficult.
- [Model predictive control](https://github.com/qpsolvers/mpc_qpbenchmark): model predictive control problems arising e.g. in robotics.
