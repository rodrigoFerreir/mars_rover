class Position:
    x = 0
    y = 0

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self, position):
        try:
            return self.x == position.x and self.y == position.y 
        except:
            print('Erro, posição invalida!')