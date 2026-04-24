import numpy as np
from scipy.integrate import odeint

def Tesla_Coil_Solver(t, pars): #take in initial value and parameters

    class Tesla_Coil:
        def __init__(self, pars):
            self.L1 = pars[0]
            self.L2 = pars[1]
            self.L3 = pars[2]
            self.L4 = pars[3]

            self.R1 = pars[4]
            self.R2 = pars[5]
            self.R3 = pars[6]
            self.Rsparky = pars[7]

            self.C1 = pars[8]
            self.C2 = pars[9]
            self.C3 = pars[10]

            self.AC_amplitude = pars[11]
            self.AC_frequency = pars[12]

            self.sparky_distance = pars[13]

            self.k1 = pars[14]
            self.k2 = pars[15]
            self.M1 = self.k1*np.sqrt(self.L1*self.L2)
            self.M2 = self.k2*np.sqrt(self.L3*self.L4)
        
            #for air
            A = 0112.5
            B = 2737.5
            p = 101325 #pascals
            gamma_se = 0.5 #Half of atoms give of another electron
            self.Breakdown_Voltage = (B*p*self.sparky_distance)/(np.log(A*p*self.sparky_distance) - np.log(np.log(1 + 1/gamma_se)))#pashen cure function
            self.q_initial = [0,0,0,0,0,0,0,0,0]
            self.q_steady_state = [0,0,0,0,0,0,0,0,0]
            #q[i-1][derivative]

        def f(self,t):
            return self.AC_amplitude*np.sin(self.AC_frequency*t)
        
        def df(self,t):
            return self.AC_frequency*self.AC_amplitude*np.cos(self.AC_frequency*t)

        def deriv(self, q,t):#organizes derivative equations with given initial


            if (self.L2*q[5] - self.M1*q[2]) < self.Breakdown_Voltage:
                dq2_2_temp = ((self.M2/self.L4)*(self.R3*q[8] + q[7]/self.C3 - self.R2*q[5] + q[4]/self.C2\
                           - (self.M1/self.L1)*(self.df(t) + q[1]/self.C1) + self.R1*q[2]))\
                           /(self.L3-self.L2 + (self.k1**2)*self.L2 - (self.k2**2)*self.L3)
                dq1_2_temp = (self.df(t) - q[1]/self.C1 - self.R1*q[2] + self.M1*dq2_2_temp)/self.L1
                dq3_2_temp = (self.R3*q[8] + q[7]/self.C3 + self.M2*dq2_2_temp)/self.L4
                dq = [q[1],\
                      q[2],\
                      dq1_2_temp,\
                      q[4],\
                      q[5],\
                      dq2_2_temp,\
                      q[7],\
                      q[8],\
                      dq3_2_temp]
            else:
                dq2_2_temp = (self.L1*(self.Rsparky - self.R2)*q[5] \
                           + self.M1*(self.df(t) - q[1]/self.C2 - self.R1*q[2]))\
                           /(self.L1*self.L2 - self.M1*self.M2)
                dq1_2_temp = (self.df(t) - q[1]/self.C1 - self.R1*q[2] + self.M1*dq2_2_temp)/self.L1
                dq3_2_temp = (self.R3*q[8] + q[7]/self.C3 + self.M2*dq2_2_temp)/self.L4
                dq = [q[1],\
                      q[2],\
                      dq1_2_temp,\
                      q[4],\
                      q[5],\
                      dq2_2_temp,\
                      q[7],\
                      q[8],\
                      dq3_2_temp]
            
            return dq
        
    def diffeq_solver_from_scipy(deriv, q_initial, t): #solves diff equation
        q = odeint(deriv, q_initial, t)
        return q
    
    input_system = Tesla_Coil(pars)

    return diffeq_solver_from_scipy(input_system.deriv, input_system.q_initial, t) 