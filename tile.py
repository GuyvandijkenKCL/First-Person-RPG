class Tile:
    def __init__(self, walls = [0, 0, 0, 0], texture=None) -> None:
        self.walls = walls
        self.texture=texture

    def __str__(self) -> str:
        return " ".join(str(x) for x in self.walls)