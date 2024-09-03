# Free-for-all test set

| Number of problems | 28 |
|:-------------------|:--------------------|
| Benchmark version  | 2.3.0 |
| Date               | 2024-09-03 14:18:49.612476+00:00 |
| CPU                | [12th Gen Intel(R) Core(TM) i7-12800H](#cpu-info) |
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

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.9.0                 |
| cvxopt   | 1.3.2                 |
| gurobi   | 11.0.3 (size-limited) |
| highs    | 1.7.2                 |
| osqp     | 0.6.7.post0           |
| piqp     | 0.4.2                 |
| proxqp   | 0.6.7                 |
| qpalm    | 1.2.3                 |
| scs      | 3.2.7                 |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.3.3.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | 12th Gen Intel(R) Core(TM) i7-12800H |
| `count` | 20 |
| `cpuinfo_version_string` | 9.0.0 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_lbr`, `arch_perfmon`, `art`, `avx`, `avx2`, `avx_vnni`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `clwb`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `gfni`, `hfi`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `hwp_pkg_req`, `ibpb`, `ibrs`, `ibrs_enhanced`, `ibt`, `ida`, `intel_pt`, `invpcid`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `movdir64b`, `movdiri`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `ospke`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pconfig`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pku`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pts`, `rdpid`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `serialize`, `sha`, `sha_ni`, `smap`, `smep`, `smx`, `split_lock_detect`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tme`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tsc_known_freq`, `tscdeadline`, `umip`, `vaes`, `vme`, `vmx`, `vnmi`, `vpclmulqdq`, `vpid`, `waitpkg`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `hz_actual_friendly` | 1.9822 GHz |
| `hz_advertised_friendly` | 1.9822 GHz |
| `l1_data_cache_size` | 557056 |
| `l1_instruction_cache_size` | 720896 |
| `l2_cache_associativity` | 7 |
| `l2_cache_line_size` | 1280 |
| `l2_cache_size` | 11.5 MiB |
| `l3_cache_size` | 25165824 |
| `model` | 154 |
| `python_version` | 3.12.5.final.0 (64 bit) |
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
| gurobi   | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``OptimalityTol``                | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``TimeLimit``                    | 10.0      |          10     |         10     |         10     |
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
| clarabel |                                78.6 |                                  3.8 |                                         3.0 |                                     3.0 |                                 2.9 |
| cvxopt   |                                78.6 |                                  4.2 |                                         3.0 |                                     3.0 |                                 2.9 |
| daqp     |                                72.7 |                                  3.2 |                                         3.9 |                                     3.9 |                                 3.7 |
| ecos     |                                59.1 |                                  5.0 |                                         5.8 |                                     5.8 |                                 5.6 |
| gurobi   |                                60.7 |                                  4.8 |                                         5.6 |                                     5.6 |                                 5.3 |
| highs    |                                71.4 |                                  2.7 |                                         3.0 |                                   268.3 |                                 3.1 |
| osqp     |                                78.6 |                                  1.6 |                                         2.0 |                                    32.0 |                                 2.3 |
| piqp     |                                89.3 |                                  2.4 |                                         1.5 |                                     1.5 |                                 1.4 |
| proxqp   |                                75.0 |                                  2.5 |                                         3.0 |                                     3.0 |                                 4.0 |
| qpalm    |                                92.9 |                                  1.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpoases  |                                72.7 |                                  3.2 |                                         3.9 |                                     3.9 |                                 3.7 |
| quadprog |                                90.9 |                                  1.0 |                                         1.3 |                                     1.3 |                                 1.2 |
| scs      |                                75.0 |                                  2.9 |                                         3.5 |                                     3.6 |                                 3.4 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                78.6 |                                  3.8 |                                         2.4 |                                     1.1 |                                 3.4 |
| cvxopt   |                                17.9 |                                  4.2 |                                         2.4 |                                 22514.1 |                            987253.8 |
| daqp     |                                72.7 |                                  3.2 |                                         3.0 |                                     1.4 |                                 2.7 |
| ecos     |                                 0.0 |                                  5.0 |                                         4.5 |                                893571.4 |                          50707211.4 |
| gurobi   |                                32.1 |                                  4.7 |                                         4.3 |                              10130716.0 |                              4067.8 |
| highs    |                                 0.0 |                                  2.7 |                                        12.5 |                           88342944247.8 |                         171888496.3 |
| osqp     |                                42.9 |                                  5.3 |                                         4.8 |                                     2.7 |                                 7.8 |
| piqp     |                                82.1 |                                  3.3 |                                         2.0 |                                     1.0 |                                 3.4 |
| proxqp   |                                71.4 |                                  3.4 |                                         5.7 |                                     1.4 |                                 6.0 |
| qpalm    |                                60.7 |                                  1.5 |                                         2.4 |                                 47335.9 |                                13.6 |
| qpoases  |                                72.7 |                                  3.2 |                                         3.0 |                                     1.4 |                                 2.7 |
| quadprog |                                81.8 |                                  1.0 |                                         1.0 |                                 39425.9 |                                 1.0 |
| scs      |                                71.4 |                                  3.0 |                                         5.0 |                                     1.4 |                                 3.5 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                78.6 |                                 70.5 |                                 773253094.7 |                                     8.5 |                                 4.6 |
| cvxopt   |                                82.1 |                                 65.4 |                                 515499847.7 |                                     5.9 |                                 2.7 |
| daqp     |                                72.7 |                                 62.5 |                                1078627982.6 |                                    10.8 |                                 3.0 |
| ecos     |                                45.5 |                                 98.5 |                                1476223746.1 |                                    23.2 |                                60.5 |
| gurobi   |                                57.1 |                                 94.0 |                                1417642295.2 |                                    96.0 |                                 4.3 |
| highs    |                                53.6 |                                 43.7 |                                 644375975.7 |                                701704.2 |                               979.4 |
| osqp     |                                57.1 |                                 37.6 |                                1311176866.5 |                                    16.5 |                                59.6 |
| piqp     |                                96.4 |                                 16.1 |                                  65024815.0 |                                     1.0 |                                 4.6 |
| proxqp   |                                82.1 |                                 40.6 |                                1558104159.5 |                                     8.5 |                                 5.5 |
| qpalm    |                                64.3 |                                 22.4 |                                 998923465.5 |                                     6.5 |                                48.4 |
| qpoases  |                                90.9 |                                  1.0 |                                         1.0 |                                273431.3 |                             10086.5 |
| quadprog |                                90.9 |                                 19.8 |                                 328044502.6 |                                     3.9 |                                 1.0 |
| scs      |                                78.6 |                                 54.7 |                                1029215969.7 |                                    10.1 |                                 4.4 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                78.6 |                                  3.7 |                                         2.4 |                                     1.8 |                                 3.5 |
| cvxopt   |                                53.6 |                                  4.2 |                                         2.4 |                                    39.2 |                              1092.0 |
| daqp     |                                72.7 |                                  3.2 |                                         3.0 |                                     2.3 |                                 3.0 |
| ecos     |                                 4.5 |                                  5.0 |                                         4.5 |                                  1489.9 |                             55970.8 |
| gurobi   |                                53.6 |                                  4.7 |                                         4.3 |                                 16856.5 |                                 8.8 |
| highs    |                                14.3 |                                  2.7 |                                         2.4 |                             146965874.8 |                            189763.2 |
| osqp     |                                53.6 |                                  4.3 |                                         4.4 |                                     3.8 |                                 9.4 |
| piqp     |                                89.3 |                                  2.2 |                                         1.2 |                                     1.0 |                                 2.5 |
| proxqp   |                                75.0 |                                  2.9 |                                         4.9 |                                     2.2 |                                 5.5 |
| qpalm    |                                75.0 |                                  1.1 |                                         1.8 |                                    79.7 |                                20.1 |
| qpoases  |                                77.3 |                                  2.6 |                                         2.5 |                                     1.9 |                                 2.5 |
| quadprog |                                86.4 |                                  1.0 |                                         1.0 |                                    66.3 |                                 1.0 |
| scs      |                                75.0 |                                  2.9 |                                         3.9 |                                     2.2 |                                 4.4 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        79 |              79 |             79 |             79 |
| cvxopt   |        79 |              18 |             82 |             54 |
| daqp     |        73 |              73 |             73 |             73 |
| ecos     |        59 |               0 |             45 |              5 |
| gurobi   |        61 |              32 |             57 |             54 |
| highs    |        71 |               0 |             54 |             14 |
| osqp     |        79 |              43 |             57 |             54 |
| piqp     |        89 |              82 |             96 |             89 |
| proxqp   |        75 |              71 |             82 |             75 |
| qpalm    |        93 |              61 |             64 |             75 |
| qpoases  |        73 |              73 |             91 |             77 |
| quadprog |        91 |              82 |             91 |             86 |
| scs      |        75 |              71 |             79 |             75 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              39 |             96 |             75 |
| daqp     |       100 |             100 |            100 |            100 |
| ecos     |       100 |              41 |             86 |             45 |
| gurobi   |       100 |              71 |             96 |             93 |
| highs    |        93 |              21 |             71 |             36 |
| osqp     |        93 |              86 |             71 |             89 |
| piqp     |       100 |             100 |             96 |            100 |
| proxqp   |        96 |             100 |            100 |            100 |
| qpalm    |       100 |              71 |             71 |             82 |
| qpoases  |       100 |             100 |             91 |            100 |
| quadprog |       100 |              91 |            100 |             95 |
| scs      |       100 |              96 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       3.8 |             3.8 |           70.5 |            3.7 |
| cvxopt   |       4.2 |             4.2 |           65.4 |            4.2 |
| daqp     |       3.2 |             3.2 |           62.5 |            3.2 |
| ecos     |       5.0 |             5.0 |           98.5 |            5.0 |
| gurobi   |       4.8 |             4.7 |           94.0 |            4.7 |
| highs    |       2.7 |             2.7 |           43.7 |            2.7 |
| osqp     |       1.6 |             5.3 |           37.6 |            4.3 |
| piqp     |       2.4 |             3.3 |           16.1 |            2.2 |
| proxqp   |       2.5 |             3.4 |           40.6 |            2.9 |
| qpalm    |       1.1 |             1.5 |           22.4 |            1.1 |
| qpoases  |       3.2 |             3.2 |            1.0 |            2.6 |
| quadprog |       1.0 |             1.0 |           19.8 |            1.0 |
| scs      |       2.9 |             3.0 |           54.7 |            2.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       3.0 |             2.4 |    773253094.7 |            2.4 |
| cvxopt   |       3.0 |             2.4 |    515499847.7 |            2.4 |
| daqp     |       3.9 |             3.0 |   1078627982.6 |            3.0 |
| ecos     |       5.8 |             4.5 |   1476223746.1 |            4.5 |
| gurobi   |       5.6 |             4.3 |   1417642295.2 |            4.3 |
| highs    |       3.0 |            12.5 |    644375975.7 |            2.4 |
| osqp     |       2.0 |             4.8 |   1311176866.5 |            4.4 |
| piqp     |       1.5 |             2.0 |     65024815.0 |            1.2 |
| proxqp   |       3.0 |             5.7 |   1558104159.5 |            4.9 |
| qpalm    |       1.0 |             2.4 |    998923465.5 |            1.8 |
| qpoases  |       3.9 |             3.0 |            1.0 |            2.5 |
| quadprog |       1.3 |             1.0 |    328044502.6 |            1.0 |
| scs      |       3.5 |             5.0 |   1029215969.7 |            3.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       3.0 |             1.1 |            8.5 |            1.8 |
| cvxopt   |       3.0 |         22514.1 |            5.9 |           39.2 |
| daqp     |       3.9 |             1.4 |           10.8 |            2.3 |
| ecos     |       5.8 |        893571.4 |           23.2 |         1489.9 |
| gurobi   |       5.6 |      10130716.0 |           96.0 |        16856.5 |
| highs    |     268.3 |   88342944247.8 |       701704.2 |    146965874.8 |
| osqp     |      32.0 |             2.7 |           16.5 |            3.8 |
| piqp     |       1.5 |             1.0 |            1.0 |            1.0 |
| proxqp   |       3.0 |             1.4 |            8.5 |            2.2 |
| qpalm    |       1.0 |         47335.9 |            6.5 |           79.7 |
| qpoases  |       3.9 |             1.4 |       273431.3 |            1.9 |
| quadprog |       1.3 |         39425.9 |            3.9 |           66.3 |
| scs      |       3.6 |             1.4 |           10.1 |            2.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       2.9 |             3.4 |            4.6 |            3.5 |
| cvxopt   |       2.9 |        987253.8 |            2.7 |         1092.0 |
| daqp     |       3.7 |             2.7 |            3.0 |            3.0 |
| ecos     |       5.6 |      50707211.4 |           60.5 |        55970.8 |
| gurobi   |       5.3 |          4067.8 |            4.3 |            8.8 |
| highs    |       3.1 |     171888496.3 |          979.4 |       189763.2 |
| osqp     |       2.3 |             7.8 |           59.6 |            9.4 |
| piqp     |       1.4 |             3.4 |            4.6 |            2.5 |
| proxqp   |       4.0 |             6.0 |            5.5 |            5.5 |
| qpalm    |       1.0 |            13.6 |           48.4 |           20.1 |
| qpoases  |       3.7 |             2.7 |        10086.5 |            2.5 |
| quadprog |       1.2 |             1.0 |            1.0 |            1.0 |
| scs      |       3.4 |             3.5 |            4.4 |            4.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
