import SimClasses2 as PP
import sys

# python simulation
seed = 1
ppModel = PP.OneSim(seed=seed)
ppModel.simulate(n_steps=1000)
print(seed)
print(ppModel.sum)
