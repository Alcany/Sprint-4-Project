import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
df = pd.read_csv('./cleaned_vehicles_us.csv')
st.title("Web Application Dashboard")
st.write('This project aims to explore a dataset of about 50k used car advertisements.')
df['manufacturer'] = df['model'].apply(lambda x: 
x.split()[0])
st.header('Data viewer')
st.dataframe(df)
st.header('Distribution of Car Prices')
price_bins = pd.cut(df['price'], bins=[0, 5000, 10000, 15000, float('inf')],
                    labels=["Low", "Moderate", "High", "Very High"])
price_distribution = price_bins.value_counts()
plt.figure(figsize=(10, 6))
plt.legend(title="Price Categories")
sns.barplot(x=price_distribution.index, y=price_distribution.values, palette="viridis")
plt.title('Distribution of Car Prices')
plt.xlabel('Price Range')
plt.ylabel('Count of Cars')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)
st.write('The prices of the cars appear to be fairly varied. With such a large inventory of vehicles, many pricepoints are represented.')
st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)
st.write('The three most popular used cars listed are Ford trucks, followed by Chevrolet trucks, and Jeep SUVs. Sedans do not feature in the top 3 vehicle categories sold.')
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
st.pyplot(plt)
st.header('Vehicle types manufacturer')
fig = px.histogram(df, x='type', color='price')
st.write(fig)
st.pyplot(plt)
st.header('Conclusion')
st.write('By looking at the used car market, the newest cars and the oldest cars have the highest pricepoints, with cars tending to lose around $10,000 for every 20,000 miles driven. Antique cars fetch mutch higher prices than even the most modern cars. Finally, this dataset confirms the United States love affair with trucks and SUVs, as they are among the most listed vehicles.')