from individual import Individual

class Population:
    members = []
    def __init__(self, target, n, mutation):
        for i in range(n):
            member = Individual(target)
            self.members.append(member)
            self.target = target

    def print_(self):
        average_fitness = 0
        for member in self.members:
            if member.dna == self.target:
                print("********** FOUND ELITE: " + member.dna + " ************")
            else:
                print(member.dna)
            average_fitness += member.fitness
        average_fitness /= len(self.members)
        print("************ average fitness: "+ str(int(average_fitness/len(self.target)*100))+"% ************")
