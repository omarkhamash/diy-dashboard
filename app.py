import streamlit as st
st.title("Mit DIY-dashboard")
st.write("Velkommen til mit DIY-dashboard!")
items = [
    {
    "name": "Skruer",
    "unit": "100 stk",
    "quantity": 2,
    "price": 28.05,
    "store": "Bauhaus",
    "url": "https://www.bauhaus.dk/skruer",
    "verified": False,
    "bought": False,
},
{
    "name": "Maling",
    "unit": "5 liter",
    "quantity": 1,
    "price": 150.0,
    "store": "Silvan",
    "url": "https://www.silvan.dk/maling",
    "verified": False,
    "bought": False,
},
{
    "name": "Trælim",
    "unit": "500 ml",
    "quantity": 1,
    "price": 12.5,
    "store": "Harald Nyborg",
    "url": "https://www.harald-nyborg.dk/traelim",
    "verified": False,
    "bought": False,
    }
]
st.write(items)
st.write(items[2]["price"])