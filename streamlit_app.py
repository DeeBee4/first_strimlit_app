import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Healthy Menu')
streamlit.header('_________________')
streamlit.text('| 🥚 Eggs Benedict         - 3 EUR')
streamlit.text('| 🥚 Mushroom Omelette     - 3 EUR')
streamlit.text('| 🥑 Guacamole             - 2 EUR')
streamlit.text('| 🥑 Avocado Toast         - 2 EUR')
streamlit.text('| ☕ Cold Brew Coffee      - 2 EUR')
streamlit.text('| ☕ Espresso              - 1 EUR')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(fruityvice_response.json()) # deactivated this line as it only writes the data to the screen

# the below line normalizes the JSON response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# the below line takes the normalized JSON and show it as a table
streamlit.dataframe(fruityvice_normalized)
