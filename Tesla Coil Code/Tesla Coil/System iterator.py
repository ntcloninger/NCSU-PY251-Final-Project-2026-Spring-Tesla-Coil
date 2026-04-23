import numpy as np
from scipy.integrate import odeint

def Tesla_Coil_Solver(t , s_initial, pars): #take in initial value and parameters
    C_1 = pars[0]
    C_2 = pars[1]
    R_1 = pars[2]
    R_2 = pars[3]
    R_3 = pars[4]
    L_1 = pars[5]
    L_2 = pars[6]
    AC_amplitude = pars[7]
    AC_frequency = pars[8]
    sparky_distance = pars[9]
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

        d_s1 = 
        if s_2[] < Breakdown_Voltage: #This makes the diff for the different states of loop 2 
            ds_2 = 
        else:
            ds_2 = 
        d_s3 = 

        deriv = [, ]
        return deriv

    def diffeq_solver_from_scipy(t, s_initial, deriv): #solves diff equation
        s = odeint(deriv, s_initial, t)
        return t,s

    return diffeq_solver_from_scipy(t, s_initial, deriv) 
