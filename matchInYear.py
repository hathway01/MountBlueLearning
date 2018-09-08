import matplotlib.pyplot as plt
from sortedcontainers import SortedDict


import csv

with open('ipl/matches.csv') as csvfile:
	matches_reader = csv.reader(csvfile,delimiter=",")
	matches_per_season={}
	# Skipping the first line because it was the metadata(header)
	next(matches_reader);
	season_column = 1
	for match in matches_reader:
	    if match[season_column] not in matches_per_season:
	        matches_per_season[match[season_column]]=1
	    else:
	        matches_per_season[match[season_column]]+=1

	matches_per_season=SortedDict(matches_per_season)
	years = list(matches_per_season.keys())
	matches = list(matches_per_season.values())
#print(dict.items(),"\n",)


plt.bar(years,matches)
plt.title("Matches played per Year")
plt.ylabel("Matches")
plt.xlabel("Year")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom= 0.2)
plt.show()