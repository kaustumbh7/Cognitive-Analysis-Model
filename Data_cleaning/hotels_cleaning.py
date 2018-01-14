import pandas as pd

#Reads the csv file and stores it in a dataframe
df = pd.read_csv('hotels.csv')

#Unnecessary columns removed
df.drop(['uniq_id','url','restaurant_id','restaurant_location','category','author','author_url','location'], axis=1, inplace=True)

print(df.head())
