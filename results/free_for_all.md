# Free-for-all test set

| Number of problems | 28 |
|:-------------------|:--------------------|
| Benchmark version  | 2.2.1 |
| Date               | 2024-07-31 18:51:42.265753+00:00 |
| CPU                | [Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz](#cpu-info) |
| Run by             | [@stephane-caron](https://github.com/stephane-caron/) |

Benchmark reports are copious as we aim to document comparison factors as much as possible. You can also [jump to results](#results-by-settings) directly.

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [CPU info](#cpu-info)
* [Known limitations](#known-limitations)
* [Results by settings](#results-by-settings)
    * [Default](#default)
    * [High accuracy](#high-accuracy)
    * [Low accuracy](#low-accuracy)
    * [Mid accuracy](#mid-accuracy)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)

## Description

Community-built test set to benchmark QP solvers.

## Solvers

| solver   | version     |
|:---------|:------------|
| clarabel | 0.9.0       |
| cvxopt   | 0.0.0       |
| highs    | 1.7.2       |
| osqp     | 0.6.7.post0 |
| piqp     | 0.4.1       |
| proxqp   | 0.6.6       |
| qpalm    | 1.2.3       |
| scs      | 3.2.6       |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.3.2.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| `count` | 4 |
| `cpuinfo_version_string` | 9.0.0 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_perfmon`, `art`, `avx`, `avx2`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fxsr`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `ibpb`, `ibrs`, `ida`, `intel_pt`, `invpcid`, `invpcid_single`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `mpx`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pti`, `pts`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `sgx`, `smap`, `smep`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tscdeadline`, `vme`, `vmx`, `vnmi`, `vpid`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `hz_actual_friendly` | 2.6000 GHz |
| `hz_advertised_friendly` | 2.5000 GHz |
| `l1_data_cache_size` | 65536 |
| `l1_instruction_cache_size` | 65536 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 256 |
| `l2_cache_size` | 524288 |
| `l3_cache_size` | 4194304 |
| `model` | 78 |
| `python_version` | 3.12.4.final.0 (64 bit) |
| `stepping` | 3 |
| `vendor_id_raw` | GenuineIntel |

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
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
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

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                92.9 |                                  2.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt   |                                85.7 |                                  8.7 |                                         2.0 |                                     2.0 |                                 2.0 |
| highs    |                                67.9 |                                  3.4 |                                         4.6 |                                     4.8 |                                 4.8 |
| osqp     |                                78.6 |                                  1.3 |                                         2.0 |                                    32.0 |                                 2.4 |
| piqp     |                                89.3 |                                  2.6 |                                         1.5 |                                     1.5 |                                 1.5 |
| proxqp   |                                78.6 |                                  4.0 |                                         2.5 |                                     2.5 |                                 3.7 |
| qpalm    |                                92.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.1 |
| qpoases  |                                50.0 |                                  5.1 |                                         7.1 |                                     7.1 |                                 7.1 |
| quadprog |                                83.3 |                                  1.6 |                                         2.3 |                                     2.3 |                                 2.3 |
| scs      |                                75.0 |                                  2.4 |                                         3.5 |                                     3.6 |                                 3.6 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                92.9 |                                  1.5 |                                         1.0 |                                     1.0 |                                 1.3 |
| cvxopt   |                                17.9 |                                  5.6 |                                         2.0 |                                 35910.7 |                            542427.0 |
| highs    |                                 0.0 |                                  2.2 |                                         4.6 |                             230969108.4 |                          94123663.7 |
| osqp     |                                42.9 |                                  2.8 |                                         6.1 |                                     7.3 |                                 4.3 |
| piqp     |                                82.1 |                                  2.2 |                                         2.5 |                                     2.5 |                                 1.8 |
| proxqp   |                                78.6 |                                  3.2 |                                         6.3 |                                     2.9 |                                 3.2 |
| qpalm    |                                64.3 |                                  1.3 |                                         4.0 |                                     3.0 |                                 7.3 |
| qpoases  |                                50.0 |                                  3.3 |                                         7.0 |                                     6.7 |                                 2.7 |
| quadprog |                                66.7 |                                  1.0 |                                         2.3 |                                187536.4 |                                 1.0 |
| scs      |                                67.9 |                                  2.0 |                                         6.5 |                                     4.3 |                                 1.9 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                92.9 |                                 13.0 |                                 441858446.0 |                                     2.0 |                                 2.3 |
| cvxopt   |                                92.9 |                                 47.6 |                                 220927339.9 |                                     1.2 |                                 1.0 |
| highs    |                                60.7 |                                 21.5 |                                1988374326.2 |                                   484.2 |                               323.2 |
| osqp     |                                57.1 |                                 12.0 |                                2252919335.7 |                                    12.6 |                                36.6 |
| piqp     |                                96.4 |                                  7.3 |                                 111471134.4 |                                     1.0 |                                 3.1 |
| proxqp   |                                82.1 |                                 26.2 |                                2671418315.1 |                                     5.1 |                                 3.9 |
| qpalm    |                                60.7 |                                  9.3 |                                1933373587.7 |                                     4.7 |                                32.9 |
| qpoases  |                                83.3 |                                  1.0 |                                         1.0 |                                451117.5 |                             12943.7 |
| quadprog |                                83.3 |                                 10.1 |                                1031000913.2 |                                     5.0 |                                 1.2 |
| scs      |                                75.0 |                                 15.3 |                                1983977754.0 |                                     8.1 |                                 3.2 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                92.9 |                                  1.4 |                                         1.0 |                                     1.0 |                                 1.3 |
| cvxopt   |                                60.7 |                                  5.6 |                                         2.0 |                                    39.2 |                               595.4 |
| highs    |                                17.9 |                                  2.2 |                                         4.5 |                                239530.0 |                            103163.4 |
| osqp     |                                53.6 |                                  2.2 |                                         5.6 |                                     6.4 |                                 5.1 |
| piqp     |                                89.3 |                                  1.5 |                                         1.5 |                                     1.9 |                                 1.4 |
| proxqp   |                                82.1 |                                  2.7 |                                         5.2 |                                     2.6 |                                 2.8 |
| qpalm    |                                71.4 |                                  1.1 |                                         3.3 |                                     2.6 |                                11.4 |
| qpoases  |                                58.3 |                                  2.6 |                                         5.8 |                                     5.9 |                                 2.5 |
| quadprog |                                75.0 |                                  1.0 |                                         2.3 |                                   196.8 |                                 1.0 |
| scs      |                                75.0 |                                  1.5 |                                         5.5 |                                     3.8 |                                 2.4 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        93 |              93 |             93 |             93 |
| cvxopt   |        86 |              18 |             93 |             61 |
| highs    |        68 |               0 |             61 |             18 |
| osqp     |        79 |              43 |             57 |             54 |
| piqp     |        89 |              82 |             96 |             89 |
| proxqp   |        79 |              79 |             82 |             82 |
| qpalm    |        93 |              64 |             61 |             71 |
| qpoases  |        50 |              50 |             83 |             58 |
| quadprog |        83 |              67 |             83 |             75 |
| scs      |        75 |              68 |             75 |             75 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              32 |             96 |             75 |
| highs    |       100 |              32 |             93 |             50 |
| osqp     |        93 |              86 |             75 |             89 |
| piqp     |       100 |             100 |             96 |            100 |
| proxqp   |        96 |             100 |            100 |            100 |
| qpalm    |       100 |              82 |             71 |             86 |
| qpoases  |       100 |             100 |             83 |            100 |
| quadprog |       100 |              83 |            100 |             92 |
| scs      |       100 |              96 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       2.2 |             1.5 |           13.0 |            1.4 |
| cvxopt   |       8.7 |             5.6 |           47.6 |            5.6 |
| highs    |       3.4 |             2.2 |           21.5 |            2.2 |
| osqp     |       1.3 |             2.8 |           12.0 |            2.2 |
| piqp     |       2.6 |             2.2 |            7.3 |            1.5 |
| proxqp   |       4.0 |             3.2 |           26.2 |            2.7 |
| qpalm    |       1.0 |             1.3 |            9.3 |            1.1 |
| qpoases  |       5.1 |             3.3 |            1.0 |            2.6 |
| quadprog |       1.6 |             1.0 |           10.1 |            1.0 |
| scs      |       2.4 |             2.0 |           15.3 |            1.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |    441858446.0 |            1.0 |
| cvxopt   |       2.0 |             2.0 |    220927339.9 |            2.0 |
| highs    |       4.6 |             4.6 |   1988374326.2 |            4.5 |
| osqp     |       2.0 |             6.1 |   2252919335.7 |            5.6 |
| piqp     |       1.5 |             2.5 |    111471134.4 |            1.5 |
| proxqp   |       2.5 |             6.3 |   2671418315.1 |            5.2 |
| qpalm    |       1.0 |             4.0 |   1933373587.7 |            3.3 |
| qpoases  |       7.1 |             7.0 |            1.0 |            5.8 |
| quadprog |       2.3 |             2.3 |   1031000913.2 |            2.3 |
| scs      |       3.5 |             6.5 |   1983977754.0 |            5.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            2.0 |            1.0 |
| cvxopt   |       2.0 |         35910.7 |            1.2 |           39.2 |
| highs    |       4.8 |     230969108.4 |          484.2 |       239530.0 |
| osqp     |      32.0 |             7.3 |           12.6 |            6.4 |
| piqp     |       1.5 |             2.5 |            1.0 |            1.9 |
| proxqp   |       2.5 |             2.9 |            5.1 |            2.6 |
| qpalm    |       1.0 |             3.0 |            4.7 |            2.6 |
| qpoases  |       7.1 |             6.7 |       451117.5 |            5.9 |
| quadprog |       2.3 |        187536.4 |            5.0 |          196.8 |
| scs      |       3.6 |             4.3 |            8.1 |            3.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.3 |            2.3 |            1.3 |
| cvxopt   |       2.0 |        542427.0 |            1.0 |          595.4 |
| highs    |       4.8 |      94123663.7 |          323.2 |       103163.4 |
| osqp     |       2.4 |             4.3 |           36.6 |            5.1 |
| piqp     |       1.5 |             1.8 |            3.1 |            1.4 |
| proxqp   |       3.7 |             3.2 |            3.9 |            2.8 |
| qpalm    |       1.1 |             7.3 |           32.9 |           11.4 |
| qpoases  |       7.1 |             2.7 |        12943.7 |            2.5 |
| quadprog |       2.3 |             1.0 |            1.2 |            1.0 |
| scs      |       3.6 |             1.9 |            3.2 |            2.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
