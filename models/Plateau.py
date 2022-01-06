class Plateau:
    MIN_WIDTH = 0
    MIN_HEIGTH = 0

    def __init__(self, width, heigth, min_width=0, min_heigth=0):
        self.width = width
        self.heigth = heigth
        self.MIN_WIDTH = min_width
        self.MIN_HEIGTH = min_heigth

    def moveAvaliablePosition(self, position):
        return self.MIN_WIDTH <= position.x <= self.width and self.MIN_HEIGTH <= position.y <= self.heigth