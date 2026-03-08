import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)

print(tables)

matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

print(matches.head())

result1 = pd.read_sql("""SELECT AVG(WIN_MARGIN), MATCH_WINNER
                        FROM Match
                        GROUP BY MATCH_WINNER
                        ORDER BY AVG(WIN_MARGIN);""", conn)

print(result1)

result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_id)
                        FROM Match
                        Where Season_id == 9;""", conn)

print(result2)

result3 = pd.read_sql("""SELECT MIN(WIN_MARGIN), MAX(WIN_MARGIN),AVG(WIN_MARGIN),COUNT(DISTINCT(Man_of_the_Match))
                        FROM Match;""", conn)

print(result3)

result4 = pd.read_sql("""SELECT Sum(WIN_MARGIN)
                        FROM Match
                        Where Season_id == 9;""", conn)

print(result4)
                      
                      













