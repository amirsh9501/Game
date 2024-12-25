
# Это мое первое изменение в программе
# А это коментарий твоего преподавателя
# Импортируем библиотеку pygame
import pygame
from pygame import *
#from player import *
#from blocks import *

#Объявляем переменные
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400" #Цвет заднего фона

class Camera(object):#отслеживает положение игрока и сдвигает видимую область так, чтобы игрок всегда оставался в центре экрана.
    def __init__(self, camera_func, width, height):#это метод конструктора класса Camera в pygame. 
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):#Метод apply(self, target) в классе Camera возвращает значение target.rect.move(self.state.topleft)
        return target.rect.move(self.state.topleft)#

    def update(self, target):#обновляет состояние, вызывая функцию camera_func, которая выполняет всю работу.
        self.state = self.camera_func(self.state, target.rect)#

    def camera_configure(camera, target_rect):# это функция, которая в Pygame позволяет настроить положение камеры, учитывая координаты целевого прямоугольника (target_rect) и размеры экрана (SCREEN_WIDTH и SCREEN_HEIGHT).
        l, t, _, _ = target_rect# это переменные, которые указывают на координаты цели (l — слева, t — сверху). 
        _, _, w, h = camera#переменные, которые указывают на параметры камеры (w — ширина, h — высота)
        l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2# это выражение, которое устанавливает координаты для перемещения камеры, учитывая половину ширины и высоты окна (WIN_WIDTH и WIN_HEIGHT). 

        l = min(0, l) # Не движемся дальше левой границы
        l = max(-(camera.width-WIN_WIDTH), l) # Не движемся дальше правой границы
        t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
        t = min(0, t) # Не движемся дальше верхней границы

        return Rect(l, t, w, h)# возвращает прямоугольник с указанными координатами и размерами. 


def main():#определяет основную функцию скрипта
    pygame.init() # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("SpaceWar") # Пишем в шапку
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR)) # Заливаем поверхность сплошным цветом

    #hero = Player(55,55) # создаем героя по (x,y) координатам
    left = right = False # по умолчанию - стоим
    up = False

    entities = pygame.sprite.Group #Все объекты
    platforms = [] # то, во что мы будем врезаться или опираться

   #entities.add(hero)#

level = [
 "----------------------------------",
 "-                                -",
 "-               --               -",
 "-                                -",
 "-      --                        -",
 "-                                -",
 "--                               -",
 "-                                -",
 "-      ----                  --- -",
 "-                                -",
 "--                               -",
 "-                                -",
 "-  ---                           -",
 "-                                -",
 "-                                -",
 "-      ---                       -",
 "-                                -",
 "-          -------      ----     -",
 "-                                -",
 "-          -                     -",
 "-          --                    -",
 "-                                -",
 "-                                -",
 "----------------------------------"]

timer = pygame.time.Clock()#создаёт новый объект Clock, который можно использовать для отслеживания времени в игре на платформе Pygame.  С его помощью можно контролировать скорость игры, управлять событиями с задержкой во времени и синхронизировать разные элементы игры. 
x=y=0 # координаты
for row in level: # вся строка
    for col in row: # каждый символ
        if col == "-":#
            #pf = Platform(x,y)
            #entities.add(pf)
            #platforms.append(pf)

        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
    y += PLATFORM_HEIGHT #то же самое и с высотой
    x = 0 #на каждой новой строчке начинаем с нуля

total_level_width = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
total_level_height = len(level)*PLATFORM_HEIGHT # высоту

camera = Camera(camera_configure, total_level_width, total_level_height)# это создание экземпляра камеры в платформе на Python с использованием библиотеки pygame.

while 1: # Основной цикл программы
    timer.tick(60)#это функция для установки частоты обновления экрана в игре на Pygame.
    for e in pygame.event.get(): # Обрабатываем события
        if e.type == QUIT:#вызывает SystemExit с сообщением «QUIT».
            raise SystemExit ; "QUIT"
        if e.type == KEYDOWN and e.key == K_UP:#устанавливает переменную up в True, если нажата клавиша вверх. 
            up = True
        if e.type == KEYDOWN and e.key == K_LEFT:#устанавливает переменную left в True, если нажата клавиша влево. 
            left = True
        if e.type == KEYDOWN and e.key == K_RIGHT:#: устанавливает переменную right в True, если нажата клавиша вправо.
            right = True


        if e.type == KEYUP and e.key == K_UP:#при отпускании клавиши вверх (K_UP) переменная up будет равна False
            up = False#
        if e.type == KEYUP and e.key == K_RIGHT:#при отпускании клавиши вверх (K_RIGHT) переменная right будет равна False
            right = False#
        if e.type == KEYUP and e.key == K_LEFT:#при отпускании клавиши вверх (K_LEFT) переменная left будет равна False
            left = False#

    screen.blit(bg, (0,0)) # Каждую итерацию необходимо всё перерисовывать


    camera.update(hero) # центризируем камеру относительно персонажа
    hero.update(left, right, up,platforms) # передвижение
    #entities.draw(screen) # отображение
    for e in entities:#
        screen.blit(e.image, camera.apply(e))# позволяет создавать эффект движения камеры: меньший прямоугольник центрируется относительно главного персонажа, и все объекты рисуются в этом прямоугольнике, за счёт чего создаётся впечатление движения камеры. 


    pygame.display.update() # обновление и вывод всех изменений на экран


if __name__ == "__main__":#позволяет определить, как именно был запущен скрипт — непосредственно или через импорт в другой скрипт. 
    main()#