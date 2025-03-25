import pandas as pd

df= pd.read_csv('./data/transformed_players_data.csv')

busquets_stats = df[df['name']== 'Sergio Busquets'].select_dtypes(include=['float64', 'int64']).iloc[0]

def is_similar(row, busquets_stats, tolerance):
    for stat in busquets_stats.index:
        if abs(row[stat] - busquets_stats[stat])>tolerance:
            return False
    return True

similar_players= df[df['name'] != 'Sergio Busquets']
similar_players= similar_players[similar_players.apply(is_similar, axis=1, busquets_stats=busquets_stats, tolerance=0.3)]

similar_players.to_csv('./data/similar_player_to_busquets.csv', index= False)

print(similar_players)