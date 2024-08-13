class Player:
    def __init__(self, x, y, facing) -> None:
        self.x = x
        self.y = y
        self.facing = facing

    def rotate_left(self):
        self.facing = self.facing - 1
        if self.facing < 0:
            self.facing = 3

    def rotate_right(self):
        self.facing = self.facing + 1
        if self.facing > 3:
            self.facing = 0

    def get_left(self):
        if self.facing - 1 < 0:
            return 3
        else:
            return self.facing - 1

    def get_right(self):
        if self.facing + 1 > 3:
            return 0
        else:
            return self.facing + 1

    def get_tile_infront(self, grid):
        match self.facing:
            case 0:
                return self.x - 1, self.y
            case 1:
                return self.x, self.y + 1
            case 2:
                return self.x + 1, self.y
            case 3:
                return self.x, self.y - 1
            
    def get_left_tile(self):
        match self.facing:
            case 0:
                return self.x, self.y - 1
            case 1:
                return self.x - 1, self.y
            case 2:
                return self.x, self.y + 1
            case 3:
                return self.x + 1, self.y
        
    def get_right_tile(self):
        match self.facing:
            case 0:
                return self.x, self.y + 1
            case 1:
                return self.x + 1, self.y
            case 2:
                return self.x, self.y - 1
            case 3:
                return self.x - 1, self.y

    def move_forward(self, grid):
        tile = grid.grid[self.x][self.y]
        if not tile.walls[self.facing]:
            match self.facing:
                case 0:
                    self.x = self.x - 1
                case 1:
                    self.y = self.y + 1
                case 2:
                    self.x = self.x + 1
                case 3:
                    self.y = self.y - 1

