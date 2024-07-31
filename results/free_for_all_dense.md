# Free-for-all dense subset

| Number of problems | 22 |
|:-------------------|:--------------------|
| Benchmark version  | 2.2.1 |
| Date               | 2024-07-31 13:15:48.136314+00:00 |
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
| daqp     | 0.5.1       |
| ecos     | 2.0.14      |
| highs    | 1.7.2       |
| hpipm    | 0.2         |
| osqp     | 0.6.7.post0 |
| piqp     | 0.4.1       |
| proxqp   | 0.6.6       |
| qpalm    | 1.2.3       |
| qpoases  | 3.2.1       |
| quadprog | 0.1.12      |
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
| highs    | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| hpipm    | ``tol_comp``                     | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_eq``                       | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_ineq``                     | -         | 1e-09           | 0.001          | 1e-06          |
| hpipm    | ``tol_stat``                     | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| piqp     | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
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
| qpalm    | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| qpoases  | ``predefined_options``           | default   | reliable        | fast           | -              |
| qpoases  | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
| scs      | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| scs      | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| scs      | ``time_limit_secs``              | 10.0      | 10.0            | 10.0           | 10.0           |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.7 |                                124.6 |                                      2860.5 |                                   236.4 |                                70.1 |
| cvxopt   |                                86.4 |                                 60.1 |                                      1421.0 |                                   117.4 |                                34.9 |
| daqp     |                                72.7 |                                124.6 |                                      2860.5 |                                   236.4 |                                70.1 |
| ecos     |                                59.1 |                                171.8 |                                      3830.7 |                                  1425.0 |                                95.6 |
| highs    |                                86.4 |                                 27.6 |                                       471.6 |                                 24112.8 |                                17.4 |
| hpipm    |                                81.8 |                                 24.0 |                                      5771.4 |                                  1065.6 |                                12.3 |
| osqp     |                                90.9 |                                  1.0 |                                         9.9 |                                  2369.8 |                                 9.1 |
| piqp     |                                90.9 |                                 39.5 |                                       945.3 |                                    78.1 |                                23.2 |
| proxqp   |                                90.9 |                                 20.4 |                                       471.6 |                                    39.0 |                                38.6 |
| qpalm    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpoases  |                                72.7 |                                124.7 |                                      2860.5 |                                   236.4 |                                70.1 |
| quadprog |                                90.9 |                                 40.1 |                                       945.3 |                                    78.1 |                                23.2 |
| scs      |                                90.9 |                                 39.5 |                                       946.4 |                                    80.6 |                                25.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.7 |                                  4.7 |                                         3.0 |                                     1.9 |                                 4.2 |
| cvxopt   |                                22.7 |                                  2.3 |                                         1.5 |                                 24158.8 |                           1262366.7 |
| daqp     |                                72.7 |                                  4.7 |                                         3.0 |                                     1.9 |                                 2.7 |
| ecos     |                                 0.0 |                                  6.5 |                                         4.0 |                            2063892540.4 |                          51716248.8 |
| highs    |                                 0.0 |                                  1.0 |                                        13.3 |                          190449824676.2 |                         218923143.5 |
| hpipm    |                                77.3 |                                  2.3 |                                         1.5 |                            8121728577.5 |                          28370454.4 |
| osqp     |                                50.0 |                                  5.6 |                                         3.6 |                                     3.3 |                                 7.7 |
| piqp     |                                77.3 |                                  3.9 |                                         2.5 |                                     1.8 |                                 3.5 |
| proxqp   |                                86.4 |                                  2.4 |                                         4.6 |                                     1.0 |                                 5.1 |
| qpalm    |                                81.8 |                                  2.3 |                                         2.7 |                                     1.1 |                                 3.0 |
| qpoases  |                                72.7 |                                  4.7 |                                         3.0 |                                     1.9 |                                 2.7 |
| quadprog |                                81.8 |                                  1.5 |                                         1.0 |                                 54073.2 |                                 1.0 |
| scs      |                                86.4 |                                  2.4 |                                         2.7 |                                     1.3 |                                 2.6 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.7 |                                100.5 |                               17058469202.3 |                                    36.1 |                                 5.7 |
| cvxopt   |                                95.5 |                                  5.4 |                                        76.6 |                                     1.0 |                                 1.4 |
| daqp     |                                72.7 |                                100.4 |                               18696218364.9 |                                    36.1 |                                 3.0 |
| ecos     |                                45.5 |                                158.3 |                               25587878265.8 |                                    78.0 |                                60.5 |
| highs    |                                68.2 |                                  6.6 |                                         1.0 |                               3537443.4 |                               877.3 |
| hpipm    |                                63.6 |                                 31.8 |                                5686105160.3 |                                150867.6 |                                45.7 |
| osqp     |                                77.3 |                                  1.0 |                               13174263934.0 |                                    35.5 |                                37.6 |
| piqp     |                               100.0 |                                  1.1 |                                1434486921.4 |                                     3.7 |                                 1.5 |
| proxqp   |                                95.5 |                                 16.5 |                               22999425615.1 |                                     6.6 |                                 4.9 |
| qpalm    |                                72.7 |                                 15.5 |                               15400347160.6 |                                    14.9 |                                43.3 |
| qpoases  |                                90.9 |                                  3.2 |                                        17.3 |                                917715.3 |                             10086.5 |
| quadprog |                                90.9 |                                 32.4 |                                5686104710.9 |                                    13.0 |                                 1.0 |
| scs      |                                90.9 |                                 31.5 |                               11314073518.3 |                                    19.3 |                                 3.6 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.7 |                                  4.6 |                                         5.9 |                                     2.7 |                                 4.1 |
| cvxopt   |                                54.5 |                                  2.2 |                                         3.0 |                                    34.6 |                              1388.3 |
| daqp     |                                72.7 |                                  4.6 |                                         5.9 |                                     2.7 |                                 3.0 |
| ecos     |                                 4.5 |                                  6.3 |                                         7.9 |                              11715702.5 |                             66552.9 |
| highs    |                                18.2 |                                  1.0 |                                         1.0 |                             262275929.0 |                            240554.2 |
| hpipm    |                                68.2 |                                  1.4 |                                         2.0 |                              11184752.1 |                             31181.2 |
| osqp     |                                63.6 |                                  3.7 |                                         6.1 |                                     3.5 |                                 9.4 |
| piqp     |                                86.4 |                                  2.2 |                                         3.0 |                                     1.5 |                                 2.6 |
| proxqp   |                                90.9 |                                  1.5 |                                         7.3 |                                     1.0 |                                 4.4 |
| qpalm    |                                86.4 |                                  1.4 |                                         4.0 |                                     1.5 |                                 6.3 |
| qpoases  |                                77.3 |                                  3.7 |                                         4.9 |                                     2.3 |                                 2.5 |
| quadprog |                                86.4 |                                  1.5 |                                         2.0 |                                    75.4 |                                 1.0 |
| scs      |                                90.9 |                                  1.5 |                                         5.4 |                                     1.2 |                                 3.1 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        73 |              73 |             73 |             73 |
| cvxopt   |        86 |              23 |             95 |             55 |
| daqp     |        73 |              73 |             73 |             73 |
| ecos     |        59 |               0 |             45 |              5 |
| highs    |        86 |               0 |             68 |             18 |
| hpipm    |        82 |              77 |             64 |             68 |
| osqp     |        91 |              50 |             77 |             64 |
| piqp     |        91 |              77 |            100 |             86 |
| proxqp   |        91 |              86 |             95 |             91 |
| qpalm    |       100 |              82 |             73 |             86 |
| qpoases  |        73 |              73 |             91 |             77 |
| quadprog |        91 |              82 |             91 |             86 |
| scs      |        91 |              86 |             91 |             91 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              36 |             95 |             68 |
| daqp     |       100 |             100 |            100 |            100 |
| ecos     |        95 |              36 |             86 |             41 |
| highs    |        91 |               5 |             68 |             23 |
| hpipm    |        86 |              91 |             73 |             77 |
| osqp     |        91 |              82 |             77 |             86 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |        95 |             100 |            100 |            100 |
| qpalm    |       100 |              95 |             77 |             95 |
| qpoases  |       100 |             100 |             91 |            100 |
| quadprog |       100 |              91 |            100 |             95 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     124.6 |             4.7 |          100.5 |            4.6 |
| cvxopt   |      60.1 |             2.3 |            5.4 |            2.2 |
| daqp     |     124.6 |             4.7 |          100.4 |            4.6 |
| ecos     |     171.8 |             6.5 |          158.3 |            6.3 |
| highs    |      27.6 |             1.0 |            6.6 |            1.0 |
| hpipm    |      24.0 |             2.3 |           31.8 |            1.4 |
| osqp     |       1.0 |             5.6 |            1.0 |            3.7 |
| piqp     |      39.5 |             3.9 |            1.1 |            2.2 |
| proxqp   |      20.4 |             2.4 |           16.5 |            1.5 |
| qpalm    |       1.0 |             2.3 |           15.5 |            1.4 |
| qpoases  |     124.7 |             4.7 |            3.2 |            3.7 |
| quadprog |      40.1 |             1.5 |           32.4 |            1.5 |
| scs      |      39.5 |             2.4 |           31.5 |            1.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |    2860.5 |             3.0 |  17058469202.3 |            5.9 |
| cvxopt   |    1421.0 |             1.5 |           76.6 |            3.0 |
| daqp     |    2860.5 |             3.0 |  18696218364.9 |            5.9 |
| ecos     |    3830.7 |             4.0 |  25587878265.8 |            7.9 |
| highs    |     471.6 |            13.3 |            1.0 |            1.0 |
| hpipm    |    5771.4 |             1.5 |   5686105160.3 |            2.0 |
| osqp     |       9.9 |             3.6 |  13174263934.0 |            6.1 |
| piqp     |     945.3 |             2.5 |   1434486921.4 |            3.0 |
| proxqp   |     471.6 |             4.6 |  22999425615.1 |            7.3 |
| qpalm    |       1.0 |             2.7 |  15400347160.6 |            4.0 |
| qpoases  |    2860.5 |             3.0 |           17.3 |            4.9 |
| quadprog |     945.3 |             1.0 |   5686104710.9 |            2.0 |
| scs      |     946.4 |             2.7 |  11314073518.3 |            5.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     236.4 |             1.9 |           36.1 |            2.7 |
| cvxopt   |     117.4 |         24158.8 |            1.0 |           34.6 |
| daqp     |     236.4 |             1.9 |           36.1 |            2.7 |
| ecos     |    1425.0 |    2063892540.4 |           78.0 |     11715702.5 |
| highs    |   24112.8 |  190449824676.2 |      3537443.4 |    262275929.0 |
| hpipm    |    1065.6 |    8121728577.5 |       150867.6 |     11184752.1 |
| osqp     |    2369.8 |             3.3 |           35.5 |            3.5 |
| piqp     |      78.1 |             1.8 |            3.7 |            1.5 |
| proxqp   |      39.0 |             1.0 |            6.6 |            1.0 |
| qpalm    |       1.0 |             1.1 |           14.9 |            1.5 |
| qpoases  |     236.4 |             1.9 |       917715.3 |            2.3 |
| quadprog |      78.1 |         54073.2 |           13.0 |           75.4 |
| scs      |      80.6 |             1.3 |           19.3 |            1.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |      70.1 |             4.2 |            5.7 |            4.1 |
| cvxopt   |      34.9 |       1262366.7 |            1.4 |         1388.3 |
| daqp     |      70.1 |             2.7 |            3.0 |            3.0 |
| ecos     |      95.6 |      51716248.8 |           60.5 |        66552.9 |
| highs    |      17.4 |     218923143.5 |          877.3 |       240554.2 |
| hpipm    |      12.3 |      28370454.4 |           45.7 |        31181.2 |
| osqp     |       9.1 |             7.7 |           37.6 |            9.4 |
| piqp     |      23.2 |             3.5 |            1.5 |            2.6 |
| proxqp   |      38.6 |             5.1 |            4.9 |            4.4 |
| qpalm    |       1.0 |             3.0 |           43.3 |            6.3 |
| qpoases  |      70.1 |             2.7 |        10086.5 |            2.5 |
| quadprog |      23.2 |             1.0 |            1.0 |            1.0 |
| scs      |      25.0 |             2.6 |            3.6 |            3.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
