CGS2017 PSHA model (Colombia), EventBased PSHA - test -  v.1 - 2018/02/11
=========================================================================

============== ===================
checksum32     3,691,355,175      
date           2018-06-05T06:40:12
engine_version 3.2.0-git65c4735   
============== ===================

num_sites = 1, num_levels = 19

Parameters
----------
=============================== ==================
calculation_mode                'disaggregation'  
number_of_logic_tree_samples    0                 
maximum_distance                {'default': 200.0}
investigation_time              1.0               
ses_per_logic_tree_path         1                 
truncation_level                3.0               
rupture_mesh_spacing            2.0               
complex_fault_mesh_spacing      2.0               
width_of_mfd_bin                0.1               
area_source_discretization      5.0               
ground_motion_correlation_model None              
minimum_intensity               {}                
random_seed                     1024              
master_seed                     0                 
ses_seed                        42                
=============================== ==================

Input files
-----------
======================= ======================================================================================================
Name                    File                                                                                                  
======================= ======================================================================================================
gsim_logic_tree         `gmpe_lt_col_2016_pga_EB.xml <gmpe_lt_col_2016_pga_EB.xml>`_                                          
job_ini                 `job.ini <job.ini>`_                                                                                  
source                  `6.05.nrml <6.05.nrml>`_                                                                              
source                  `6.75.nrml <6.75.nrml>`_                                                                              
source_model_logic_tree `source_model_lt_col18_full_model_S_test_slab.xml <source_model_lt_col18_full_model_S_test_slab.xml>`_
======================= ======================================================================================================

Composite source model
----------------------
========= ======= ================ ================
smlt_path weight  gsim_logic_tree  num_realizations
========= ======= ================ ================
b1        1.00000 trivial(0,1,0,0) 1/1             
========= ======= ================ ================

Required parameters per tectonic region type
--------------------------------------------
====== ======================= ========== ============ ==============
grp_id gsims                   distances  siteparams   ruptparams    
====== ======================= ========== ============ ==============
0      MontalvaEtAl2016SSlab() rhypo rrup backarc vs30 hypo_depth mag
1      MontalvaEtAl2016SSlab() rhypo rrup backarc vs30 hypo_depth mag
====== ======================= ========== ============ ==============

Realizations per (TRT, GSIM)
----------------------------

::

  <RlzsAssoc(size=2, rlzs=1)
  0,MontalvaEtAl2016SSlab(): [0]
  1,MontalvaEtAl2016SSlab(): [0]>

Number of ruptures per tectonic region type
-------------------------------------------
======================================= ====== =============== ============ ============
source_model                            grp_id trt             eff_ruptures tot_ruptures
======================================= ====== =============== ============ ============
slab_buc0/6.05.nrml slab_buc1/6.75.nrml 0      Deep Seismicity 15           7           
slab_buc0/6.05.nrml slab_buc1/6.75.nrml 1      Deep Seismicity 15           8           
======================================= ====== =============== ============ ============

============= ==
#TRT models   2 
#eff_ruptures 30
#tot_ruptures 15
#tot_weight   15
============= ==

Slowest sources
---------------
========= ========================== ============ ========= ========== ========= ========= ======
source_id source_class               num_ruptures calc_time split_time num_sites num_split events
========= ========================== ============ ========= ========== ========= ========= ======
buc06pt05 NonParametricSeismicSource 7            0.00410   3.195E-05  1.00000   14        0     
buc16pt75 NonParametricSeismicSource 8            8.416E-05 1.931E-05  1.00000   16        0     
========= ========================== ============ ========= ========== ========= ========= ======

Computation times by source typology
------------------------------------
========================== ========= ======
source_class               calc_time counts
========================== ========= ======
NonParametricSeismicSource 0.00418   2     
========================== ========= ======

Duplicated sources
------------------
There are no duplicated sources

Information about the tasks
---------------------------
================== ======= ======= ======= ======= =========
operation-duration mean    stddev  min     max     num_tasks
RtreeFilter        0.00395 0.00146 0.00133 0.00814 15       
count_eff_ruptures 0.00638 NaN     0.00638 0.00638 1        
================== ======= ======= ======= ======= =========

Fastest task
------------
taskno=1, weight=15, duration=0 s, sources="buc06pt05 buc16pt75"

======== ======= ====== ======= ======= ==
variable mean    stddev min     max     n 
======== ======= ====== ======= ======= ==
nsites   1.00000 0.0    1       1       15
weight   1.00000 0.0    1.00000 1.00000 15
======== ======= ====== ======= ======= ==

Slowest task
------------
taskno=1, weight=15, duration=0 s, sources="buc06pt05 buc16pt75"

======== ======= ====== ======= ======= ==
variable mean    stddev min     max     n 
======== ======= ====== ======= ======= ==
nsites   1.00000 0.0    1       1       15
weight   1.00000 0.0    1.00000 1.00000 15
======== ======= ====== ======= ======= ==

Data transfer
-------------
================== ====================================================================== ========
task               sent                                                                   received
RtreeFilter        srcs=22.65 KB monitor=5.07 KB srcfilter=4.09 KB                        23.25 KB
count_eff_ruptures sources=15.12 KB param=561 B monitor=353 B srcfilter=233 B gsims=129 B 451 B   
================== ====================================================================== ========

Slowest operations
------------------
============================== ========= ========= ======
operation                      time_sec  memory_mb counts
============================== ========= ========= ======
PSHACalculator.run             0.35676   0.0       1     
managing sources               0.15960   0.0       1     
total prefilter                0.05928   3.60156   15    
reading composite source model 0.01058   0.0       1     
total count_eff_ruptures       0.00638   5.75781   1     
store source_info              0.00533   0.0       1     
unpickling prefilter           0.00461   0.0       15    
reading site collection        8.748E-04 0.0       1     
splitting sources              3.648E-04 0.0       1     
unpickling count_eff_ruptures  1.986E-04 0.0       1     
aggregate curves               1.941E-04 0.0       1     
saving probability maps        1.600E-04 0.0       1     
============================== ========= ========= ======