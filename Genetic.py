from Population import Population
from Individual import  Individual
import random

class Genetic:

    def __init__(self, mutationRate):

        self.population = Population(10)
        self.mutationRate = mutationRate
        self.fittest = None
        self.secondFittest = None
        self.genCount = 0

    def MainProcess(self, maze):
        self.population.CalFitForWholePop(maze)
        print("Generacion: " + str(self.genCount) + " Fitness: " + str(self.population.fittest))

        while(self.population.fittest < Individual.MAX_FITNESS):
            self.genCount += 1

            self.Selection()
            self.CrossOver()

            if random.uniform(0, 1) <= self.mutationRate:
                self.Mutation()

            self.AddFittestOffspring(maze)
            self.population.CalFitForWholePop(maze)
            print("Generacion: " + str(self.genCount) + " Fitness: " + str(self.population.fittest) +
                  " Genes: " + self.population.FindTheFittest().PrintGenes())

        print("Solucion encontrada en la generacion " + str(self.genCount))
        print("Fitness: " + str(self.population.FindTheFittest().fitness))
        print("Genes: " + self.population.FindTheFittest().PrintGenes())

    # Elige a los dos individuos mas aptos para el proceso de cruza.
    def Selection(self):

        self.fittest = self.population.FindTheFittest()
        self.secondFittest = self.population.FindTheSecoundFittest()

    """
    Elige un punto aleatorio en la lista de genes de un individuo e intercambia los genes de 
    los dos individuos mas aptos, hasta ese punto.
    """
    def CrossOver(self):

        crossPoint = random.randint(0, Individual.GENE_LENGTH - 1)

        for i in range(crossPoint):
            temp = self.fittest.genes[i]
            self.fittest.genes[i] = self.secondFittest.genes[i]
            self.secondFittest.genes[i] = temp

    """Si se produce una mutacion, esta funcion elige un punto aleatorio en la lista de genes 
       de un individuo y aleatoriza todos los genes hasta ese punto."""
    def Mutation(self):

        mutaionPoint = random.randint(0, Individual.GENE_LENGTH - 1)

        self.fittest.MutateGene(mutaionPoint)

        mutaionPoint = random.randint(0, Individual.GENE_LENGTH - 1)

        self.secondFittest.MutateGene(mutaionPoint)

    def FindFittestOffspring(self):

        if self.fittest.fitness > self.secondFittest.fitness:
            return self.fittest

        return self.secondFittest

    """Encuentra al individuo menos apto y lo reemplaza con la descendencia mas apta."""
    def AddFittestOffspring(self, maze):

        maze.RunGenesThroughMaze(self.fittest)
        maze.RunGenesThroughMaze(self.secondFittest)

        leastFit = self.population.FindLeastFittest()
        leastFit.CopyGenes(self.FindFittestOffspring())





