from population import Population
import random
import sys

if len(sys.argv) == 2:
    foundTarget = False
    target = sys.argv[1]
    n = 200
    mutation_rate = 0.01
    generation = 0

    population = Population(target, n, mutation_rate)

    while not foundTarget:
        pool = []
        for member in population.members:
            if(member.dna == target):
                foundTarget = True
                break
            for i in range(int(member.fitness)):
                    pool.append(member)

        if not foundTarget:
            for i in range(len(population.members)):
                index = int(random.random()*len(pool))
                parentA = pool[index]
                index = int(random.random()*len(pool))
                parentB = pool[index]
                child = parentA.reproduce(parentB)
                child = child.mutate(mutation_rate)
                print(child.dna + ' ' + str(int(child.fitness/len(target)*100)) + "%")
                population.members[i] = child
            generation += 1

    print()
    print("************ GENERATION: " + str(generation) + " ************")
    print("************ FINAL POPULATION ************")
    population.members.sort(key=lambda x: x.fitness, reverse=True) #redundant
    population.print_()
else:
    print("Please pass exactly one string as an argument.")
