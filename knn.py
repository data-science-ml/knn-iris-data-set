from collections import Counter


class Knn:
    def __init__(self):
        self.vectors = []
        self.species = []

    def train(self, vector, species):
        self.vectors.append(vector)
        self.species.append(species)

    def predict(self, vector, k):
        lengths = [(vector.scale(-1) + v).norm() for v in self.vectors]
        lenspec = [(length, self.species[i]) for i, length in enumerate(lengths)]
        tuples = sorted(lenspec, key=lambda t: t[0])[:k]
        species = [t[1] for t in tuples]
        counter = Counter(species)
        return counter.most_common(1)[0][0]
