import pandas as pd

from sklearn.preprocessing import MinMaxScaler

df= pd.read_csv('./data/fifa_players.csv')

df = df[['name', 'positions', 'body_type', 'short_passing', 'dribbling', 'long_passing', 
         'ball_control', 'agility', 'reactions', 'balance', 'stamina', 'interceptions', 
         'positioning', 'vision', 'composure', 'marking', 'standing_tackle']]

df = df[df['positions'].str.contains('CM|CDM|CB', na=False)]


numeric_cols=['short_passing', 'dribbling', 'long_passing', 
         'ball_control', 'agility', 'reactions', 'balance', 'stamina', 'interceptions', 
         'positioning', 'vision', 'composure', 'marking', 'standing_tackle']
df[numeric_cols]=df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df[numeric_cols]= df[numeric_cols].fillna(df[numeric_cols].mean())
scalar=MinMaxScaler()
df[numeric_cols]= scalar.fit_transform(df[numeric_cols])

print(df.head())

df.to_csv('./data/transformed_players_data.csv', index=False)
