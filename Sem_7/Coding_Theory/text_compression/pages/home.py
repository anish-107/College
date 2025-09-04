import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Home | Text Compression Visualizer",
    page_icon="🗜",
    layout="wide"
)

st.title("Text Compression Visualizer")
st.subheader("Huffman vs Arithmetic Coding")

st.markdown("""
Welcome to the **Text Compression Visualizer**! 

This tool will let you:
- Upload or paste text
- Compress with **Huffman** and **Arithmetic Coding**
- Compare **compression ratio, entropy, redundancy**
- Visualize **Huffman trees** & **Arithmetic intervals**

---
""")

st.info("⚡ The full experience is **coming soon**. Stay tuned!")

# --- Navigation Cards ---
st.markdown("## Explore Sections")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Huffman Coding")
    st.caption("Visualize Huffman tree and compare efficiency.")
    st.button("Coming Soon", disabled=True, key="btn_huffman")

with col2:
    st.markdown("### Arithmetic Coding")
    st.caption("See how probability intervals encode text.")
    st.button("Coming Soon", disabled=True, key="btn_arithmetic")

with col3:
    st.markdown("### Comparison Dashboard")
    st.caption("Compare compression ratio, entropy, and redundancy.")
    st.button("Coming Soon", disabled=True, key="btn_comparison")


st.markdown("---")
st.caption("© 2025 Text Compression Visualizer | Built with Streamlit")
