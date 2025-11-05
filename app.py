import streamlit as st

st.title("Scheduling Optimization using Genetic Algorithm")

st.markdown("### Step 3: Modify GA Parameters")

# --- User Input Sliders ---
CO_R = st.slider("Crossover Rate", 0.0, 0.95, 0.8, step=0.01)
MUT_R = st.slider("Mutation Rate", 0.01, 0.05, 0.02, step=0.01)

st.write("You selected:")
st.write(f"- Crossover Rate: {CO_R}")
st.write(f"- Mutation Rate: {MUT_R}")

# --- Button to run algorithm ---
if st.button("Run Genetic Algorithm"):
    st.success("Genetic Algorithm executed successfully!")
    # Here is where you’ll later insert your GA code and display results.
