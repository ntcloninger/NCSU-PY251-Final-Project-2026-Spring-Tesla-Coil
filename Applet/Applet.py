import streamlit as st
import numpy as np
import pandas as pd
from Input_Wrapper import input_wrapper
from Steady_State_Driver import # put in the function 
from System_iterator import Tesla_Coil_Solver

# import any libraries that we need

# get input parameters from user and assigns those values to their corresponding value

# Shows the tesla coil curcuit for demonstration purposes 
st.image("1000002237.jpg", caption="tesla coil")

C1 = st.number_input("Type C1 Value: ")
C2 = st.number_input("Type C2 Value: ")
R1 = st.number_input("Type R1 Value: ")
R2 = st.number_input("Type R2 Value: ")
R3 = st.number_input("Type R3 Value: ")
L1 = st.number_input("Type L1 Value: ")
L2 = st.number_input("Type L2 Value: ")
sparky = st.number_input("Spark Gap Distance Value: ")
ac_amp = st.number_input("AC Amplitude Value: ")
ac_freq = st.number_input("AC Frequency Value: ")


# calls global wrapper function, plugging in those input parameters
# puts the return values into their own variables
init_state, pars = input_wrapper(C_1=C1, C_2=C2, R_1=R1, R_2=R2, R_3=R3, L_1=L1, L_2=L2, 
                                 AC_amplitude=ac_amp, AC_frequency=ac_freq, sparky_distance=sparky)

# sends those values to the global steady state function
# returned values get used to make a graph 



