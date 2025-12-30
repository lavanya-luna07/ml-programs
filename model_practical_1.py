import csv
import random
import statistics


sales = []
ads = []

with open("sales_data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        sales.append(float(row[0]))
        ads.append(float(row[1]))


print("First 5 rows:")
for i in range(5):
    print("Sales:", sales[i], "Advertising:", ads[i])


print("\nStatistics:")
print("Sales Mean:", statistics.mean(sales))
print("Sales Min:", min(sales), "Max:", max(sales))
print("Advertising Mean:", statistics.mean(ads))


print("\nNull Values:")
print("Sales:", sales.count(None))
print("Advertising:", ads.count(None))


data = list(zip(ads, sales))
random.shuffle(data)
split = int(0.8*len(data))
train = data[:split]
test = data[split:]

X_train = [x for x,y in train]
y_train = [y for x,y in train]
X_test = [x for x,y in test]
y_test = [y for x,y in test]


x_mean = statistics.mean(X_train)
y_mean = statistics.mean(y_train)
m = sum((X_train[i]-x_mean)*(y_train[i]-y_mean) for i in range(len(X_train))) / sum((X_train[i]-x_mean)**2 for i in range(len(X_train)))
c = y_mean - m*x_mean

print("\nLinear Regression Equation: y = {:.2f}x + {:.2f}".format(m,c))

print("\nTest Predictions:")
for i in range(len(X_test)):
    pred = m*X_test[i]+c
    print("Advertising:", X_test[i], "Predicted:", round(pred,2), "Actual:", y_test[i])

