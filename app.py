import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Exploring COVID-19 research papers dataset")

@st.cache_data
def load_data():
    df = pd.read_csv("data/sample_metadata.csv", low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_length'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

df = load_data()

st.subheader("Dataset Preview")
num_rows = st.slider("Select number of rows to view", 5, 20, 10)
st.dataframe(df.head(num_rows))

st.subheader("Number of Publications by Year")
year_counts = df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values, color='skyblue')
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

st.subheader("Top 10 Journals")
top_journals = df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
ax2.barh(top_journals.index[::-1], top_journals.values[::-1], color='lightgreen')
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

st.subheader("Word Cloud of Paper Titles")
text = " ".join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)
