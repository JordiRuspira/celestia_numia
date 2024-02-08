import pandas as pd
import plotly.express as px

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("celestia.csv", sep=",")
df.dropna(subset=["transformed_date"], inplace=True)

# Group by and aggregate 
grouped_df_fees = df.groupby(["transformed_date", "namespace_value"])["total_fees"].sum().reset_index()
grouped_df_mb = df.groupby(["transformed_date", "namespace_value"])["mb_posted"].sum().reset_index()


# Plot a bar chart
fig = px.bar(grouped_df_fees, x="transformed_date", y="total_fees", color="namespace_value",
             title="Bar Chart of total fees (in TIA) by date and encoded namespace",
             labels={"transformed_date": "Date", "total_fees": "Total fees (TIA)"})
fig.show()

fig = px.bar(grouped_df_mb, x="transformed_date", y="mb_posted", color="namespace_value",
             title="Bar Chart of data posted to blobs (in MB) by date and encoded namespace",
             labels={"transformed_date": "Date", "mb_posted": "MB"})
fig.show()