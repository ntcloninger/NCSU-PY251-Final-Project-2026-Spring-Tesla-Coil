def input_wrapper(C_1 = 1, C_2 = 100, R_1 = 10, R_2 = 20, R_3 = 100, L_1 = 1, L_2 = 50, \
                  AC_amplitude = 170, AC_frequency = 60, Distance_Sparky = 0.1):
    #set these to standard conditions in function call.
    pars = [C_1, C_2, R_1, R_2, R_3, L_1, L_2, \
            AC_amplitude, AC_frequency, Distance_Sparky] #parameters
    
    initial_state = [ ]

    return initial_state, pars
