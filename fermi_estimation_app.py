import streamlit as st
import pandas as pd
import altair as alt
import math

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

# 3. Visual: Grid in a 10x10 square
st.header("How squished are the birds?")
st.write("This grid shows exactly how many birds fit into a small 10x10 foot floor space.")

sample_area = 100
sample_birds = int((sample_area / space_per_bird) * tiers)

# Create a perfect grid shape (like a checkerboard)
cols = math.ceil(math.sqrt(sample_birds))

x_coords = []
y_coords = []

for i in range(sample_birds):
    x_coords.append(i % cols) 
    y_coords.append(i // cols) 

df = pd.DataFrame({
    'x': x_coords,
    'y': y_coords
})

# Draw the grid tiles
chart = alt.Chart(df).mark_rect(
    color='orange', 
    stroke='white', 
    strokeWidth=1
).encode(
    x=alt.X('x:O', axis=None), 
    y=alt.Y('y:O', axis=None)
).properties(
    title=f"{sample_birds} birds tightly packed in 100 square feet",
    height=400
).configure_view(
    strokeWidth=0
)

st.altair_chart(chart, use_container_width=True)

# 4. Math Equations
st.header("The Math")
st.write("General Formula:")
st.latex(r"\text{Total Birds} = \text{Barns} \times \text{Tiers} \times \frac{\text{Width} \times \text{Length}}{\text{Space per Bird}}")

st.write("Your Filled Equation:")
st.latex(rf"\text{{Total Birds}} = {barns} \times {tiers} \times \frac{{{barn_width} \times {barn_length}}}{{{space_per_bird}}} = {int(total_birds):,}")
