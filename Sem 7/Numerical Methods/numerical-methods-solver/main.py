import streamlit as st
import numpy as np
import sympy as sp

# Import methods
from methods.integration import trapezoidal_rule, simpson_1_by_3_rule
from utils.plotter import plot_trapezoidal, plot_simpson_1_by_3


# ---------------- STREAMLIT APP ----------------
st.set_page_config(page_title="Numerical Methods Toolkit", layout="wide")

st.title("Numerical Methods Solver Toolkit")
st.sidebar.header("Choose a Module")

# Sidebar Menu
module = st.sidebar.radio(
    "Select Category",
    ["Integration", "Roots", "Interpolation", "Linear Systems", "ODEs"]
)

# ======================================================
# ---------------- Integration ----------------
# ======================================================
if module == "Integration":
    st.header("Integration Methods")

    method = st.selectbox("Select Method", ["Trapezoidal Rule", "Simpson 1/3 Rule"])  # add other methods later.

    # --- User inputs ---
    user_func = st.text_input("Enter function f(x)", value="sin(x**2)")
    a = st.number_input("Lower limit (a)", value=0.0)
    b = st.number_input("Upper limit (b)", value=1.0)
    n = st.slider("Number of subintervals (n)", min_value=1, max_value=50, value=6)

    if st.button("Compute Integral"):
        try:
            # Convert string to lambda function
            x = sp.symbols('x')
            func_expr = sp.sympify(user_func) 
            func = sp.lambdify(x, func_expr, "numpy")

            if method == "Trapezoidal Rule":
                result = trapezoidal_rule(func, a, b, n)
                st.success(f"Approximate Integral = {result:.6f}")

                # Plot
                fig = plot_trapezoidal(func, a, b, n)
                st.pyplot(fig)
            elif method == "Simpson 1/3 Rule":
                result = simpson_1_by_3_rule(func, a, b, n)
                st.success(f"Approximate Integral = {result:.6f}")

                # Plot
                fig = plot_simpson_1_by_3(func, a, b, n)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Error: {e}")
    
# ======================================================
# ---------------- Other Modules ----------------
# ======================================================
elif module == "Roots":
    st.header("Root Finding Methods")
    st.info("Coming soon.")

elif module == "Interpolation":
    st.header("Interpolation Methods")
    st.info("Coming soon.")

elif module == "Linear Systems":
    st.header("System of Linear Equations")
    st.info("Coming soon.")

elif module == "ODEs":
    st.header("Ordinary Differential Equations")
    st.info("Coming soon.")
