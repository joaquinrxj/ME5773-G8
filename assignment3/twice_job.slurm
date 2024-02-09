#!/bin/bash
#
# ======================================================================
# This file provides an example slurm job file to handle multitasking
# with heterogeneous tasks within a bash file:
#   - The program twice.sh is executed 6 times on each call
#   - They are started in 'background mode' and wait for execution.
#   - total time is measured with a nanosecond date counter.
# 
#   sbatch parallel_run.slurm
#
# DISCLAIMER: 
# This file was created for educational purposes to be used in the
# ME 5773 High Performance Computing course at the University of Texas 
# at San Antonio to be used with Arc HPC cluster. 
# Use it at your own risk.
# 
#
# Authors: Joaquin Rodriguez
#          Juan Camilo Velasquez
#
# Last modification date: 02/08/2024
# Version: 0.1
# ======================================================================
#
#
# The following commands specify SLURM configuration:
# more information can be found on 
# https://slurm.schedmd.com/sbatch.html
#
#SBATCH -J paralRun2
#SBATCH -o outFile.%j.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p amdonly           # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 4                 # Total number of tasks to be requested.
#SBATCH -c 8                 # Number of threads used by each task.
#SBATCH -t 00:05:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user juancamilo.velasquezgonzalez@my.utsa.edu # Put your utsa-email here.
#SBATCH --mail-user joaquin.rodriguez@my.utsa.edu # Put your utsa-email here.
#

# Print start time stamp
tstart=`date +%s%N` 
echo Starting job - `date`


srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 5 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 2 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 7 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 6 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 1 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK bash twice.sh 3 & 

echo Waiting for all executions to complete

wait

# Print end time stamp
tend=`date +%s%N`

# Calculate the difference in end and start times
tdiff=$(( (tend-tstart)/1000000 ))

# Output calculation time.
echo "Calculations ended"
echo "Total CPU time $tdiff [ms]"
