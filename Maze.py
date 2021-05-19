class Maze:

    def __init__(self):
        """
        I = Inicio del laberinto
        S = Salida del laberinto
        _ = Camino o espacio
        X = Muro
        """
        self.maze = [
            ["_", "_", "X", "X", "_", "X"],
            ["X", "_", "_", "X", "_", "X"],
            ["X", "X", "_", "X", "_", "S"],
            ["X", "_", "_", "_", "_", "X"],
            ["X", "_", "X", "_", "X", "X"],
            ["I", "_", "X", "_", "_", "X"]
        ]

        """
        maxMag es la magnitud del espacio que esta mas lejos del final del laberinto.
        """
        self.maxMag = 6.0

        self.startLocation = self.FindCharLocation("I")
        self.currentLocation = self.startLocation
        self.endLocation = self.FindCharLocation("S")

    def FindCharLocation(self, targetChar):

        for x in range(len(self.maze)):
            for y in range(len(self.maze[x])):
                if self.maze[x][y] == targetChar:
                    return [x, y]

        return None

    def PrintMaze(self):

        for x in self.maze:
            row = ""
            for y in x:
                row += y
                row += " "

            print(row)

    """
        Mueve la posicion actual a traves del laberinto de a cuerdo a la secuencia de genes 
        del individuo. Si self.currentLocation realiza un movimiento no válido, la aptitud 
        del individuo se calcula en función de la distancia actual de self.currentLocation 
        hasta el final del laberinto.
    """
    def RunGenesThroughMaze(self, individual):

        self.currentLocation = self.startLocation

        for aGene in individual.genes:

            possibleMove = None

            if aGene == "N":
                possibleMove = [self.currentLocation[0] - 1, self.currentLocation[1]]
            elif aGene == "E":
                possibleMove = [self.currentLocation[0], self.currentLocation[1] + 1]
            elif aGene == "S":
                possibleMove = [self.currentLocation[0] + 1, self.currentLocation[1]]
            elif aGene == "W":
                possibleMove = [self.currentLocation[0], self.currentLocation[1] - 1]
            else:
                print("Warning! Invalid gene detected: " + aGene)


            if self.CheckForVaildMove(possibleMove):
                self.currentLocation = possibleMove
            else:
                individual.CalFitness(self.currentLocation, self.endLocation, self.maxMag)
                break

    def CheckForVaildMove(self, posibleMove):

        if (posibleMove[0] >= 0 and posibleMove[0] < len(self.maze) and
                posibleMove[1] >= 0 and posibleMove[1] < len(self.maze[0])):

            if self.maze[posibleMove[0]][posibleMove[1]] != "X":
                return True

        return False
