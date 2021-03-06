# Solving question 3

import matplotlib.pyplot as plt

import csv
plt.style.use('ggplot')

with open('ipl/matches.csv') as csvfile:
    matches_reader = csv.reader(csvfile, delimiter=",")
    next(matches_reader)

    idlist = []
    for match in matches_reader:
        if(int(match[1]) == 2016):
            idlist.append(match[0])
csvfile.close()

result = {}

with open('ipl/deliveries.csv') as csvfile:
    deliveries_reader = csv.reader(csvfile, delimiter=",")
    next(deliveries_reader)
    match_id_index = 0
    for delivery in deliveries_reader:
        if(delivery[match_id_index] in idlist):
            if delivery[3] not in result:
                result[delivery[3]] = int(delivery[16])
            else:
                result[delivery[3]] += int(delivery[16])
csvfile.close()

for team in result:
    plt.bar(team, result[team])

plt.title("Runs Conceded By Teams")
plt.ylabel("Runs")
plt.xlabel("Teams")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
