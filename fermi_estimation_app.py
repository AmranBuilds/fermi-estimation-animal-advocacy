import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title("Fermi Estimation: Chickens on a Farm")

# 1. Sliders on the left side
st.sidebar.header("Inputs")
barns = st.sidebar.slider("How many barns?", 1, 50, 10)
barn_width = st.sidebar.slider("Barn Width (feet)", 10, 100, 50)
barn_length = st.sidebar.slider("Barn Length (feet)", 50, 1000, 500)
farm_type = st.sidebar.selectbox(
    "Farm Style", 
    ["Battery Cages (Midwest Standard)", "Cage-Free (West Coast Standard)"]
)

# 2. Assign variables based on the sliders
if farm_type == "Battery Cages (Midwest Standard)":
    space_per_bird = 0.46 
    tiers = 4 
else:
    space_per_bird = 1.2 
    tiers = 1 

barn_area = barn_width * barn_length
birds_per_barn = (barn_area / space_per_bird) * tiers
total_birds = birds_per_barn * barns

# 3. Visual: Density in a 10x10 square
st.header("How squished are the birds?")
st.write("This box represents a small 10x10 foot space. Each dot is one bird.")

sample_area = 100
sample_birds = int((sample_area / space_per_bird) * tiers)

# Make random dots for the visual
df = pd.DataFrame({
    'x': np.random.uniform(0, 10, sample_birds),
    'y': np.random.uniform(0, 10, sample_birds)
})

# Draw the dots
chart = alt.Chart(df).mark_circle(size=30, color='orange', opacity=0.7).encode(
    x=alt.X('x', axis=None, scale=alt.Scale(domain=[0, 10])),
    y=alt.Y('y', axis=None, scale=alt.Scale(domain=[0, 10]))
).properties(
    height=300
)
st.altair_chart(chart, use_container_width=True)

# 4. Math Equations
st.header("The Math")
st.write("General Formula:")
st.latex(r"\text{Total Birds} = \text{Barns} \times \text{Tiers} \times \frac{\text{Width} \times \text{Length}}{\text{Space per Bird}}")

st.write("Your Filled Equation:")
st.latex(rf"\text{{Total Birds}} = {barns} \times {tiers} \times \frac{{{barn_width} \times {barn_length}}}{{{space_per_bird}}} = {int(total_birds):,}")
