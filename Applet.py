# import any libraries that we need
import streamlit as st
import numpy as np
import pandas as pd
from Tesla_Coil_Code.Input_Wrapper import input_wrapper
from Tesla_Coil_Code.Graph_Creater import Cycle_Graph_20
from Tesla_Coil_Code.TeslaCoil import Tesla_Coil_Solver


# Shows the tesla coil curcuit for demonstration purposes 
st.image("1000002237.jpg", caption="Tesla Coil Circuit Diagram")

with st.form("Calc_Form"):
    st.header("Input Parameters")

    #creates inputs for users
    C1 = st.number_input("Type C1 Value[F]: ", value=1)
    C2 = st.number_input("Type C2 Value[F]: ",value=100)
    C3 = st.number_input("Type C3 Value[F]: ",value=100)
    R1 = st.number_input("Type R1 Value[Ohm]: ", value=10)
    R2 = st.number_input("Type R2 Value[Ohm]: ", value=20)
    R3 = st.number_input("Type R3 Value[Ohm]: ", value=100)
    L1 = st.number_input("Type L1 Value[H]: ", value=1)
    L2 = st.number_input("Type L2 Value[H]: ", value=50)
    L3 = st.number_input("Type L3 Value[H]: ", value=10)
    L4 = st.number_input("Type L4 Value[H]: ", value=100)
    k1 = st.number_input("Type k1 Value[F]: ",value=1)
    k2 = st.number_input("Type k1 Value[F]: ",value=0.5)
    sparky_distance = st.number_input("Spark Gap Distance Value[m]: ",value=0.1)
    ac_amp = st.number_input("AC Amplitude Value[m]: ",value=170)
    ac_freq = st.number_input("AC Frequency Value[Hz]: ",value=60)

    submitted = st.form_submit_button("Upload and Run")

#confirms submissions
if submitted:
    st.success("Values uploaded!")

#creates graphs
t_array = np.linspace(0,10/(pars[11]*2*np.pi),10000)
q1, q2 = Tesla_Coil_Solver(t, pars)
VA1_array = (pars[0])*q1[:,2]+(pars[4])*q1[:,1]+(pars[7])*q1[:,0]
VA2_array = (pars[0])*q2[:,2]+(pars[4])*q2[:,1]+(pars[7])*q2[:,0]

chart_data = pd.DataFrame(VA1_array, index=t_array)

st.line_chart(chart_data)

# calls global wrapper function, plugging in those input parameters
# puts the return values into their own variables
pars = input_wrapper(L_1=L1, L_2=L2, L_3=L3, L_4=L4, R_1=R1, R_2=R2, R_3=R3, C_1=C1, C_2=C2, C_3=C3,
                    AC_amplitude=ac_amp, AC_frequency=ac_freq, sparky_distance=sparky_distance, k1= k1, k2=k1)


# sends those values to the global steady state function
# returned values get used to make a graph 
times = np.linspace(0.0, 10.0, 100)
voltPars = Tesla_Coil_Solver(times, pars)
# loop 1: voltPars[0] returns charge, voltPars[1] is change in charge, voltPars[2] change in change in charge
# loop 2: voltPars[3] returns charge, voltPars[4] is change in charge, voltPars[5] change in change in charge
# loop 3: voltPars[6] returns charge, voltPars[7] is change in charge, voltPars[8] change in change in charge

# creates the 3 graphs
Cycle_Graph_20(pars=pars, q=voltPars, t=times)

""" Va = 
Vb = 
Vc =  """



