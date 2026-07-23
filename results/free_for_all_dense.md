# Free-for-all dense subset

| Number of problems | 22 |
|:-------------------|:--------------------|
| Benchmark version  | 2.7.1 |
| Date               | 2026-07-23 15:02:46.859695+00:00 |
| CPU                | [AMD Ryzen 7 8845HS w/ Radeon 780M Graphics](#cpu-info) |
| Run by             | [@stephane-caron](https://github.com/stephane-caron/) |
| Results file       | ``free_for_all_dense.parquet`` |
| Results checksum   | ``74954d8589a4983e1a423028f92cb64b3cdfbaaad4e9a5d34a5035b81f2aa879`` |

Benchmark reports are copious as we aim to document comparison factors as much as possible. You can also [jump to results](#results-by-settings) directly.

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Results by settings](#results-by-settings)
    * [Default settings](#default-settings)
    * [High accuracy settings](#high-accuracy-settings)
    * [Low accuracy settings](#low-accuracy-settings)
    * [Mid accuracy settings](#mid-accuracy-settings)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)
* [Settings](#settings)
* [Known limitations](#known-limitations)
* [CPU info](#cpu-info)

## Description

Community-built test set to benchmark QP solvers.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.11.1                |
| cvxopt   | 1.3.3                 |
| daqp     | 0.8.7                 |
| ecos     | 2.0.14                |
| gurobi   | 13.0.2 (size-limited) |
| highs    | 1.15.1                |
| kvxopt   | 1.3.3.1               |
| osqp     | 1.1.3                 |
| piqp     | 0.6.3                 |
| proxqp   | 0.7.3                 |
| qpalm    | 1.2.6                 |
| quadprog | 0.1.13                |
| scs      | 3.2.11                |
| sip      | 0.0.2                 |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.13.0.

## Results by settings

### Default settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                90.9 |                                 87.3 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                72.7 |                                278.7 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp     |                                90.9 |                                 87.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos     |                                54.5 |                                496.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| gurobi   |                                77.3 |                                228.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| highs    |                                81.8 |                                 91.0 |                                         1.0 |                                    29.9 |                                 1.0 |
| kvxopt   |                                72.7 |                                281.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp     |                                90.9 |                                  1.0 |                                         1.0 |                                     3.7 |                                 1.0 |
| piqp     |                               100.0 |                                  2.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                                90.9 |                                 44.5 |                                         1.0 |                                     1.0 |                                 1.1 |
| qpalm    |                               100.0 |                                  1.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| quadprog |                                72.7 |                                278.6 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                                90.9 |                                 87.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                               100.0 |                                  6.0 |                                         1.0 |                                     1.0 |                                 1.0 |

### High accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                90.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                22.7 |                                  3.2 |                                         1.0 |                                     1.0 |                            126082.0 |
| daqp     |                                72.7 |                                  1.0 |                                         1.0 |                                    98.0 |                              3963.8 |
| ecos     |                                 0.0 |                                  5.7 |                                         1.0 |                                191940.3 |                           5641180.8 |
| gurobi   |                                31.8 |                                  2.6 |                                         1.0 |                               2594699.9 |                               519.9 |
| highs    |                                 0.0 |                                  1.0 |                                         1.0 |                           26702943203.3 |                          21884340.2 |
| kvxopt   |                                22.7 |                                  3.2 |                                         1.0 |                                     1.0 |                            126082.0 |
| osqp     |                                68.2 |                                  3.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| piqp     |                                90.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                                81.8 |                                  2.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                81.8 |                                  1.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| quadprog |                                72.7 |                                  3.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                                90.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                                90.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |

### Low accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                90.9 |                                 55.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                68.2 |                                175.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp     |                                90.9 |                                 55.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos     |                                40.9 |                                313.1 |                                         1.0 |                                     1.0 |                                 6.5 |
| gurobi   |                                72.7 |                                144.3 |                                         1.0 |                                     3.5 |                                 1.0 |
| highs    |                                68.2 |                                  2.1 |                                         1.0 |                                 26706.0 |                                80.5 |
| kvxopt   |                                68.2 |                                176.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp     |                                95.5 |                                 27.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| piqp     |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                                95.5 |                                 27.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                72.7 |                                 27.1 |                                         1.0 |                                     1.0 |                                 4.4 |
| quadprog |                                72.7 |                                175.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                                90.9 |                                 55.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                                95.5 |                                 27.2 |                                         1.0 |                                     1.0 |                                 1.0 |

### Mid accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                90.9 |                                  2.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                45.5 |                                  6.5 |                                         1.0 |                                     1.0 |                               126.8 |
| daqp     |                                72.7 |                                  2.0 |                                         1.0 |                                     1.0 |                                 4.8 |
| ecos     |                                 4.5 |                                 11.5 |                                         1.0 |                                   192.4 |                              5641.7 |
| gurobi   |                                68.2 |                                  5.3 |                                         1.0 |                                  2595.6 |                                 1.4 |
| highs    |                                18.2 |                                  2.1 |                                         1.0 |                              26702899.6 |                             21885.0 |
| kvxopt   |                                45.5 |                                  6.5 |                                         1.0 |                                     1.0 |                               126.8 |
| osqp     |                                77.3 |                                  5.3 |                                         1.0 |                                     1.0 |                                 1.0 |
| piqp     |                                95.5 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp   |                                90.9 |                                  2.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpalm    |                                86.4 |                                  2.0 |                                         1.0 |                                     1.0 |                                 1.3 |
| quadprog |                                72.7 |                                  6.5 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs      |                                90.9 |                                  2.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| sip      |                                95.5 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        91 |              91 |             91 |             91 |
| cvxopt   |        73 |              23 |             68 |             45 |
| daqp     |        91 |              73 |             91 |             73 |
| ecos     |        55 |               0 |             41 |              5 |
| gurobi   |        77 |              32 |             73 |             68 |
| highs    |        82 |               0 |             68 |             18 |
| kvxopt   |        73 |              23 |             68 |             45 |
| osqp     |        91 |              68 |             95 |             77 |
| piqp     |       100 |              91 |            100 |             95 |
| proxqp   |        91 |              82 |             95 |             91 |
| qpalm    |       100 |              82 |             73 |             86 |
| quadprog |        73 |              73 |             73 |             73 |
| scs      |        91 |              91 |             91 |             91 |
| sip      |       100 |              91 |             95 |             95 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              50 |             95 |             73 |
| daqp     |       100 |              82 |            100 |             82 |
| ecos     |       100 |              45 |             86 |             50 |
| gurobi   |       100 |              55 |             95 |             91 |
| highs    |        91 |               9 |             68 |             27 |
| kvxopt   |       100 |              50 |             95 |             73 |
| osqp     |        91 |             100 |            100 |            100 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |        95 |             100 |            100 |            100 |
| qpalm    |       100 |              95 |             77 |             95 |
| quadprog |       100 |             100 |            100 |            100 |
| scs      |       100 |             100 |            100 |            100 |
| sip      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |      87.3 |             1.0 |           55.1 |            2.0 |
| cvxopt   |     278.7 |             3.2 |          175.9 |            6.5 |
| daqp     |      87.5 |             1.0 |           55.2 |            2.0 |
| ecos     |     496.0 |             5.7 |          313.1 |           11.5 |
| gurobi   |     228.9 |             2.6 |          144.3 |            5.3 |
| highs    |      91.0 |             1.0 |            2.1 |            2.1 |
| kvxopt   |     281.1 |             3.2 |          176.0 |            6.5 |
| osqp     |       1.0 |             3.8 |           27.2 |            5.3 |
| piqp     |       2.5 |             1.0 |            1.0 |            1.0 |
| proxqp   |      44.5 |             2.1 |           27.9 |            2.0 |
| qpalm    |       1.1 |             1.5 |           27.1 |            2.0 |
| quadprog |     278.6 |             3.2 |          175.9 |            6.5 |
| scs      |      87.8 |             1.0 |           55.1 |            2.0 |
| sip      |       6.0 |             1.0 |           27.2 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| daqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| ecos     |       1.0 |             1.0 |            1.0 |            1.0 |
| gurobi   |       1.0 |             1.0 |            1.0 |            1.0 |
| highs    |       1.0 |             1.0 |            1.0 |            1.0 |
| kvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| osqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |       1.0 |             1.0 |            1.0 |            1.0 |
| qpalm    |       1.0 |             1.0 |            1.0 |            1.0 |
| quadprog |       1.0 |             1.0 |            1.0 |            1.0 |
| scs      |       1.0 |             1.0 |            1.0 |            1.0 |
| sip      |       1.0 |             1.0 |            1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| daqp     |       1.0 |            98.0 |            1.0 |            1.0 |
| ecos     |       1.0 |        191940.3 |            1.0 |          192.4 |
| gurobi   |       1.0 |       2594699.9 |            3.5 |         2595.6 |
| highs    |      29.9 |   26702943203.3 |        26706.0 |     26702899.6 |
| kvxopt   |       1.0 |             1.0 |            1.0 |            1.0 |
| osqp     |       3.7 |             1.0 |            1.0 |            1.0 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |       1.0 |             1.0 |            1.0 |            1.0 |
| qpalm    |       1.0 |             1.0 |            1.0 |            1.0 |
| quadprog |       1.0 |             1.0 |            1.0 |            1.0 |
| scs      |       1.0 |             1.0 |            1.0 |            1.0 |
| sip      |       1.0 |             1.0 |            1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |       1.0 |        126082.0 |            1.0 |          126.8 |
| daqp     |       1.0 |          3963.8 |            1.0 |            4.8 |
| ecos     |       1.0 |       5641180.8 |            6.5 |         5641.7 |
| gurobi   |       1.0 |           519.9 |            1.0 |            1.4 |
| highs    |       1.0 |      21884340.2 |           80.5 |        21885.0 |
| kvxopt   |       1.0 |        126082.0 |            1.0 |          126.8 |
| osqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |       1.1 |             1.0 |            1.0 |            1.0 |
| qpalm    |       1.0 |             1.0 |            4.4 |            1.3 |
| quadprog |       1.0 |             1.0 |            1.0 |            1.0 |
| scs      |       1.0 |             1.0 |            1.0 |            1.0 |
| sip      |       1.0 |             1.0 |            1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).

## Settings

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |        10 |          10     |         10     |         10     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|:---------------------------------|:----------|----------------:|---------------:|---------------:|
| clarabel | ``tol_feas``                     | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_rel``                  | -         |           0     |          0     |          0     |
| cvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| daqp     | ``dual_tol``                     | -         |           1e-09 |          0.001 |          1e-06 |
| daqp     | ``primal_tol``                   | -         |           1e-09 |          0.001 |          1e-06 |
| ecos     | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``OptimalityTol``                | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``TimeLimit``                    | 10.0      |          10     |         10     |         10     |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| kvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| osqp     | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| piqp     | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| piqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| piqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| proxqp   | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm    | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| qpalm    | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm    | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| scs      | ``time_limit_secs``              | 10.0      |          10     |         10     |         10     |
| sip      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| sip      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| sip      | ``time_limit``                   | 10.0      |          10     |         10     |         10     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | AMD Ryzen 7 8845HS w/ Radeon 780M Graphics |
| `count` | 16 |
| `family` | 25 |
| `flags` | `3dnowext`, `3dnowprefetch`, `abm`, `adx`, `aes`, `amd_lbr_v2`, `aperfmperf`, `apic`, `arat`, `avx`, `avx2`, `avx512_bf16`, `avx512_bitalg`, `avx512_vbmi2`, `avx512_vnni`, `avx512_vpopcntdq`, `avx512bitalg`, `avx512bw`, `avx512cd`, `avx512dq`, `avx512f`, `avx512ifma`, `avx512vbmi`, `avx512vbmi2`, `avx512vl`, `avx512vnni`, `avx512vpopcntdq`, `bmi1`, `bmi2`, `bpext`, `cat_l3`, `cdp_l3`, `clflush`, `clflushopt`, `clwb`, `clzero`, `cmov`, `cmp_legacy`, `constant_tsc`, `cpb`, `cppc`, `cpuid`, `cpuid_fault`, `cqm`, `cqm_llc`, `cqm_mbm_local`, `cqm_mbm_total`, `cqm_occup_llc`, `cr8_legacy`, `cx16`, `cx8`, `dbx`, `de`, `decodeassists`, `erms`, `extapic`, `extd_apicid`, `f16c`, `flush_l1d`, `flushbyasid`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `fxsr_opt`, `gfni`, `ht`, `hw_pstate`, `ibpb`, `ibrs`, `ibrs_enhanced`, `ibs`, `invpcid`, `irperf`, `lahf_lm`, `lbrv`, `lm`, `mba`, `mca`, `mce`, `misalignsse`, `mmx`, `mmxext`, `monitor`, `movbe`, `msr`, `mtrr`, `mwaitx`, `nonstop_tsc`, `nopl`, `npt`, `nrip_save`, `nx`, `ospke`, `osvw`, `osxsave`, `overflow_recov`, `pae`, `pat`, `pausefilter`, `pci_l2i`, `pclmulqdq`, `pdpe1gb`, `perfctr_core`, `perfctr_llc`, `perfctr_nb`, `perfmon_v2`, `pfthreshold`, `pge`, `pku`, `pni`, `popcnt`, `pqe`, `pqm`, `pse`, `pse36`, `rapl`, `rdpid`, `rdpru`, `rdrand`, `rdrnd`, `rdseed`, `rdt_a`, `rdtscp`, `rep_good`, `sep`, `sha`, `sha_ni`, `skinit`, `smap`, `smca`, `smep`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `sse4a`, `ssse3`, `stibp`, `succor`, `svm`, `svm_lock`, `syscall`, `tce`, `topoext`, `tsc`, `tsc_scale`, `umip`, `user_shstk`, `v_spec_ctrl`, `vaes`, `vgif`, `vmcb_clean`, `vme`, `vmmcall`, `vnmi`, `vpclmulqdq`, `wbnoinvd`, `wdt`, `x2apic`, `x2avic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveerptr`, `xsaveopt`, `xsaves`, `xtopology` |
| `l1_data_cache_size` | 262144 |
| `l1_instruction_cache_size` | 262144 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 1024 |
| `l2_cache_size` | 8388608 |
| `l3_cache_size` | 1048576 |
| `model` | 117 |
| `python_version` | 3.14.6.final.0 (64 bit) |
| `stepping` | 2 |
| `vendor_id_raw` | AuthenticAMD |

