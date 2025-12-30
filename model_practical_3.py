import csv
import random
import math

# Read CSV
X=[]
y=[]
with open("logistic_data.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        # Scale age by 100, salary by 1000 to prevent overflow
        X.append([float(row[0])/100.0, float(row[1])/1000.0])
        y.append(int(row[2]))

# Train-test split (80-20)
data=list(zip(X,y))
random.shuffle(data)
split=int(0.8*len(data))
train=data[:split]
test=data[split:]

X_train=[x for x,y in train]
y_train=[y for x,y in train]
X_test=[x for x,y in test]
y_test=[y for x,y in test]


w=[0.0,0.0]
b=0.0
lr=0.1   
epochs=500


def sigmoid(z):

    if z < -700: z = -700
    if z > 700: z = 700
    return 1/(1+math.exp(-z))


for _ in range(epochs):
    dw=[0]*2
    db=0
    for i in range(len(X_train)):
        z=sum([w[j]*X_train[i][j] for j in range(2)])+b
        pred=sigmoid(z)
        error=pred-y_train[i]
        for j in range(2):
            dw[j]+=error*X_train[i][j]
        db+=error
    for j in range(2):
        w[j]-=lr*dw[j]
    b-=lr*db

print("\nWeights:", w, "Bias:", b)

print("\nTest Predictions:")
for i in range(len(X_test)):
    z=sum([w[j]*X_test[i][j] for j in range(2)])+b
    pred=sigmoid(z)
    pred_label=1 if pred>=0.5 else 0
    print("Input:", X_test[i], "Predicted:", pred_label, "Actual:", y_test[i])
