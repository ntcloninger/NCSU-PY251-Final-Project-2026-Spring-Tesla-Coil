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
    C2 = st.number_input("Type C2 Value[F]: ",value=100)
    R3 = st.number_input("Type R3 Value[Ohm]: ", value=100)
    L1 = st.number_input("Type L1 Value[H]: ", value=1)
    L2 = st.number_input("Type L2 Value[H]: ", value=50)
    L3 = st.number_input("Type L3 Value[H]: ", value=10)
    L4 = st.number_input("Type L4 Value[H]: ", value=100)
    k1 = st.number_input("Type k1 Value[F]: ",value=0.6)
    k2 = st.number_input("Type k1 Value[F]: ",value=0.3)
    sparky_distance = st.number_input("Spark Gap Distance Value[m]: ",value=0.1)
    ac_amp = st.number_input("AC Amplitude Value[m]: ",value=170)
    ac_freq = st.number_input("AC Frequency Value[Hz]: ",value=60)
    voltage_point = st.string_input("Voltage Point (A/B/C): ",value='C')
    breakdown = st.string_input("Before or After Breakdown (B/A): ",value="B")

    submitted = st.form_submit_button("Upload and Run")

#confirms submissions
if submitted:
    st.success("Values uploaded!")

#creates graphs

pars = input_wrapper(L_1=L1, L_2=L2, L_3=L3, L_4=L4, R_1=R1, R_2=R2, R_3=R3, C_1=C1, C_2=C2, C_3=C3,
                    AC_amplitude=ac_amp, AC_frequency=ac_freq, sparky_distance=sparky_distance, k1= k1, k2=k1)

t_array = np.linspace(0,10/(pars[11]*2*np.pi),10000)
q1, q2 = Tesla_Coil_Solver(t_array, pars)

VA1_array = (pars[0])*q1[:,2]+(pars[4])*q1[:,1]+(pars[7])*q1[:,0] - pars[13]*np.sqrt(pars[0]*pars[1])*q1[:,5]
VA2_array = (pars[0])*q2[:,2]+(pars[4])*q2[:,1]+(pars[7])*q2[:,0]

VB1_array = (pars[0])*q1[:,2]+(pars[4])*q1[:,1]+(pars[7])*q1[:,0]
VB2_array = (pars[0])*q2[:,2]+(pars[4])*q2[:,1]+(pars[7])*q2[:,0]

VC1_array = (pars[0])*q1[:,2]+(pars[4])*q1[:,1]+(pars[7])*q1[:,0] - pars[14]*np.sqrt(pars[2]*pars[3])*q1[:,5]
VC2_array = (pars[0])*q2[:,2]+(pars[4])*q2[:,1]+(pars[7])*q2[:,0]

if str.capitalize(list(voltage_point)[-1]) == 'A':
    if str.capitalize(breakdown) == 'B' or str.capitalize(breakdown) == 'BEFORE':
        output_voltage_array = VA1_array

    if str.capitalize(breakdown) == 'A' or str.capitalize(breakdown) == 'AFTER':
        output_voltage_array = VA2_array

if str.capitalize(list(voltage_point)[-1]) == 'B':
    if str.capitalize(breakdown) == 'B' or str.capitalize(breakdown) == 'BEFORE':
        output_voltage_array = VB1_array

    if str.capitalize(breakdown) == 'A' or str.capitalize(breakdown) == 'AFTER':
        output_voltage_array = VB2_array

if str.capitalize(list(voltage_point)[-1]) == 'C':
    if str.capitalize(breakdown) == 'B' or str.capitalize(breakdown) == 'BEFORE':
        output_voltage_array = VC1_array

    if str.capitalize(breakdown) == 'A' or str.capitalize(breakdown) == 'AFTER':
        output_voltage_array = VC2_array



chart_data = pd.DataFrame(output_voltage_array, index=t_array)

st.line_chart(chart_data)

# calls global wrapper function, plugging in those input parameters
# puts the return values into their own variables


# sends those values to the global steady state function
# returned values get used to make a graph 
# creates the 3 graphs

""" Va = 
Vb = 
Vc =  """



