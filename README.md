# Frameworks Assignment: CORD-19 Data Explorer

## Overview
This project explores the CORD-19 research dataset (`metadata.csv`) and provides:
- Data exploration and cleaning
- Basic visualizations
- A simple **Streamlit app** for interactive exploration

## Repo Structure
`analysis.ipynb` → Jupyter notebook with data cleaning, analysis, and visualizations.
- `app.py` → Streamlit web app for interactive data exploration.
- `requirements.txt` → List of dependencies.
- `README.md` → Documentation.

How to Run
1. Clone this repository:
   ```bash
   git clone <your_repo_url>
   cd Frameworks_Assignment

          Install requirements:
pip install -r requirements.txt

from the official CORD-19 Kaggle dataset
.

After downloading, place the file into this folder: frameworks_assignement/data/metadata.csv


           Run Streamlit app:
streamlit run app.py

Open the link provided in your terminal to view the app in your browser.

📊 Features

Publications over time (line chart)

Top journals (bar chart)

Word cloud of paper titles

Top data sources (bar chart)

Interactive year filter

Sample data table

📝 Reflection

Challenges: Handling missing values (many abstracts/titles missing).

Learning: Practiced data cleaning, basic visualization, and building an interactive app with Streamlit.