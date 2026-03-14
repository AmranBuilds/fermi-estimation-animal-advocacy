import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Animal Advocacy EV Calculator")
st.title("Expected Value in Animal Advocacy")

# Sidebar for variables
st.sidebar.header("Campaign Parameters")
impact = st.sidebar.slider("Impact (Animals helped if successful)", 0, 10000, 5000)
probability = st.sidebar.slider("Probability of Success (%)", 0, 100, 20) / 100

# Calculate EV
ev = impact * probability

# Display Equations
st.header("The Math")
st.latex(r"EV = P(\text{success}) \times \text{Impact}")
st.latex(rf"EV = {probability} \times {impact} = {ev:,.0f} \text{{ animals}}")

# Visual Representation [cite: 8]
st.header("Impact Comparison")
data = pd.DataFrame({
    "Scenario": ["Maximum Potential Impact", "Expected Value (Adjusted for Risk)"],
    "Animals Helped": [impact, ev]
})

fig = px.bar(data, x="Scenario", y="Animals Helped", color="Scenario",
             text_auto='.2s', title="Potential vs. Probable Impact")
st.plotly_chart(fig)

# ELI5 at the bottom
st.info("**How to read this chart:** The tall bar shows how many animals we *could* help if everything goes perfectly. The short bar is the 'Expected Value'—it shows the realistic impact when we consider that the project might fail. In Data Analysis, we use the short bar to decide which campaigns are worth the investment[cite: 9].")
