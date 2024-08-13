import pygame
import pygame.gfxdraw
from grid import Grid
from player import Player
from tile import Tile

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 750))

clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption("Megaten at home")

player = Player(0, 0, 0)
grid = Grid(3, 3)

texture = pygame.image.load("C:\\Users\\guyva\\OneDrive\\Documents\\Megaten at home\\wall_textures\\Wall.png").convert()


tile = Tile([1, 0, 0, 1], texture)
tileN = Tile([1, 0, 0, 0], texture)
tile2 = Tile([1, 1, 0, 0], texture)
tile3 = Tile([0, 0, 1, 1], texture)
tile4 = Tile([0, 1, 1, 0], texture)
tileE = Tile([0, 1, 0, 0], texture)
tileW = Tile([0, 0, 0, 1], texture)
tileS = Tile([0, 0, 1, 0], texture)
tileC = Tile()


grid = Grid(4, 4)
grid.set_tile(0, 0, tile)
grid.set_tile(0, 1, tileN)
grid.set_tile(0, 2, tileN)
grid.set_tile(0, 3, tile2)

grid.set_tile(1, 0, tileW)
grid.set_tile(1, 1, tileC)
grid.set_tile(1, 2, tileC)
grid.set_tile(1, 3, tileE)

grid.set_tile(2, 0, tileW)
grid.set_tile(2, 1, tileC)
grid.set_tile(2, 2, tileC)
grid.set_tile(2, 3, tileE)

grid.set_tile(3, 0, tile3)
grid.set_tile(3, 1, tileS)
grid.set_tile(3, 2, tileS)
grid.set_tile(3, 3, tile4)



# grid.set_tile(1, 1, tileC)

# grid.set_tile(0, 0, tile)
# grid.set_tile(1, 0, tileW)
# grid.set_tile(0, 1, tileN)
# grid.set_tile(1, 2, tileE)
# grid.set_tile(2, 1, tileS)

# grid.set_tile(0, 2, tile2)
# grid.set_tile(2, 0, tile3)
# grid.set_tile(2, 2, tile4)

# for i in range(len(grid.grid)):
#     for j in range(len(grid.grid[i])):
#         print(grid.grid[i][j])

rect = pygame.draw.polygon(surface=screen, color=999999, points = [(0,0), (100, 20), (100, 800), (0, 100)])

def display_map(grid, surface):
    for j in range(len(grid.grid[0])):
        for i in range(len(grid.grid)):
            if grid.grid[j][i].walls[0]:
                pygame.draw.line(surface, "red", (i * 10, j * 10), ((i + 1) * 10, j * 10))
            if grid.grid[j][i].walls[1]:
                pygame.draw.line(surface, "red", ((i + 1) * 10, j * 10), ((i + 1) * 10, (j + 1) * 10))
            if grid.grid[j][i].walls[2]:
                pygame.draw.line(surface, "red", (i * 10, (j + 1) * 10), ((i + 1) * 10, (j + 1) * 10))
            if grid.grid[j][i].walls[3]:
                pygame.draw.line(surface, "red", ((i) * 10, j * 10), ((i) * 10, (j + 1) * 10))

def display_corner_ui(surface, player):
    directions = {
        0: "North",
        1: "East",
        2: "South",
        3: "West"
    }

    rect = pygame.Rect(0, 0, surface.get_width() * 0.1, surface.get_height() * 0.1)
    # shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    shape_surf = pygame.image.load("C:\\Users\\guyva\\OneDrive\\Documents\\Megaten at home\\ui\\CornerUI.png").convert()
    shape_surf.set_alpha(180)
    # pygame.draw.rect(shape_surf, (0, 0, 255), shape_surf.get_rect())
    surface.blit(shape_surf, rect)

    my_font = pygame.font.SysFont('arial', 20)
    text_surface = my_font.render(directions[player.facing], False, (255, 255, 255))
    surface.blit(text_surface, (0,0))

    text_surface = my_font.render(f'{player.x}, {player.y}', False, (255, 255, 255))
    surface.blit(text_surface, (0,20))


def display_party_ui(surface):
    width = surface.get_width()
    height = surface.get_height()
    pygame.draw.polygon(surface=surface, color=5005, points = [(width, height), (width, height*0.6), (0, height*0.6), (0, height)])
    
def draw_bg():
    screen.fill((0,0,0))

def pos_sum(n, x, m):
    for i in range(x):
        n = n + (m  / (2 ** i))
    return n

def neg_sum(n, x, m):
    for i in range(x):
        n = n - (m  / (2 ** i))
    return n

def draw_left_tile(surface, grid, player, scale, depth):
    x, y = player.get_left_tile()
    tile = grid.grid[x][y]
    width = surface.get_width()
    height = surface.get_height()
    # [(width * 0.25, height * 0.4), (width * 0.75, height * 0.4), (width * 0.625, height * 0.3), (width * 0.375, height * 0.3)]
    
    points = [
        (width * pos_sum(0, depth, 0.25), height * neg_sum(0.6, depth, 0.2)),  
        (width * (pos_sum(0, depth, 0.25) - (scale * (neg_sum(1, depth, 0.25) - pos_sum(0, depth, 0.25)))), height * neg_sum(0.6, depth, 0.2)),
        (width * (pos_sum(0, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), height * neg_sum(0.6, depth + 1, 0.2)),
        (width * pos_sum(0, depth + 1, 0.25), height * neg_sum(0.6, depth + 1, 0.2))
    ]    
    pygame.draw.polygon(surface=surface, color='red', points = points)

    player = Player(x, y, player.facing)
    if tile.walls[player.facing]:
        points = [
            (width * (pos_sum(0, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), height * neg_sum(0.6, depth + 1, 0.2)),
            (width * pos_sum(0, depth + 1, 0.25), height * neg_sum(0.6, depth + 1, 0.2)),
            (width * pos_sum(0, depth + 1, 0.25), 0),
            (width * (pos_sum(0, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), 0),
        ]  
        pygame.draw.polygon(surface=surface, color='blue', points = points)

    if tile.walls[player.get_left()]:
        points = [
            (width * (pos_sum(0, depth, 0.25) - (scale * (neg_sum(1, depth, 0.25) - pos_sum(0, depth, 0.25)))), height * neg_sum(0.6, depth, 0.2)),
            (width * (pos_sum(0, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), height * neg_sum(0.6, depth + 1, 0.2)),
            (width * (pos_sum(0, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), 0),
            (width * (pos_sum(0, depth, 0.25) - (scale * (neg_sum(1, depth, 0.25) - pos_sum(0, depth, 0.25)))), 0),
        ]
        pygame.draw.polygon(surface=surface, color='orange', points = points)

    else:
        draw_left_tile(surface, grid, player, scale + 1, depth)

def draw_right_tile(surface, grid, player, scale, depth):
    x, y = player.get_right_tile()
    tile = grid.grid[x][y]
    width = surface.get_width()
    height = surface.get_height()
    # [(width * 0.25, height * 0.4), (width * 0.75, height * 0.4), (width * 0.625, height * 0.3), (width * 0.375, height * 0.3)]
    
    points = [
        (width * neg_sum(1, depth, 0.25), height * neg_sum(0.6, depth, 0.2)),  
        (width * (neg_sum(1, depth, 0.25) - (scale * (neg_sum(1, depth, 0.25) - pos_sum(0, depth, 0.25)))), height * neg_sum(0.6, depth, 0.2)),
        (width * (neg_sum(1, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), height * neg_sum(0.6, depth + 1, 0.2)),
        (width * neg_sum(1, depth + 1, 0.25), height * neg_sum(0.6, depth + 1, 0.2))
    ]    
    pygame.draw.polygon(surface=surface, color='green', points = points)

    player = Player(x, y, player.facing)
    if tile.walls[player.facing]:
        points = [
            (width * (neg_sum(1, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), height * neg_sum(0.6, depth + 1, 0.2)),
            (width * neg_sum(1, depth + 1, 0.25), height * neg_sum(0.6, depth + 1, 0.2)),
            (width * neg_sum(1, depth + 1, 0.25), 0),
            (width * (neg_sum(1, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), 0),
        ]  
        pygame.draw.polygon(surface=surface, color='yellow', points = points)

    if tile.walls[player.get_right()]:
        pass
        points = [
            (width * (neg_sum(1, depth, 0.25) - (scale * (neg_sum(1, depth, 0.25) - pos_sum(0, depth, 0.25)))), height * neg_sum(0.6, depth, 0.2)),
            (width * (neg_sum(1, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), height * neg_sum(0.6, depth + 1, 0.2)),
            (width * (neg_sum(1, depth + 1, 0.25) - (scale * (neg_sum(1, depth + 1, 0.25) - pos_sum(0, depth + 1, 0.25)))), 0),
            (width * (neg_sum(1, depth, 0.25) - (scale * (neg_sum(1, depth, 0.25) - pos_sum(0, depth, 0.25)))), 0),
        ]
        pygame.draw.polygon(surface=surface, color='brown', points = points)
    else:
        draw_left_tile(surface, grid, player, scale + 1, depth)


def draw_tile(surface, grid, player, scale):
    width = surface.get_width()
    height = surface.get_height()
    tile = grid.grid[player.x][player.y]

    if tile.walls[player.facing]:
        points = [
            (width * pos_sum(0, scale + 1, 0.25), height * neg_sum(0.4, scale, 0.1)),
            (width * pos_sum(0, scale + 1, 0.25), 0), 
            (width * neg_sum(1, scale + 1, 0.25), 0),
            (width * neg_sum(1, scale + 1, 0.25), height * neg_sum(0.4, scale, 0.1)),
            ]
        if tile.texture:
            pygame.gfxdraw.textured_polygon(surface, points, tile.texture, 0, 0)
        else:
            pygame.draw.polygon(surface=surface, color=444444, points = points)
        # pygame.draw.polygon(surface=surface, color=444444, points = points)
    elif scale < 4:
        x, y = player.get_tile_infront(grid)
        player = Player(x, y, player.facing)
        draw_tile(surface, grid, player, scale+1)
    #floor
    points = [
        (width * pos_sum(0, scale, 0.25), height * neg_sum(0.6, scale, 0.2)),  
        (width * neg_sum(1, scale, 0.25), height * neg_sum(0.6, scale, 0.2)),
        (width * neg_sum(1, scale + 1, 0.25), height * neg_sum(0.6, scale + 1, 0.2)),
        (width * pos_sum(0, scale + 1, 0.25), height * neg_sum(0.6, scale + 1, 0.2))
        ]
    
    pygame.draw.polygon(surface=surface, color=999999, points = points)

    #left wall
    if tile.walls[player.get_left()]:
        points = [
            (width * pos_sum(0, scale, 0.25),  height * neg_sum(0.6, scale, 0.2)),
            (width * pos_sum(0, scale, 0.25), 0), 
            (width * pos_sum(0, scale + 1, 0.25), 0), 
            (width * pos_sum(0, scale + 1, 0.25), height * neg_sum(0.4, scale, 0.1)), 
            ]
        pygame.draw.polygon(surface=screen, color=111333, points = points)
        if tile.texture:
            pygame.gfxdraw.textured_polygon(surface, points, tile.texture, 0, 0)
        else:
            pygame.draw.polygon(surface=screen, color=111333, points = points)
    else:
        draw_left_tile(surface, grid, player, 1, scale)
    if tile.walls[player.get_right()]:
        points = [
            (width * neg_sum(1, scale, 0.25),  height * neg_sum(0.6, scale, 0.2)),
            (width * neg_sum(1, scale, 0.25), 0), 
            (width * neg_sum(1, scale + 1, 0.25), 0), 
            (width * neg_sum(1, scale + 1, 0.25), height * neg_sum(0.4, scale, 0.1)), 
            ]
        pygame.draw.polygon(surface=screen, color=111333, points = points)
    # else:
    #     draw_right_tile(surface, grid, player, 1, scale)







def draw_tiles(surface, player, grid):
    width = surface.get_width()
    height = surface.get_height()

    #Draw tile player is on
    draw_tile(surface, grid, player, 0)
    # points = [(width, height*0.6), (0, height*0.6), (width * 0.25, height * 0.4), (width * 0.75, height * 0.4)]
    # pygame.draw.polygon(surface=screen, color=999999, points = points)

    tile = grid.grid[player.x][player.y]


    # if tile.walls[player.facing]:
    #     pass
    #     # points = [(width * 0.25, height * 0.4), (width * 0.75, height * 0.4), (width * 0.75, 0), (width * 0.25, 0)]
    #     # pygame.draw.polygon(surface=screen, color=444444, points = points)
    # else:
    #     #Tile in front of player
    #     x, y = player.get_tile_infront(grid)
    #     next_tile = grid.grid[x][y]
    #     # points = [(width * 0.25, height * 0.4), (width * 0.75, height * 0.4), (width * 0.625, height * 0.3), (width * 0.375, height * 0.3)]
    #     # pygame.draw.polygon(surface=screen, color=994499, points = points)
    #     #Draw wall/tile in front of player
    #     if next_tile.walls[player.facing]:
    #         points = [(width * 0.625, height * 0.3), (width * 0.375, height * 0.3), (width * 0.375, 0), (width * 0.625, 0)]
    #         pygame.draw.polygon(surface=screen, color=444444, points = points)
    #     else:
    #         points = [(width * 0.625, height * 0.3), (width * 0.375, height * 0.3), (width * 0.4375, height * 0.25), (width * 0.5625, height * 0.25)]
    #         pygame.draw.polygon(surface=screen, color=444444, points = points)
    #     if tile.walls[left]:
    #         points = [(width * 0.25, height * 0.4), (width * 0.375, height * 0.3), (width * 0.375, height * 0), (width * 0.25, height * 0)]
    #         pygame.draw.polygon(surface=screen, color=111333, points = points)
    #     # else:
    #     #     points = [(width * 0.25, height * 0.4), (width * 0.375, height * 0.3), (width * 0.375, height * 0), (width * 0.25, height * 0)]
    #     #     pygame.draw.polygon(surface=screen, color=111333, points = points)
    #     if tile.walls[right]:
    #         points = [(width * 0.75, height * 0.4), (width * 0.625, height * 0.3), (width * 0.625, height * 0), (width * 0.75, height * 0)]
    #         pygame.draw.polygon(surface=screen, color=666666, points = points)
        
    # #Walls/tiles to the left
    # if tile.walls[left]:
    #     points = [(0, 0), (width * 0.25, 0), (width * 0.25, height * 0.4), (0,  height * 0.6)]
    #     pygame.draw.polygon(surface=screen, color=111333, points = points)
    # else:
    #     points = [(width * 0.25, height * 0.4), (0,  height * 0.6), (0, height * 0.4)]
    #     pygame.draw.polygon(surface=screen, color=111333, points = points)

    # #Walls/tiles to the right
    # if tile.walls[right]:
    #     points = [(width, 0), (width * 0.75, 0), (width * 0.75, height * 0.4), (width,  height * 0.6)]
    #     pygame.draw.polygon(surface=screen, color=666666, points = points)
    # else:
    #     points = [(width * 0.75, height * 0.4), (width,  height * 0.6), (width, height * 0.4)]
    #     pygame.draw.polygon(surface=screen, color=666666, points = points)

keepGameRunning = True
while keepGameRunning:
    clock.tick(FPS)
    # screen.blit()
    pygame.display.update()
    draw_bg()
    display_party_ui(screen)
    draw_tiles(screen, player, grid)
    display_corner_ui(screen, player)
    # display_map(grid, screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            keepGameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.rotate_left()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.rotate_right()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.rotate_right()
                player.rotate_right()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move_forward(grid)

    

        

    

pygame.quit()
quit()