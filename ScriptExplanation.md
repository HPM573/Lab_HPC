`#!/bin/bash` -> indicator that this file is a bash script 

`#SBATCH -C avx2` -> gets you the newer nodes on the cluster to avoid errors
`#SBATCH --job-name=SimPyRun` -> name of the job
`#SBATCH --time=00:30` -> time limit to run the script 
`#SBATCH -n 15` -> number of tasks

`module load Python` -> loads python 
`module load parallel` -> loads GNU parallel

`NUM_TASKS=${SLURM_NTASKS}` -> total number of cores requested in a job that will be from the `SBATCH -n 15` line 

`SRUN="srun --export=all -n1 -N1  --exclusive"` -> srun command to run the file 
`MODEL_PATH="SimModel/RunSimOnCluster.py"` -> file you are running
`MODEL="python $MODEL_PATH z"` -> runs the file on python and adds the z flag for parallel command 

`PARALLEL_OPTS="-Iz -j$NUM_TASKS"` -> options for parallel to pipe in seq

`time seq 15 | parallel $PARALLEL_OPTS $SRUN $MODEL >> file.csv` -> runs the whole thing on parallel with sequence and times it 
