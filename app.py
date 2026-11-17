import streamlit as st
import json
st.title("Mit DIY-dashboard")
st.write("Velkommen til mit DIY-dashboard!")
with open("data.json", "r", encoding="utf-8") as f:
    projects = json.load(f)
items = projects[0]["items"]

total = 0
for item in items:
    if item["bought"] == False:
        total = total + item["quantity"] * item["price"]
st.metric("Mangler at købe", f"{total} kr")

for item in items:
    checked = st.checkbox(item["name"], value=item["bought"])
    st.caption(f"{item['quantity']} × {item['unit']} · {item['price']} kr · {item['store']}")
    if checked != item["bought"]:
        item["bought"] = checked
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(projects, f, ensure_ascii=False, indent=2)
        st.rerun()