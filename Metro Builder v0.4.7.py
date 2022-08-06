'''
                                                                                 ,,    ,,         ,,                    
`7MMM.     ,MMF'           mm                           `7MM"""Yp,               db  `7MM       `7MM                    
  MMMb    dPMM             MM                             MM    Yb                     MM         MM                    
  M YM   ,M MM   .gP"Ya  mmMMmm  `7Mb,od8  ,pW"Wq.        MM    dP `7MM  `7MM  `7MM    MM    ,M""bMM   .gP"Ya  `7Mb,od8 
  M  Mb  M' MM  ,M'   Yb   MM      MM' "' 6W'   `Wb       MM"""bg.   MM    MM    MM    MM  ,AP    MM  ,M'   Yb   MM' "' 
  M  YM.P'  MM  8M""""""   MM      MM     8M     M8       MM    `Y   MM    MM    MM    MM  8MI    MM  8M""""""   MM     
  M  `YM'   MM  YM.    ,   MM      MM     YA.   ,A9       MM    ,9   MM    MM    MM    MM  `Mb    MM  YM.    ,   MM     
.JML. `'  .JMML. `Mbmmd'   `Mbmo .JMML.    `Ybmd9'      .JMMmmmd9    `Mbod"YML..JMML..JMML. `Wbmd"MML. `Mbmmd' .JMML.   
'''

#**************Подключение заголовков**************
import pygame
import random
import os
from math import *
from os import path
import winsound

#Название игры и версия
game_name_str = 'Metro Builder'
game_version = 'v0.4.7'

#**************Директории******************
snd_dir = path.join(path.dirname(__file__), 'snd')
img_dir = path.join(path.dirname(__file__), 'img')
svg_dir = path.join(path.dirname(__file__), 'svg\metrobuilder.save')

#**************Настройка окна**************
WIDTH = 1280
HEIGHT = 720
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
GREEN = (0, 255, 0)
BLUE = (65, 105, 225)
DARK_BLUE = (34, 0, 64)
PURPLE = (255, 0, 255)
YELLOW = (255, 215, 0)
GRAY = (192, 192, 192)

rgb = (0, 0, 0)
cl_interface = DARK_BLUE

ICON = pygame.image.load(img_dir+'\icon.png')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(game_name_str)
clock = pygame.time.Clock()
pygame.display.set_icon(ICON)

print('Metro Builder ' + game_version)

#**************Интерфейс************
#Общий шрифт
font_global = 'Consolas'
font_name = None

button_font = pygame.font.SysFont(font_global,75) #Шрифт кнопок 1 (100)
button_font_interface = pygame.font.SysFont(font_global,25) #Шрифт кнопок 2 (42)
balance_font = pygame.font.SysFont(font_global, 25) #Шрифт баланса (32)
store_font = pygame.font.SysFont(font_global, 15) #Шрифт в магазине (22)
happening_font = pygame.font.SysFont(font_global, 18) #Шрифт в событиях

#Меню
#Название игры в главном меню
game_name_font = pygame.font.SysFont(font_name,180)
game_name_text_f = game_name_font.render(game_name_str, True, YELLOW)
game_name_text_b = game_name_font.render(game_name_str, True, BLUE)

#Кнопка выхода из игры
button_quit = pygame.Rect(390, 548, 500, 100)
button_quit_text = button_font.render('EXIT', True, WHITE)

#Кнопка начала игры
button_play = pygame.Rect(390, 428, 500, 100)
button_play_text = button_font.render('PLAY', True, WHITE)

#Интерфейс
#Отрисовка баланса
balance_text = balance_font.render('money', True, YELLOW)

#Отрисовка количества поездов
trains_text = balance_font.render('trains', True, YELLOW)

#Отрисовка общего дохода
income_text = balance_font.render('Earnings: ', True, YELLOW)

#Кнопка выхода в главное меню
button_tomenu_text = button_font.render('EXIT', True, WHITE)

#Кнопка создания станции.
button_st_cr = pygame.Rect(WIDTH-(WIDTH/4)+30, HEIGHT/2 , 250, 42)
button_st_cr_text = button_font_interface.render('Create station', True, WHITE)
button_st_cr_cost = button_font_interface.render('money', True, YELLOW)

#Кнопка покупки поезда.
button_train_buy = pygame.Rect(WIDTH-(WIDTH/4)+30, (HEIGHT/2)+90 , 250, 42)
button_train_buy_text = button_font_interface.render('Buy train', True, WHITE)
button_train_buy_cost = button_font_interface.render('cost', True, YELLOW)

#Кнопка ремонта.
button_repair = pygame.Rect(WIDTH-(WIDTH/4)+30, (HEIGHT/2)-90 , 250, 42)
button_repair_text = button_font_interface.render('Repair', True, WHITE)
button_repait_cost = button_font_interface.render('cost', True, YELLOW)

#Кнопка отправки поезда.
button_dispatch = pygame.Rect(WIDTH-(WIDTH/4)+30, (HEIGHT/2)-180 , 250, 42)
button_dispatch_text = button_font_interface.render('Train dispatch', True, WHITE)

#Отображение кол-ва свободных и занятых поездов
trains_status = button_font_interface.render('Not busy: '+' Busy: ',True, YELLOW)

#Шкала здоровья метрополитена
scale_health = pygame.Rect(WIDTH-(WIDTH/4)+35, (HEIGHT/5)-100, 250, 22)
scale_health_text = button_font_interface.render('Train condition', True, GREEN)

#Магазин
#Кнопка перехода в магазин.
button_store = pygame.Rect(WIDTH-(WIDTH/4)+30, (HEIGHT/2)+180 , 250, 42)
button_store_text = button_font_interface.render('Store', True, WHITE)

#Кнопка покупки улучшения поездов
button_tr_lvl_up = pygame.Rect((WIDTH/2)-380, (HEIGHT/2.5)+70, 250, 42)
button_tr_lvl_up_text = button_font_interface.render('Upgrade', True, WHITE)
tr_lvl_cost_txt = button_font_interface.render('', True, YELLOW)

#Кнопка покупки улучшения станций
button_st_lvl_up = pygame.Rect((WIDTH/2)+130, (HEIGHT/2.5)+70, 250, 42)
button_st_lvl_up_text = button_font_interface.render('Upgrade', True, WHITE)
st_lvl_cost_txt = button_font_interface.render('', True, YELLOW)

#События
happening_text = happening_font.render('', True, GREEN)

#Поле ввода никнейма
input_box_name = pygame.Rect(100, 100, 140, 32)

#Кнопка выхода из магазина.
button_togame_text = button_font.render('BACK', True, WHITE)

#**************Классы**************
class station:
    st_id = 0
    color = GRAY
    
    def __init__(self, st_id, color, pos_x, pos_y):
        self.st_id = st_id
        self.color = color
        self.pos_y = pos_y
        self.pos_x = pos_x

class train:
    tr_id = 0
    earn_mult = 1.0
    def __init__(self, tr_id, earn_mult):
        self.earn_mult = earn_mult
        self.tr_id = tr_id

#Настройка цикла
running = True
menu = True
ingame = False
instore = False #Магазин
inhappening = False #Случай

#Начальные Значения
money = 1250
station_cost = 825
train_cost = 100
free_trains = 0
busy_trains = 0
train_numb = free_trains + busy_trains
max_train_numb = 0
st_numb = 1
st_max_numb = 24
health = 250
station_list = []
train_list = []

train_lvl = 1; #Уровень поездов
train_lvl_cost = 15000; #Стоимость апгрейда поездов
st_lvl = 1; #Уровень станций
st_lvl_cost = 30000; #Стоимость апгрейда станций

iEgg = 0

#Открытие файла сохранения
if path.exists(svg_dir):
    svg_file = open(svg_dir, 'r')
else:
    svg_file = open(svg_dir, 'tw')

svg_data = []

if os.stat(svg_dir).st_size == 0:
    print('svg file is empty!')
    with open(svg_dir, 'w') as svg_file:
        svg_file.write(str(money)+'|')
        svg_file.write(str(station_cost)+'|')
        svg_file.write(str(train_cost)+'|')
        svg_file.write(str(free_trains)+'|')
        svg_file.write(str(busy_trains)+'|')
        svg_file.write(str(train_numb)+'|')
        svg_file.write(str(max_train_numb)+'|')
        svg_file.write(str(st_numb)+'|')
        svg_file.write(str(st_max_numb)+'|')
        svg_file.write(str(health)+'|')
        svg_file.write(str(train_lvl)+'|')
        svg_file.write(str(st_lvl)+'|')

else:
    with open(svg_dir, 'r') as svg_file:
        tmp_line = svg_file.read()
        print(tmp_line)
        tmp = str()
        for ch in tmp_line:
            if ch != '|':
                tmp += ch
            else:
                svg_data.append(tmp)
                tmp = str()
                
    print(svg_data)
    money = int(svg_data[0])
    station_cost = int(svg_data[1])
    train_cost = int(svg_data[2])
    free_trains = int(svg_data[3])
    busy_trains = int(svg_data[4])
    train_numb = int(svg_data[5])
    max_train_numb = int(svg_data[6])
    st_numb = int(svg_data[7])
    st_max_numb = int(svg_data[8])
    health = int(svg_data[9])
    train_lvl = int(svg_data[10])
    st_lvl = int(svg_data[11])
    
    print(train_list)

if st_numb > 1:
    max_train_numb = (st_numb-1)*2
else:
    max_train_numb = 0
happening_id = 0
profit = (st_numb*70)+(75*busy_trains)
repair_cost = (((st_numb*70)+(75*train_numb))+((st_numb*70)+(75*train_numb)))

for i in range(1, train_lvl):
    train_lvl_cost *= 3

for i in range(1, st_lvl):
    st_lvl_cost *= 3

station_pos_collection = [
    (370, 310), (270, 250), (150, 250), (50, 200), (570, 310), (670, 280), (770, 250), (870, 250), #8 - RED
    (380, 390), (280, 390), (180, 490), (80, 490), (570, 230), (620, 120), (720, 110), (820, 90), #8-16 - BLUE
    (520, 410), (630, 420), (690, 480), (790, 480), (420, 210), (340, 110), (240, 110), (140, 50) #16-24 - YELLOW
]
obj_main_station = station(0, GRAY, 470, 310)

timer_cooldown = int(FPS*25)
timer_health = int(FPS*8)
timer_train_cooldown = int(FPS*45)
timer_happening = int(FPS*20)
timer_rainbow = int(FPS/2)

#Картинки
tr_lvl1 = pygame.image.load(img_dir + '\p_lvl1.jpg')
tr_lvl2 = pygame.image.load(img_dir + '\p_lvl2.jpg')
tr_lvl3 = pygame.image.load(img_dir + '\p_lvl3.jpg')

st_lvl1 = pygame.image.load(img_dir + '\st_lvl1.jpg')
st_lvl2 = pygame.image.load(img_dir + '\st_lvl2.jpg')
st_lvl3 = pygame.image.load(img_dir + '\st_lvl3.jpg')

menu_bg1 = pygame.image.load(img_dir+'\menu_bg.jpg')
menu_bg2 = pygame.image.load(img_dir+'\menu_bg2.jpg')
menu_bg3 = pygame.image.load(img_dir+'\menu_bg3.jpg')
menu_bgs = [menu_bg1, menu_bg2, menu_bg3]

dict_menu_bgs = {1 : menu_bg1, 2 : menu_bg2, 3 : menu_bg3}
MENU = dict_menu_bgs.get(random.randint(1,3))
print(dict_menu_bgs.items())

#Звуки
snd_doors_close = pygame.mixer.Sound(path.join(snd_dir, 'doors.mp3'))
snd_doors_close.set_volume(2.3)
snd_upps = pygame.mixer.Sound(path.join(snd_dir, 'upps.wav'))
snd_upps.set_volume(0.3)
snd_bpsn = pygame.mixer.Sound(path.join(snd_dir, 'bpsn_2.wav'))
snd_horn = pygame.mixer.Sound(path.join(snd_dir, 'horn.wav'))
snd_horn.set_volume(0.2)

snd_pneumo_1 = pygame.mixer.Sound(path.join(snd_dir, 'pneumo_3.wav'))
snd_pneumo_2 = pygame.mixer.Sound(path.join(snd_dir, 'pneumo_6.wav'))

snd_ring_1 = pygame.mixer.Sound(path.join(snd_dir, 'ring2.wav'))
snd_ring_1.set_volume(0.3)

snd_magic = pygame.mixer.Sound(path.join(snd_dir, 'magic.mp3'))

snd_vu_on = pygame.mixer.Sound(path.join(snd_dir, 'vu_on.wav'))
snd_button = pygame.mixer.Sound(path.join(snd_dir, 'button_1_off.wav'))
snd_button_ingame_1 = pygame.mixer.Sound(path.join(snd_dir, 'drive_on2.wav'))
snd_button_ingame_2 = pygame.mixer.Sound(path.join(snd_dir, 'pb_on.wav'))
snd_button_ingame_3 = pygame.mixer.Sound(path.join(snd_dir, 'pb_off.wav'))

snd_list_train = [snd_pneumo_1, snd_pneumo_2]
snd_list_earn = [snd_doors_close, snd_upps, snd_ring_1]
snd_list_button = [snd_button, snd_button_ingame_1, snd_button_ingame_2, snd_button_ingame_3, snd_vu_on]

#************************Функции**********************
def save_game():
    with open(svg_dir, 'w') as svg_file:
        svg_file.write(str(money)+'|')
        svg_file.write(str(station_cost)+'|')
        svg_file.write(str(train_cost)+'|')
        svg_file.write(str(free_trains)+'|')
        svg_file.write(str(busy_trains)+'|')
        svg_file.write(str(train_numb)+'|')
        svg_file.write(str(max_train_numb)+'|')
        svg_file.write(str(st_numb)+'|')
        svg_file.write(str(st_max_numb)+'|')
        svg_file.write(str(health)+'|')
        svg_file.write(str(train_lvl)+'|')
        svg_file.write(str(st_lvl)+'|')

#******************Главный Цикл*****************
while running:
    #**************События****************
    mouse_x, mouse_y = pygame.mouse.get_pos() #Постоянная проверка позиции мыши на экране игры

    #Рандомный цвет
    if timer_rainbow <= int(FPS/2) and timer_rainbow > 0:
        timer_rainbow -= 1
    else:
        timer_rainbow = int(FPS/2)
        rgb = (random.randint(10,255), random.randint(10,255), random.randint(10,255))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Событие нажатия на крестик окна
            running = False
            save_game()

        #События нажатия кнопок в меню
        elif menu == True and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and mouse_x >= 390 and mouse_y >= 548 and mouse_x <= 890 and mouse_y <= 648: #Событие кнопки выхода
                print('event: button_quit')
                save_game()
                running = False
            else:
                pass
                
            if event.button == 1 and mouse_x >= 390 and mouse_y >= 428 and mouse_x <= 890 and mouse_y <= 548: #Событие кнопки "играть"
                print('event: button_play')
                random.choice(snd_list_button).play()
                menu = False
                ingame = True
            else:
                pass

        #События наведения курсора на кнопки в меню
        elif menu == True:
            if mouse_x >= 390 and mouse_y >= 548 and mouse_x <= 890 and mouse_y <= 648: #Событие наведения курсора на кнопку выхода
                button_quit_text = button_font.render('EXIT', True, YELLOW)
            else:
                button_quit_text = button_font.render('EXIT', True, WHITE)
                
            if mouse_x >= 390 and mouse_y >= 428 and mouse_x <= 890 and mouse_y <= 528: #Событие наведения курсора на кнопку начала игры
                button_play_text = button_font.render('PLAY', True, YELLOW)
            else:
                button_play_text = button_font.render('PLAY', True, WHITE)

        #События нажатия кнопок в основном игровом интерфейсе
        elif menu == False and ingame == True and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and mouse_x >= 960 and mouse_y >= HEIGHT-(HEIGHT/6): #Событие кнопки выхода в меню
                MENU = random.choice(menu_bgs)
                random.choice(snd_list_button).play()
                print('event: button_inmenu')
                ingame = False
                menu = True
            else:
                pass
                
            if event.button == 1 and mouse_x >= obj_main_station.pos_x - 15 and mouse_y >= obj_main_station.pos_y - 15 and mouse_x <= obj_main_station.pos_x + 15 and mouse_y <= obj_main_station.pos_y + 15:
                iEgg += 1
                print('egg', iEgg)
                winsound.Beep(iEgg*100, 50)
                if iEgg >= 30:
                    iEgg = 0
                else:
                    pass
            else:
                pass
            
            if event.button == 1 and mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= HEIGHT/2 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= HEIGHT-(HEIGHT/2)+42 and money >= station_cost and st_numb <= st_max_numb: #Событие кнопки создания станции
                random.choice(snd_list_button).play()
                obj_station = station(st_numb, RED, station_pos_collection[st_numb-1][0], station_pos_collection[st_numb-1][1])
                st_numb += 1
                station_list.append((obj_station.st_id, obj_station.color, obj_station.pos_x, obj_station.pos_y))
                print(station_list)
                print('event: st_create')
                money -= station_cost
                max_train_numb += 2
                station_cost *= 1.15
                station_cost = int(station_cost)
            else:
                pass
                    
            if event.button == 1 and mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)+90 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= HEIGHT-(HEIGHT/2)+132 and money >= train_cost and st_numb > 1 and train_numb < max_train_numb: #Событие кнопки покупки поезда
                random.choice(snd_list_button).play()
                obj_train = train(train_numb, 1.0)
                train_list.append((obj_train.tr_id, obj_train.earn_mult))
                money -= train_cost
                train_cost *= 1.2
                train_cost = int(train_cost)
                free_trains += 1
                print('event: train_buy')
                print(train_list)
                print(train_numb)
            else:
                pass        
                    
            if event.button == 1 and mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)+180 and mouse_x <= (WIDTH-(WIDTH/4)+280) and mouse_y <= HEIGHT-(HEIGHT/2)+222: #Событие кнопки перехода в story
                random.choice(snd_list_button).play()
                instore = True
                menu = False
                ingame = False
                print('event: button_story')
            else:
                pass
                
            if event.button == 1 and mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)-90 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= ((HEIGHT/2)-48) and money >= repair_cost and train_numb > 0: #Событие кнопки починки 
                money -= repair_cost
                health = 250
                random.choice(snd_list_button).play()
                print('event: button_repair')
            else:
                pass
                
            if event.button == 1 and mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)-180 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= (HEIGHT-(HEIGHT/2)-138) and free_trains > 0: #Событие кнопки отправки поездов
                random.choice(snd_list_train).play()
                free_trains -= 1
                busy_trains += 1
            else:
                pass
                    
        elif ingame == True and menu == False: #События наведения кнопок в интерфейсе игры
        
            if mouse_x >= 960 and mouse_y >= 600: #Событие наведения курсора на кнопку выхода в меню
                button_tomenu_text = button_font.render('EXIT', True, YELLOW)
            else:
                button_tomenu_text = button_font.render('EXIT', True, WHITE)
            
            button_txt = 'Repair'
            if mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)-90 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= (HEIGHT-(HEIGHT/2)-48): #Событие наведения на кнопку ремонта
                button_repair_text = button_font_interface.render(button_txt.upper(), True, YELLOW)
            else:
                button_repair_text = button_font_interface.render(button_txt.lower(), True, WHITE)

            button_txt = 'Create station'
            if mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= HEIGHT/2 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= HEIGHT-(HEIGHT/2)+42: #Событие наведения на кнопку создания станции
                button_st_cr_text = button_font_interface.render(button_txt.upper(), True, YELLOW)
            else:
                button_st_cr_text = button_font_interface.render(button_txt.lower(), True, WHITE)
               
            button_txt = 'Buy train'
            if mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)+90 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= HEIGHT-(HEIGHT/2)+132: #Событие наведения на кнопку покупки поезда
                button_train_buy_text = button_font_interface.render(button_txt.upper(), True, YELLOW)
            else:
                button_train_buy_text = button_font_interface.render(button_txt.lower(), True, WHITE)
            
            button_txt = 'Store'
            if mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)+180 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= HEIGHT-(HEIGHT/2)+222: #Событие наведения на кнопку исторического режима
                button_store_text = button_font_interface.render(button_txt.upper(), True, YELLOW)
            else:
                button_store_text = button_font_interface.render(button_txt.lower(), True, WHITE)
                
            button_txt = 'Train dispatch'
            if mouse_x >= WIDTH-(WIDTH/4)+30 and mouse_y >= (HEIGHT/2)-180 and mouse_x <= WIDTH-(WIDTH/4)+280 and mouse_y <= (HEIGHT-(HEIGHT/2)-138): #Событие наведения на кнопку ремонта
                if free_trains > 0:
                    button_dispatch_text = button_font_interface.render(button_txt.upper(), True, YELLOW)
                else:
                    button_dispatch_text = button_font_interface.render(button_txt.upper(), True, RED)
            else:
                if free_trains > 0:
                    button_dispatch_text = button_font_interface.render(button_txt.lower(), True, WHITE)
                else:
                    button_dispatch_text = button_font_interface.render(button_txt.lower(), True, RED)
            
        #События нажатия кнопок в store
        elif event.type == pygame.MOUSEBUTTONDOWN and instore == True and menu == False and ingame == False:
            if event.button == 1 and mouse_x >= 960 and mouse_y >= HEIGHT-(HEIGHT/6): #Событие кнопки выхода в меню
                random.choice(snd_list_button).play()
                print('event: button_togame')
                ingame = True
                instore = False
                
            #Покупка улучшения станций
            elif event.button == 1 and mouse_x >= (WIDTH/2)+130 and mouse_y >= (HEIGHT/2.5)+70 and mouse_x <= (WIDTH/2)+380 and mouse_y <= (HEIGHT/2.5)+112 and money >= st_lvl_cost and st_lvl < 3:
                random.choice(snd_list_button).play()
                money -= st_lvl_cost
                st_lvl_cost *= 3
                st_lvl += 1
                    
            #Покупка улучшения поездов
            elif event.button == 1 and mouse_x >= (WIDTH/2)-380 and mouse_y >= (HEIGHT/2.5)+70 and mouse_x <= (WIDTH/2)-130 and mouse_y <= (HEIGHT/2.5)+112 and money >= train_lvl_cost and train_lvl < 3:
                random.choice(snd_list_button).play()
                money -= train_lvl_cost
                train_lvl_cost *= 3
                train_lvl += 1
            else:
                pass

        #События наведения кнопок в store
        elif instore == True and menu == False and ingame == False:
            if mouse_x >= 960 and mouse_y >= 600: #Событие наведения курсора на кнопку "обратно"
                button_togame_text = button_font.render('BACK', True, YELLOW)
            else:
                button_togame_text = button_font.render('BACK', True, WHITE)
            
            #апгрейд поездов
            button_txt = 'upgrade'
            if mouse_x >= (WIDTH/2)-380 and mouse_y >= (HEIGHT/2.5)+70 and mouse_x <= (WIDTH/2)-130 and mouse_y <= (HEIGHT/2.5)+112:
                button_tr_lvl_up_text = button_font_interface.render(button_txt.upper(), True, YELLOW)
            else:
                button_tr_lvl_up_text = button_font_interface.render(button_txt.lower(), True, WHITE)

            #апгрейд станций
            button_txt = 'upgrade'
            if mouse_x >= (WIDTH/2)+130 and mouse_y >= (HEIGHT/2.5)+70 and mouse_x <= (WIDTH/2)+380 and mouse_y <= (HEIGHT/2.5)+112:
                button_st_lvl_up_text = button_font_interface.render(button_txt.upper(), True, YELLOW)
            else:
                button_st_lvl_up_text = button_font_interface.render(button_txt.lower(), True, WHITE)
            
            '''
            elif inname == True and menu == False:
                text = ''
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            '''
        else:
            pass
            
    #Таймер работы поездов (Таймер)
    if busy_trains > 0 and timer_train_cooldown > 0:
        timer_train_cooldown -= 1
        if timer_cooldown % FPS == 0:
            print(int(timer_train_cooldown/FPS))
        else:
            pass
    elif timer_train_cooldown <= 0:
        snd_horn.play()
        busy_trains -= 1
        free_trains += 1
        timer_train_cooldown = FPS*45
    else:
        pass
        
    #Таймер случаев
    if (ingame == True or instore == True) and menu == False:
        if timer_happening > 0:
            timer_happening -= 1
            if timer_happening <= 6000:
                happening_text = happening_font.render('', True, RED)
            else:
                pass
            
        elif timer_happening <= 0:
            timer_happening = FPS*120
            print('event: happening')
            happening_id = random.randint(1, 7)
            print(happening_id)
            if train_numb >= 2:
                if happening_id == 1:
                    if st_numb > 3:
                        money -= 250
                        print('event: happening: bad, -250$')
                        happening_text = happening_font.render('Some problems -250 $', True, RED)
                    else:
                        pass
                        
                elif happening_id == 2:
                    if st_numb > 4:
                        money += 2500
                        print('event: happening: nice, +2500$')
                        happening_text = happening_font.render('You get a subsidy! +2500 $', True, GREEN)
                    else:
                        pass
                elif happening_id == 3:
                    if st_numb > 2:
                        money -= 100
                        print('event: happening: bad, -100$')
                        happening_text = happening_font.render('Some problems -100 $', True, RED)
                    else:
                        pass
                elif happening_id == 4:
                    if st_numb > 2:
                        money += 5000
                        print('event: happening: nice, +5000$')
                        happening_text = happening_font.render('You get a big subsidy! +5000 $', True, GREEN)
                    else:
                        pass
                else:
                    money -= 10
                    print('event: happening: coffee')
                    happening_text = happening_font.render('The machinist bought coffee. -10$', True, YELLOW)
            else:
                pass
                
    #Доход от поездов (Таймер), рассчёт дохода.
    profit = ((st_numb*70)*st_lvl)+((busy_trains*75)*train_lvl)
    if timer_cooldown > 0 and st_numb > 1:
        timer_cooldown -= 1

    elif busy_trains >= 1 or st_numb > 1:
        money += profit
        timer_cooldown = FPS*25
        print('event: payday')
        if ingame == True or instore == True:
            random.choice(snd_list_earn).play()
        else:
            pass
    else:
        pass
        
    #Расчёт кол-ва поездов
    train_numb = free_trains + busy_trains
    
    #Расчёт стоимости ремонта
    repair_cost = (profit+profit)
    if repair_cost > 7500:
        repair_cost = 7500
    else:
        pass
    
    #Таймер здоровья
    if timer_health > 0:
        timer_health -= 1
        #print(timer_health)
    elif health > 0 and busy_trains > 0:
        timer_health = int(FPS*8)
        health -= 10 + busy_trains
        print(health)
    elif health <= 0:
        if train_numb > 0:
            if free_trains > 0:
                free_trains -= 1
            elif busy_trains > 0: 
                busy_trains -= 1
            else:
                pass
        else:
            pass
        timer_health = int(FPS*8)
    else:
        pass
    
    clock.tick(FPS)
    #**************Обновление****************
    
    #**************Визуализация**************
    screen.fill(BLACK)
    
    if menu: #Отрисовка элементов интерфейса
        #Отрисовка заднего фона в меню
        screen.blit(MENU, MENU.get_rect(bottomright = (WIDTH, HEIGHT)))
        
        #Отрисовка названия игры
        screen.blit(game_name_text_b, (230, 125))
        screen.blit(game_name_text_f, (240, 120))
        
        #Кнопка начала игры
        pygame.draw.rect(screen, WHITE, button_play, 4)
        screen.blit(button_font.render('PLAY', True, BLACK), (WIDTH-(WIDTH/2)-105, HEIGHT-(HEIGHT/10)-195))
        screen.blit(button_play_text, (WIDTH-(WIDTH/2)-100, HEIGHT-(HEIGHT/10)-200))
        
        #Кнопка выхода
        pygame.draw.rect(screen, WHITE, button_quit, 4)
        screen.blit(button_font.render('EXIT', True, BLACK), (WIDTH-(WIDTH/2)-105, HEIGHT-(HEIGHT/10)-75))
        screen.blit(button_quit_text, (WIDTH-(WIDTH/2)-100, HEIGHT-(HEIGHT/10)-80))
        
        #Автор
        screen.blit(pygame.font.SysFont(font_global,30).render('@Pavel Bunos', True, rgb), (10, HEIGHT-40))
        
        #Версия
        screen.blit(pygame.font.SysFont(font_global,30).render(game_version.upper(), True, YELLOW), (980, HEIGHT-490))
    else:
        pass
        
    if ingame: #Отрисовка игровой области
        
        #Отрисовка интерфейса в игре
        pygame.draw.rect(screen, cl_interface, pygame.Rect((0, HEIGHT-(HEIGHT/6), 1280, 720)))
        pygame.draw.rect(screen, cl_interface, pygame.Rect((WIDTH-(WIDTH/4), 0, 1280, 720)))
        
        pygame.draw.line(screen, WHITE, [WIDTH-(WIDTH/4), 0], [WIDTH-(WIDTH/4), 720], 4)
        pygame.draw.line(screen, WHITE, [WIDTH-(WIDTH/4), (HEIGHT/5)], [1280, (HEIGHT/5)], 4)
        pygame.draw.line(screen, WHITE, [0, (HEIGHT-(HEIGHT/6))], [1280, (HEIGHT-(HEIGHT/6))], 4)
        pygame.draw.line(screen, WHITE, [(WIDTH/4)+130, (HEIGHT-(HEIGHT/6))], [(WIDTH/4)+130, 720], 4)
        
        #Монитор событий
        pygame.draw.rect(screen, BLACK, pygame.Rect((WIDTH/4)+160, HEIGHT-(HEIGHT/6)+25, 450, 75))
        pygame.draw.rect(screen, WHITE, pygame.Rect((WIDTH/4)+160, HEIGHT-(HEIGHT/6)+25, 450, 75), 4)
        screen.blit(happening_text, ((WIDTH/4)+170, HEIGHT-(HEIGHT/6)+55))
        if timer_happening <= 6000 and ingame == True:
            happening_text = button_font_interface.render('', True, GREEN)   
        else:
            pass
            
        #Кнопка выхода в меню
        screen.blit(button_tomenu_text, (WIDTH-(WIDTH/4)+70, 630))
        
        #Кнопка ремонта
        pygame.draw.rect(screen, WHITE, button_repair, 4)
        screen.blit(button_repair_text, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)-80))
        if money >= repair_cost and train_numb > 0:
            button_repair_cost = button_font_interface.render(str(repair_cost)+'$', True, YELLOW)
        else:
            button_repair_cost = button_font_interface.render(str(repair_cost)+'$', True, RED)
        screen.blit(button_repair_cost, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)-40))
        
        #Кнопка отправки поезда
        pygame.draw.rect(screen, WHITE, button_dispatch, 4)
        screen.blit(button_dispatch_text, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)-170))
        
        #Кнопка создания станции
        pygame.draw.rect(screen, WHITE, button_st_cr, 4)
        screen.blit(button_st_cr_text, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)+10))
        
        #Кнопка покупки поезда
        pygame.draw.rect(screen, WHITE, button_train_buy, 4)
        screen.blit(button_train_buy_text, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)+100))
        
        #Отображение кол-ва занятых и не занятых поездов
        trains_status = button_font_interface.render('Free: '+str(free_trains)+' Busy: '+str(busy_trains),True, YELLOW)
        screen.blit(trains_status, (WIDTH-(WIDTH/4)+40, (HEIGHT/5)+85))
        
        #Шкала здоровья метрополитена
        screen.blit(scale_health_text, (WIDTH-(WIDTH/4)+35, (HEIGHT/5)-130))
        pygame.draw.rect(screen, GREEN, pygame.Rect(WIDTH-(WIDTH/4)+35, (HEIGHT/5)-100, health, 22))
        pygame.draw.rect(screen, WHITE, scale_health, 4)
        
        #Кнопка перехода в story
        pygame.draw.rect(screen, WHITE, button_store, 4)
        screen.blit(button_store_text, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)+190))
        
        #Отрисовка стоимости станции
        if st_numb < st_max_numb:
            if money >= station_cost and st_numb <= st_max_numb:
                button_st_cr_cost = button_font_interface.render(str(station_cost)+'$', True, YELLOW)
            else:
                button_st_cr_cost = button_font_interface.render(str(station_cost)+'$', True, RED)
        else:
            button_st_cr_cost = button_font_interface.render('Max', True, rgb)
        screen.blit(button_st_cr_cost, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)+50))
        
        #Отрисовка стоимости поезда
        if train_numb < max_train_numb:
            if money >= train_cost and st_numb > 1 and train_numb < max_train_numb:
                button_train_buy_cost = button_font_interface.render(str(train_cost)+'$', True, YELLOW)
            else:
                button_train_buy_cost = button_font_interface.render(str(train_cost)+'$', True, RED)
        else:
            button_train_buy_cost = button_font_interface.render('Max', True, rgb)
        screen.blit(button_train_buy_cost, (WIDTH-(WIDTH/4)+40, (HEIGHT/2)+140))
        
        #Отрисовка линий
        '''
        i = 1
        obj_before = (obj_main_station.pos_x, obj_main_station.pos_y)
        for obj in station_list:
            pygame.draw.line(screen, GRAY, (obj_before[0], obj_before[1]), (obj[2], obj[3]), 4)
            if i < 4:
                obj_before = (obj[2], obj[3])
                i += 1
            else:
                obj_before = (obj_main_station.pos_x, obj_main_station.pos_y)
                i = 1
        '''
        #Отрисовка линий без ООП (временное решение)
        i = 1
        numb_rend_st = 1
        pos_before = (obj_main_station.pos_x, obj_main_station.pos_y)
        for pos in station_pos_collection:
            if numb_rend_st < st_numb:
                pygame.draw.line(screen, GRAY, (pos_before[0], pos_before[1]), (pos[0], pos[1]), 4)
                if i < 4:
                    pos_before = (pos[0], pos[1])
                    i += 1
                else:
                    pos_before = (obj_main_station.pos_x, obj_main_station.pos_y)
                    i = 1
                numb_rend_st += 1
            else:
                break

        #Отрисовка станций
        '''
        i = 0
        for obj in station_list:
            if i < 8:
                pygame.draw.circle(screen, RED, (obj[2], obj[3]), 15)
            elif i < 16 and i >= 8:
                pygame.draw.circle(screen, BLUE, (obj[2], obj[3]), 15)
            elif i < 24 and i >= 16:
                pygame.draw.circle(screen, YELLOW, (obj[2], obj[3]), 15)
            i += 1
        '''

        #Отрисовка станций без ООП (временное решение)
        i = 0
        for pos in station_pos_collection:
            if i < st_numb-1:
                if i < 8:
                    pygame.draw.circle(screen, RED, (pos[0], pos[1]), 15)
                elif i < 16 and i >= 8:
                    pygame.draw.circle(screen, BLUE, (pos[0], pos[1]), 15)
                elif i < 24 and i >= 16:
                    pygame.draw.circle(screen, YELLOW, (pos[0], pos[1]), 15)
            else:
                break
            i += 1

        #Отрисовка баланса
        if timer_cooldown >= (FPS*25)-50 and (train_numb >= 1 or st_numb > 1):
            balance_text = balance_font.render('Balance: '+str(money)+'$ +'+str(profit)+'$', True, GREEN)
        else:
            balance_text = balance_font.render('Balance: '+str(money)+'$', True, YELLOW)
        screen.blit(balance_text, (20, 610))
  
        #Отрисовка прибыли
        balance_text = balance_font.render(str(int(timer_cooldown/60))+' sec '+'Profit: '+str(profit)+'$', True, YELLOW)
        screen.blit(balance_text, (20, 645))

        #Отрисовка количества поездов и станций
        trains_text = balance_font.render('Trains: '+str(train_numb)+' Stations: '+str(st_numb-1), True, YELLOW)
        screen.blit(trains_text, (20, 680))

        if iEgg < 23:
            pygame.draw.circle(screen, WHITE, (obj_main_station.pos_x, obj_main_station.pos_y), 20, 5)
            pygame.draw.circle(screen, WHITE, (obj_main_station.pos_x, obj_main_station.pos_y), 10)
        else:
            pygame.draw.circle(screen, rgb, (obj_main_station.pos_x, obj_main_station.pos_y), 20, 5)
            pygame.draw.circle(screen, rgb, (obj_main_station.pos_x, obj_main_station.pos_y), 10)
    else:
        pass
        
    if instore:

        screen.fill(cl_interface)
        
        #Отрисовка интерфейса в магазине
        pygame.draw.rect(screen, cl_interface, pygame.Rect((0, HEIGHT-(HEIGHT/6), 1280, 720)))
        pygame.draw.line(screen, WHITE, [0, (HEIGHT-(HEIGHT/6))], [1280, (HEIGHT-(HEIGHT/6))], 4)
        pygame.draw.line(screen, WHITE, [WIDTH-(WIDTH/4), (HEIGHT-(HEIGHT/6))], [WIDTH-(WIDTH/4), 720], 4)
        pygame.draw.line(screen, WHITE, [(WIDTH/4)+130, (HEIGHT-(HEIGHT/6))], [(WIDTH/4)+130, 720], 4)
        
        #train lvl картинка
        if train_lvl == 1:
            screen.blit(tr_lvl1, ((WIDTH/2)-450, (HEIGHT/2.5)-250))
        elif train_lvl == 2:
            screen.blit(tr_lvl2, ((WIDTH/2)-450, (HEIGHT/2.5)-250))
        elif train_lvl == 3:
            screen.blit(tr_lvl3, ((WIDTH/2)-450, (HEIGHT/2.5)-250))
        else:
            pass
        
        #Отрисовка кнопки улучшения поездов
        pygame.draw.rect(screen, WHITE, button_tr_lvl_up, 4)
        screen.blit(button_tr_lvl_up_text, ((WIDTH/2)-305, (HEIGHT/2.5)+80))
        if money >= train_lvl_cost and train_lvl < 3:
            tr_lvl_cost_txt = button_font_interface.render('Price: '+str(train_lvl_cost)+'$', True, YELLOW)
        elif money < train_lvl_cost:
            tr_lvl_cost_txt = button_font_interface.render('Price: '+str(train_lvl_cost)+'$', True, RED)
        else:
            tmp_txt = 'Train LvL: MAX!'
            tr_lvl_cost_txt = button_font_interface.render(chr(random.randint(1,255))+tmp_txt.capitalize()+chr(random.randint(1,255)), True, rgb)
            
        screen.blit(tr_lvl_cost_txt, ((WIDTH/2)-380, (HEIGHT/2.5)+120))
        
        #train lvl рамка
        pygame.draw.rect(screen, WHITE, ((WIDTH/2)-450, (HEIGHT/2.5)-250, 400, 300), 4)
        
        #station lvl картинка
        if st_lvl == 1:
            screen.blit(st_lvl1, ((WIDTH/2)+50, (HEIGHT/2.5)-250))
        elif st_lvl == 2:
            screen.blit(st_lvl2, ((WIDTH/2)+50, (HEIGHT/2.5)-250))
        elif st_lvl == 3:
            screen.blit(st_lvl3, ((WIDTH/2)+50, (HEIGHT/2.5)-250))
        else:
            pass
            
        #Отрисовка кнопки улучшения станций
        pygame.draw.rect(screen, WHITE, button_st_lvl_up, 4)
        screen.blit(button_st_lvl_up_text, ((WIDTH/2)+205, (HEIGHT/2.5)+80))
        if money >= st_lvl_cost and st_lvl < 3:
            st_lvl_cost_txt = button_font_interface.render('Price: '+str(st_lvl_cost)+'$', True, YELLOW)
        elif money < st_lvl_cost:
            st_lvl_cost_txt = button_font_interface.render('Price: '+str(st_lvl_cost)+'$', True, RED)
        else:
            tmp_txt = 'Train LvL: MAX!'
            st_lvl_cost_txt = button_font_interface.render(chr(random.randint(1,255))+tmp_txt.capitalize()+chr(random.randint(1,255)), True, rgb)
        screen.blit(st_lvl_cost_txt, ((WIDTH/2)+130, (HEIGHT/2.5)+120))
        
        #station lvl рамка
        pygame.draw.rect(screen, WHITE, ((WIDTH/2)+50, (HEIGHT/2.5)-250, 400, 300), 4)
        
        #Отрисовка баланса
        if timer_cooldown >= (FPS*25)-50 and (train_numb >= 1 or st_numb > 1):
            balance_text = balance_font.render('Balance: '+str(money)+'$ +'+str(profit)+'$', True, GREEN)
        else:
            balance_text = balance_font.render('Balance: '+str(money)+'$', True, YELLOW)
        screen.blit(balance_text, (20, 610))
  
        #Отрисовка прибыли
        balance_text = balance_font.render(str(int(timer_cooldown/60))+' sec '+'Profit: '+str(profit)+'$', True, YELLOW)
        screen.blit(balance_text, (20, 645))

        #Отрисовка количества поездов и станций
        trains_text = balance_font.render('Trains: '+str(train_numb)+' Stations: '+str(st_numb-1), True, YELLOW)
        screen.blit(trains_text, (20, 680))
        
        #Монитор событий
        pygame.draw.rect(screen, BLACK, pygame.Rect((WIDTH/4)+160, HEIGHT-(HEIGHT/6)+25, 450, 75))
        pygame.draw.rect(screen, WHITE, pygame.Rect((WIDTH/4)+160, HEIGHT-(HEIGHT/6)+25, 450, 75), 4)
        screen.blit(happening_text, ((WIDTH/4)+170, HEIGHT-(HEIGHT/6)+55))
        if timer_happening <= 6000 and ingame == True:
            happening_text = button_font_interface.render('', True, GREEN)   
        else:
            pass
            
        #Кнопка выхода в меню
        screen.blit(button_togame_text, (WIDTH-(WIDTH/4)+70, 630))
    else:
        pass
        
    #Конец визуализации
    pygame.display.flip()

pygame.quit()