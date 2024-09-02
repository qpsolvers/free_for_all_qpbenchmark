# Free-for-all dense subset

| Number of problems | 22 |
|:-------------------|:--------------------|
| Benchmark version  | 2.2.3 |
| Date               | 2024-09-02 14:42:30.690534+00:00 |
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

| solver   | version     |
|:---------|:------------|
| clarabel | 0.9.0       |
| cvxopt   | 1.3.2       |
| daqp     | 0.5.1.post1 |
| ecos     | 2.0.14      |
| highs    | 1.7.2       |
| osqp     | 0.6.7.post0 |
| piqp     | 0.4.2       |
| proxqp   | 0.6.7       |
| qpalm    | 1.2.3       |
| qpoases  | 3.2.1       |
| quadprog | 0.1.12      |
| scs      | 3.2.7       |

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
| `hz_actual_friendly` | 560.4720 MHz |
| `hz_advertised_friendly` | 560.4720 MHz |
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
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 10.0      | 10.0            | 10.0           | 10.0           |
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
| clarabel |                                72.7 |                                267.6 |                                      2860.5 |                                  2671.9 |                                70.1 |
| cvxopt   |                                86.4 |                                128.2 |                                      1421.0 |                                  1327.3 |                                34.9 |
| daqp     |                                72.7 |                                267.6 |                                      2860.5 |                                  2671.9 |                                70.1 |
| ecos     |                                59.1 |                                421.6 |                                      4318.9 |                                  4036.0 |                               107.3 |
| highs    |                                86.4 |                                 48.2 |                                       471.6 |                                272545.1 |                                17.4 |
| osqp     |                                90.9 |                                  1.0 |                                         9.9 |                                 26784.4 |                                 9.1 |
| piqp     |                                86.4 |                                128.0 |                                      1421.0 |                                  1327.3 |                                34.8 |
| proxqp   |                                90.9 |                                 42.3 |                                       471.6 |                                   440.5 |                                38.6 |
| qpalm    |                               100.0 |                                  1.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpoases  |                                72.7 |                                267.7 |                                      2860.5 |                                  2671.9 |                                70.1 |
| quadprog |                                90.9 |                                 84.7 |                                       945.3 |                                   883.0 |                                23.2 |
| scs      |                                90.9 |                                 84.5 |                                       946.4 |                                   911.0 |                                25.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.7 |                                  6.2 |                                         3.0 |                                     2.0 |                                 4.2 |
| cvxopt   |                                22.7 |                                  3.0 |                                         1.5 |                                 42356.0 |                           1256444.9 |
| daqp     |                                72.7 |                                  6.2 |                                         3.0 |                                     2.0 |                                 2.7 |
| ecos     |                                 0.0 |                                  9.8 |                                         4.5 |                               1320885.1 |                          50707211.4 |
| highs    |                                 0.0 |                                  1.1 |                                        13.3 |                          196153180117.9 |                         217896172.2 |
| osqp     |                                50.0 |                                  7.4 |                                         3.6 |                                     3.4 |                                 7.6 |
| piqp     |                                77.3 |                                  5.1 |                                         2.5 |                                     1.9 |                                 3.5 |
| proxqp   |                                86.4 |                                  3.1 |                                         4.6 |                                     1.0 |                                 5.0 |
| qpalm    |                                77.3 |                                  1.0 |                                         1.7 |                                 89054.7 |                                 3.5 |
| qpoases  |                                72.7 |                                  6.2 |                                         3.0 |                                     2.0 |                                 2.7 |
| quadprog |                                81.8 |                                  2.0 |                                         1.0 |                                 58279.8 |                                 1.0 |
| scs      |                                90.9 |                                  2.2 |                                         2.6 |                                     1.0 |                                 2.2 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.7 |                                273.2 |                               17058469202.3 |                                     9.8 |                                 5.7 |
| cvxopt   |                                90.9 |                                 47.2 |                                2843045977.7 |                                     2.0 |                                 1.9 |
| daqp     |                                72.7 |                                273.2 |                               18696218364.9 |                                     9.8 |                                 3.0 |
| ecos     |                                45.5 |                                430.5 |                               25587878265.8 |                                    21.3 |                                60.5 |
| highs    |                                68.2 |                                  6.6 |                                         1.0 |                                963614.0 |                               877.3 |
| osqp     |                                72.7 |                                 10.9 |                               13174356162.9 |                                    12.6 |                                37.6 |
| piqp     |                               100.0 |                                  1.6 |                                1434486926.4 |                                     1.0 |                                 1.5 |
| proxqp   |                               100.0 |                                  1.3 |                               20156286781.9 |                                     1.6 |                                 4.4 |
| qpalm    |                                77.3 |                                  1.0 |                               12557245156.6 |                                     3.8 |                                42.8 |
| qpoases  |                                90.9 |                                  4.4 |                                        17.3 |                                249989.4 |                             10086.5 |
| quadprog |                                90.9 |                                 86.7 |                                5686104710.9 |                                     3.6 |                                 1.0 |
| scs      |                                90.9 |                                 85.6 |                               11314073640.0 |                                     5.2 |                                 3.6 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                72.7 |                                201.0 |                                         5.9 |                                     2.5 |                                 4.1 |
| cvxopt   |                                54.5 |                                 96.3 |                                         3.0 |                                    54.0 |                              1388.3 |
| daqp     |                                72.7 |                                201.0 |                                         5.9 |                                     2.5 |                                 3.0 |
| ecos     |                                 4.5 |                                316.7 |                                         8.9 |                                  1649.1 |                             55970.8 |
| highs    |                                18.2 |                                 35.8 |                                         1.0 |                             244344945.3 |                            240553.0 |
| osqp     |                                63.6 |                                165.0 |                                         6.1 |                                     3.3 |                                 9.4 |
| piqp     |                                86.4 |                                 96.0 |                                         3.0 |                                     1.4 |                                 2.5 |
| proxqp   |                                90.9 |                                 63.6 |                                         7.3 |                                     1.0 |                                 4.4 |
| qpalm    |                                90.9 |                                  1.0 |                                         2.1 |                                   111.5 |                                 5.3 |
| qpoases  |                                77.3 |                                164.9 |                                         4.9 |                                     2.1 |                                 2.5 |
| quadprog |                                86.4 |                                 63.7 |                                         2.0 |                                    73.4 |                                 1.0 |
| scs      |                                90.9 |                                 63.7 |                                         4.8 |                                     1.1 |                                 3.1 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        73 |              73 |             73 |             73 |
| cvxopt   |        86 |              23 |             91 |             55 |
| daqp     |        73 |              73 |             73 |             73 |
| ecos     |        59 |               0 |             45 |              5 |
| highs    |        86 |               0 |             68 |             18 |
| osqp     |        91 |              50 |             73 |             64 |
| piqp     |        86 |              77 |            100 |             86 |
| proxqp   |        91 |              86 |            100 |             91 |
| qpalm    |       100 |              77 |             77 |             91 |
| qpoases  |        73 |              73 |             91 |             77 |
| quadprog |        91 |              82 |             91 |             86 |
| scs      |        91 |              91 |             91 |             91 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              36 |             95 |             68 |
| daqp     |       100 |             100 |            100 |            100 |
| ecos     |       100 |              41 |             86 |             45 |
| highs    |        91 |               5 |             68 |             23 |
| osqp     |        91 |              82 |             73 |             86 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |        95 |             100 |            100 |            100 |
| qpalm    |       100 |              82 |             77 |             91 |
| qpoases  |       100 |             100 |             91 |            100 |
| quadprog |       100 |              91 |            100 |             95 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |     267.6 |             6.2 |          273.2 |          201.0 |
| cvxopt   |     128.2 |             3.0 |           47.2 |           96.3 |
| daqp     |     267.6 |             6.2 |          273.2 |          201.0 |
| ecos     |     421.6 |             9.8 |          430.5 |          316.7 |
| highs    |      48.2 |             1.1 |            6.6 |           35.8 |
| osqp     |       1.0 |             7.4 |           10.9 |          165.0 |
| piqp     |     128.0 |             5.1 |            1.6 |           96.0 |
| proxqp   |      42.3 |             3.1 |            1.3 |           63.6 |
| qpalm    |       1.2 |             1.0 |            1.0 |            1.0 |
| qpoases  |     267.7 |             6.2 |            4.4 |          164.9 |
| quadprog |      84.7 |             2.0 |           86.7 |           63.7 |
| scs      |      84.5 |             2.2 |           85.6 |           63.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |    2860.5 |             3.0 |  17058469202.3 |            5.9 |
| cvxopt   |    1421.0 |             1.5 |   2843045977.7 |            3.0 |
| daqp     |    2860.5 |             3.0 |  18696218364.9 |            5.9 |
| ecos     |    4318.9 |             4.5 |  25587878265.8 |            8.9 |
| highs    |     471.6 |            13.3 |            1.0 |            1.0 |
| osqp     |       9.9 |             3.6 |  13174356162.9 |            6.1 |
| piqp     |    1421.0 |             2.5 |   1434486926.4 |            3.0 |
| proxqp   |     471.6 |             4.6 |  20156286781.9 |            7.3 |
| qpalm    |       1.0 |             1.7 |  12557245156.6 |            2.1 |
| qpoases  |    2860.5 |             3.0 |           17.3 |            4.9 |
| quadprog |     945.3 |             1.0 |   5686104710.9 |            2.0 |
| scs      |     946.4 |             2.6 |  11314073640.0 |            4.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |    2671.9 |             2.0 |            9.8 |            2.5 |
| cvxopt   |    1327.3 |         42356.0 |            2.0 |           54.0 |
| daqp     |    2671.9 |             2.0 |            9.8 |            2.5 |
| ecos     |    4036.0 |       1320885.1 |           21.3 |         1649.1 |
| highs    |  272545.1 |  196153180117.9 |       963614.0 |    244344945.3 |
| osqp     |   26784.4 |             3.4 |           12.6 |            3.3 |
| piqp     |    1327.3 |             1.9 |            1.0 |            1.4 |
| proxqp   |     440.5 |             1.0 |            1.6 |            1.0 |
| qpalm    |       1.0 |         89054.7 |            3.8 |          111.5 |
| qpoases  |    2671.9 |             2.0 |       249989.4 |            2.1 |
| quadprog |     883.0 |         58279.8 |            3.6 |           73.4 |
| scs      |     911.0 |             1.0 |            5.2 |            1.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |      70.1 |             4.2 |            5.7 |            4.1 |
| cvxopt   |      34.9 |       1256444.9 |            1.9 |         1388.3 |
| daqp     |      70.1 |             2.7 |            3.0 |            3.0 |
| ecos     |     107.3 |      50707211.4 |           60.5 |        55970.8 |
| highs    |      17.4 |     217896172.2 |          877.3 |       240553.0 |
| osqp     |       9.1 |             7.6 |           37.6 |            9.4 |
| piqp     |      34.8 |             3.5 |            1.5 |            2.5 |
| proxqp   |      38.6 |             5.0 |            4.4 |            4.4 |
| qpalm    |       1.0 |             3.5 |           42.8 |            5.3 |
| qpoases  |      70.1 |             2.7 |        10086.5 |            2.5 |
| quadprog |      23.2 |             1.0 |            1.0 |            1.0 |
| scs      |      25.0 |             2.2 |            3.6 |            3.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
