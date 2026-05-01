def input_wrapper(C_1 = 1, C_2 = 100, C_3 = 0.0001, R_1 = 10, R_2 = 20, R_3 = 100, 
                   L_1 = 1, L_2 = 50, L_3 = 10, L_4 = 500, AC_amplitude = 170, AC_frequency = 60, 
                   Distance_Sparky = 0.1, k1 = 1, k2 = 0.5):
    #set these to standard conditions in function call.
    pars = [C_1, C_2, C_3, R_1, R_2, R_3, L_1, L_2, L_3, L_4,
                    AC_amplitude, AC_frequency, Distance_Sparky, k1, k2] #parameters

    return pars
