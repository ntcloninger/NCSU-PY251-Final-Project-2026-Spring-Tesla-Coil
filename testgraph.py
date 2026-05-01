from Tesla_Coil_Code.TeslaCoil import Tesla_Coil_Solver
from Tesla_Coil_Code.Input_Wrapper import input_wrapper
import numpy as np
import matplotlib.pyplot as plt
pars = input_wrapper()
t = np.linspace(0,pars[11],10000)
q1, q2 = Tesla_Coil_Solver(t, pars)
plt.plot(t,(pars[1])*q1[:,3])
plt.savefig("testgraph.jpg")
