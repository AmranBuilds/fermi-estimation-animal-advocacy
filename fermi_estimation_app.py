import streamlit as st

st.title("Fermi Estimation: Chickens on a Farm")

# 1. Sliders on the left side
st.sidebar.header("Inputs")
barns = st.sidebar.slider("How many Containers (Barns)?", 1, 50, 10)
tiers = st.sidebar.slider("How many Layers (Tiers)?", 1, 10, 4)
barn_width = st.sidebar.slider("Barn Width (feet)", 10, 100, 25)
barn_length = st.sidebar.slider("Barn Length (feet)", 50, 1000, 500)
farm_type = st.sidebar.selectbox(
    "Space per Unit (Farm Style)", 
    ["Battery Cages (Midwest Standard)", "Cage-Free (West Coast Standard)"]
)

# 2. Assign variables based on the sliders
if farm_type == "Battery Cages (Midwest Standard)":
    space_per_bird = 0.46 
else:
    space_per_bird = 1.2 

barn_area = barn_width * barn_length
birds_per_barn = (barn_area / space_per_bird) * tiers
total_birds = birds_per_barn * barns

# 3. Math Equations
st.header("The Math")
st.write("General Fermi Formula:")
st.latex(r"\text{Total Estimate} = \text{Containers} \times \text{Layers} \times \frac{\text{Available Space}}{\text{Space per Unit}}")

st.write("Your Filled Equation:")
st.latex(rf"\text{{Total Birds}} = {barns} \times {tiers} \times \frac{{{barn_width} \times {barn_length}}}{{{space_per_bird}}} = {int(total_birds):,}")

# 4. Step-by-Step Breakdown
st.header("How This Works")
st.markdown("""
* **Step 1: Measure the Building.** We use satellite pictures and shadow lengths to find the exact width and length of one barn.
* **Step 2: Find the Chicken Space.** We use known industry data to see exactly how much room one chicken is given.
* **Step 3: Fill the Floor.** We divide the total floor space of the barn by the space one chicken needs. This tells us how many chickens fit on one level.
* **Step 4: Stack and Multiply.** We multiply that number by the amount of stacked rows (layers) inside the barn, and then multiply by the total number of barns on the farm.
""")
