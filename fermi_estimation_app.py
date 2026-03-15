import streamlit as st

# The title of your web app
st.title("Fermi Estimation: Chickens on a Farm")

# 1. Ask the user for the farm size
st.header("Farm Size")
barns = st.number_input("How many barns?", min_value=1, value=10)
barn_width = st.number_input("Barn Width (feet)", min_value=10, value=50)
barn_length = st.number_input("Barn Length (feet)", min_value=10, value=500)

# Calculate the footprint of one barn
barn_area = barn_width * barn_length

# 2. Ask the user for the farm type (Region/Style)
st.header("Farm Style")
farm_type = st.selectbox(
    "How are the birds kept?", 
    ["Battery Cages (Midwest Standard)", "Cage-Free (West Coast Standard)"]
)

# 3. Do the math based on the farm type
if farm_type == "Battery Cages (Midwest Standard)":
    # Birds get very little space and cages are stacked like bunk beds
    space_per_bird = 0.46 
    tiers = 4 
    birds_per_barn = (barn_area / space_per_bird) * tiers
else:
    # Birds walk on the floor, so they need more space and are not stacked
    space_per_bird = 1.2 
    tiers = 1 
    birds_per_barn = barn_area / space_per_bird

# Calculate the final number
total_birds = birds_per_barn * barns

# 4. Show the answer to the user
st.header("Estimation Results")
st.write(f"- **Size of one barn:** {barn_area:,.0f} square feet")
st.write(f"- **Estimated birds in ONE barn:** {birds_per_barn:,.0f}")
st.write(f"- **Total estimated birds on the farm:** {total_birds:,.0f}")
