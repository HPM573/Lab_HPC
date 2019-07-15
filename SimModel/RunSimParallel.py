import SimModel.SimClasses as PP
import time

N_STEPS = 10000
N_RUNS = 100

if __name__ == '__main__':  # this line is needed to avoid errors that occur on Windows computers

    t0 = time.time()

    parallelModel = PP.ParallelMultiSim(num_simulations=N_RUNS)
    parallelModel.simulate(n_steps=N_STEPS)

    t1 = time.time()

    print('Time = {0}'.format(t1-t0))
