
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
data = pd.read_csv("country_profile_variables.csv")
if st.checkbox('Show Raw Data'):
    data

options = data['Region'].unique().tolist()
selected_options = st.sidebar.multiselect('Chose a Region',options)
filtered_data = data[data["Region"].isin(selected_options)]
min_Population, max_Population = st.sidebar.slider('Population in thousands', 0,1410000,(0,1410000))

df = filtered_data[filtered_data['Population'].between(min_Population, max_Population)]
if st.checkbox('Show Filtered Raw Data'):
    df
"The number of filtered data samples: ", df.shape[0]

fig, ax =plt.subplots()

ax.bar(df['country'], height = df['GDPP'])
ax.set_ylabel("GDP Per Capita (USD)")
plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

plt.tight_layout()
st.pyplot(fig)
