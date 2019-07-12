# Steps 
1. git clone this directory 
2. go back to your home directory in your cluster and also git clone the SimPy model 
3. `cd updated_Lab_HPC/PyUsingSimPy` then `vim SimClasses2.py`
  press i to make corrections and change `sys.path.insert(0, '/home/yjj2/Lab_HPC/PyUsingSimPy/SimPy/SimPy')` to `sys.path.insert(0, '/home/yjj2/SimPy/SimPy')`
4. press esc then `:wq`
5. `cd ..`
6. `sbatch SimPy_Run.sh` to run it on multiple nodes 
7. `sbatch oneNode_Run.sh` to run it on one node
8. "file.csv" will be the output for SimPy_Run.sh and "node.csv" is the output for Serial_Run.sh
9. There will be some kind of slurm.out file after you run sbatch. `cat <output file name>` to see the time it took to run the script

# python 3
1. `module load Python/3.6.2-foss-2017b` on sbatch script

# Corrections 
- CSV outputs 
