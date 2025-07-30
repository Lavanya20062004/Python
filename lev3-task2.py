import pandas as pd
import plotly.express as px

# Load the CSV file you just created
df = pd.read_csv("data.csv")

# Create an interactive bar chart
fig = px.bar(df, x="Name", y="Score", title="Scores of Students")
fig.show()