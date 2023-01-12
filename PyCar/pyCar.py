import pygame
import random
from time import sleep, time

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

class Car:
    image_obstacles = ['stop.png', 'conical.png', 'barricade.png']
    
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image_mycar = 'mycar.png'
        self.image_obstacle = ''
        self.image_police = 'police.png'
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

    def load_image_police(self):
        self.image_police = pygame.image.load('police.png')
        self.width = self.image_police.get_rect().size[0]
        self.height = self.image_police.get_rect().size[1]

    def draw_image_mycar(self):
        screen.blit(self.image_mycar, [self.x, self.y])
    
    def draw_image_obstacle(self):
        screen.blit(self.image_obstacle, [self.x, self.y])

    def draw_image_police(self):
        screen.blit(self.image_police, [self.x, self.y])

    def move_x(self):
        self.x += self.dx
    
    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):
        if self.x + self.width > WINDOW_WIDTH or self.x < 0:
            self.x -= self.dx
    
    def check_crash(self, car, last_x):
        if (last_x != car.x) and (self.x + self.width - 10 > car.x) and (self.x < car.x + car.width - 10) and (self.y < car.y + car.height - 30) and (self.y + self.height - 30 > car.y):
            last_x = car.x
            return [last_x, True]
        else:
            last_x = 9999
            return [last_x, False]
    
    def check_crash_police(self, car, last_px):
        if (last_px != car.x) and (self.x + self.width - 10 > car.x) and (self.x < car.x + car.width - 10) and (self.y < car.y + car.height - 30) and (self.y + self.height - 30 > car.y):
            last_px = car.x
            return [last_px, True]
        else:
            return [last_px, False]

start_time = int(time()) + 5

def draw_main_menu():
    draw_x = WINDOW_WIDTH / 2
    draw_y = WINDOW_HEIGHT / 2
    image_intro = pygame.image.load('intro.png')
    screen.blit(image_intro, [0, 0])
    font_25 = pygame.font.SysFont('malgungothic', 25, True, False)
    font_15 = pygame.font.SysFont('malgungothic', 15, True, False)
    text_score = font_25.render('Score: ' + str(score), True, WHITE)
    screen.blit(text_score, [draw_x - text_score.get_rect().size[0] / 2, draw_y + 100])
    text_start = font_15.render('SPACE를 눌러 게임을 시작하세요', True, RED)
    screen.blit(text_start, [draw_x - text_start.get_rect().size[0] / 2, draw_y + 350])
    pygame.display.flip()
    
def draw_ending():
    draw_x = WINDOW_WIDTH / 2
    draw_y = WINDOW_HEIGHT / 2
    image_ending = pygame.image.load('ending.png')
    screen.blit(image_ending, [0, 0])
    font_25 = pygame.font.SysFont('malgungothic', 25, True, False)
    font_15 = pygame.font.SysFont('malgungothic', 15, True, False)
    text_score = font_25.render('Score: ' + str(score), True, WHITE)
    screen.blit(text_score, [draw_x - text_score.get_rect().size[0] / 2, draw_y - 350])
    text_start = font_15.render('SPACE를 눌러 게임을 시작하세요', True, WHITE)
    screen.blit(text_start, [draw_x - text_start.get_rect().size[0] / 2, draw_y - 300])
    pygame.display.flip()

def draw_score():
    font_25 = pygame.font.SysFont('FixedSys', 30, True, False)
    text_score = font_25.render('Score: ' + str(score), True, BLACK)
    screen.blit(text_score, [15, 15])

def draw_time():
    now_time = int(time()) - start_time
    font_25 = pygame.font.SysFont('FixedSys', 30, True, False)
    text_score = font_25.render(f'time: {now_time}', True, BLACK)
    screen.blit(text_score, [370, 15])
    return now_time

def draw_life(life):
    image_life = pygame.image.load('wheel.png')
    ddx = 45
    for _ in range(life):
        screen.blit(image_life, [120+ddx, 15])
        ddx += 45

def load_image_bullet(bx, by):
    image_bullet = pygame.image.load('bullet.png')
    screen.blit(image_bullet, [bx, by])


if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('PyCar')
    clock = pygame.time.Clock()

    pygame.mixer.music.load('1round.mp3')
    sound_roundchange = pygame.mixer.Sound('roundchange.mp3')
    sound_crash = pygame.mixer.Sound('crash.wav')
    sound_engine = pygame.mixer.Sound('engine.wav')

    player = Car(WINDOW_WIDTH/2, (WINDOW_HEIGHT - 150), 0, 0)
    player.load_image_mycar()

    obstacles = []
    obstacle_count = 3
    for i in range(obstacle_count):
        x = random.randrange(0, WINDOW_WIDTH - 55)
        y = 0
        obstacle = Car(x, y, 0, random.randint(5, 10))
        obstacle.load_image_obstacle()
        obstacles.append(obstacle)

    x = random.randrange(0, WINDOW_WIDTH - 55)
    y = random.randrange(-150, -50)
    police = Car(x, y, 0, random.randint(5, 10))
    police.load_image_police()
    
    # lanes = []
    # lane_width = 10
    # lane_height = 80
    # lane_margin = 20
    # lane_count = 20
    # lane_x = (WINDOW_WIDTH - lane_width) / 2
    # lane_y = -10
    # for i in range(lane_count):
    #     lanes.append([lane_x, lane_y])
    #     lane_y += lane_height + lane_margin

    background_1 = pygame.image.load('background1.png')
    background_2 = pygame.image.load('background2.png')
    background_3 = pygame.image.load('background3.png')
    background_rect = background_1.get_rect()

    bulletXY = []
    isShot = False
    shotCount = 0

    life = 3
    boundary = 0
    score = 0
    last_x = 9999
    last_px = 9999
    music_var_2 = 0
    music_var_3 = 0
    ismain = True
    crash = True
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
        
            if crash:
                # cur.executemany(f'INSERT INTO score VALUES (null, ?)', [score])
                # conn.commit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    crash = False
                    start_time = int(time()) + 5
                    for i in range(obstacle_count):
                        obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                        obstacles[i].y = random.randrange(-150, -50)
                        obstacles[i].load_image_obstacle()
                    
                    police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                    police.y = random.randrange(-150, -50)
                    police.load_image_police()
                    
                    player.x = WINDOW_WIDTH/2
                    player.dx = 0
                    score = 0
                    boundary = 0
                    life = 3
                    music_var_2 = 0
                    music_var_3 = 0
                    ismain = False
                    pygame.mouse.set_visible(False)
                    sound_engine.play()
                    sleep(5)
                    pygame.mixer.music.play(-1) # 음악 반복
                
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
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        bulletX = player.x
                        bulletY = player.y
                        bulletXY.append([bulletX, bulletY])

        if boundary == 2:
            screen.blit(background_3, background_rect)
            # background_rect.y += 5
            # if background_rect.y > WINDOW_HEIGHT:
            #     background_rect.y = 0 - background_rect.height
        elif boundary == 1:
            screen.blit(background_2, background_rect)
            # background_rect.y += 5
            # if background_rect.y > WINDOW_HEIGHT:
            #     background_rect.y = 0 - background_rect.height
        else:
            screen.blit(background_1, background_rect)
            # background_rect.y += 5
            # if background_rect.y > WINDOW_HEIGHT:
            #     background_rect.y = 0 - background_rect.height
        
        if not crash:
            # for i in range(lane_count):
            #     pygame.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
            #     lanes[i][1] += 10
            #     if lanes[i][1] > WINDOW_HEIGHT:
            #         lanes[i][1] = -40 - lane_height
            
            player.draw_image_mycar()
            player.move_x()
            player.check_out_of_screen()
            
            if boundary == 0:
                for i in range(obstacle_count):
                    obstacles[i].draw_image_obstacle()
                    obstacles[i].y += obstacles[i].dy
                    if obstacles[i].y > WINDOW_HEIGHT:
                        score += 10
                        obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                        obstacles[i].y = 0
                        obstacles[i].dy = random.randint(3, 7) # 장애물 속도
                        obstacles[i].load_image_obstacle()
                
                police.draw_image_police()
                police.y += police.dy
                if police.y > WINDOW_HEIGHT:
                    score += 10
                    police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                    police.y = 0
                    police.dy = random.randint(3, 7) # 장애물 속도
                police.load_image_police()
                
            elif boundary == 1:
                for i in range(obstacle_count):
                    obstacles[i].draw_image_obstacle()
                    obstacles[i].y += obstacles[i].dy
                    if obstacles[i].y > WINDOW_HEIGHT:
                        score += 10
                        obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                        obstacles[i].y = 0
                        obstacles[i].dy = random.randint(5, 9) # 장애물 속도
                        obstacles[i].load_image_obstacle()
                
                police.draw_image_police()
                police.y += police.dy
                if police.y > WINDOW_HEIGHT:
                    score += 10
                    police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                    police.y = random.randrange(-150, -50)
                    police.dy = random.randint(5, 9) # 장애물 속도
                police.load_image_police()
            else:
                for i in range(obstacle_count):
                    obstacles[i].draw_image_obstacle()
                    obstacles[i].y += obstacles[i].dy
                    if obstacles[i].y > WINDOW_HEIGHT:
                        score += 10
                        obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                        obstacles[i].y = random.randrange(-150, -50)
                        obstacles[i].dy = random.randint(7, 12) # 장애물 속도
                        obstacles[i].load_image_obstacle()
                
                police.draw_image_police()
                police.y += police.dy
                if police.y > WINDOW_HEIGHT:
                    score += 10
                    police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                    police.y = random.randrange(-150, -50)
                    police.dy = random.randint(7, 12) # 장애물 속도
                police.load_image_police()

            if len(bulletXY) != 0:
                for j, bxy in enumerate(bulletXY):
                    bxy[1] -= 10
                    bulletXY[j][1] = bxy[1]

                    if bxy[1] < police.y:
                        if bxy[0] > police.x + 10 and bxy[0] + 10 < police.x + police.width:
                            bulletXY.remove(bxy)
                            isShot = True
                            shotCount += 1

                if bxy[1] <= 0:
                    try:
                        bulletXY.remove(bxy)
                    except:
                        pass
                        
            # print(shotCount)
            if len(bulletXY) != 0:
                for bx, by in bulletXY:
                    load_image_bullet(bx, by)

            for i in range(obstacle_count):
                cc = player.check_crash(obstacles[i], last_x)
                if cc[1]:
                    sound_crash.play()
                    last_x = cc[0]
                    life -= 1
                    if life == 0:
                        pygame.mixer.music.stop()
                        crash = True
                        pygame.mouse.set_visible(True)
                        break
            
            ccp = player.check_crash_police(police, last_px)
            if ccp[1]:
                sound_crash.play()
                last_px = ccp[0]
                life -= 1
                if life == 0:
                    pygame.mixer.music.stop()
                    crash = True
                    pygame.mouse.set_visible(True)

            if isShot:
                x = random.randrange(0, WINDOW_WIDTH - 55)
                y = random.randrange(-150, -50)
                police = Car(x, y, 0, random.randint(5, 10))
                police.load_image_police()
                isShot = False

            draw_score()
            draw_life(life)
            now = draw_time()
            if now > 20:
                boundary = 2
                if music_var_3 == 0:
                    music_var_3 += 1
                    sound_roundchange.play()
            elif now > 5:
                boundary = 1
                if music_var_2 == 0:
                    music_var_2 += 1
                    sound_roundchange.play()

            pygame.display.flip()
        
        else:
            if not ismain:
                draw_ending()
            else:
                draw_main_menu()
            
        clock.tick(60)

    # conn.close()
    pygame.quit()
