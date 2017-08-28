import random
import string

letters = [string.ascii_letters]
letters.append(' ')
alphabet = ''.join(letters)

class Individual:
    def __init__(self, target):
        self.target = target
        self.dna = self.generate_new(target)
        self.fitness = self.get_fitness(target)

    def __str__(self):
        return self.dna

    def generate_new(self, target):
        word = []
        for i in range(len(target)):
            letter = random.choice(alphabet)
            word.append(letter)
        return ''.join(word)

    def get_fitness(self, target):
        score = 0
        for i in range(len(target)):
            if target[i] == self.dna[i]:
                score += 1
        #return (score / len(target))
        return score

    def reproduce(self, partner):
        child = Individual(self.target)
        new_dna = []
        for i in range(len(self.target)):
            number = random.random()
            if(number > 0.5):
                new_dna.append(self.dna[i])
            else:
                new_dna.append(partner.dna[i])
        new_dna = ''.join(new_dna)
        child.dna = new_dna
        child.fitness = child.get_fitness(self.target)
        return child

    def mutate(self, mutation):
        new_dna = []
        for i in range(len(self.dna)):
            letter = random.random()
            if letter < mutation:
                new_dna.append(random.choice(alphabet))
            else:
                new_dna.append(self.dna[i])
        self.dna = ''.join(new_dna)
        return self
