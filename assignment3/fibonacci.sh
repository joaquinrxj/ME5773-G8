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
# Last modification date: 02/08/2024
# Version: 0.1
# ====================================================================== 
echo The N-Number is: $1
echo The K-Term is: $2

N=$1
K=$2


declare -a Array

# Base cases
if (( N <= K )); then
    echo "1"
    
fi

# Fill the array with 1s for the first K elements
for (( i=0; i<K; i++ )); do
    Array[$i]=1
done

# Set the (K+1)th element to K, as the sum of the first K elements (which are all 1)
Array[$K]=$K
sum=$K

# Start calculating from (K+2)th element to Nth
for (( i=K+1; i<N; i++ )); do
    # Update sum: add the last element, subtract the element at (i-K-1)
    sum=$((sum + Array[i-1] - Array[i-K-1]))
    Array[$i]=$sum
done

# Output the Nth element
echo "${Array[N-1]}"

#declare -a Array
#
#for (( i = 0; i <= N; i++ )); do
#    Array[i]=0
#done
#
## If N is less than or equal to K, then the element is '1    
#if (( N <= K )); then
#    echo -n "1",
#    return
#fi
#
#sm=$K
#
#
#for (( i = 1; i <= K; i++ )); do
#    Array[i]=1
#    echo -n "${Array[i]}",
#done
#
#Array[i+1]=$sm
#
#echo -n ${Array[i+1]},
#
#
#for (( i = K + 2; i <= N; i++ )); do
#    # Subtract the element at index i-K-1 and add the element at index i-1 from the sum
#    # (sum contains the sum of previous 'K' elements)
#    Array[i]=$((sm - Array[i-K-1] + Array[i-1]))
#    echo -n ${Array[i]},
#
#    # Set the new sum
#    sm=${Array[i]}
#done
#
#echo "${Array[N]}"
#
## This last echo is needed because all previous echo commands were
## executed with the -n flag, so no new line would be executed.
#echo 


