import pandas
import streamlit as st
import requests
import snowflake.connector
from urllib.error import URLError
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
st.header('Fruityvice Fruit Advice')

try:
   fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
   if not fruit_choice:
        st.error('Please select a frut to get information.')
   else:
        st.write('The user entered ', fruit_choice)
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
        # st.header("Fruityvice Fruit Advice!")
        st.text(fruityvice_response)
        # st.text(fruityvice_response.json())
        
        # write your own comment -what does the next line do? 
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        # write your own comment - what does this do?
        st.dataframe(fruityvice_normalized)
except URLError as e:
    st.error()  



st.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
st.text("The Fruit load list contains:")
st.text(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like Choose?')
st.text("Thanks for adding "+add_my_fruit)

my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")
