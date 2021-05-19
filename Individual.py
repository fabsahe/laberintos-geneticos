import random
import math

class Individual:

  MAX_FITNESS = 100

  """Estos posibles genes que puede tener un individuo corresponden con una direccion de movimiento.
     N = North E = East S = South W = West"""
  POSSIBLE_GENES = ["N", "E", "S", "W"]

  """GENE_LENGTH debe ser uno mas la cantidad minima de movimientos necesarios para llegar al final 
     del laberinto. Esto permitira que el algoritmo calcule la aptitud de un individuo cuando se 
     encuentra al final del laberinto."""
  GENE_LENGTH = 9

  def __init__(self):
    self.fitness = 0
    self.genes = []

    for x in range(Individual.GENE_LENGTH):
        self.genes.append(random.choice(Individual.POSSIBLE_GENES))

  """Calcula la magnitud de la distancia entre la ubicacion actual y el final de la ubicacion 
     del laberinto. Cuanto menor sea la magnitud, mas cerca estara la ubicacian actual del final 
     del laberinto. Por lo tanto, cuanto menor sea la magnitud, mayor sera la puntuacion de 
     aptitud que recibira el individuo."""
  def CalFitness(self, curLoc, endLoc, maxMag):
      x = curLoc[0] - endLoc[0]
      y = curLoc[1] - endLoc[1]

      x = x ** 2
      y = y ** 2

      mag = math.sqrt(x + y)
      fitMod = 1.0 - (mag / maxMag)
      fitness = Individual.MAX_FITNESS * fitMod
      fitness = int(round(fitness))

      self.fitness = fitness


  def MutateGene(self, index):
      self.genes[index] = random.choice(Individual.POSSIBLE_GENES)

  def CopyGenes(self, otherIndividual):

      for x in range(Individual.GENE_LENGTH):
          self.genes[x] = otherIndividual.genes[x]

      self.fitness = otherIndividual.fitness

  def PrintGenes(self):

      count = 0
      geneOutput = ""

      for item in self.genes:
          geneOutput += str(count) + ":" + item + " "
          count += 1

      return geneOutput
