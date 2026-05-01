from Tesla_Coil_Code.TeslaCoil import Tesla_Coil_Solver
from Tesla_Coil_Code.Input_Wrapper import input_wrapper
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,10,10000)
pars = input_wrapper()
q = Tesla_Coil_Solver(t, pars)
plt.plot(t,q[:,0])
plt.savefig("testgraph.jpg")
