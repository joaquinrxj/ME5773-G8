#!/bin/bash
#
# ======================================================================
# Running a python file that uses multiprocessing sbatch mode.
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
# Author: Juan Camilo Velasquez, 
#         Joaquin Rodriguez
#
# Last modification date: 02/21/2024
# Version: 0.1
# ======================================================================
#
#
# The following commands specify SLURM configuration:
# more information can be found on 
# https://slurm.schedmd.com/sbatch.html
#
#SBATCH -J multProcPy
#SBATCH -o outFile.txt    # Name of 'stdout' output file.
#SBATCH -e errFile.txt    # Name of 'stderr' error file.
#SBATCH -p compute2          # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 10                 # Total number of tasks to be requested.
#SBATCH -c 8                 # Number of threads used by each task.
#SBATCH -t 10:00:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user your_@email.edu # Put your utsa-email here.
#

# Print start time stamp
tstart=`date +%s%N` 
echo Starting job - `date`


# Setup environment
module load anaconda3
source activate hpc


# Runing the python script.
python3 FE_system_group08.py


# Print end time stamp
tend=`date +%s%N`

# Calculate the difference in end and start times
tdiff=$(( (tend-tstart)/1000000 ))

# Output calculation time.
echo "Calculations ended"
echo "Total CPU time $tdiff [ms]"
