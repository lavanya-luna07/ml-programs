import csv
from collections import defaultdict

X=[]
y=[]
with open("naive_bayes_data.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        X.append(row[:-1])
        y.append(row[-1])

labels=set(y)
features=len(X[0])
prob = {}
for label in labels:
    prob[label]={}
    count=sum(1 for i in y if i==label)
    prob[label]['prior']=count/len(y)
    for f in range(features):
        prob[label][f]={}
        vals=set(row[f] for row in X)
        for val in vals:
            cnt=sum(1 for i in range(len(X)) if X[i][f]==val and y[i]==label)
            prob[label][f][val]=(cnt+1)/(count+len(vals))  # Laplace smoothing


def predict(row):
    max_prob=-1
    best_label=None
    for label in labels:
        p=prob[label]['prior']
        for f in range(features):
            p*=prob[label][f].get(row[f],1e-6)
        if p>max_prob:
            max_prob=p
            best_label=label
    return best_label

print("Predictions:")
for i,row in enumerate(X):
    print("Input:", row, "Predicted:", predict(row), "Actual:", y[i])
