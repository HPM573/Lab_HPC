import sys
sys.path.insert(0, '/home/ry87/SimPy')
import SimClasses as PP
import sys

VAL = 0
ARR_NUM = int(sys.argv[1].split(' ')[VAL])
# python simulation
ppModel = PP.OneSim(ARR_NUM)
ppModel.simulate(n_steps=1000)
print(ARR_NUM)
print(ppModel.sum)
#ppModel.export_results()
VAL = VAL + 1

