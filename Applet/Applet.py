import streamlit as st
import numpy as np
import pandas as pd
from Input_Wrapper import input_wrapper
from Steady_State_Driver import # put in the function 
from System_iterator import Tesla_Coil_Solver

# import any libraries that we need

# get input parameters from user and assigns those values to their corresponding value

st.image("1000002237.jpg", caption="tesla coil")

C1 = st.number_input("Type C1 Value: ")
C2 = st.number_input("Type C2 Value: ")
sparky_distance = st.number_input("Spark Gap Distance Value: ")
ac_amp = st.number_input("AC Amplitude Value: ")
ac_freq = st.number_input("AC Frequency Value: ")


# calls global wrapper function, plugging in those input parameters
# puts the return values into their own variables
init_state, pars = input_wrapper(C_1=C1 )


# sends those values to the global steady state function
# returned values get used to make a graph 

