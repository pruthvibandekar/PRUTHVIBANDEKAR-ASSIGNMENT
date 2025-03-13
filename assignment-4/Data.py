import pandas as pd

# Load the CSV file using the full path
df = pd.read_csv(r'assignment-4/2021_CEV_Data__Current_Population_Survey_Civic_Engagement_and_Volunteering_Supplement.csv',header=None)
# Display the first few rows of the dataset
print(df.head())