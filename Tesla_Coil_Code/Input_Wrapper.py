def input_wrapper(L_1 = 0.1, L_2 = 1, L_3 = 0.001, L_4 = 5, R_1 = 10, R_2 = 20, R_3 = 100000, 
                    C_1 = 0.00001, C_2 = 1, C_3 = 0.0000001, AC_amplitude = 170, AC_frequency = 60, 
                   sparky_distance = 0.07, k1 = 1, k2 = 0.5):
    #set these to standard conditions in function call.
    pars = [L_1, L_2, L_3, L_4, R_1, R_2, R_3, C_1, C_2, C_3,
                    AC_amplitude, AC_frequency, sparky_distance, k1, k2] #parameters

    return pars
