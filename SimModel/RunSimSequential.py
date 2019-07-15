import SimModel.SimClasses as PP
import time

N_STEPS = 10000
N_RUNS = 100

t0 = time.time()

for seed in range(N_RUNS):
    model = PP.OneSim(seed=seed)
    model.simulate(n_steps=N_STEPS)
    model.export_results(directory='ResultsSequential')

t1 = time.time()

print('Time = {0}'.format(t1-t0))
