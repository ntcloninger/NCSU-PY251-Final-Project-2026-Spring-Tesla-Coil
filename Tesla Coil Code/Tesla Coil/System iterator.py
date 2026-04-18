import numpy as np
from scipy.integrate import odeint

def Tesla_Coil_Solver(t , s_initial, pars): #take in initial value and parameters
    def deriv(s,t):#organizes derivative equations with given initial
        sparky_distance = pars[]
        resistance  = pars[]
        #some function of temp and sparky distance for sparky resistance

        s_1 = s[] #loop 1
        s_2 = s[] #loop 2
        s_3 = s[] #loop 3
        temp_sparky = s[] #sparky temp

        #for air
        A = 112.5
        B = 2737.5
        p = 101325 #pascals
        gamma_se = 100 #????? fix this

        Breakdown_Voltage = (B*p*sparky_distance)/(np.log(A*p*sparky_distance) - np.log(np.log(1 + 1/gamma_se)))#pashen cure function


        if s_2[] < Breakdown_Voltage: #This makes the diff for the different states of loop 2 
            ds_2 = 
        else:
            ds_2 = 

        deriv = [, ]
        return deriv

    def diffeq_solver_from_scipy(t, s_initial, deriv): #solves diff equation
        s = odeint(deriv, s_initial, t)
        return t,s

    return diffeq_solver_from_scipy(t, s_initial, deriv) 
