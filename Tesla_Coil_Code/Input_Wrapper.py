def input_wrapper(C_1 = 0.00001, C_2 = 1, C_3 = 0.0000001, R_1 = 10, R_2 = 20, R_3 = 100000, 
                   L_1 = 0.1, L_2 = 1, L_3 = 0.001, L_4 = 5, AC_amplitude = 170, AC_frequency = 60, 
                   Distance_Sparky = 0.07, k1 = 1, k2 = 0.5):
    #set these to standard conditions in function call.
    pars = [C_1, C_2, C_3, R_1, R_2, R_3, L_1, L_2, L_3, L_4,
                    AC_amplitude, AC_frequency, Distance_Sparky, k1, k2] #parameters

    return pars
