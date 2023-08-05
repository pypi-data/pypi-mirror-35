/* File: findgroups.h */
/*
  This file is a part of the Corrfunc package
  Copyright (C) 2015-- Manodeep Sinha (manodeep@gmail.com)
  License: MIT LICENSE. See LICENSE file under the top-level
  directory at https://github.com/manodeep/Corrfunc/
*/

#pragma once


#ifdef __cplusplus
extern "C" {
#endif

#include "defs.h"
#include <stdint.h>
    
    //define the results structure
    typedef struct{
        int64_t ngroups;/* total number of groups*/
        int64_t *npart_in_groups;/* number of particles in each group */
        uint64_t *partids;/* all particle ids present across all groups */
    } results_findgroups;
    
    extern int findgroups(const int64_t ND1, void * restrict X1, void * restrict Y1, void * restrict Z1,
                          const double boxsize,
                          const double linkx, const double linky, const double linkz, 
                          const int numthreads,
                          results_findgroups *result,
                          struct config_options *options,
                          struct extra_options *extra) __attribute__((warn_unused_result));

    extern void free_results_findgroups(results_findgroups *results);

#ifdef __cplusplus
}
#endif
