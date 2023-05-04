import pandas
import streamlit as st

# set the app's title
st.title("My Parents healthy Diner")
 
# header
st.header("Breakfast Menu")

st.text(" 🥣 Omega 3 & Blueberry Oatmeal")
st.text(" 🥗 Kale , Spinach & Rocket Smmothie")
st.text("🐔 Hard-Boiled Free Ege")
st.text("🥑🍞 Avocado Toast")
 

st.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.dataframe(my_fruit_list)
