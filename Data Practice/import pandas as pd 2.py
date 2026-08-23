import pandas as pd 

#Going to put a link here for a live CSV
csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

data = pd.read_csv(csv_url)

#Going now use Pandas to fetch and read the file instantly
df = pd.read_csv(csv_url)

#View the top 5 rows only 
print("--- First 5 Rows of the Dataset ---")
print(df.head())
#Count how many flowers of each species are there in the dataset
print("\n--- Count of Each Species ---")
print(df['species'].value_counts())
