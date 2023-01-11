import pygame
import random
from time import sleep, time

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
background_tmp_1 = (0, 150, 0)
background_tmp_2 = (0, 0, 150)
RED = (255, 0, 0)

class Car:
    image_obstacles = ['stop.png', 'police.png', 'conical.png', 'barricade.png']
    
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image_mycar = 'mycar.png'
        self.image_obstacle = ''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def load_image_mycar(self):
        self.image_mycar = pygame.image.load(self.image_mycar)
        self.width = self.image_mycar.get_rect().size[0]
        self.height = self.image_mycar.get_rect().size[1]

    def load_image_obstacle(self):
        self.image_obstacle = pygame.image.load(random.choice(self.image_obstacles))
        self.width = self.image_obstacle.get_rect().size[0]
        self.height = self.image_obstacle.get_rect().size[1]

    def draw_image_mycar(self):
        screen.blit(self.image_mycar, [self.x, self.y])
    
    def draw_image_obstacle(self):
        screen.blit(self.image_obstacle, [self.x, self.y])

    def move_x(self):
        self.x += self.dx
    
    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):
        if self.x + self.width > WINDOW_WIDTH or self.x < 0:
            self.x -= self.dx
    
    def check_crash(self, car):
        if (self.x + self.width > car.x) and (self.x < car.x + car.width) and (self.y < car.y + car.height) and (self.y + self.height > car.y):
            return True
        else:
            return False

start_time = int(time()) + 5

def draw_main_menu():
    draw_x = (WINDOW_WIDTH / 2) - 200
    draw_y = WINDOW_HEIGHT / 2
    image_intro = pygame.image.load('PyCar.png')
    screen.blit(image_intro, [draw_x, draw_y - 280])
    font_40 = pygame.font.SysFont('FixedSys', 40, True, False)
    font_30 = pygame.font.SysFont('FixedSys', 30, True, False)
    text_title = font_40.render('PyCar', True, BLACK)
    screen.blit(text_title, [draw_x, draw_y])
    text_score = font_40.render('Score: ' + str(score), True, WHITE)
    screen.blit(text_score, [draw_x, draw_y + 70])
    text_start = font_30.render('Press SPACE', True, RED)
    screen.blit(text_start, [draw_x, draw_y + 140])
    pygame.display.flip()

def draw_score():
    font_40 = pygame.font.SysFont('FixedSys', 30, True, False)
    text_score = font_40.render('Score: ' + str(score), True, BLACK)
    screen.blit(text_score, [15, 15])

def draw_time():
    now_time = int(time()) - start_time
    font_40 = pygame.font.SysFont('FixedSys', 30, True, False)
    text_score = font_40.render(f'time: {now_time}', True, BLACK)
    screen.blit(text_score, [370, 15])
    return now_time

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('PyCar')
    clock = pygame.time.Clock()

    # pygame.mixer.music.load('race.wav')
    # sound_crash = pygame.mixer.Sound('crash.wav')
    # sound_engine = pygame.mixer.Sound('engine.wav')

    player = Car(WINDOW_WIDTH/2, (WINDOW_HEIGHT - 150), 0, 0)
    player.load_image_mycar()

    obstacles = []
    obstacle_count = 3
    for i in range(obstacle_count):
        x = random.randrange(0, WINDOW_WIDTH - 55)
        y = random.randrange(-150, -50)
        obstacle = Car(x, y, 0, random.randint(5, 10))
        obstacle.load_image_obstacle()
        obstacles.append(obstacle)
    
    lanes = []
    lane_width = 10
    lane_height = 80
    lane_margin = 20
    lane_count = 20
    lane_x = (WINDOW_WIDTH - lane_width) / 2
    lane_y = -10
    for i in range(lane_count):
        lanes.append([lane_x, lane_y])
        lane_y += lane_height + lane_margin
    
    boundary = 0
    score = 0
    crash = True
    game_on = True
    while game_on:
        if boundary == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_on = False
            
                if crash:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        crash = False
                        start_time = int(time()) + 5
                        for i in range(obstacle_count):
                            obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                            obstacles[i].y = random.randrange(-150, -50)
                            obstacles[i].load_image_obstacle()
                        
                        player.x = WINDOW_WIDTH/2
                        player.dx = 0
                        score = 0
                        boundary = 0
                        pygame.mouse.set_visible(False)
                        # sound_engine.play()
                        # sleep(5)
                        # pygame.mixer.music.play(-1) # 음악 반복
                    
                if not crash:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 4
                        elif event.key == pygame.K_LEFT:
                            player.dx = -4
                    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 0
                        elif event.key == pygame.K_LEFT:
                            player.dx = 0

        elif boundary == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_on = False
            
                if crash:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        crash = False
                        start_time = int(time()) + 5
                        for i in range(obstacle_count):
                            obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                            obstacles[i].y = random.randrange(-150, -50)
                            obstacles[i].load_image_obstacle()
                        
                        player.x = WINDOW_WIDTH/2
                        player.dx = 0
                        score = 0
                        boundary = 0
                        pygame.mouse.set_visible(False)
                        # sound_engine.play()
                        # sleep(5)
                        # pygame.mixer.music.play(-1) # 음악 반복
                    
                if not crash:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 4
                        elif event.key == pygame.K_LEFT:
                            player.dx = -4
                    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 0
                        elif event.key == pygame.K_LEFT:
                            player.dx = 0
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_on = False
            
                if crash:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        crash = False
                        start_time = int(time()) + 5
                        for i in range(obstacle_count):
                            obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                            obstacles[i].y = random.randrange(-150, -50)
                            obstacles[i].load_image_obstacle()
                        
                        player.x = WINDOW_WIDTH/2
                        player.dx = 0
                        score = 0
                        boundary = 0
                        pygame.mouse.set_visible(False)
                        # sound_engine.play()
                        # sleep(5)
                        # pygame.mixer.music.play(-1) # 음악 반복
                    
                if not crash:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 4
                        elif event.key == pygame.K_LEFT:
                            player.dx = -4
                    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 0
                        elif event.key == pygame.K_LEFT:
                            player.dx = 0

        if boundary == 2:
                screen.fill(background_tmp_2)
        elif boundary == 1:
            screen.fill(background_tmp_1)
        else:
            screen.fill(GRAY)

        if not crash:
            for i in range(lane_count):
                pygame.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
                lanes[i][1] += 10
                if lanes[i][1] > WINDOW_HEIGHT:
                    lanes[i][1] = -40 - lane_height
            
            player.draw_image_mycar()
            player.move_x()
            player.check_out_of_screen()

            for i in range(obstacle_count):
                obstacles[i].draw_image_obstacle()
                obstacles[i].y += obstacles[i].dy
                if obstacles[i].y > WINDOW_HEIGHT:
                    score += 10
                    obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                    obstacles[i].y = random.randrange(-150, -50)
                    obstacles[i].dy = random.randint(5, 10) # 장애물 속도
                    obstacles[i].load_image_obstacle()
            
            for i in range(obstacle_count):
                if player.check_crash(obstacles[i]):
                    crash = True
                    # pygame.mixer.music.stop()
                    # sound_crash.play()
                    sleep(2)
                    pygame.mouse.set_visible(True)
                    break
            
            draw_score()
            now = draw_time()
            if now > 5:
                boundary = 2
            elif now > 0:
                boundary = 1

            pygame.display.flip()
        
        else:
            draw_main_menu()

        clock.tick(60)
    
    pygame.quit()
