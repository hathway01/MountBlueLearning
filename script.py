import matplotlib.pyplot as plt

import csv

with open('ipl/matches.csv') as csvfile:
   	reader = csv.reader(csvfile,delimiter=",")
   	dict={}
   	next(reader);
   	for row in reader:
   		if row[1] not in dict:
   			dict[row[1]]=1
   		else:
   			dict[row[1]]+=1

 	
years = list(dict.keys())
matches = list(dict.values())

plt.bar(range(len(dict)),matches,tick_label=years)
#plt.savefig('bar.png')
plt.show()