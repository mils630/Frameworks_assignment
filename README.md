# CORD-19 Data Explorer

This project is a simple Streamlit app for exploring a sample of the CORD-19 COVID-19 research papers dataset.

Streamlit app link: 
https://mils630-frameworks-assignment-app-5fbqrp.streamlit.app/
NOTE: this app is running on a smaple metadata.csv and not the full data, this is purely optional and users can use the the full metadata.csv but in chunks.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/mils630/Frameworks_Assignment.git
cd Frameworks_Assignment
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Friendly Reminder

- The full `metadata.csv` is **not included** because it is very large.  
- Use `data/sample_metadata.csv` for testing and deployment.  
- Make sure your virtual environment is active when running the app.
