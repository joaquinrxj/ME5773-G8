FC = ifort

all: f2py

f2py: searchutils.f90
	# This comand runs f2py to compile a fortran function/subroutine into a python module.
	# -L, -l, -I flags used as in compiler commands.
	
	python -m numpy.f2py -c searchutils.f90 -m searchUtilsTeam08 --fcompiler=intel