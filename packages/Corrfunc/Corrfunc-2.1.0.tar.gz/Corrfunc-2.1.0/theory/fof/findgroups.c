/* File: findgroups.c */
/*
  This file is a part of the Corrfunc package
  Copyright (C) 2015-- Manodeep Sinha (manodeep@gmail.com)
  License: MIT LICENSE. See LICENSE file under the top-level
  directory at https://github.com/manodeep/Corrfunc/
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "findgroups.h" //function proto-type for API
#include "findgroups_impl_double.h"//actual implementations for double
#include "findgroups_impl_float.h"//actual implementations for float

void free_results_findgroups(results_findgroups *results)
{
    if(results == NULL)
        return;

    free(results->npart_in_groups);
    free(results->partids);
    results->npart_in_groups = NULL;
    results->partids = NULL;
}

int findgroups(const int64_t ND1, void * restrict X1, void * restrict Y1, void * restrict Z1,
               const double boxsize,
               const double linkx, const double linky, const double linkz, 
               const int numthreads,
               results_findgroups *result,
               struct config_options *options,
               struct extra_options *extra) __attribute__((warn_unused_result))
{
    if( ! (options->float_type == sizeof(float) || options->float_type == sizeof(double))){
        fprintf(stderr,"ERROR: In %s> Can only handle doubles or floats. Got an array of size = %zu\n",
                __FUNCTION__, options->float_type);
        return EXIT_FAILURE;
    }
    
    if( strncmp(options->version, STR(VERSION), sizeof(options->version)/sizeof(char)-1 ) != 0) {
        fprintf(stderr,"Error: Do not know this API version = `%s'. Expected version = `%s'\n", options->version, STR(VERSION));
        return EXIT_FAILURE;
    }

    if(options->float_type == sizeof(float)) {
      return findgroups_float(ND, (float * restrict) X, (float * restrict) Y, (float * restrict) Z,
                              boxsize,
                              linkx, linky, linkz,
                              numthreads,
                              results,
                              options,
                              extra);
    } else {
      return findgroups_double(ND, (double * restrict) X, (double * restrict) Y, (double * restrict) Z,
                               boxsize,
                               linkx, linky, linkz,
                               numthreads,
                               results,
                               options,
                               extra);
    }
}
