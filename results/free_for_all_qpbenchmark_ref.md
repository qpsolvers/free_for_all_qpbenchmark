# Free-for-all test set

| Number of problems | 12 |
|:-------------------|:--------------------|
| Benchmark version  | 2.2.0 |
| Date               | 2024-01-16 19:45:01.899684+00:00 |
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
| piqp     | 0.2.4     |
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
| clarabel |                                83.3 |                                 51.7 |                                       987.9 |                                 31501.4 |                       10770558535.6 |
| cvxopt   |                                75.0 |                                 80.5 |                                      1487.8 |                                 47442.0 |                       16220343368.7 |
| daqp     |                               100.0 |                                 11.3 |                                        49.6 |                                     1.0 |                                 1.0 |
| ecos     |                                50.0 |                                140.4 |                                      2499.5 |                                511506.8 |                       27353594117.5 |
| highs    |                                66.7 |                                113.1 |                                      1991.6 |                                 71628.5 |                       24489138562.3 |
| osqp     |                                83.3 |                                  1.4 |                                         4.9 |                               1041711.6 |                        1785998434.6 |
| piqp     |                                75.0 |                                 79.8 |                                      1487.8 |                                 47447.7 |                       16220337611.9 |
| proxqp   |                                83.3 |                                 26.9 |                                       492.0 |                                 15688.6 |                       17987654842.3 |
| qpalm    |                               100.0 |                                  1.0 |                                         1.0 |                                   381.8 |                          22119372.4 |
| qpoases  |                                50.0 |                                173.5 |                                      3011.4 |                                 96025.6 |                       32831806433.2 |
| quadprog |                                83.3 |                                 53.1 |                                       987.9 |                                 31504.2 |                       10770558272.4 |
| scs      |                                83.3 |                                 52.6 |                                       988.5 |                                 31501.6 |                       10771351524.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                83.3 |                                  4.4 |                                         1.0 |                                     1.0 |                                19.4 |
| cvxopt   |                                41.7 |                                  6.8 |                                         1.5 |                                 37227.5 |                              6105.3 |
| daqp     |                                66.7 |                                  1.0 |                                        81.9 |                                 30469.5 |                                 1.0 |
| ecos     |                                 0.0 |                                 11.9 |                                         2.5 |                            1424753028.7 |                           5431893.0 |
| highs    |                                 0.0 |                                  9.6 |                                         2.0 |                             239711169.6 |                        2688771435.7 |
| osqp     |                                50.0 |                                 14.7 |                                         3.0 |                                     3.1 |                                34.0 |
| piqp     |                                58.3 |                                 12.0 |                                         2.5 |                                     2.5 |                                28.3 |
| proxqp   |                                83.3 |                                  6.2 |                                         3.7 |                                     1.0 |                                51.8 |
| qpalm    |                                83.3 |                                  4.4 |                                         2.2 |                                     1.0 |                                14.6 |
| qpoases  |                                50.0 |                                 14.7 |                                         3.0 |                                     3.0 |                                33.6 |
| quadprog |                                66.7 |                                  4.5 |                                         1.0 |                                 83321.1 |                                12.3 |
| scs      |                                75.0 |                                  9.5 |                                         2.8 |                                     1.5 |                                20.7 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                83.3 |                                 27.6 |                                1031005674.6 |                                    32.8 |                          18774569.9 |
| cvxopt   |                               100.0 |                                  5.5 |                                        14.0 |                                     2.7 |                              6097.5 |
| daqp     |                                83.3 |                                  5.9 |                             2889462570690.3 |                                     1.0 |                                 1.0 |
| ecos     |                                50.0 |                                 93.2 |                                3093054289.2 |                                   104.8 |                          34737446.0 |
| highs    |                                58.3 |                                 60.6 |                                2062019009.1 |                                  7933.1 |                        2651094957.3 |
| osqp     |                                66.7 |                                  8.0 |                                2188946694.9 |                                    78.1 |                         350106859.6 |
| piqp     |                               100.0 |                                  1.0 |                                 260099579.8 |                                    12.6 |                           4868575.4 |
| proxqp   |                                91.7 |                                 14.6 |                                3096117437.2 |                                    16.6 |                          35884457.1 |
| qpalm    |                                83.3 |                                 13.4 |                                2683073204.9 |                                    17.9 |                          39499636.3 |
| qpoases  |                                83.3 |                                  2.8 |                                         1.0 |                               3196491.1 |                      114768098134.0 |
| quadprog |                                83.3 |                                 28.6 |                                1031000913.2 |                                    35.5 |                          10961688.5 |
| scs      |                                83.3 |                                 27.8 |                                1576146005.2 |                                    45.4 |                          29802445.9 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                83.3 |                                  4.5 |                                         1.0 |                                     1.8 |                             16363.4 |
| cvxopt   |                                58.3 |                                  7.0 |                                         1.5 |                                    68.7 |                             22905.0 |
| daqp     |                                83.3 |                                  1.0 |                                     48257.6 |                                    54.0 |                                 1.0 |
| ecos     |                                 0.0 |                                 12.2 |                                         2.5 |                              22429004.4 |                          98999358.2 |
| highs    |                                41.7 |                                  9.8 |                                         2.0 |                                425202.7 |                        2688793924.9 |
| osqp     |                                66.7 |                                  9.4 |                                         2.5 |                                     3.6 |                             22502.7 |
| piqp     |                                75.0 |                                  6.9 |                                         1.5 |                                     3.4 |                             20421.9 |
| proxqp   |                                91.7 |                                  2.6 |                                         3.0 |                                     1.0 |                             45065.5 |
| qpalm    |                                83.3 |                                  4.5 |                                         2.0 |                                     2.2 |                             27031.2 |
| qpoases  |                                58.3 |                                 12.1 |                                         2.5 |                                     4.5 |                             28027.8 |
| quadprog |                                75.0 |                                  4.6 |                                         1.0 |                                   149.6 |                             11212.1 |
| scs      |                                83.3 |                                  4.7 |                                         2.5 |                                     1.8 |                             17872.5 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        83 |              83 |             83 |             83 |
| cvxopt   |        75 |              42 |            100 |             58 |
| daqp     |       100 |              67 |             83 |             83 |
| ecos     |        50 |               0 |             50 |              0 |
| highs    |        67 |               0 |             58 |             42 |
| osqp     |        83 |              50 |             67 |             67 |
| piqp     |        75 |              58 |            100 |             75 |
| proxqp   |        83 |              83 |             92 |             92 |
| qpalm    |       100 |              83 |             83 |             83 |
| qpoases  |        50 |              50 |             83 |             58 |
| quadprog |        83 |              67 |             83 |             75 |
| scs      |        83 |              75 |             83 |             83 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |             100 |            100 |            100 |
| cvxopt   |       100 |              67 |            100 |             83 |
| daqp     |       100 |              67 |             83 |             83 |
| ecos     |        92 |              42 |            100 |             42 |
| highs    |       100 |              33 |             92 |             75 |
| osqp     |        83 |             100 |             67 |            100 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |        92 |             100 |            100 |            100 |
| qpalm    |       100 |             100 |             92 |            100 |
| qpoases  |       100 |             100 |             83 |            100 |
| quadprog |       100 |              83 |            100 |             92 |
| scs      |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |      51.7 |             4.4 |           27.6 |            4.5 |
| cvxopt   |      80.5 |             6.8 |            5.5 |            7.0 |
| daqp     |      11.3 |             1.0 |            5.9 |            1.0 |
| ecos     |     140.4 |            11.9 |           93.2 |           12.2 |
| highs    |     113.1 |             9.6 |           60.6 |            9.8 |
| osqp     |       1.4 |            14.7 |            8.0 |            9.4 |
| piqp     |      79.8 |            12.0 |            1.0 |            6.9 |
| proxqp   |      26.9 |             6.2 |           14.6 |            2.6 |
| qpalm    |       1.0 |             4.4 |           13.4 |            4.5 |
| qpoases  |     173.5 |            14.7 |            2.8 |           12.1 |
| quadprog |      53.1 |             4.5 |           28.6 |            4.6 |
| scs      |      52.6 |             9.5 |           27.8 |            4.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |    low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|----------------:|---------------:|
| clarabel |     987.9 |             1.0 |    1031005674.6 |            1.0 |
| cvxopt   |    1487.8 |             1.5 |            14.0 |            1.5 |
| daqp     |      49.6 |            81.9 | 2889462570690.3 |        48257.6 |
| ecos     |    2499.5 |             2.5 |    3093054289.2 |            2.5 |
| highs    |    1991.6 |             2.0 |    2062019009.1 |            2.0 |
| osqp     |       4.9 |             3.0 |    2188946694.9 |            2.5 |
| piqp     |    1487.8 |             2.5 |     260099579.8 |            1.5 |
| proxqp   |     492.0 |             3.7 |    3096117437.2 |            3.0 |
| qpalm    |       1.0 |             2.2 |    2683073204.9 |            2.0 |
| qpoases  |    3011.4 |             3.0 |             1.0 |            2.5 |
| quadprog |     987.9 |             1.0 |    1031000913.2 |            1.0 |
| scs      |     988.5 |             2.8 |    1576146005.2 |            2.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |   31501.4 |             1.0 |           32.8 |            1.8 |
| cvxopt   |   47442.0 |         37227.5 |            2.7 |           68.7 |
| daqp     |       1.0 |         30469.5 |            1.0 |           54.0 |
| ecos     |  511506.8 |    1424753028.7 |          104.8 |     22429004.4 |
| highs    |   71628.5 |     239711169.6 |         7933.1 |       425202.7 |
| osqp     | 1041711.6 |             3.1 |           78.1 |            3.6 |
| piqp     |   47447.7 |             2.5 |           12.6 |            3.4 |
| proxqp   |   15688.6 |             1.0 |           16.6 |            1.0 |
| qpalm    |     381.8 |             1.0 |           17.9 |            2.2 |
| qpoases  |   96025.6 |             3.0 |      3196491.1 |            4.5 |
| quadprog |   31504.2 |         83321.1 |           35.5 |          149.6 |
| scs      |   31501.6 |             1.5 |           45.4 |            1.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|--------------:|----------------:|---------------:|---------------:|
| clarabel | 10770558535.6 |            19.4 |     18774569.9 |        16363.4 |
| cvxopt   | 16220343368.7 |          6105.3 |         6097.5 |        22905.0 |
| daqp     |           1.0 |             1.0 |            1.0 |            1.0 |
| ecos     | 27353594117.5 |       5431893.0 |     34737446.0 |     98999358.2 |
| highs    | 24489138562.3 |    2688771435.7 |   2651094957.3 |   2688793924.9 |
| osqp     |  1785998434.6 |            34.0 |    350106859.6 |        22502.7 |
| piqp     | 16220337611.9 |            28.3 |      4868575.4 |        20421.9 |
| proxqp   | 17987654842.3 |            51.8 |     35884457.1 |        45065.5 |
| qpalm    |    22119372.4 |            14.6 |     39499636.3 |        27031.2 |
| qpoases  | 32831806433.2 |            33.6 | 114768098134.0 |        28027.8 |
| quadprog | 10770558272.4 |            12.3 |     10961688.5 |        11212.1 |
| scs      | 10771351524.0 |            20.7 |     29802445.9 |        17872.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
