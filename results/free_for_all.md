# Free-for-all test set

| Number of problems | 28 |
|:-------------------|:--------------------|
| Benchmark version  | 2.4.0 |
| Date               | 2025-05-07 18:44:55.577915+00:00 |
| CPU                | [11th Gen Intel(R) Core(TM) i9-11900KF @ 3.50GHz](#cpu-info) |
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
| clarabel | 0.10.0                |
| cvxopt   | 1.3.2                 |
| gurobi   | 12.0.2 (size-limited) |
| highs    | 1.10.0                |
| osqp     | 0.6.7.post3           |
| piqp     | 0.4.2                 |
| proxqp   | 0.7.2                 |
| qpalm    | 1.2.5                 |
| scs      | 3.2.7.post2           |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.6.0.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | 11th Gen Intel(R) Core(TM) i9-11900KF @ 3.50GHz |
| `count` | 16 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_perfmon`, `art`, `avx`, `avx2`, `avx512_bitalg`, `avx512_vbmi2`, `avx512_vnni`, `avx512_vpopcntdq`, `avx512bitalg`, `avx512bw`, `avx512cd`, `avx512dq`, `avx512f`, `avx512ifma`, `avx512vbmi`, `avx512vbmi2`, `avx512vl`, `avx512vnni`, `avx512vpopcntdq`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `gfni`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `hwp_pkg_req`, `ibpb`, `ibrs`, `ibrs_enhanced`, `intel_pt`, `invpcid`, `invpcid_single`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `mpx`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `ospke`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pku`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pts`, `rdpid`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `sha`, `sha_ni`, `smap`, `smep`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tsc_known_freq`, `tscdeadline`, `umip`, `vaes`, `vme`, `vmx`, `vnmi`, `vpclmulqdq`, `vpid`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `l1_data_cache_size` | 393216 |
| `l1_instruction_cache_size` | 262144 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 256 |
| `l2_cache_size` | 4194304 |
| `l3_cache_size` | 16777216 |
| `model` | 167 |
| `python_version` | 3.12.10.final.0 (64 bit) |
| `stepping` | 1 |
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

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                92.9 |                                  2.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt      |                                67.9 |                                  5.5 |                                         4.6 |                                     4.6 |                                 4.6 |
| daqp        |                                71.4 |                                  3.0 |                                         4.0 |                                     4.0 |                                 4.0 |
| ecos        |                                52.4 |                                  5.4 |                                         6.8 |                                     6.8 |                                 6.9 |
| gurobi      |                                60.7 |                                  4.3 |                                         5.6 |                                     5.6 |                                 5.6 |
| highs       |                                71.4 |                                  2.5 |                                         3.0 |                                   268.6 |                                 3.3 |
| jaxopt_osqp |                                71.4 |                                  4.2 |                                         4.0 |                                     4.0 |                                 4.1 |
| kvxopt      |                                71.4 |                                  3.0 |                                         4.0 |                                     4.0 |                                 4.0 |
| osqp        |                                78.6 |                                  1.4 |                                         2.0 |                                    32.0 |                                 2.4 |
| piqp        |                                89.3 |                                  2.2 |                                         1.5 |                                     1.5 |                                 1.5 |
| proxqp      |                                75.0 |                                  2.3 |                                         3.0 |                                     3.0 |                                 4.2 |
| qpalm       |                                92.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.1 |
| qpax        |                                71.4 |                                  2.5 |                                         2.7 |                                   180.8 |                                17.9 |
| qpswift     |                                28.6 |                                  8.8 |                                        10.3 |                                    10.3 |                                10.3 |
| quadprog    |                                71.4 |                                  3.0 |                                         4.0 |                                     4.0 |                                 4.0 |
| scs         |                                78.6 |                                  2.6 |                                         3.0 |                                     3.1 |                                 3.1 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                92.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt      |                                17.9 |                                  2.7 |                                         4.5 |                                     4.5 |                            456449.2 |
| daqp        |                                71.4 |                                  1.5 |                                         4.0 |                                     4.0 |                                 1.3 |
| ecos        |                                 0.0 |                                  2.7 |                                         6.6 |                               2754237.4 |                          27215257.3 |
| gurobi      |                                28.6 |                                  2.1 |                                         5.6 |                              28348187.8 |                              1881.0 |
| highs       |                                 0.0 |                                  1.8 |                                         4.6 |                          247204867460.9 |                          79225209.8 |
| jaxopt_osqp |                                 9.5 |                                  5.6 |                                        18.6 |                                    11.9 |                                 6.1 |
| kvxopt      |                                19.0 |                                  1.5 |                                         4.0 |                                     4.0 |                            608570.1 |
| osqp        |                                42.9 |                                  2.4 |                                         6.1 |                                     7.5 |                                 3.6 |
| piqp        |                                78.6 |                                  1.5 |                                         2.5 |                                     2.9 |                                 1.8 |
| proxqp      |                                71.4 |                                  1.5 |                                         7.3 |                                     4.0 |                                 2.8 |
| qpalm       |                                64.3 |                                  1.1 |                                         4.0 |                                     3.1 |                                 6.1 |
| qpax        |                                 9.5 |                                  4.4 |                                        34.2 |                          166171535383.8 |                        4689614291.4 |
| qpswift     |                                 4.8 |                                  4.4 |                                        10.0 |                                    10.5 |                                21.5 |
| quadprog    |                                71.4 |                                  1.5 |                                         4.0 |                                     4.0 |                                 1.3 |
| scs         |                                71.4 |                                  1.3 |                                         6.5 |                                     4.0 |                                 1.6 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                92.9 |                                  2.0 |                                         4.0 |                                     2.0 |                                 2.6 |
| cvxopt      |                                64.3 |                                  6.3 |                                        17.8 |                                     8.9 |                                 3.5 |
| daqp        |                                71.4 |                                  3.4 |                                        17.4 |                                     7.9 |                                 2.4 |
| ecos        |                                38.1 |                                  6.1 |                                        26.4 |                                    18.7 |                                53.5 |
| gurobi      |                                57.1 |                                  4.9 |                                        21.8 |                                    67.5 |                                 3.3 |
| highs       |                                53.6 |                                  2.3 |                                         9.9 |                                493443.1 |                               746.5 |
| jaxopt_osqp |                                33.3 |                                  4.5 |                                        21.7 |                                    14.1 |                                15.8 |
| kvxopt      |                                66.7 |                                  3.4 |                                        15.9 |                                     7.9 |                                 3.5 |
| osqp        |                                57.1 |                                  2.1 |                                        20.2 |                                    11.6 |                                45.4 |
| piqp        |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| proxqp      |                                78.6 |                                  2.6 |                                        25.9 |                                     6.0 |                                 4.5 |
| qpalm       |                                60.7 |                                  1.6 |                                        17.3 |                                     4.7 |                                37.2 |
| qpax        |                                66.7 |                                  2.6 |                                        11.1 |                                331696.2 |                              8538.7 |
| qpswift     |                                28.6 |                                 10.0 |                                        39.6 |                                    19.8 |                                 6.0 |
| quadprog    |                                71.4 |                                  3.4 |                                        15.9 |                                     7.9 |                                 2.4 |
| scs         |                                78.6 |                                  2.8 |                                        16.9 |                                     7.1 |                                 3.4 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                92.9 |                                  1.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| cvxopt      |                                46.4 |                                  3.2 |                                         4.5 |                                     4.5 |                               472.8 |
| daqp        |                                71.4 |                                  1.7 |                                         4.0 |                                     4.0 |                                 1.4 |
| ecos        |                                 4.8 |                                  3.1 |                                         6.7 |                                  2778.1 |                             28103.6 |
| gurobi      |                                53.6 |                                  2.5 |                                         5.5 |                                 28530.3 |                                 3.8 |
| highs       |                                14.3 |                                  1.4 |                                         3.0 |                             248745433.7 |                             82079.6 |
| jaxopt_osqp |                                28.6 |                                  3.9 |                                         9.6 |                                     9.6 |                                 5.3 |
| kvxopt      |                                42.9 |                                  1.7 |                                         4.0 |                                     4.0 |                               629.7 |
| osqp        |                                53.6 |                                  2.3 |                                         5.6 |                                     6.4 |                                 4.1 |
| piqp        |                                92.9 |                                  1.0 |                                         1.0 |                                     2.5 |                                 1.2 |
| proxqp      |                                75.0 |                                  1.5 |                                         6.2 |                                     3.6 |                                 2.4 |
| qpalm       |                                71.4 |                                  1.0 |                                         3.3 |                                     2.6 |                                 9.0 |
| qpax        |                                19.0 |                                  3.5 |                                       185.7 |                             167207151.8 |                           4842333.6 |
| qpswift     |                                 4.8 |                                  5.1 |                                        10.0 |                                    10.5 |                                12.9 |
| quadprog    |                                71.4 |                                  1.7 |                                         4.0 |                                     4.0 |                                 1.4 |
| scs         |                                75.0 |                                  1.5 |                                         5.0 |                                     3.8 |                                 1.8 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |        93 |              93 |             93 |             93 |
| cvxopt      |        68 |              18 |             64 |             46 |
| daqp        |        71 |              71 |             71 |             71 |
| ecos        |        52 |               0 |             38 |              5 |
| gurobi      |        61 |              29 |             57 |             54 |
| highs       |        71 |               0 |             54 |             14 |
| jaxopt_osqp |        71 |              10 |             33 |             29 |
| kvxopt      |        71 |              19 |             67 |             43 |
| osqp        |        79 |              43 |             57 |             54 |
| piqp        |        89 |              79 |            100 |             93 |
| proxqp      |        75 |              71 |             79 |             75 |
| qpalm       |        93 |              64 |             61 |             71 |
| qpax        |        71 |              10 |             67 |             19 |
| qpswift     |        29 |               5 |             29 |              5 |
| quadprog    |        71 |              71 |             71 |             71 |
| scs         |        79 |              71 |             79 |             75 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |              50 |             96 |             79 |
| daqp        |       100 |             100 |            100 |            100 |
| ecos        |       100 |              48 |             86 |             52 |
| gurobi      |       100 |              68 |             96 |             93 |
| highs       |        93 |              32 |             71 |             36 |
| jaxopt_osqp |       100 |              95 |             62 |             81 |
| kvxopt      |       100 |              48 |             95 |             71 |
| osqp        |        93 |              86 |             71 |             89 |
| piqp        |       100 |              96 |            100 |            100 |
| proxqp      |        96 |             100 |            100 |            100 |
| qpalm       |       100 |              82 |             71 |             86 |
| qpax        |        90 |              81 |             86 |             71 |
| qpswift     |       100 |              76 |            100 |             76 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |              96 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       2.0 |             1.0 |            2.0 |            1.1 |
| cvxopt      |       5.5 |             2.7 |            6.3 |            3.2 |
| daqp        |       3.0 |             1.5 |            3.4 |            1.7 |
| ecos        |       5.4 |             2.7 |            6.1 |            3.1 |
| gurobi      |       4.3 |             2.1 |            4.9 |            2.5 |
| highs       |       2.5 |             1.8 |            2.3 |            1.4 |
| jaxopt_osqp |       4.2 |             5.6 |            4.5 |            3.9 |
| kvxopt      |       3.0 |             1.5 |            3.4 |            1.7 |
| osqp        |       1.4 |             2.4 |            2.1 |            2.3 |
| piqp        |       2.2 |             1.5 |            1.0 |            1.0 |
| proxqp      |       2.3 |             1.5 |            2.6 |            1.5 |
| qpalm       |       1.0 |             1.1 |            1.6 |            1.0 |
| qpax        |       2.5 |             4.4 |            2.6 |            3.5 |
| qpswift     |       8.8 |             4.4 |           10.0 |            5.1 |
| quadprog    |       3.0 |             1.5 |            3.4 |            1.7 |
| scs         |       2.6 |             1.3 |            2.8 |            1.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       1.0 |             1.0 |            4.0 |            1.0 |
| cvxopt      |       4.6 |             4.5 |           17.8 |            4.5 |
| daqp        |       4.0 |             4.0 |           17.4 |            4.0 |
| ecos        |       6.8 |             6.6 |           26.4 |            6.7 |
| gurobi      |       5.6 |             5.6 |           21.8 |            5.5 |
| highs       |       3.0 |             4.6 |            9.9 |            3.0 |
| jaxopt_osqp |       4.0 |            18.6 |           21.7 |            9.6 |
| kvxopt      |       4.0 |             4.0 |           15.9 |            4.0 |
| osqp        |       2.0 |             6.1 |           20.2 |            5.6 |
| piqp        |       1.5 |             2.5 |            1.0 |            1.0 |
| proxqp      |       3.0 |             7.3 |           25.9 |            6.2 |
| qpalm       |       1.0 |             4.0 |           17.3 |            3.3 |
| qpax        |       2.7 |            34.2 |           11.1 |          185.7 |
| qpswift     |      10.3 |            10.0 |           39.6 |           10.0 |
| quadprog    |       4.0 |             4.0 |           15.9 |            4.0 |
| scs         |       3.0 |             6.5 |           16.9 |            5.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       1.0 |             1.0 |            2.0 |            1.0 |
| cvxopt      |       4.6 |             4.5 |            8.9 |            4.5 |
| daqp        |       4.0 |             4.0 |            7.9 |            4.0 |
| ecos        |       6.8 |       2754237.4 |           18.7 |         2778.1 |
| gurobi      |       5.6 |      28348187.8 |           67.5 |        28530.3 |
| highs       |     268.6 |  247204867460.9 |       493443.1 |    248745433.7 |
| jaxopt_osqp |       4.0 |            11.9 |           14.1 |            9.6 |
| kvxopt      |       4.0 |             4.0 |            7.9 |            4.0 |
| osqp        |      32.0 |             7.5 |           11.6 |            6.4 |
| piqp        |       1.5 |             2.9 |            1.0 |            2.5 |
| proxqp      |       3.0 |             4.0 |            6.0 |            3.6 |
| qpalm       |       1.0 |             3.1 |            4.7 |            2.6 |
| qpax        |     180.8 |  166171535383.8 |       331696.2 |    167207151.8 |
| qpswift     |      10.3 |            10.5 |           19.8 |           10.5 |
| quadprog    |       4.0 |             4.0 |            7.9 |            4.0 |
| scs         |       3.1 |             4.0 |            7.1 |            3.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       1.0 |             1.0 |            2.6 |            1.0 |
| cvxopt      |       4.6 |        456449.2 |            3.5 |          472.8 |
| daqp        |       4.0 |             1.3 |            2.4 |            1.4 |
| ecos        |       6.9 |      27215257.3 |           53.5 |        28103.6 |
| gurobi      |       5.6 |          1881.0 |            3.3 |            3.8 |
| highs       |       3.3 |      79225209.8 |          746.5 |        82079.6 |
| jaxopt_osqp |       4.1 |             6.1 |           15.8 |            5.3 |
| kvxopt      |       4.0 |        608570.1 |            3.5 |          629.7 |
| osqp        |       2.4 |             3.6 |           45.4 |            4.1 |
| piqp        |       1.5 |             1.8 |            1.0 |            1.2 |
| proxqp      |       4.2 |             2.8 |            4.5 |            2.4 |
| qpalm       |       1.1 |             6.1 |           37.2 |            9.0 |
| qpax        |      17.9 |    4689614291.4 |         8538.7 |      4842333.6 |
| qpswift     |      10.3 |            21.5 |            6.0 |           12.9 |
| quadprog    |       4.0 |             1.3 |            2.4 |            1.4 |
| scs         |       3.1 |             1.6 |            3.4 |            1.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
