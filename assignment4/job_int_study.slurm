#!/bin/bash
#
# ======================================================================
# This file executes a run time analysis of a lintegral.py code
# 
#   sbatch job_integral.slurmm
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
# Last modification date: 02/17/2024
# Version: 0.1
# ======================================================================
#
#
# The following commands specify SLURM configuration:
# more information can be found on 
# https://slurm.schedmd.com/sbatch.html
#
#SBATCH -J Time
#SBATCH -o outFileIntegral.out # Name of 'stdout' output file.
#SBATCH -e errFileIntegral.err # Name of 'stderr' error file.
#SBATCH -p compute1            # Partition
#SBATCH -N 1                   # Total number of nodes to be requested.
#SBATCH -n 1                   # Total number of tasks to be requested.
#SBATCH -c 80                  # Number of threads used by each task.
#SBATCH -t 00:30:00            # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL        # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user juancamilo.velasquezgonzalez@my.utsa.edu # Put your utsa-email here.
#SBATCH --mail-user joaquin.rodriguez@my.utsa.edu # Put your utsa-email here.
#

# Print start time stamp
tstart=`date +%s%N` 
echo Starting job - `date`

# Load Requiered Modules
ml anaconda3

# Activate Anaconda Environments
conda activate envTeam8

# Running the jobs with different OMP_NUM_THREADS Values

for num_threads in 1 2 4 8; do
    echo "--------------------------------"

	export OMP_NUM_THREADS=$num_threads

	# Print the Number of Threads on Each Run
    echo "Execution with OMP_NUM_THREADS=$num_threads"

    # Execute the Python script
    python3 integral.py
    echo "Executing Python Script"

done
echo "All executions complete"
echo "--------------------------------"

# Print end time stamp
tend=`date +%s%N`

# Calculate the difference in end and start times
tdiff=$(( (tend-tstart)/1000000 ))

# Output calculation time.
echo "Calculations ended"
echo "Total CPU time $tdiff [ms]"