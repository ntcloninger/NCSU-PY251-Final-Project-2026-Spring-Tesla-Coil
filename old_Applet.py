# import any libraries that we need
import streamlit as st
import numpy as np
import pandas as pd
#pip install streamlit schemdraw 
import schemdraw
import schemdraw.elements as e

#https://schemdraw.readthedocs.io/en/stable/elements/electrical.html
#Background Color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E0D3AF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Shows the tesla coil circuit for demonstration purposes 
st.image("1000002237.jpg", caption="Tesla Coil Circuit Diagram")

# Create a simple RC circuit
with schemdraw.Drawing() as d:

    #creates all of the parts of the circuit
    source = d.add(e.SourceSin().up())
    tr = d.add(e.Transformer().down())
    d += d.add(e.Line().right().at(source.start).to(tr.p1)) 
    d += d.add(e.Line().left().at(source.end).to(tr.p2))

    #d += d.add(e.SparkGap().right())
    #d += d.add(e.Capacitor().up())
    #d += d.add(e.Inductor().right())
    #d += d.add(e.Ground().down())
    #d += d.add(e.Inductor().up())
    #d += d.add(e.AntennaLoop().up())

    # Save to file
    d.save('circuit.png')

# Display in Streamlit
st.image('circuit.png')