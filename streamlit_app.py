import streamlit
import snowflake.connector
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Idli, Dosa, Upma, Vada')
streamlit.text('🥑🍞Idli,Masala Dosa,Semya Upma,Vada')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
#streamlit.dataframe(my_fruit_list)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_show)
import requests
streamlit.header('Fruityvice Advice')
fruityvice_input = streamlit.text_input('What fruit would you like information about?' , 'kiwi')
streamlit.write('User entered input', fruityvice_input)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"  + fruityvice_input )
#streamlit.text(fruityvice_response.json())
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalize)

#snowflake connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
add_my_fruit = streamlit.text_input('What fruit would you like to add' , 'jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
