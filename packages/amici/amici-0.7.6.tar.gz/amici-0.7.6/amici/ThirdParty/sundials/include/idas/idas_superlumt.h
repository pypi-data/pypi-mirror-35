/*
 * -----------------------------------------------------------------
 * $Revision: 4491 $
 * $Date: 2015-04-30 16:56:10 -0700 (Thu, 30 Apr 2015) $
 * ----------------------------------------------------------------- 
 * Programmer(s): Carol S. Woodward @ LLNL
 * -----------------------------------------------------------------
 * LLNS Copyright Start
 * Copyright (c) 2014, Lawrence Livermore National Security
 * This work was performed under the auspices of the U.S. Department 
 * of Energy by Lawrence Livermore National Laboratory in part under 
 * Contract W-7405-Eng-48 and in part under Contract DE-AC52-07NA27344.
 * Produced at the Lawrence Livermore National Laboratory.
 * All rights reserved.
 * For details, see the LICENSE file.
 * LLNS Copyright End
 * -----------------------------------------------------------------
 * This is the header file for the IDASuperLUMT linear solver module.
 * -----------------------------------------------------------------
 */

#ifndef _IDASSUPERLUMT_H
#define _IDASSUPERLUMT_H

#include "idas/idas_sparse.h"
#include "sundials/sundials_sparse.h"

#ifdef __cplusplus  /* wrapper to enable C++ usage */
extern "C" {
#endif
/*
 * -----------------------------------------------------------------
 * Function : IDASuperLUMT
 * -----------------------------------------------------------------
 * A call to the IDASuperLUMT function links the main integrator      
 * with the IDASuperLUMT linear solver module.                        
 *                                                                
 * ida_mem is the pointer to integrator memory returned by        
 *     IDACreate.             
 *
 * num_threads is the number of threads that SuperLUMT should invoke     
 *                                                                
 * IDASuperLUMT returns:                                              
 *     IDASLU_SUCCESS   = 0  if successful                              
 *     IDASLU_LMEM_FAIL = -1 if there was a memory allocation failure   
 *     IDASLU_ILL_INPUT = -2 if NVECTOR found incompatible           
 *                                                                
 * NOTE: The SuperLUMT linear solver assumes a serial implementation  
 *       of the NVECTOR package. Therefore, IDASuperLUMT will first
 *       test for a compatible N_Vector internal representation
 *       by checking that the functions N_VGetArrayPointer and
 *       N_VSetArrayPointer exist.
 * -----------------------------------------------------------------
 */

  SUNDIALS_EXPORT int IDASuperLUMT(void *ida_mem, int num_threads, 
				   int n, int nnz); 

/* 
 * -----------------------------------------------------------------
 * Optional Input Specification Functions
 * -----------------------------------------------------------------
 *
 * IDASuperLUMTSetOrdering sets the ordering used by SuperLUMT for 
 * reducing fill.
 * Options are: 
 * 0 for natural ordering
 * 1 for minimal degree ordering on A'*A
 * 2 for minimal degree ordering on A'+A
 * 3 for approximate minimal degree ordering for unsymmetric matrices
 * The default used in SUNDIALS is 3 for COLAMD.
 * -----------------------------------------------------------------
 */

  SUNDIALS_EXPORT int IDASuperLUMTSetOrdering(void *ida_mem, 
					      int ordering_choice); 



/*
 * -----------------------------------------------------------------
 * Function: IDASuperLUMTB
 * -----------------------------------------------------------------
 * IDASuperLUMTB links the main IDAS integrator with the IDASuperLUMT
 * linear solver for the backward integration.
 * The 'which' argument is the int returned by IDACreateB.
 * -----------------------------------------------------------------
 */

  SUNDIALS_EXPORT int IDASuperLUMTB(void *ida_mem, int which, int num_threads, 
				    int nB, int nnzB);


/*
 * -----------------------------------------------------------------
 * Function: IDASuperLUMTSetOrderingB
 * -----------------------------------------------------------------
 * IDASuperLUMTSetOrderingB pulls off the memory block associated with the which parameter
 * and sets the ordering for the KLU solver associated with that memory block.
 * The 'which' argument is the int returned by IDACreateB.
 * -----------------------------------------------------------------
 */
  SUNDIALS_EXPORT int IDASuperLUMTSetOrderingB(void *ida_mem, int which, 
					      int ordering_choiceB); 


  
#ifdef __cplusplus
}
#endif

#endif
