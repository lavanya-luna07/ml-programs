import csv

concepts = []
with open("candidate_data.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        concepts.append(row)

# Initialize S and G
S = ['0']* (len(concepts[0])-1)
G = [['?']* (len(concepts[0])-1)]

for instance in concepts:
    attrs = instance[:-1]
    label = instance[-1]

    if label == 'Yes':
        for i in range(len(S)):
            if S[i]=='0':
                S[i]=attrs[i]
            elif S[i]!=attrs[i]:
                S[i]='?'
        G = [g for g in G if all(g[i]=='?' or g[i]==S[i] for i in range(len(S)))]
    else:
        new_G=[]
        for g in G:
            for i in range(len(attrs)):
                if g[i]=='?' and S[i]!=attrs[i]:
                    temp = g.copy()
                    temp[i]=S[i]
                    new_G.append(temp)
        G=new_G

print("Final Specific Hypothesis:", S)
print("Final General Hypothesis:", G)
