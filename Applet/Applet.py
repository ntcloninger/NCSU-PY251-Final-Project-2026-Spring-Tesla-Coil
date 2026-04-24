import streamlit as st
import numpy as np
import pandas as pd
from Tesla Coil Code
from Steady_State_Driver import # put in the function 
from System_iterator import Tesla_Coil_Solver

# import any libraries that we need



# Shows the tesla coil curcuit for demonstration purposes 
st.image("1000002237.jpg", caption="Tesla Coil Circuit Diagram")

# get input parameters from user and assigns those values to their corresponding value
C1 = st.number_input("Type C1 Value[F]: ", value=1)
C2 = st.number_input("Type C2 Value[F]: ",value=100)
R1 = st.number_input("Type R1 Value[Ohm]: ", value=10)
R2 = st.number_input("Type R2 Value[Ohm]: ", value=20)
R3 = st.number_input("Type R3 Value[Ohm]: ", value=100)
L1 = st.number_input("Type L1 Value[H]: ", value=1)
L2 = st.number_input("Type L2 Value[H]: ", value=50)
sparky = st.number_input("Spark Gap Distance Value[m]: ",value=0.1)
ac_amp = st.number_input("AC Amplitude Value[m]: ",value=170)
ac_freq = st.number_input("AC Frequency Value[Hz]: ",value=60)


# calls global wrapper function, plugging in those input parameters
# puts the return values into their own variables
init_state, pars = input_wrapper(C_1=C1, C_2=C2, R_1=R1, R_2=R2, R_3=R3, L_1=L1, L_2=L2, 
                                 AC_amplitude=ac_amp, AC_frequency=ac_freq, sparky_distance=sparky)

# sends those values to the global steady state function
# returned values get used to make a graph 



