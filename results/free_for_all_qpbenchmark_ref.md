# Free-for-all test set

| Number of problems | 11 |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.0 |
| Date               | 2023-12-21 15:00:27.787755+00:00 |
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

| solver   | version   |
|:---------|:----------|
| clarabel | 0.6.0     |
| cvxopt   | 1.3.2     |
| daqp     | 0.5.1     |
| ecos     | 2.0.11    |
| highs    | 1.5.3     |
| osqp     | 0.6.3     |
| piqp     | 0.2.3     |
| proxqp   | 0.6.1     |
| qpalm    | 1.2.1     |
| qpoases  | 3.2.1     |
| quadprog | 0.1.11    |
| scs      | 3.2.3     |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.2.0.

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
| `python_version` | 3.10.13.final.0 (64 bit) |
| `stepping` | 3 |
| `vendor_id_raw` | GenuineIntel |

## Settings

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |      1000 |        1000     |       1000     |       1000     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   | high_accuracy   | low_accuracy   | mid_accuracy   |
|:---------|:---------------------------------|:----------|:----------------|:---------------|:---------------|
| clarabel | ``tol_feas``                     | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_abs``                  | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_rel``                  | -         | 0.0             | 0.0            | 0.0            |
| cvxopt   | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``dual_tol``                     | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``primal_tol``                   | -         | 1e-09           | 0.001          | 1e-06          |
| ecos     | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| piqp     | ``check_duality_gap``            | -         | True            | True           | True           |
| piqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| piqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``check_duality_gap``            | -         | True            | True           | True           |
| proxqp   | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| qpalm    | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| qpoases  | ``predefined_options``           | default   | reliable        | fast           | -              |
| qpoases  | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| scs      | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| scs      | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| scs      | ``time_limit_secs``              | 1000.0    | 1000.0          | 1000.0         | 1000.0         |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                81.8 |                                477.5 |                                       988.6 |                                 31524.2 |                       10779325511.4 |
| cvxopt   |                                72.7 |                                918.4 |                                      1489.4 |                                 47493.7 |                       16239442815.5 |
| daqp     |                               100.0 |                                 10.6 |                                        49.6 |                                     1.0 |                                 1.0 |
| ecos     |                                45.5 |                               2596.2 |                                      2504.0 |                                517125.4 |                       27405872563.1 |
| highs    |                                63.6 |                               1598.3 |                                      1994.5 |                                 71745.7 |                       24531421200.4 |
| osqp     |                                81.8 |                                  1.4 |                                         4.9 |                               1063577.5 |                        1785279267.6 |
| piqp     |                                81.8 |                                479.4 |                                       988.6 |                                 31526.5 |                       10779325976.0 |
| proxqp   |                                90.9 |                                191.8 |                                       492.2 |                                 15694.1 |                        5394467341.5 |
| qpalm    |                               100.0 |                                  1.0 |                                         1.0 |                                    15.5 |                          21273412.7 |
| qpoases  |                                45.5 |                               4137.6 |                                      3018.0 |                                 96235.5 |                       32906542581.1 |
| quadprog |                                81.8 |                                480.2 |                                       988.6 |                                 31527.0 |                       10779325473.3 |
| scs      |                                81.8 |                                480.0 |                                       989.2 |                                 31524.4 |                       10780037399.4 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                81.8 |                                246.7 |                                         1.0 |                                     1.0 |                                17.1 |
| cvxopt   |                                45.5 |                                474.9 |                                         1.5 |                                 37236.4 |                                79.3 |
| daqp     |                                63.6 |                                  5.8 |                                        81.9 |                                 30476.7 |                                 1.0 |
| ecos     |                                 0.0 |                               1340.9 |                                         2.5 |                            1426583072.9 |                           5311083.5 |
| highs    |                                 0.0 |                                825.0 |                                         2.0 |                             239811631.4 |                        2689498679.2 |
| osqp     |                                45.5 |                               2137.1 |                                         3.0 |                                     3.0 |                                33.6 |
| piqp     |                                54.5 |                               1341.8 |                                         2.5 |                                     2.7 |                                28.5 |
| proxqp   |                                81.8 |                                269.7 |                                         3.7 |                                     1.0 |                                48.8 |
| qpalm    |                                72.7 |                                  1.0 |                                         1.2 |                                133265.0 |                                21.4 |
| qpoases  |                                45.5 |                               2137.1 |                                         3.0 |                                     3.0 |                                33.6 |
| quadprog |                                63.6 |                                248.6 |                                         1.0 |                                 83341.0 |                                12.3 |
| scs      |                                81.8 |                                278.2 |                                         2.3 |                                     1.0 |                                17.2 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                81.8 |                                529.6 |                                1033846693.8 |                                    32.8 |                          16615131.1 |
| cvxopt   |                               100.0 |                                 10.3 |                                        14.0 |                                     2.7 |                               205.2 |
| daqp     |                                81.8 |                                 11.9 |                             2903488800289.4 |                                     1.0 |                                 1.0 |
| ecos     |                                45.5 |                               4589.5 |                                3101582148.6 |                                   103.6 |                          34622973.9 |
| highs    |                                54.5 |                               1771.6 |                                2067702634.9 |                                  7934.5 |                        2651888237.5 |
| osqp     |                                72.7 |                                  1.6 |                                2181414622.9 |                                    48.4 |                         350041345.5 |
| piqp     |                               100.0 |                                  1.9 |                                 258440949.9 |                                     7.7 |                           4701266.3 |
| proxqp   |                               100.0 |                                  2.4 |                                2587711374.7 |                                    14.8 |                          28384995.6 |
| qpalm    |                                90.9 |                                  1.0 |                                2173531712.5 |                                    15.5 |                          33196358.7 |
| qpoases  |                                81.8 |                                  5.5 |                                         1.0 |                               3364129.8 |                      115647396363.7 |
| quadprog |                                81.8 |                                533.8 |                                1033841919.3 |                                    35.5 |                          10962977.7 |
| scs      |                                81.8 |                                530.4 |                                1578509771.1 |                                    45.4 |                          29675918.0 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                81.8 |                                280.7 |                                         1.0 |                                     1.6 |                             16143.2 |
| cvxopt   |                                63.6 |                                540.5 |                                         1.5 |                                    60.1 |                             16880.5 |
| daqp     |                                81.8 |                                  6.4 |                                     49357.8 |                                    47.3 |                                 1.0 |
| ecos     |                                 0.0 |                               1526.5 |                                         2.6 |                              19805808.4 |                          98887576.6 |
| highs    |                                36.4 |                                938.8 |                                         2.0 |                                372181.4 |                        2689521178.5 |
| osqp     |                                63.6 |                                930.5 |                                         2.5 |                                     3.1 |                             22504.6 |
| piqp     |                                72.7 |                                539.2 |                                         1.6 |                                     2.5 |                             20326.9 |
| proxqp   |                                90.9 |                                115.7 |                                         3.1 |                                     1.0 |                             43582.3 |
| qpalm    |                                90.9 |                                  1.0 |                                         1.0 |                                   207.2 |                             11357.4 |
| qpoases  |                                54.5 |                               1526.1 |                                         2.6 |                                     3.9 |                             28030.3 |
| quadprog |                                72.7 |                                282.8 |                                         1.0 |                                   130.9 |                             11213.1 |
| scs      |                                81.8 |                                283.8 |                                         2.0 |                                     1.6 |                             15369.7 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        82 |              82 |             82 |             82 |
| cvxopt   |        73 |              45 |            100 |             64 |
| daqp     |       100 |              64 |             82 |             82 |
| ecos     |        45 |               0 |             45 |              0 |
| highs    |        64 |               0 |             55 |             36 |
| osqp     |        82 |              45 |             73 |             64 |
| piqp     |        82 |              55 |            100 |             73 |
| proxqp   |        91 |              82 |            100 |             91 |
| qpalm    |       100 |              73 |             91 |             91 |
| qpoases  |        45 |              45 |             82 |             55 |
| quadprog |        82 |              64 |             82 |             73 |
| scs      |        82 |              82 |             82 |             82 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              73 |            100 |             91 |
| daqp     |       100 |              64 |             82 |             82 |
| ecos     |        91 |              45 |            100 |             45 |
| highs    |       100 |              36 |             91 |             73 |
| osqp     |        82 |             100 |             73 |            100 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpalm    |       100 |              73 |             91 |             91 |
| qpoases  |       100 |             100 |             82 |            100 |
| quadprog |       100 |              82 |            100 |             91 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     477.5 |           246.7 |          529.6 |          280.7 |
| cvxopt   |     918.4 |           474.9 |           10.3 |          540.5 |
| daqp     |      10.6 |             5.8 |           11.9 |            6.4 |
| ecos     |    2596.2 |          1340.9 |         4589.5 |         1526.5 |
| highs    |    1598.3 |           825.0 |         1771.6 |          938.8 |
| osqp     |       1.4 |          2137.1 |            1.6 |          930.5 |
| piqp     |     479.4 |          1341.8 |            1.9 |          539.2 |
| proxqp   |     191.8 |           269.7 |            2.4 |          115.7 |
| qpalm    |       1.0 |             1.0 |            1.0 |            1.0 |
| qpoases  |    4137.6 |          2137.1 |            5.5 |         1526.1 |
| quadprog |     480.2 |           248.6 |          533.8 |          282.8 |
| scs      |     480.0 |           278.2 |          530.4 |          283.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |    low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|----------------:|---------------:|
| clarabel |     988.6 |             1.0 |    1033846693.8 |            1.0 |
| cvxopt   |    1489.4 |             1.5 |            14.0 |            1.5 |
| daqp     |      49.6 |            81.9 | 2903488800289.4 |        49357.8 |
| ecos     |    2504.0 |             2.5 |    3101582148.6 |            2.6 |
| highs    |    1994.5 |             2.0 |    2067702634.9 |            2.0 |
| osqp     |       4.9 |             3.0 |    2181414622.9 |            2.5 |
| piqp     |     988.6 |             2.5 |     258440949.9 |            1.6 |
| proxqp   |     492.2 |             3.7 |    2587711374.7 |            3.1 |
| qpalm    |       1.0 |             1.2 |    2173531712.5 |            1.0 |
| qpoases  |    3018.0 |             3.0 |             1.0 |            2.6 |
| quadprog |     988.6 |             1.0 |    1033841919.3 |            1.0 |
| scs      |     989.2 |             2.3 |    1578509771.1 |            2.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   31524.2 |             1.0 |           32.8 |            1.6 |
| cvxopt   |   47493.7 |         37236.4 |            2.7 |           60.1 |
| daqp     |       1.0 |         30476.7 |            1.0 |           47.3 |
| ecos     |  517125.4 |    1426583072.9 |          103.6 |     19805808.4 |
| highs    |   71745.7 |     239811631.4 |         7934.5 |       372181.4 |
| osqp     | 1063577.5 |             3.0 |           48.4 |            3.1 |
| piqp     |   31526.5 |             2.7 |            7.7 |            2.5 |
| proxqp   |   15694.1 |             1.0 |           14.8 |            1.0 |
| qpalm    |      15.5 |        133265.0 |           15.5 |          207.2 |
| qpoases  |   96235.5 |             3.0 |      3364129.8 |            3.9 |
| quadprog |   31527.0 |         83341.0 |           35.5 |          130.9 |
| scs      |   31524.4 |             1.0 |           45.4 |            1.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|--------------:|----------------:|---------------:|---------------:|
| clarabel | 10779325511.4 |            17.1 |     16615131.1 |        16143.2 |
| cvxopt   | 16239442815.5 |            79.3 |          205.2 |        16880.5 |
| daqp     |           1.0 |             1.0 |            1.0 |            1.0 |
| ecos     | 27405872563.1 |       5311083.5 |     34622973.9 |     98887576.6 |
| highs    | 24531421200.4 |    2689498679.2 |   2651888237.5 |   2689521178.5 |
| osqp     |  1785279267.6 |            33.6 |    350041345.5 |        22504.6 |
| piqp     | 10779325976.0 |            28.5 |      4701266.3 |        20326.9 |
| proxqp   |  5394467341.5 |            48.8 |     28384995.6 |        43582.3 |
| qpalm    |    21273412.7 |            21.4 |     33196358.7 |        11357.4 |
| qpoases  | 32906542581.1 |            33.6 | 115647396363.7 |        28030.3 |
| quadprog | 10779325473.3 |            12.3 |     10962977.7 |        11213.1 |
| scs      | 10780037399.4 |            17.2 |     29675918.0 |        15369.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
