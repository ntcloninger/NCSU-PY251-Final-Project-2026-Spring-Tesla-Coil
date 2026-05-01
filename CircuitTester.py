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

    d.config(unit=2.2)

    #Power supply
    d += e.SourceSin().at((0,0)).label("AC")
    d+= e.Line().right().length(1.5)
    #Add the transformer
    d += e.Transformer(t1=4, t2=4).anchor("p1")
    d += e.Line().at((1.5,0)).to((1.5, -2))
    d += e.Line().at((0, -2)).to((1.5, -2))
    d += e.Line().at((0, -2)).up().length(2)

    #Start the second part of the loop
    d += e.Line().at((4.5, 0.8)).right().length(1.5)
    d += e.Capacitor().right()
    d += e.Line().right().length(1)
    #Spark gap
    d += e.SparkGap().down()
    d += e.Line().down().length(1)
    #Coil
    d += e.Inductor2().left()
    d += e.Line().left().length(1)
    d += e.Line().up().to((4.5, -0.8))

    #Right side
    d += e.Inductor().at((10, -1.5)).up().length(4)
    d += e.Line().at((10, -1.5)).down().length(1)
    d += e.Ground()
    #Torus
    d += e.Line().at((10, 2.5)).up().length(0.5)
    d += e.Dot()


    #creates all of the parts of the circuit
    """ source = d.add(e.SourceSin().down())
    d += d.add(e.Line().right()) 
    tr = d.add(e.Transformer().right())
    d += d.add(e.Line().right()) """

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