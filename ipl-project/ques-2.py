import matplotlib.pyplot as plt
import csv


with open('ipl/matches.csv') as csvfile:
    matches_reader = csv.DictReader(csvfile, delimiter=",")
    match_won_per_season = {}
    winners = []
    seasons = []
    for match in matches_reader:
        if match["winner"] not in winners and len(match["winner"]) > 0:
            winners.append(match["winner"])
        if match["season"] not in seasons:
            seasons.append(match["season"])
        if match["season"] not in match_won_per_season:
            match_won_per_season[match["season"]] = {}
        if len(match["winner"]) > 0:
            if match["winner"] not in match_won_per_season[match["season"]]:
                match_won_per_season[match["season"]][match["winner"]] = 1
            else:
                match_won_per_season[match["season"]][match["winner"]] += 1
    seasons.sort()
    match_won_in_season = {}
    for winner in winners:
        team_record = []
        for season in seasons:
            if winner not in match_won_per_season[season]:
                match_won_per_season[season][winner] = 0
            team_record.append(match_won_per_season[season][winner])
        match_won_in_season[winner] = team_record

    bottomlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for team in winners:
        if(team == winners[0]):
            plt.bar(seasons, match_won_in_season[team])
        else:
            plt.bar(seasons, match_won_in_season[team], bottom = bottomlist)
        bottomlist = list(map(lambda x,y: x+y,bottomlist, match_won_in_season[team]))
plt.legend(winners,loc='upper right')
plt.show()

