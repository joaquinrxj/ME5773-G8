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

echo The input Number was: $1
echo The K-Term is: $2


declare -a Array
N=$1
K=$2

# Initialize array and base cases
declare -a Array
for (( i=0; i<K; i++ )); do
    Array[$i]=1
done

# For N less than or equal to K, simply print 1 N times and exit
if (( N <= K )); then
    for (( i=1; i<=N; i++ )); do
        echo -n "1 "
    done
    exit
fi

# Calculate sum of the first K elements
sum=$K

# Continue filling the array based on K-Fibonacci logic
for (( i=K; i<N; i++ )); do
    Array[$i]=$sum
    # Update sum for next element; add current and subtract the element (i-K) away from current
    if (( i - K >= 0 )); then
        sum=$((sum + Array[i] - Array[i-K]))
    else
        sum=$((sum + Array[i]))
    fi
done

# Print the sequence
for (( i=0; i<N; i++ )); do
    echo -n "${Array[$i]} ",
done
echo


