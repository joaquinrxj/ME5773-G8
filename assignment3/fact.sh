#!/bin/bash
#
# ======================================================================
# This file provides a simple example of a bash script that:
#   - Given an input number <N>, it outputs all factorials from 1 to N each new line. 
#   - That is, if N=4 the output should be 
#
# To run this file on a linux machine, use the command:
#
#   bash fact.sh 5
#
# -or simply execute the file (make sure you have correct permissions):
#  
#   ./fact.sh 5
#
#
# DISCLAIMER: 
#
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

echo The input Number was: $1

N=$1
fact=1


for ((i = 1; i <= N; i++)); do
    fact=$((fact * i))
    echo "$i"! = ${fact}
done

# This last echo is needed because all previous echo commands were
# executed with the -n flag, so no new line would be executed.
echo 


