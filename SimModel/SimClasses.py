import sys
import SimPy.RandomVariantGenerators as RVGs
import SimPy.InOutFunctions as IO
import SimPy.StatisticalClasses as Stat
import multiprocessing as mp



class OneSim:
    def __init__(self, seed):
        self.rng = RVGs.RNG(seed=seed)
        self.beta = RVGs.Beta(a=1, b=2)
        self.sum = 0
        self.seed = seed

    def simulate(self, n_steps):
        self.sum = 0
        for i in range(n_steps):
            self.sum += self.rng.random_sample() + self.beta.sample(rng=self.rng)

    def export_results(self, directory):
        rows = [[self.seed, self.sum]]
        name = 'Seed ' + str(self.seed) + ".csv"
        IO.write_csv(rows=rows, file_name=name, directory=directory)


class ParallelMultiSim:
    def __init__(self, num_simulations):

        self.models = []
        for seed in range(num_simulations):
            self.models.append(OneSim(seed=seed))

    def simulate(self, n_steps):

        max_processes = mp.cpu_count()  # maximum number of processors

        # create a list of arguments for simulating the cohorts in parallel
        args = [(model, n_steps) for model in self.models]

        # simulate all cohorts in parallel
        with mp.Pool(max_processes) as pl:
            pl.starmap(simulate_this_model, args)


def simulate_this_model(model, n_steps):

    # simulate and return the cohort
    model.simulate(n_steps)
    model.export_results(directory='ResultsParallel')
    return model
