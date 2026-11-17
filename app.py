import streamlit as st
import json
st.title("Mit DIY-dashboard")
st.write("Velkommen til mit DIY-dashboard!")

with open("data.json", "r", encoding="utf-8") as f:
    items = json.load(f)
for item in items:
    checked = st.checkbox(item["name"], value=item["bought"])
    st.write(checked)