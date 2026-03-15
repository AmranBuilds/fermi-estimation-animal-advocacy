import streamlit as st

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

# 3. Math Equations
st.header("The Math")
st.write("General Fermi Formula:")
st.latex(r"\text{Total Estimate} = \text{Containers} \times \text{Layers} \times \frac{\text{Available Space}}{\text{Space per Unit}}")

st.write("Your Filled Equation:")
st.latex(rf"\text{{Total Birds}} = {barns} \times {tiers} \times \frac{{{barn_width} \times {barn_length}}}{{{space_per_bird}}} = {int(total_birds):,}")
