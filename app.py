import streamlit as st
st.title("Mit DIY-dashboard")
st.write("Velkommen til mit DIY-dashboard!")
item = {
    "name": "Skruer",
    "quantity": 100,
    "price": 0.05,
    "store": "Bauhaus",
    "url": "https://www.bauhaus.dk/skruer",
    "verified": False,
    "bought": False,
}
st.write(item)