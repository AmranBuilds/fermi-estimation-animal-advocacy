import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fermi Estimation: Animal Advocacy Impact", layout="wide")

st.sidebar.header("Estimation Variables")
human_population = st.sidebar.number_input("Human Population", min_value=100000, max_value=1000000000, value=10000000, step=1000000)
meat_consumption_per_capita = st.sidebar.slider("Meat Consumption (kg/person/year)", min_value=10, max_value=150, value=50, step=5)
yield_per_animal = st.sidebar.slider("Yield per Animal (kg)", min_value=1.0, max_value=500.0, value=2.5, step=0.5)

animals_impacted = (human_population * meat_consumption_per_capita) / yield_per_animal

st.title("Fermi Estimation: Animal Advocacy Impact")

st.header("The Math")
st.latex(r"N = \frac{P \times C}{Y}")
st.markdown(r"""
* $N$ = Total Animals Impacted
* $P$ = Human Population
* $C$ = Meat Consumption per Capita (kg/year)
* $Y$ = Yield per Animal (kg)
""")

st.latex(rf"N = \frac{{{human_population:,.0f} \times {meat_consumption_per_capita}}}{{{yield_per_animal}}} = {animals_impacted:,.0f}")

st.header("Visual Representation")
data = pd.DataFrame({
    "Metric": ["Total Meat Demanded (kg)", "Total Animals Impacted"],
    "Value": [human_population * meat_consumption_per_capita, animals_impacted]
})
st.bar_chart(data.set_index("Metric"))

st.info("How to read this chart: The first bar represents the total mass of meat demanded by the human population. The second bar shows the estimated number of individual animals required to meet that demand. This demonstrates how Fermi estimation derives large-scale impact figures from basic population and consumption inputs.")
