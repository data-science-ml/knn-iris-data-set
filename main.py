from knn import Knn
from vector import Vector

model = Knn()

with open('data/train.csv') as f:
    for line in f:
        data = line.strip().split(',')
        vector = Vector(*map(float, data[:4]))
        species = data[-1]
        model.train(vector, species)

experiments = []
with open('data/test.csv') as f:
    for line in f:
        data = line.strip().split(',')
        vector = Vector(*map(float, data[:4]))
        species = data[-1]
        prediction = model.predict(vector, 3)
        experiments.append(species == prediction)

accuracy = sum(experiments) / len(experiments)
print('accuracy:', accuracy)
