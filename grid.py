from tile import Tile
import numpy as np

class Grid:
    def __init__(self, width, height):
        self.grid = np.zeros((width, height)).tolist()

    def set_tile(self, x, y, tile):
        self.grid[x][y] = tile

    def get_player_tile(self, player):
        return self.grid[player.x][player.y]
        
    def get_field_of_view(self, x, y):
        pass