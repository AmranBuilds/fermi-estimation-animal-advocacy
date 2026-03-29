import streamlit as st

st.title("Fermi Estimation: Chickens on a Farm")

# 1. Sliders on the left side
st.sidebar.header("Inputs")
barns = st.sidebar.slider("How many Containers (Barns)?", 1, 50, 10)
barn_width = st.sidebar.slider("Barn Width (feet)", 10, 100, 25)
barn_length = st.sidebar.slider("Barn Length (feet)", 50, 1000, 500)
farm_type = st.sidebar.selectbox(
    "Density Factor (Farm Style)", 
    ["Battery Cages (Midwest Standard)", "Cage-Free (West Coast Standard)"]
)

# 2. Assign variables based on the sliders
if farm_type == "Battery Cages (Midwest Standard)":
    # Average of 8.7 birds stacked above every 1 square foot of floor
    density_factor = 8.7 
else:
    # 1 bird needs about 1.2 square feet, which equals 0.83 birds per square foot
    density_factor = 0.83 

barn_area = barn_width * barn_length
birds_per_barn = barn_area * density_factor
total_birds = birds_per_barn * barns

# 3. Math Equations
st.header("The Math")
st.write("General Fermi Formula:")
st.latex(r"\text{Total Estimate} = \text{Containers} \times \text{Available Space} \times \text{Density Factor}")

st.write("Your Filled Equation:")
st.latex(rf"\text{{Total Birds}} = {barns} \times ({barn_width} \times {barn_length}) \times {density_factor} = {int(total_birds):,}")

# 4. Step-by-Step Breakdown
st.header("How This Works")
st.markdown("""
* **Step 1: Measure the Building.** Use satellite pictures to find the exact floor area of one barn (Width × Length).
* **Step 2: Apply the Density Factor.** Multiply the floor area by an industry-standard "Density Factor." This factor accounts for all the stacked cages automatically. It estimates how many total birds sit above one square foot of floor space.
* **Step 3: Multiply by Barns.** Take the total birds in one barn and multiply it by the number of barns on the farm.
""")
