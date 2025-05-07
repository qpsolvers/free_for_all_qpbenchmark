# Free-for-all dense subset

| Number of problems | 22 |
|:-------------------|:--------------------|
| Benchmark version  | 2.4.0 |
| Date               | 2025-05-07 18:13:31.503468+00:00 |
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
| daqp     | 0.6.0                 |
| ecos     | 2.0.14                |
| gurobi   | 12.0.2 (size-limited) |
| highs    | 1.10.0                |
| osqp     | 0.6.7.post3           |
| piqp     | 0.4.2                 |
| proxqp   | 0.7.2                 |
| qpalm    | 1.2.5                 |
| quadprog | 0.1.13                |
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
| daqp     | ``dual_tol``                     | -         |           1e-09 |          0.001 |          1e-06 |
| daqp     | ``primal_tol``                   | -         |           1e-09 |          0.001 |          1e-06 |
| ecos     | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
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
| clarabel    |                                90.9 |                                 88.7 |                                       945.3 |                                    78.1 |                                23.2 |
| cvxopt      |                                72.7 |                                283.3 |                                      2860.5 |                                   236.4 |                                70.2 |
| daqp        |                                72.7 |                                283.2 |                                      2860.5 |                                   236.4 |                                70.1 |
| ecos        |                                54.5 |                                504.2 |                                      4809.3 |                                   397.6 |                               119.5 |
| gurobi      |                                77.3 |                                232.7 |                                      2378.6 |                                   198.9 |                                58.3 |
| highs       |                                86.4 |                                 54.7 |                                       471.6 |                                 24112.8 |                                17.4 |
| jaxopt_osqp |                                71.4 |                                413.7 |                                      2999.8 |                                   248.0 |                                73.9 |
| kvxopt      |                                71.4 |                                298.2 |                                      2998.6 |                                   247.8 |                                73.5 |
| osqp        |                                90.9 |                                  1.4 |                                         9.9 |                                  2369.7 |                                 9.1 |
| piqp        |                                86.4 |                                135.7 |                                      1421.0 |                                   117.4 |                                34.8 |
| proxqp      |                                90.9 |                                 45.4 |                                       471.6 |                                    39.0 |                                38.6 |
| qpalm       |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| qpax        |                                71.4 |                                252.1 |                                      1990.1 |                                 11087.9 |                               324.8 |
| qpswift     |                                28.6 |                                871.9 |                                      7652.5 |                                   632.4 |                               187.6 |
| quadprog    |                                72.7 |                                283.2 |                                      2860.5 |                                   236.4 |                                70.1 |
| scs         |                                90.9 |                                 89.5 |                                       946.3 |                                    80.6 |                                25.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                90.9 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.2 |
| cvxopt      |                                22.7 |                                  3.2 |                                         3.0 |                                     3.0 |                            580138.4 |
| daqp        |                                72.7 |                                  3.2 |                                         3.0 |                                     3.0 |                                 1.3 |
| ecos        |                                 0.0 |                                  5.7 |                                         5.0 |                               2097131.1 |                          25956689.0 |
| gurobi      |                                36.4 |                                  2.6 |                                         2.6 |                              28349573.1 |                              2389.6 |
| highs       |                                 0.0 |                                  2.1 |                                         2.0 |                          291755195729.1 |                         100296257.6 |
| jaxopt_osqp |                                 9.5 |                                 12.7 |                                        14.7 |                                     9.4 |                                 6.1 |
| kvxopt      |                                19.0 |                                  3.4 |                                         3.1 |                                     3.1 |                            607764.3 |
| osqp        |                                50.0 |                                  3.8 |                                         3.6 |                                     5.1 |                                 3.5 |
| piqp        |                                77.3 |                                  2.6 |                                         2.5 |                                     2.8 |                                 1.6 |
| proxqp      |                                86.4 |                                  1.6 |                                         4.7 |                                     1.5 |                                 2.3 |
| qpalm       |                                81.8 |                                  1.5 |                                         2.7 |                                     1.6 |                                 1.4 |
| qpax        |                                 9.5 |                                  9.8 |                                        27.0 |                          130566113626.2 |                        4683404709.5 |
| qpswift     |                                 4.8 |                                  9.8 |                                         7.9 |                                     8.3 |                                21.5 |
| quadprog    |                                72.7 |                                  3.2 |                                         3.0 |                                     3.0 |                                 1.3 |
| scs         |                                90.9 |                                  1.0 |                                         2.8 |                                     1.5 |                                 1.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                90.9 |                                 46.9 |                                5686130971.1 |                                     2.0 |                                 2.8 |
| cvxopt      |                                68.2 |                                149.8 |                               17058469202.3 |                                     6.0 |                                 2.9 |
| daqp        |                                72.7 |                                149.7 |                               18696218364.7 |                                     6.0 |                                 2.0 |
| ecos        |                                40.9 |                                266.5 |                               28431040463.2 |                                    14.2 |                                44.6 |
| gurobi      |                                72.7 |                                122.9 |                               14215359467.4 |                                    61.9 |                                 1.7 |
| highs       |                                68.2 |                                  5.3 |                                         1.0 |                                585390.8 |                               583.4 |
| jaxopt_osqp |                                33.3 |                                210.5 |                               24483925716.1 |                                    11.2 |                                13.8 |
| kvxopt      |                                66.7 |                                157.6 |                               17870788863.7 |                                     6.3 |                                 3.1 |
| osqp        |                                72.7 |                                  9.7 |                               13174356162.9 |                                     7.6 |                                25.0 |
| piqp        |                               100.0 |                                  1.0 |                                1434487185.9 |                                     1.0 |                                 1.0 |
| proxqp      |                                95.5 |                                 23.9 |                               22999425614.6 |                                     1.1 |                                 3.3 |
| qpalm       |                                72.7 |                                 23.1 |                               15400347160.6 |                                     2.5 |                                28.8 |
| qpax        |                                66.7 |                                118.2 |                               12509905567.7 |                                261983.4 |                              7448.8 |
| qpswift     |                                28.6 |                                460.9 |                               44677929493.3 |                                    15.7 |                                 5.2 |
| quadprog    |                                72.7 |                                149.7 |                               17058469202.3 |                                     6.0 |                                 2.0 |
| scs         |                                90.9 |                                 46.9 |                               11346944409.7 |                                     3.2 |                                 2.4 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                90.9 |                                  1.7 |                                         2.0 |                                     1.0 |                                 1.0 |
| cvxopt      |                                45.5 |                                  5.3 |                                         5.9 |                                     3.0 |                               542.0 |
| daqp        |                                72.7 |                                  5.3 |                                         5.9 |                                     3.0 |                                 1.2 |
| ecos        |                                 4.5 |                                  9.4 |                                         9.8 |                                  2115.1 |                             24202.0 |
| gurobi      |                                68.2 |                                  4.3 |                                         4.9 |                                 28528.1 |                                 3.2 |
| highs       |                                18.2 |                                  1.0 |                                         1.0 |                             293567158.6 |                             93823.0 |
| jaxopt_osqp |                                28.6 |                                 12.4 |                                        14.8 |                                     7.6 |                                 4.8 |
| kvxopt      |                                42.9 |                                  5.6 |                                         6.2 |                                     3.1 |                               567.9 |
| osqp        |                                63.6 |                                  4.3 |                                         6.1 |                                     3.9 |                                 3.7 |
| piqp        |                                90.9 |                                  1.7 |                                         2.1 |                                     2.5 |                                 1.0 |
| proxqp      |                                90.9 |                                  1.7 |                                         7.3 |                                     1.1 |                                 1.7 |
| qpalm       |                                86.4 |                                  1.7 |                                         4.0 |                                     1.6 |                                 2.5 |
| qpax        |                                19.0 |                                 11.4 |                                       287.2 |                             131377040.9 |                           4366466.4 |
| qpswift     |                                 4.8 |                                 16.3 |                                        15.5 |                                     8.3 |                                11.6 |
| quadprog    |                                72.7 |                                  5.3 |                                         5.9 |                                     3.0 |                                 1.2 |
| scs         |                                90.9 |                                  1.7 |                                         5.0 |                                     1.3 |                                 1.1 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |        91 |              91 |             91 |             91 |
| cvxopt      |        73 |              23 |             68 |             45 |
| daqp        |        73 |              73 |             73 |             73 |
| ecos        |        55 |               0 |             41 |              5 |
| gurobi      |        77 |              36 |             73 |             68 |
| highs       |        86 |               0 |             68 |             18 |
| jaxopt_osqp |        71 |              10 |             33 |             29 |
| kvxopt      |        71 |              19 |             67 |             43 |
| osqp        |        91 |              50 |             73 |             64 |
| piqp        |        86 |              77 |            100 |             91 |
| proxqp      |        91 |              86 |             95 |             91 |
| qpalm       |       100 |              82 |             73 |             86 |
| qpax        |        71 |              10 |             67 |             19 |
| qpswift     |        29 |               5 |             29 |              5 |
| quadprog    |        73 |              73 |             73 |             73 |
| scs         |        91 |              91 |             91 |             91 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |              50 |             95 |             73 |
| daqp        |       100 |             100 |            100 |            100 |
| ecos        |       100 |              45 |             86 |             50 |
| gurobi      |       100 |              59 |             95 |             91 |
| highs       |        91 |              18 |             68 |             23 |
| jaxopt_osqp |       100 |              95 |             62 |             81 |
| kvxopt      |       100 |              48 |             95 |             71 |
| osqp        |        91 |              82 |             73 |             86 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |        95 |             100 |            100 |            100 |
| qpalm       |       100 |              95 |             77 |             95 |
| qpax        |        90 |              81 |             86 |             71 |
| qpswift     |       100 |              76 |            100 |             76 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |      88.7 |             1.0 |           46.9 |            1.7 |
| cvxopt      |     283.3 |             3.2 |          149.8 |            5.3 |
| daqp        |     283.2 |             3.2 |          149.7 |            5.3 |
| ecos        |     504.2 |             5.7 |          266.5 |            9.4 |
| gurobi      |     232.7 |             2.6 |          122.9 |            4.3 |
| highs       |      54.7 |             2.1 |            5.3 |            1.0 |
| jaxopt_osqp |     413.7 |            12.7 |          210.5 |           12.4 |
| kvxopt      |     298.2 |             3.4 |          157.6 |            5.6 |
| osqp        |       1.4 |             3.8 |            9.7 |            4.3 |
| piqp        |     135.7 |             2.6 |            1.0 |            1.7 |
| proxqp      |      45.4 |             1.6 |           23.9 |            1.7 |
| qpalm       |       1.0 |             1.5 |           23.1 |            1.7 |
| qpax        |     252.1 |             9.8 |          118.2 |           11.4 |
| qpswift     |     871.9 |             9.8 |          460.9 |           16.3 |
| quadprog    |     283.2 |             3.2 |          149.7 |            5.3 |
| scs         |      89.5 |             1.0 |           46.9 |            1.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |     945.3 |             1.0 |   5686130971.1 |            2.0 |
| cvxopt      |    2860.5 |             3.0 |  17058469202.3 |            5.9 |
| daqp        |    2860.5 |             3.0 |  18696218364.7 |            5.9 |
| ecos        |    4809.3 |             5.0 |  28431040463.2 |            9.8 |
| gurobi      |    2378.6 |             2.6 |  14215359467.4 |            4.9 |
| highs       |     471.6 |             2.0 |            1.0 |            1.0 |
| jaxopt_osqp |    2999.8 |            14.7 |  24483925716.1 |           14.8 |
| kvxopt      |    2998.6 |             3.1 |  17870788863.7 |            6.2 |
| osqp        |       9.9 |             3.6 |  13174356162.9 |            6.1 |
| piqp        |    1421.0 |             2.5 |   1434487185.9 |            2.1 |
| proxqp      |     471.6 |             4.7 |  22999425614.6 |            7.3 |
| qpalm       |       1.0 |             2.7 |  15400347160.6 |            4.0 |
| qpax        |    1990.1 |            27.0 |  12509905567.7 |          287.2 |
| qpswift     |    7652.5 |             7.9 |  44677929493.3 |           15.5 |
| quadprog    |    2860.5 |             3.0 |  17058469202.3 |            5.9 |
| scs         |     946.3 |             2.8 |  11346944409.7 |            5.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |      78.1 |             1.0 |            2.0 |            1.0 |
| cvxopt      |     236.4 |             3.0 |            6.0 |            3.0 |
| daqp        |     236.4 |             3.0 |            6.0 |            3.0 |
| ecos        |     397.6 |       2097131.1 |           14.2 |         2115.1 |
| gurobi      |     198.9 |      28349573.1 |           61.9 |        28528.1 |
| highs       |   24112.8 |  291755195729.1 |       585390.8 |    293567158.6 |
| jaxopt_osqp |     248.0 |             9.4 |           11.2 |            7.6 |
| kvxopt      |     247.8 |             3.1 |            6.3 |            3.1 |
| osqp        |    2369.7 |             5.1 |            7.6 |            3.9 |
| piqp        |     117.4 |             2.8 |            1.0 |            2.5 |
| proxqp      |      39.0 |             1.5 |            1.1 |            1.1 |
| qpalm       |       1.0 |             1.6 |            2.5 |            1.6 |
| qpax        |   11087.9 |  130566113626.2 |       261983.4 |    131377040.9 |
| qpswift     |     632.4 |             8.3 |           15.7 |            8.3 |
| quadprog    |     236.4 |             3.0 |            6.0 |            3.0 |
| scs         |      80.6 |             1.5 |            3.2 |            1.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |      23.2 |             1.2 |            2.8 |            1.0 |
| cvxopt      |      70.2 |        580138.4 |            2.9 |          542.0 |
| daqp        |      70.1 |             1.3 |            2.0 |            1.2 |
| ecos        |     119.5 |      25956689.0 |           44.6 |        24202.0 |
| gurobi      |      58.3 |          2389.6 |            1.7 |            3.2 |
| highs       |      17.4 |     100296257.6 |          583.4 |        93823.0 |
| jaxopt_osqp |      73.9 |             6.1 |           13.8 |            4.8 |
| kvxopt      |      73.5 |        607764.3 |            3.1 |          567.9 |
| osqp        |       9.1 |             3.5 |           25.0 |            3.7 |
| piqp        |      34.8 |             1.6 |            1.0 |            1.0 |
| proxqp      |      38.6 |             2.3 |            3.3 |            1.7 |
| qpalm       |       1.0 |             1.4 |           28.8 |            2.5 |
| qpax        |     324.8 |    4683404709.5 |         7448.8 |      4366466.4 |
| qpswift     |     187.6 |            21.5 |            5.2 |           11.6 |
| quadprog    |      70.1 |             1.3 |            2.0 |            1.2 |
| scs         |      25.0 |             1.0 |            2.4 |            1.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
