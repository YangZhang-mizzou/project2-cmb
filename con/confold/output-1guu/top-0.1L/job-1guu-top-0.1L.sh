#!/bin/bash -l
#SBATCH -J 1guu-0.1L
#SBATCH -o 1guu-0.1L.log
#SBATCH -p Bonus,Lewis
#SBATCH -n 1
#SBATCH --mem 2G
#SBATCH -t 2-00:00
mv /Users/zhangyang/Desktop/project2/con/confold/output-1guu/top-0.1L.queued /Users/zhangyang/Desktop/project2/con/confold/output-1guu/top-0.1L.running
/Users/zhangyang/Desktop/project2/con/confold/core.pl -asymptote 0 -rswitch 1.8 -mcount 20 -rr /Users/zhangyang/Desktop/project2/con/confold/dry-run/input/1guu.rr -ss /Users/zhangyang/Desktop/project2/con/confold/dry-run/input/1guu.ss -selectrr 0.1L -o ./
rm /Users/zhangyang/Desktop/project2/con/confold/output-1guu/top-0.1L.running
