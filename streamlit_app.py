import pandas
import streamlit as st
import requests
import snowflake.connector

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
my_fruit_list = my_fruit_list.set_index('Fruit')

st.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
st.header("Fruityvice Fruit Advice!")
st.text(fruityvice_response)
# st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)


