from Tesla_Coil_Code.Tesla_Coil.TeslaCoil import Tesla_Coil_Solver
from Tesla_Coil_Code.Steady_State.Input_Wrapper import input_wrapper
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,100,1000)
pars = input_wrapper()
q = Tesla_Coil_Solver(t, pars)
plt.plot(t,q)
plt.savefig("./testgraph.jpg")
