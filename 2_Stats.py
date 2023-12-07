import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Rio Crime",
                   page_icon=":knife:")

final_df = pd.read_csv('final_df.csv')

selection_box = st.sidebar.selectbox(
    "Select the type of crime you wish to analyse",
    ("Attempted Murder", "Rape", "Missing People", "Homicides", "Thefts", "Kidnapping", "Total Crime")
)

st.title("Historical Data")

if selection_box == "Attempted Murder":
    st.image('Plot Murders.png', use_column_width=True)
    st.write("There has been an increase of 7% in attempted murders between 2003 and 2018, alongside a notable decrease of 20% from 2015 to 2018 following a substantial increase of 61% between 2013 and 2015.")
elif selection_box == "Rape":
    st.image('Plot Rapes.png', use_column_width=True)
    st.write("Between 2003 and 2018, there was a 79% increase in reported rape cases. Notably, there was a 17% decrease in occurrences from 2012 to 2018.")
elif selection_box == "Missing People":
    st.image('Plot missing people.png', use_column_width=True)
    st.write("Across the period from 2003 to 2018, there was a marginal decrease of 3% in missing persons cases. This decline becomes significant considering the substantial 50% increase between 2003 and 2015, followed by a notable 35% decrease in the last 3 years observed.")
elif selection_box == "Homicides":
    st.image('Plot homicides.png', use_column_width=True)
    st.write("Remarkably positive trends were observed in homicide rates during the analyzed period, showcasing a significant 39% decrease. However, it's essential to note the recent increase of 29% in the last 3 years.")
elif selection_box == "Thefts":
    st.image('Plot theft.png', use_column_width=True)
    st.write("Theft cases exhibited a notable 43% increase, making it a crucial concern for visitors. It emphasizes the necessity to exercise extra caution regarding personal belongings when visiting Rio.")
elif selection_box == "Kidnapping":
    st.image('Plot kidnapping.png', use_column_width=True)
    st.write("Despite being the smallest in total numbers, the alarming 353% increase in kidnapping cases from 2003 to 2018 highlights its significant impact on safety and security.")
elif selection_box == "Total Crime":
    st.image('Plot total crime.png', use_column_width=True)
    st.write("This overview represents the collective summary of all the various crime types. Notably, it bears similarity to theft cases, which dominate the majority of reported crimes.")


st.markdown("---")

st.title("Interactive Crime Analysis")

def create_bar_chart(data, selected_year, selected_crime, selected_area):
    filtered_data = data[(data['Year'] == selected_year) & (data['Area'] == selected_area)]
    crimes_by_type = filtered_data[selected_crime].sum()

    fig = px.bar(x=[selected_crime], y=[crimes_by_type],
                 labels={'x': 'Crime Type', 'y': 'Total Crimes'},
                 title=f'Total {selected_crime} in {selected_area} for {selected_year}')

    fig.update_layout(bargap=0.8)
    st.plotly_chart(fig)

data = pd.read_csv('final_df.csv')

years = data['Year'].unique().tolist()
crime_types = ['Attempted murder', 'Rape', 'Missing people', 'Homicides', 'Thefts', 'Kidnapping']
areas = data['Area'].unique().tolist()

selected_year = st.selectbox('Select Year', years)
selected_crime = st.selectbox('Select Crime Type', crime_types)
selected_area = st.selectbox('Select Area', areas)

create_bar_chart(data, selected_year, selected_crime, selected_area)