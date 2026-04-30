import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


st.image("1000002237.jpg", caption="Tesla Coil Circuit Diagram")

with st.form("Calc_Form"):
    st.header("Input Parameters")

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

if submitted:
    st.success("Values uploaded!")

    t_array = np.linspace(0, 10, 20)
    y_array = 2 * t_array

    chart_data = pd.DataFrame(y_array, index=t_array)

    st.line_chart(chart_data)