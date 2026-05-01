from Tesla_Coil_Code.TeslaCoil import Tesla_Coil_Solver
from Tesla_Coil_Code.Input_Wrapper import input_wrapper
import numpy as np
import matplotlib.pyplot as plt
pars = input_wrapper()
t = np.linspace(0,10/(pars[11]*2*np.pi),10000)
q1, q2 = Tesla_Coil_Solver(t, pars)
VA1 = (pars[0])*q1[:,2]+(pars[4])*q1[:,1]+(pars[7])*q1[:,0]
VA2 = (pars[0])*q2[:,2]+(pars[4])*q2[:,1]+(pars[7])*q2[:,0]
plt.plot(t,VA1)
plt.savefig("testgraph.jpg")
