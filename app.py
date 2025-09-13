# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# --- Title ---
st.title("CORD-19 Data Explorer")
st.write("Exploring COVID-19 research papers dataset")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv", low_memory=False)
    # Convert publish_time to datetime
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    # Abstract word count
    df['abstract_length'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

df = load_data()

# --- Display Data ---
st.subheader("Dataset Preview")
num_rows = st.slider("Select number of rows to view", 5, 20, 10)
st.dataframe(df.head(num_rows))

# --- Publications over time ---
st.subheader("Number of Publications by Year")
year_counts = df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values, color='skyblue')
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
ax1.set_title("Publications per Year")
st.pyplot(fig1)

# --- Top Journals ---
st.subheader("Top 10 Journals Publishing COVID-19 Research")
top_journals = df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
ax2.barh(top_journals.index[::-1], top_journals.values[::-1], color='lightgreen')
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
ax2.set_title("Top 10 Journals")
st.pyplot(fig2)

# --- Word Cloud of Titles ---
st.subheader("Word Cloud of Paper Titles")
text = " ".join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# --- Abstract Length Distribution ---
st.subheader("Distribution of Abstract Length")
fig4, ax4 = plt.subplots()
sns.histplot(df['abstract_length'], bins=20, kde=True, ax=ax4, color='orange')
ax4.set_xlabel("Abstract Length (words)")
ax4.set_ylabel("Number of Papers")
st.pyplot(fig4)

# --- Scatter: Abstract Length vs Year ---
st.subheader("Abstract Length vs Publication Year")
fig5, ax5 = plt.subplots()
ax5.scatter(df['year'], df['abstract_length'], alpha=0.6, color='purple')
ax5.set_xlabel("Year")
ax5.set_ylabel("Abstract Length (words)")
st.pyplot(fig5)

# --- Filter by Year ---
st.subheader("Filter Papers by Year")
years_selected = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered_df = df[(df['year'] >= years_selected[0]) & (df['year'] <= years_selected[1])]
st.write(f"Number of papers in selected range: {len(filtered_df)}")
st.dataframe(filtered_df.head(20))
