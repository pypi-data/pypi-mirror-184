import csv

with open("3new.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

specific = data[1][:-1]
general = [['?' for i in range(len(specific))] for j in range(len(specific))]

for index,i in enumerate(data):
    if i[-1] == "Yes":
        for j in range(len(specific)):
            if i[j] != specific[j]
                specific[j] = "?"
                general[j][j] = "?"

    elif i[-1] == "No":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                general[j][j] = specific[j]
            else:
                general[j][j] = "?"

    print("\nStep " + str(index) + " of Candidate Elimination Algorithm")
    print(specific)
    print(general)

#gh = [] # gh = general Hypothesis
#for i in general:
#    for j in i:
#        if j != '?':
#            gh.append(i)
#            break
gh = [i for i in general if len(set(i)) != 1]
print("\nFinal Specific hypothesis:\n", specific)
print("\nFinal General hypothesis:\n", gh)
