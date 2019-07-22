#!/bin/bash

#SBATCH -C avx2
#SBATCH --job-name=oneNode
#SBATCH --time=00:30
module load Python
module load parallel

NUM_TASKS=${SLURM_NTASKS}

SRUN="srun --export=all -n1 --exclusive"
MODEL_PATH="SimModel/RunSimOnCluster.py"
MODEL="python $MODEL_PATH z"

PARALLEL_OPTS="-Iz -j$NUM_TASKS"

time seq 70 | parallel $PARALLEL_OPTS $SRUN $MODEL >> node.csv
