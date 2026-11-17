import streamlit as st
import json
st.title("Mit DIY-dashboard")
st.write("Velkommen til mit DIY-dashboard!")
with open("data.json", "r", encoding="utf-8") as f:
    items = json.load(f)
for item in items:
    checked = st.checkbox(item["name"], value=item["bought"])
    st.caption(f"{item['quantity']} × {item['unit']} · {item['price']},-  · {item['store']}")
    if checked != item["bought"]:
        item["bought"] = checked
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)