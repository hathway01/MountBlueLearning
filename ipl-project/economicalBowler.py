import matplotlib.pyplot as plt
import collections
import csv

matches_file = csv.DictReader(open("ipl/matches.csv"))
match_ids=[]
for match in matches_file:    
    if(int(match["season"])==2015):
        match_ids.append(match["id"])

bowler_record={}

deliveries_file = csv.DictReader(open("ipl/deliveries.csv"))
total_run_coloumn=0
total_ball_coloumn=1
for delivery in deliveries_file:
    if delivery["match_id"] in match_ids:
        if delivery["bowler"] not in bowler_record:
            bowler_record[delivery["bowler"]]=[]
            bowler_record[delivery["bowler"]].append(int(delivery["total_runs"]))
            bowler_record[delivery["bowler"]].append(1)
        else:
            bowler_record[delivery["bowler"]][total_run_coloumn]+=int(delivery["total_runs"])
            bowler_record[delivery["bowler"]][total_ball_coloumn]+=1
          
            
for bowler in bowler_record:
    bowler_record[bowler]=round((bowler_record[bowler][total_run_coloumn]/bowler_record[bowler][total_ball_coloumn])*6,2)

bowler_record = sorted(bowler_record.items(), key=lambda x: x[1])

merit_Size=10
for (ith_bowler,bowler) in zip(range(1,merit_Size+1),bowler_record):
    plt.bar(bowler[0],bowler[1])

plt.xticks(rotation=90)
plt.xlabel("Bowlers")
plt.ylabel("Run-rate")
plt.title("Top economical bowlers")
plt.show() 
        