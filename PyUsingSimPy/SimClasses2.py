import sys
sys.path.insert(0, '/home/yjj2/Lab_HPC/PyUsingSimPy/SimPy/SimPy')
import csv
import os
import RandomVariantGenerators as RVGs
import InOutFunctions as IO
import StatisticalClasses as Stat


class OneSim:
    def __init__(self, seed):
        self.rng = RVGs.RNG(seed=seed)
        self.beta = RVGs.Beta(a=1, b=2)
        self.sum = 0
        self.obs = []
	self.num = seed

    def simulate(self, n_steps):
        for i in range(n_steps):
            self.sum += self.rng.random_sample() + self.beta.sample(rng=self.rng)

        self.obs.append(self.sum)


    def export_results(self):
        rows = []
        for obs in self.obs:
            rows.append([self.obs])
	name = str(self.num) + ".csv"
        IO.write_csv(rows=rows, file_name=name, directory='Results')


class MultiSim:
    def __init__(self):
        self.obs = []

    def simulate(self, n_steps, n_iterations):

        for i in range(n_iterations):
            sim = OneSim(seed=i)
            sim.simulate(n_steps=n_steps)
            self.obs.append(sim.sum)

        stat = Stat.SummaryStat(name='', data=self.obs)

        print(stat.get_mean())

    def export_results(self):

        rows = []
        for obs in self.obs:
            rows.append([obs])

        IO.write_csv(rows=rows, file_name='results.csv', directory='Results')
