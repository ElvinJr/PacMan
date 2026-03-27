import pygame
import sys
import random

# ---- Funciones de Pac-Man ----
def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    return touching_ghost and not power_pellet_active

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)


# ---- Configuración ----
pygame.init()
TILE = 24
COLS, ROWS = 28, 26
WIDTH, HEIGHT = COLS * TILE, ROWS * TILE + 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20, bold=True)
big_font = pygame.font.SysFont("Arial", 48, bold=True)

# Colores
BLACK  = (0, 0, 0)
BLUE   = (33, 33, 222)
YELLOW = (255, 255, 0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
PINK   = (255, 182, 255)
CYAN   = (0, 255, 255)
ORANGE = (255, 182, 85)
SCARED = (50, 50, 200)
GOLD   = (255, 215, 0)

# Mapa: 0=vacío, 1=pared, 2=punto, 3=pastilla
MAPA = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
    [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,0,1,1,1,0,0,1,1,1,0,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
    [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
    [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
    [1,3,2,2,1,1,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,1,1,2,2,3,1],
    [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
    [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
]

def contar_puntos():
    return sum(row.count(2) + row.count(3) for row in MAPA)

total_puntos = contar_puntos()

# ---- Clases ----
class PacMan:
    def __init__(self):
        self.x, self.y = 14, 23
        self.dx, self.dy = 0, 0
        self.power = False
        self.power_timer = 0
        self.puntos = 0
        self.vivo = True

    def mover(self, mapa):
        nx, ny = self.x + self.dx, self.y + self.dy
        if 0 <= nx < COLS and 0 <= ny < ROWS and mapa[ny][nx] != 1:
            self.x, self.y = nx, ny

        celda = mapa[self.y][self.x]
        tocando_punto = celda == 2
        tocando_pastilla = celda == 3

        if score(tocando_pastilla, tocando_punto):
            self.puntos += 10 if tocando_punto else 50
            mapa[self.y][self.x] = 0

        if tocando_pastilla:
            self.power = True
            self.power_timer = 200

        if self.power:
            self.power_timer -= 1
            if self.power_timer <= 0:
                self.power = False

    def dibujar(self, surface):
        cx = self.x * TILE + TILE // 2
        cy = self.y * TILE + TILE // 2
        color = GOLD if self.power else YELLOW
        pygame.draw.circle(surface, color, (cx, cy), TILE // 2 - 2)


class Ghost:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.color = color
        self.timer = 0
        self.scared = False

    def mover(self, mapa, pac):
        self.scared = pac.power
        self.timer += 1
        if self.timer < 15:
            return
        self.timer = 0

        direcciones = [(0,-1),(0,1),(-1,0),(1,0)]
        random.shuffle(direcciones)
        for dx, dy in direcciones:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and mapa[ny][nx] != 1:
                self.x, self.y = nx, ny
                break

    def dibujar(self, surface):
        cx = self.x * TILE + TILE // 2
        cy = self.y * TILE + TILE // 2
        color = SCARED if self.scared else self.color
        pygame.draw.circle(surface, color, (cx, cy), TILE // 2 - 2)
        pygame.draw.rect(surface, color, (self.x * TILE + 2, cy, TILE - 4, TILE // 2 - 2))


def dibujar_mapa(surface, mapa):
    for row in range(ROWS):
        for col in range(COLS):
            x, y = col * TILE, row * TILE
            celda = mapa[row][col]
            if celda == 1:
                pygame.draw.rect(surface, BLUE, (x, y, TILE, TILE))
                pygame.draw.rect(surface, (0, 0, 180), (x, y, TILE, TILE), 2)
            elif celda == 2:
                pygame.draw.circle(surface, WHITE, (x + TILE//2, y + TILE//2), 3)
            elif celda == 3:
                pygame.draw.circle(surface, GOLD, (x + TILE//2, y + TILE//2), 7)


def pantalla_final(surface, mensaje, color):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    surface.blit(overlay, (0, 0))
    texto = big_font.render(mensaje, True, color)
    rect = texto.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    surface.blit(texto, rect)
    sub = font.render("Presiona R para reiniciar o ESC para salir", True, WHITE)
    sub_rect = sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
    surface.blit(sub, sub_rect)


def main():
    mapa = [row[:] for row in MAPA]
    pac = PacMan()
    fantasmas = [
        Ghost(13, 13, RED),
        Ghost(14, 13, PINK),
        Ghost(13, 14, CYAN),
        Ghost(14, 14, ORANGE),
    ]
    game_over = False
    ganaste = False
    puntos_totales = contar_puntos()

    while True:
        clock.tick(10)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if game_over or ganaste:
                    if event.key == pygame.K_r:
                        main()
                else:
                    if event.key == pygame.K_w: pac.dx, pac.dy = 0, -1
                    if event.key == pygame.K_s: pac.dx, pac.dy = 0, 1
                    if event.key == pygame.K_a: pac.dx, pac.dy = -1, 0
                    if event.key == pygame.K_d: pac.dx, pac.dy = 1, 0

        if not game_over and not ganaste:
            pac.mover(mapa)
            for g in fantasmas:
                g.mover(mapa, pac)
                if lose(pac.power, g.x == pac.x and g.y == pac.y):
                    game_over = True
                if eat_ghost(pac.power, g.x == pac.x and g.y == pac.y):
                    pac.puntos += 200
                    g.x, g.y = 13, 13

            puntos_restantes = sum(row.count(2) + row.count(3) for row in mapa)
            if win(puntos_restantes == 0, pac.power, False):
                ganaste = True

        dibujar_mapa(screen, mapa)
        pac.dibujar(screen)
        for g in fantasmas:
            g.dibujar(screen)

        # HUD
        pygame.draw.rect(screen, BLACK, (0, ROWS * TILE, WIDTH, 60))
        pts = font.render(f"Puntos: {pac.puntos}", True, WHITE)
        screen.blit(pts, (10, ROWS * TILE + 10))
        if pac.power:
            pw = font.render("⚡ PODER ACTIVO", True, GOLD)
            screen.blit(pw, (WIDTH // 2 - 70, ROWS * TILE + 10))

        if game_over:
            pantalla_final(screen, "💀 PERDISTE 💀", RED)
        if ganaste:
            pantalla_final(screen, "🏆 GANASTE 🏆", GOLD)

        pygame.display.flip()

main()