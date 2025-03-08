import streamlit as st
import pandas as pd
import numpy as np

# 🎨 Set Page Config
st.set_page_config(page_title="My Streamlit Website", page_icon="🚀", layout="wide")

# 🏆 Website Header
st.title("Welcome to My Awesome Website! 🚀")
st.subheader("Built with Python & Streamlit")

# 📌 Sidebar Navigation
st.sidebar.header("Navigation")
st.sidebar.write("🔗 [Visit My GitHub](https://github.com/)")

# ✍️ User Input
name = st.text_input("Enter your name:", "John Doe")
st.write(f"👋 Hello, {name}! Welcome to my website.")

# 📊 Generate and Display a Chart
st.subheader("📈 Random Data Chart")
data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(data)

# 📸 Image Upload
st.subheader("📷 Upload an Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# 🎲 Add a Button
if st.button("Click Me"):
    st.success("🎉 You clicked the button!")

# 📢 Footer
st.markdown("---")
st.write("💡 Made with ❤️ using Streamlit")
