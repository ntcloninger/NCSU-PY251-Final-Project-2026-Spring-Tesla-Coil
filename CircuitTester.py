# import any libraries that we need
import streamlit as st
import numpy as np
import pandas as pd
#pip install streamlit schemdraw 
import schemdraw
import schemdraw.elements as e

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
with schemdraw.Drawing() as d:

    d.config(unit=2.2)

    #Power supply
    d += e.SourceSin().at((0,0))
    d += e.Dot().label("Node A")
    d += e.Line().right().length(1.5)
    #Add the transformer
    d += e.Transformer(t1=10, t2=10).anchor("p1")
    d += e.Line().at((0, -1.8)).to((1.5, -1.8))
    d += e.Line().at((0, -1.8)).up().length(2)

    #Start the second part of the loop
    d += e.Line().at((2.5, 2.2)).right().length(1.5)
    d += e.Dot().label("Node B")
    d += e.Line().right().length(1)
    d += e.Capacitor().right()
    
    #Spark gap
    d += e.Line().at((2.5, -1.8)).right().length(1.5)
    d += e.SparkGap().up().length(4)
    d += e.Line().at((4,-1.8)).right().length(3.2)
    #Coil
    d += e.Inductor2().up()
    d += e.Line().at((7.2,0)).length(2.2)

    #Right side
    d += e.Inductor().at((8, 2.6)).down().length(4)
    d += e.Ground()
    #Torus
    d += e.AntennaLoop().at((8,2.6))
    d += e.Dot().label("Node C").at((8.1,4))

    # Save to file
    d.save('circuit.png')

# Display in Streamlit
st.image('circuit.png')