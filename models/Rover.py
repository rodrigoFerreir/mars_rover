
import models.Position as Position
"""
 -- Criando classe Rover--
    :param plateau:
    :param position:
    :param heading:
"""
class Rover:
    COMANDS={
        'M': 'move',
        'L': 'moveLeft', #90º a esquerda
        'R': 'moveRigth', #90º a direita
    }

    DIRECTIONS={
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }
    initial = DIRECTIONS['N']

    def __init__(self, plateau, position, heading, instructions):
        self.plateau = plateau
        self.position = position
        self.heading = heading
        self.instructions = instructions
        self.process()

    #representation
    def __str__(self) -> str:
            return '{} {} {}'.format(self.position.x, self.position.y, self.getHeading)

    
    def setPosition(self, x, y, heading):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position.x = x
            self.position.y = y
            
        self.heading = heading

    @property
    def getHeading(self):
        direction = list(self.DIRECTIONS.keys())
        try:
            direction = direction[self.heading - 1] # Definindo a direção
        except IndexError:
            direction = 'N'
            print('Erro na direção!')
        
        return direction

    def process(self):
        for index in range(len(self.instructions)):
            self.runCommand(self.instructions[index])

    def runCommand(self, command):
        if command == 'L':
            self.moveLeft()
        elif command == 'R':
            self.moveRigth()
        elif command == 'M':
            if not self.move():
                print("Para onde você está indo?")
                return exit()
        else:
            print("Verifique os parametros!...")
            return exit()

    def move(self):
        if not self.plateau.moveAvaliablePosition(self.position):
            return False

        if self.DIRECTIONS['N'] == self.heading:
            self.position.y += 1
        elif self.DIRECTIONS['E'] == self.heading:
            self.position.x += 1
        elif self.DIRECTIONS['S'] == self.heading:
            self.position.y -= 1
        elif self.DIRECTIONS['W'] == self.heading:
            self.position.x -= 1     
        return True
    
    def moveLeft(self):
        self.heading = self.DIRECTIONS['W'] if (self.heading - 1) < self.DIRECTIONS['N'] else self.heading - 1
    
    def moveRigth(self):
        self.heading = self.DIRECTIONS['N'] if (self.heading + 1) > self.DIRECTIONS['W'] else self.heading + 1
