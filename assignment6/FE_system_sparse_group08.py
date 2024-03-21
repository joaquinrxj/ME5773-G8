# =====================================================================================
# This file defines a system of Finite Element Equations for a simple spring system.
# 
# The purpose of this is to provide a base file that ME5773 students can use to apply
# the concepts of parallelization with Python's multiprocessing module.
#
# Author: Mauricio Aristizabal, PhD
# Last modified: 03/19/2024
#
# =====================================================================================

# =====================================================================================
# Required Libraries
import multiprocessing as mproc
import numpy as np
import scipy as sp # Install scipy using "conda install scipy"
import time
import os
import scipy.sparse as spr
# =====================================================================================


def assembleParallel(args):
	"""
	DESCRIPTION: Assemble an element's system matrix and rhs into a global 
	             system of equations for 1D Finite Element problem.
	             
	             This assembly function only supports linear elastic problems
	             of springs assembled in the form:
				
	        x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

	
	INPUTS:
		-e: (integer) Element index.
		-Ke: (Float array, Shape: (2,2) ) Elemental stiffness matrix.
		-fe: (Float array, Shape: (2,) )  Elemental force vector.
		-Kg: (Float array, Shape: (2,2) ) Global stiffness matrix.
		-fg: (Float array, Shape: (2,) )  Global force vector.
	
	OUTPUTS:
		Nothing, global inputs are modified.

		"""
	Ne1, Ne2, k_list, Ndof = args
	Kg_cpus=np.zeros((Ndof,Ndof))
	Kg_cpus = spr.lil_array(Kg_cpus)
	fg_cpus = np.zeros((Ndof,))

	for e in range( Ne1, Ne2):

		# Compute element stiffness matrix and load vector.
		Ke, fe = elasticElement(e,k_list)

		# Assemble the elemental values into the global components.

		for i in range(2):
			for j in range(2):
				Kg_cpus[e+i,e+j] = Kg_cpus[e+i,e+j] + Ke[i,j]
			fg_cpus[e+i] = fg_cpus[e+i] + fe[i]

	return Kg_cpus,fg_cpus
			# end for 
		# end for 

# end function


def elasticElement(e,k_list):
	"""
	DESCRIPTION: Assemble an element's system of equation into a global 
	             system of equations for 1D Finite Element problem.
	             
	             This assembly function only supports linear elastic problems
	             of springs assembled in the form:
				
	        x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x
	        
	
	INPUTS:
		-e: (integer) Element index.
		-k_list: (List of floats, len: Ne ) Element stiffness values. Ne: Number of elements.
		
	OUTPUTS:
		- Ke: Elemental stifness matrix
		- fe: Elemental force vector.

		"""

	Ke = k_list[e] * np.array([[ 1,-1],
		[-1, 1]])

	fe = np.array([0.0,
		0.0])

	return Ke,fe

# end function


def elasticFEProblem( Ndof, Ne1, Ne2, k_list,NProc ):
	"""
	DESCRIPTION: This function assembles the global stiffness matrix for a sequence 
	             of spring elements, aranged in the following manner:
				
	        x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

	INPUTS:
		-Ndof: Total number of degrees of freedom.
		-k_list: (List of floats, len: Ne ) Element stiffness values. Ne: Number of elements.
		-Ne1: Starting element to be evaluated.
        -Ne2: Final element to be evaluated.
	
	OUTPUTS:
		-Kg: (Float array, Shape: (2,2) ) Global stiffness matrix.
        -fg: (Float array, Shape: (2,) )  Global force vector.

        """
	# Create Parallel Pool

	p = mproc.Pool( processes = NProc ) # Number of processes created

	# Create the global matrix.
	Kg = np.zeros((Ndof,Ndof))
	Kg = spr.lil_array(Kg)
	fg = np.zeros((Ndof,))

	Ne = len(k_list) # Number of elements.
	Nu = Ne+1        # Number of nodes.

	Ne_div = Ne // NProc # Number of Divisions

	res=Ne % NProc


	args = []
	start_index = 0
	for i in range(NProc):
    # Calculate end index considering the remainder
		end_index = start_index + Ne_div + (1 if i < res else 0)
		args.append((start_index, end_index, k_list, Ndof))
		start_index = end_index  # Update start index

	
	output=p.map(assembleParallel,args)
	for Kg_cpus, fg_cpus in output:
		Kg +=Kg_cpus
		fg += fg_cpus

		p.close()


	return Kg, fg

# end function


if __name__ == '__main__':

	# Main process ID ()
	print( " Process ID executing the main thread {0}".format(os.getpid()))
	print(" OS cpu_count: {0}".format(os.cpu_count()))
	print(" multiprocessing cpu_count: {0}".format(mproc.cpu_count()))

	# Get number of processors from SLURM_NTASKS
	NProc = int(os.environ['SLURM_NTASKS'])
	print(' Using SLURM defined NProc = {}'.format(NProc) )



	# Total number of degrees of freedom to be generated
	Ndof = 1000
	Ne   = Ndof-1 # number of elements.

	print('Number of Degrees of freedom: {0}'.format(Ndof))
	

	# List of elemental stiffness values.
	#
	# This should be created such that each element 
	# may have a different stiffness value.

	k_list  = [1]*Ne
	
	
	t_start = time.time()
	
	# Create the global system
	Kg, fg = elasticFEProblem( Ndof, 0, Ne, k_list,NProc ) 

	t_end   = time.time()
	print(Kg)

	print('Total time to assemble:',t_end-t_start)

# end if __main__
