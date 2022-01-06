from models.Plateau import Plateau
from models.Rover import Rover
from models.Position import Position

def main():
    print("PROGRAMA EXECUTADO")
    
    # Criação da instacia dos rovers
    # Rover 1
    rover1 = Rover(Plateau(5, 5), Position(1, 2), Rover.DIRECTIONS['N'], "LMLMLMLMM")
    print(rover1)  # print=> 1 3 N

    # Rover 2
    rover2 = Rover(Plateau(5, 5), Position(3, 3), Rover.DIRECTIONS['E'], "MMRMMRMRRM")
    print(rover2)  # print=> 5 1 E


if __name__ == "__main__":
    main()