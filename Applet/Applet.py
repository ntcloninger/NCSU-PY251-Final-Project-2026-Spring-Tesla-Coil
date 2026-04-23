import streamlit as st
import numpy as np
import pandas as pd
from Input_Wrapper import input_wrapper
from Steady_State_Driver import # put in the function 
from System_iterator import Tesla_Coil_Solver

# import any libraries that we need

# get input parameters from user and assigns those values to their corresponding value


C1 = # put in user's input for C1
C2 = # put in user's input for C2
sparky_distance = # put in user's input for sparky's distance
ac_amp = # put in user's input for ac amplitude
ac_freq = # put n user's input input for ac frequency 


# calls global wrapper function, plugging in those input parameters
# puts the return values into their own variables
init_state, pars = input_wrapper(C_1=C1 )


# sends those values to the global steady state function
# returned values get used to make a graph 

