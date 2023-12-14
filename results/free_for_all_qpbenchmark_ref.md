# Free-for-all test set

| Number of problems | 11       |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.0rc1 |
| Date               | 2023-12-14 14:32:18.588048+00:00              |
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
| qpoases  | 3.2.1     |
| quadprog | 0.1.11    |
| scs      | 3.2.3     |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.1.1.

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
| `hz_actual_friendly` | 2.7589 GHz |
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
| piqp     | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| piqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| piqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| proxqp   | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
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
| clarabel |                                81.8 |                                334.0 |                                       203.1 |                                     2.0 |                                 6.0 |
| cvxopt   |                                72.7 |                                642.6 |                                       306.0 |                                     3.0 |                                 9.1 |
| daqp     |                                45.5 |                               2893.6 |                                       620.0 |                                     6.1 |                                18.4 |
| ecos     |                                45.5 |                               1815.7 |                                       514.4 |                                    33.0 |                                15.3 |
| highs    |                                45.5 |                               1115.3 |                                       409.7 |                                  1487.6 |                                13.7 |
| osqp     |                                81.8 |                                  1.0 |                                         1.0 |                                    67.8 |                                 1.0 |
| piqp     |                                81.8 |                                334.7 |                                       203.1 |                                     2.0 |                                 6.0 |
| proxqp   |                                90.9 |                                134.1 |                                       101.1 |                                     1.0 |                                 3.0 |
| qpoases  |                                45.5 |                               2893.7 |                                       620.0 |                                     6.1 |                                18.4 |
| quadprog |                                81.8 |                                336.8 |                                       203.1 |                                     2.0 |                                 6.0 |
| scs      |                                81.8 |                                335.6 |                                       203.2 |                                     2.0 |                                 6.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                81.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.1 |
| cvxopt   |                                45.5 |                                  1.9 |                                         1.5 |                                 37121.5 |                                 6.5 |
| daqp     |                                45.5 |                                  8.7 |                                         3.0 |                                     3.0 |                                 2.7 |
| ecos     |                                 0.0 |                                  5.4 |                                         2.5 |                            1422181453.0 |                            432144.5 |
| highs    |                                 0.0 |                                  3.3 |                                         2.0 |                          683326354371.1 |                         218835194.0 |
| osqp     |                                45.5 |                                  8.7 |                                         3.0 |                                     3.0 |                                 2.7 |
| piqp     |                                54.5 |                                  5.4 |                                         2.5 |                                     2.7 |                                 2.3 |
| proxqp   |                                81.8 |                                  1.1 |                                         3.7 |                                     1.0 |                                 4.1 |
| qpoases  |                                45.5 |                                  8.7 |                                         3.0 |                                     3.0 |                                 2.7 |
| quadprog |                                63.6 |                                  1.0 |                                         1.0 |                                 83083.8 |                                 1.0 |
| scs      |                                72.7 |                                  2.1 |                                         2.8 |                                     1.5 |                                 1.7 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                81.8 |                                272.7 |                                1033846693.9 |                                    12.0 |                             80957.0 |
| cvxopt   |                               100.0 |                                  5.9 |                                        14.0 |                                     1.0 |                                 1.0 |
| daqp     |                                45.5 |                               2363.0 |                                3101582147.3 |                                    36.1 |                            160253.4 |
| ecos     |                                45.5 |                               2363.2 |                                3101582148.6 |                                    38.0 |                            168699.6 |
| highs    |                                36.4 |                                909.7 |                                2067702634.9 |                               8260623.8 |                          12921261.5 |
| osqp     |                                63.6 |                                  9.2 |                                2181431392.1 |                                    28.4 |                           1705568.1 |
| piqp     |                               100.0 |                                  1.0 |                                 258440949.9 |                                     2.8 |                             22906.8 |
| proxqp   |                                90.9 |                                110.3 |                                3104653749.0 |                                     6.1 |                            165010.6 |
| qpoases  |                                81.8 |                                  3.7 |                                         1.0 |                               1235568.0 |                         563489150.2 |
| quadprog |                                81.8 |                                274.9 |                                1033841919.3 |                                    13.0 |                             53416.8 |
| scs      |                                81.8 |                                273.1 |                                1578509712.5 |                                    16.7 |                            144595.2 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                81.8 |                                  2.4 |                                         1.0 |                                     1.8 |                                 1.4 |
| cvxopt   |                                63.6 |                                  4.6 |                                         1.5 |                                    68.7 |                                 1.5 |
| daqp     |                                45.5 |                                 20.9 |                                         3.0 |                                     5.3 |                                 3.0 |
| ecos     |                                 0.0 |                                 13.1 |                                         2.5 |                              22631535.0 |                              8818.9 |
| highs    |                                27.3 |                                  8.1 |                                         2.0 |                            1215549040.8 |                            239855.3 |
| osqp     |                                63.6 |                                  8.0 |                                         2.5 |                                     3.6 |                                 2.0 |
| piqp     |                                72.7 |                                  4.6 |                                         1.5 |                                     2.8 |                                 1.8 |
| proxqp   |                                90.9 |                                  1.0 |                                         3.0 |                                     1.0 |                                 4.0 |
| qpoases  |                                54.5 |                                 13.1 |                                         2.5 |                                     4.5 |                                 2.5 |
| quadprog |                                72.7 |                                  2.4 |                                         1.0 |                                   149.6 |                                 1.0 |
| scs      |                                81.8 |                                  2.4 |                                         2.5 |                                     1.8 |                                 1.6 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        82 |              82 |             82 |             82 |
| cvxopt   |        73 |              45 |            100 |             64 |
| daqp     |        45 |              45 |             45 |             45 |
| ecos     |        45 |               0 |             45 |              0 |
| highs    |        45 |               0 |             36 |             27 |
| osqp     |        82 |              45 |             64 |             64 |
| piqp     |        82 |              55 |            100 |             73 |
| proxqp   |        91 |              82 |             91 |             91 |
| qpoases  |        45 |              45 |             82 |             55 |
| quadprog |        82 |              64 |             82 |             73 |
| scs      |        82 |              73 |             82 |             82 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              73 |            100 |             91 |
| daqp     |       100 |             100 |            100 |            100 |
| ecos     |        91 |              45 |            100 |             45 |
| highs    |        82 |              36 |             73 |             64 |
| osqp     |        82 |             100 |             64 |            100 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |       100 |             100 |            100 |            100 |
| qpoases  |       100 |             100 |             82 |            100 |
| quadprog |       100 |              82 |            100 |             91 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     334.0 |             1.0 |          272.7 |            2.4 |
| cvxopt   |     642.6 |             1.9 |            5.9 |            4.6 |
| daqp     |    2893.6 |             8.7 |         2363.0 |           20.9 |
| ecos     |    1815.7 |             5.4 |         2363.2 |           13.1 |
| highs    |    1115.3 |             3.3 |          909.7 |            8.1 |
| osqp     |       1.0 |             8.7 |            9.2 |            8.0 |
| piqp     |     334.7 |             5.4 |            1.0 |            4.6 |
| proxqp   |     134.1 |             1.1 |          110.3 |            1.0 |
| qpoases  |    2893.7 |             8.7 |            3.7 |           13.1 |
| quadprog |     336.8 |             1.0 |          274.9 |            2.4 |
| scs      |     335.6 |             2.1 |          273.1 |            2.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     203.1 |             1.0 |   1033846693.9 |            1.0 |
| cvxopt   |     306.0 |             1.5 |           14.0 |            1.5 |
| daqp     |     620.0 |             3.0 |   3101582147.3 |            3.0 |
| ecos     |     514.4 |             2.5 |   3101582148.6 |            2.5 |
| highs    |     409.7 |             2.0 |   2067702634.9 |            2.0 |
| osqp     |       1.0 |             3.0 |   2181431392.1 |            2.5 |
| piqp     |     203.1 |             2.5 |    258440949.9 |            1.5 |
| proxqp   |     101.1 |             3.7 |   3104653749.0 |            3.0 |
| qpoases  |     620.0 |             3.0 |            1.0 |            2.5 |
| quadprog |     203.1 |             1.0 |   1033841919.3 |            1.0 |
| scs      |     203.2 |             2.8 |   1578509712.5 |            2.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       2.0 |             1.0 |           12.0 |            1.8 |
| cvxopt   |       3.0 |         37121.5 |            1.0 |           68.7 |
| daqp     |       6.1 |             3.0 |           36.1 |            5.3 |
| ecos     |      33.0 |    1422181453.0 |           38.0 |     22631535.0 |
| highs    |    1487.6 |  683326354371.1 |      8260623.8 |   1215549040.8 |
| osqp     |      67.8 |             3.0 |           28.4 |            3.6 |
| piqp     |       2.0 |             2.7 |            2.8 |            2.8 |
| proxqp   |       1.0 |             1.0 |            6.1 |            1.0 |
| qpoases  |       6.1 |             3.0 |      1235568.0 |            4.5 |
| quadprog |       2.0 |         83083.8 |           13.0 |          149.6 |
| scs      |       2.0 |             1.5 |           16.7 |            1.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       6.0 |             1.1 |        80957.0 |            1.4 |
| cvxopt   |       9.1 |             6.5 |            1.0 |            1.5 |
| daqp     |      18.4 |             2.7 |       160253.4 |            3.0 |
| ecos     |      15.3 |        432144.5 |       168699.6 |         8818.9 |
| highs    |      13.7 |     218835194.0 |     12921261.5 |       239855.3 |
| osqp     |       1.0 |             2.7 |      1705568.1 |            2.0 |
| piqp     |       6.0 |             2.3 |        22906.8 |            1.8 |
| proxqp   |       3.0 |             4.1 |       165010.6 |            4.0 |
| qpoases  |      18.4 |             2.7 |    563489150.2 |            2.5 |
| quadprog |       6.0 |             1.0 |        53416.8 |            1.0 |
| scs      |       6.0 |             1.7 |       144595.2 |            1.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
