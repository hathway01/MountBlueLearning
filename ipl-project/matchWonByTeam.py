import matplotlib.pyplot as plt

import csv
plt.style.use('ggplot')

with open('ipl/matches.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=",")
    matrix={}
    teams=[]
    years=[]
    next(reader)
    for row in reader:
        if row[10] not in teams and len(row[10])>0:
            teams.append(row[10])
        if row[1] not in years:
            years.append(row[1])
        if row[1] not in matrix:
            matrix[row[1]]={}
        if len(row[10])>0:
            if row[10] not in matrix[row[1]]:
                matrix[row[1]][row[10]]=1
            else:
                matrix[row[1]][row[10]]+=1
    
    years.sort()
    result={}
    for team in teams:
        record=[]
        for year in years:
            if team not in matrix[year]:
                matrix[year][team]=0
            record.append(matrix[year][team])
        result[team]=record

    for team in result:
        print(team,":",result[team])
        plt.bar(years,result[team],0.8,label=team)
    plt.xticks(rotation=90)
    plt.show()

