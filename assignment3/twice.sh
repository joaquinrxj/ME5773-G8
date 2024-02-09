# ======================================================================
# This file provides a simple example of a bash script that:
#   - Given an input <N>, the execution sleeps for <2N> seconds. 
#   - After sleeping, it outputs "Terminated a task <2N> seconds."
#   - 
# 
# To run this file on a linux machine, use the following command line:
#
#   bash simple1.sh
#
# DISCLAIMER: 
#   This file was created for educational purposes to be used in the
#   ME 5773 High Performance Computing course at the University of Texas 
#   at San Antonio within the Arc HPC cluster. 
#   Use it at your own risk.
# 
#
# Authors: Joaquin Rodriguez
#	   Juan Camilo Velasquez
#
# Last modification date: 02/06/2024
# Version: 0.1
# ====================================================================== 

echo "Hello $USER! You are successfully running a bash script file"

# print in console the start date.
N=$1
N=$((N * 2))



# A simple process to stop processing for N seconds
sleep ${N}

echo Terminated a task that takes ${N} seconds


