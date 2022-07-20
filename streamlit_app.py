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
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
