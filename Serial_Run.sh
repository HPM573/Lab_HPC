#!/bin/bash

#SBATCH -C avx2
#SBATCH --job-name=SimPyRun
#SBATCH --time=00:30
#SBATCH -n 5
module load Python
module load parallel

NUM_TASKS=${SLURM_NTASKS}

SRUN="srun --export=all -n1 --exclusive"
MODEL_PATH="Lab_HPC/PyUsingSimPy/RunSim2.py"
MODEL="python $MODEL_PATH z"

PARALLEL_OPTS="-Iz -j$NUM_TASKS"

time seq 15 | parallel $PARALLEL_OPTS $SRUN $MODEL >> serial.csv
