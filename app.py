import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('./cleaned_vehicles_us.csv')
st.title("Web Application Dashboard")
st.header('Vehicle types manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')
st.write(fig)
st.write('The three most popular used cars listed are Ford trucks, followed by Chevrolet trucks, and Jeep SUVs. Sedans do not feature in the top 3 vehicle categories sold.')
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
fig = px.histogram(df,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
st.write(fig)
st.header('Conclusion')
st.write('By looking at the used car market, the newest cars and the oldest cars have the highest pricepoints, with cars tending to lose around $10,000 for every 20,000 miles driven. Antique cars fetch mutch higher prices than even the most modern cars. Finally, this dataset confirms the United States love affair with trucks and SUVs, as they are among the most listed vehicles.')