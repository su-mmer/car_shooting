import pygame
import random
from time import sleep, time
import sys

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

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
        if (last_x != car.x) and (self.x + self.width - 20 > car.x) and (self.x < car.x + car.width - 20) and (self.y < car.y + car.height - 30) and (self.y + self.height - 30 > car.y):
            last_x = car.x
            return [last_x, True]
        else:
            last_x = 9999
            return [last_x, False]
    
    def check_crash_police(self, car, last_px):
        if (last_px != car.x) and (self.x + self.width - 20 > car.x) and (self.x < car.x + car.width - 20) and (self.y < car.y + car.height - 30) and (self.y + self.height - 30 > car.y):
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
    text_score_1 = font_25.render('1st: ' + str(score_data[0]), True, WHITE)
    screen.blit(text_score_1, [draw_x - text_score_1.get_rect().size[0] / 2, draw_y + 100])
    
    text_score_2 = font_25.render('2st: ' + str(score_data[1]), True, WHITE)
    screen.blit(text_score_2, [draw_x - text_score_2.get_rect().size[0] / 2, draw_y + 150])
    
    text_score_3 = font_25.render('3st: ' + str(score_data[2]), True, WHITE)
    screen.blit(text_score_3, [draw_x - text_score_3.get_rect().size[0] / 2, draw_y + 200])
    
    text_start = font_15.render('Press SPACE', True, RED)
    screen.blit(text_start, [draw_x - text_start.get_rect().size[0] / 2, draw_y + 350])
    pygame.display.flip()
    
def draw_ending():
    draw_x = WINDOW_WIDTH / 2
    draw_y = WINDOW_HEIGHT / 2
    image_ending = pygame.image.load('ending.png')
    screen.blit(image_ending, [0, 0])
    font_25 = pygame.font.SysFont('malgungothic', 25, True, False)
    font_15 = pygame.font.SysFont('malgungothic', 15, True, False)
    text_score_1 = font_25.render('1st: ' + str(score_data[0]), True, WHITE)
    screen.blit(text_score_1, [draw_x - text_score_1.get_rect().size[0] / 2, draw_y - 350])
    
    text_score_2 = font_25.render('2st: ' + str(score_data[1]), True, WHITE)
    screen.blit(text_score_2, [draw_x - text_score_2.get_rect().size[0] / 2, draw_y - 300])
    
    text_score_3 = font_25.render('3st: ' + str(score_data[2]), True, WHITE)
    screen.blit(text_score_3, [draw_x - text_score_3.get_rect().size[0] / 2, draw_y - 250])
    
    text_score = font_25.render('??? ??????: ' + str(score), True, WHITE)
    screen.blit(text_score, [draw_x - text_score.get_rect().size[0] / 2, draw_y - 200])
    
    text_start = font_15.render('Press SPACE for Restart', True, YELLOW)
    screen.blit(text_start, [draw_x - text_start.get_rect().size[0] / 2, draw_y - 380])
    pygame.display.flip()

def draw_score():
    font_25 = pygame.font.SysFont('FixedSys', 25, True, False)
    text_score = font_25.render('Score  ' + str(score), True, BLACK)
    screen.blit(text_score, [380, 30])


def draw_time():
    now_time = int(time()) - start_time
    font_25 = pygame.font.SysFont('FixedSys', 25, True, False)
    if now_time < 60:
        text_score = font_25.render(f'00:{now_time}', True, BLACK)
    else:
        text_score = font_25.render(f'0{now_time//60}:{now_time - 60*(now_time//60)}', True, BLACK)
    screen.blit(text_score, [420, 15])
    return now_time

def draw_life(life):
    image_life = pygame.image.load('wheel.png')
    ddx = 0
    for _ in range(life):
        screen.blit(image_life, [15+ddx, 15])
        ddx += 45

def draw_fire(shot_count):
    image_fire = pygame.image.load('fire.png')
    fdx = 0
    for _ in range(shot_count):
        screen.blit(image_fire, [15+fdx, 65])
        fdx += 30

def load_image_bullet(bx, by):
    image_bullet = pygame.image.load('bullet.png')
    screen.blit(image_bullet, [bx, by])

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('?????????, ????????? ?????????!')
    clock = pygame.time.Clock()

    pygame.mixer.music.load('1round.mp3')
    sound_roundchange = pygame.mixer.Sound('roundchange.mp3')
    sound_crash = pygame.mixer.Sound('crash.wav')
    sound_engine = pygame.mixer.Sound('engine.wav')

    sys.stdin = open('data.txt')
    score_data = list(map(int, input().split()))
    
    player = Car(WINDOW_WIDTH/2, (WINDOW_HEIGHT - 150), 0, 0)
    player.load_image_mycar()

    obstacles = []
    obstacle_count = 5
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

    background_1 = pygame.image.load('background1.png')
    background_2 = pygame.image.load('background2.png')
    background_3 = pygame.image.load('background3.png')
    background_rect = background_1.get_rect()

    power_car = pygame.image.load('powercar.png')

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
    isPower = False
    s_time = 0
    game_on = True
    while game_on:
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
                    
                    police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                    police.y = random.randrange(-150, -50)
                    police.load_image_police()
                    
                    score_data.append(score)
                    score_data.sort(reverse=True)
                    score_data = score_data[:3]
                    f = open('data.txt', 'w')
                    f.write(f'{score_data[0]} {score_data[1]} {score_data[2]}')
                    
                    player.x = WINDOW_WIDTH/2
                    player.dx = 0
                    score = 0
                    boundary = 0
                    life = 3
                    music_var_2 = 0
                    music_var_3 = 0
                    ismain = False
                    isPower = False
                    shotCount = 0
                    pygame.mouse.set_visible(False)
                    sound_engine.play()
                    sleep(5)
                    pygame.mixer.music.play(-1) # ?????? ??????
                
            if not crash:
                if boundary == 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 6
                        elif event.key == pygame.K_LEFT:
                            player.dx = -6
                    
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 0
                        elif event.key == pygame.K_LEFT:
                            player.dx = 0
                elif boundary == 1:
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
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            player.dx = 3
                        elif event.key == pygame.K_LEFT:
                            player.dx = -3
                    
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

            if shotCount == 5:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        s_time = int(time())
                        isPower = True

        if boundary == 2:
            screen.blit(background_3, background_rect)
        elif boundary == 1:
            screen.blit(background_2, background_rect)
        else:
            screen.blit(background_1, background_rect)
        
        if not crash:
            if isPower:
                screen.blit(power_car, [player.x, player.y])
            else:
                player.draw_image_mycar()
            player.move_x()
            player.check_out_of_screen()
            
            if isPower:
                for i in range(obstacle_count):
                    obstacles[i].draw_image_obstacle()
                    obstacles[i].y += obstacles[i].dy
                    if obstacles[i].y > WINDOW_HEIGHT:
                        score += 10
                        obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                        obstacles[i].y = 0
                        obstacles[i].dy = 40 # ????????? ??????
                        obstacles[i].load_image_obstacle()
                
                police.draw_image_police()
                police.y += police.dy
                if police.y > WINDOW_HEIGHT:
                    score += 10
                    police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                    police.y = 0
                    police.dy = 40 # ????????? ??????
                police.load_image_police()
            else:
                if boundary == 0:
                    for i in range(obstacle_count):
                        obstacles[i].draw_image_obstacle()
                        obstacles[i].y += obstacles[i].dy
                        if obstacles[i].y > WINDOW_HEIGHT:
                            score += 10
                            obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                            obstacles[i].y = 0
                            obstacles[i].dy = random.randint(3, 7) # ????????? ??????
                            obstacles[i].load_image_obstacle()
                    
                    police.draw_image_police()
                    police.y += police.dy
                    if police.y > WINDOW_HEIGHT:
                        score += 10
                        police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                        police.y = 0
                        police.dy = random.randint(3, 7) # ????????? ??????
                    police.load_image_police()
                    
                elif boundary == 1:
                    for i in range(obstacle_count):
                        obstacles[i].draw_image_obstacle()
                        obstacles[i].y += obstacles[i].dy
                        if obstacles[i].y > WINDOW_HEIGHT:
                            score += 10
                            obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                            obstacles[i].y = 0
                            obstacles[i].dy = random.randint(5, 11) # ????????? ??????
                            obstacles[i].load_image_obstacle()
                    
                    police.draw_image_police()
                    police.y += police.dy
                    if police.y > WINDOW_HEIGHT:
                        score += 10
                        police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                        police.y = random.randrange(-150, -50)
                        police.dy = random.randint(5, 11) # ????????? ??????
                    police.load_image_police()
                
                else:
                    for i in range(obstacle_count):
                        obstacles[i].draw_image_obstacle()
                        obstacles[i].y += obstacles[i].dy
                        if obstacles[i].y > WINDOW_HEIGHT:
                            score += 10
                            obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                            obstacles[i].y = random.randrange(-150, -50)
                            obstacles[i].dy = random.randint(8, 13) # ????????? ??????
                            obstacles[i].load_image_obstacle()
                    
                    police.draw_image_police()
                    police.y += police.dy
                    if police.y > WINDOW_HEIGHT:
                        score += 10
                        police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                        police.y = random.randrange(-150, -50)
                        police.dy = random.randint(8, 13) # ????????? ??????
                    police.load_image_police()

            if len(bulletXY) != 0:
                for j, bxy in enumerate(bulletXY):
                    bxy[1] -= 10
                    bulletXY[j][1] = bxy[1]

                    if bxy[1] < police.y:
                        if bxy[0] + 20 > police.x and bxy[0] - 20 < police.x + police.width:
                            bulletXY.remove(bxy)
                            isShot = True
                            if shotCount < 5:
                                shotCount += 1

                if bxy[1] <= 0:
                    try:
                        bulletXY.remove(bxy)
                    except:
                        pass
                        
            if len(bulletXY) != 0:
                for bx, by in bulletXY:
                    load_image_bullet(bx, by)
            if isPower:
                if int(time())-s_time == 5:
                    isPower = False
            elif not isPower and int(time())-s_time <= 6:
                for i in range(obstacle_count):
                    obstacles[i].draw_image_obstacle()
                    obstacles[i].y += obstacles[i].dy
                    if obstacles[i].y > WINDOW_HEIGHT:
                        score += 10
                        obstacles[i].x = random.randrange(0, WINDOW_WIDTH-obstacles[i].width)
                        obstacles[i].y = 0
                        obstacles[i].dy = random.randint(3, 7) # ????????? ??????
                        obstacles[i].load_image_obstacle()
                
                police.draw_image_police()
                police.y += police.dy
                if police.y > WINDOW_HEIGHT:
                    score += 10
                    police.x = random.randrange(0, WINDOW_WIDTH-police.width)
                    police.y = 0
                    police.dy = random.randint(3, 7) # ????????? ??????
                police.load_image_police()
                shotCount = 0
            else:
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
                    score += 20
                    x = random.randrange(0, WINDOW_WIDTH - 55)
                    y = random.randrange(-150, -50)
                    police = Car(x, y, 0, random.randint(5, 10))
                    police.load_image_police()
                    isShot = False

            draw_score()
            draw_life(life)
            draw_fire(shotCount)
            now = draw_time()
            if now > 60:
                boundary = 2
                if music_var_3 == 0:
                    music_var_3 += 1
                    sound_roundchange.play()
            elif now > 30:
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

    score_data.append(score)
    score_data.sort(reverse=True)
    score_data = score_data[:3]
    f = open('data.txt', 'w')
    f.write(f'{score_data[0]} {score_data[1]} {score_data[2]}')
    pygame.quit()
