import csv
import matplotlib.pyplot as plt

matches_file = csv.DictReader(open("ipl/matches.csv"))
players={}
total_matches=0
cities={}
umpires={}

for match in matches_file:
    if match["player_of_match"] not in players:
        players[match["player_of_match"]]=1
    else:
        players[match["player_of_match"]]+=1
    total_matches+=1

    if match["city"] not in cities:
        cities[match["city"]]=1
    else:
        cities[match["city"]]+=1



top_players={}

top_players['Others']=0
for player in players:
    if players[player]>13:
        top_players[player]=(players[player]/total_matches)*100
    else:
        top_players['Others']+=1
top_players['Others']=(top_players['Others']/total_matches)*100

top_cities={}

top_cities['Others']=0
for city in cities:
    if cities[city]>13:
        top_cities[city]=(cities[city]/total_matches)*100
    else:
        top_cities['Others']+=1
top_cities['Others']=(top_cities['Others']/total_matches)*100


fig,(chart1,chart2) = plt.subplots(2, 1,figsize=(50,50))
chart1.pie(top_players.values(),labels=top_players.keys(), autopct='%1.1f%%')
chart1.axis("equal")
chart1.set_title("Men Of The Match Distribution")

chart2.pie(top_cities.values(),labels=top_cities.keys(), autopct='%1.1f%%')
chart2.axis("equal")
chart2.set_title("Match Location Distribution")


plt.show()