# Выполнил студент группы 21-ЗИЭ Малюков М.П.
# Дисциплина - Программирование
# Задача № 1 - Согласно своему варианту написать программу на языке Pуthon, формирующую указанное изображение с использованием графических примитивов.
    # Допускается собственный рисунок. Цветовую гамму и размер выбрать самостоятельно.
    # Вариант № 6 - Куб.
# Задача № 2 - Используя результаты предыдущей работы, напишите на языке  Pуthon программу анимации для вашего графического объекта. 
    # Перемещение управляется клавишами стрелками. Траекторию и завершение движения определите по варианту.


# Подключаем графический модуль
from graph import *   

# Определяем цвета
blueForeground = (30,136,229)
blueLight = (33,150,243)
blueDark = (25,118,210)
blueLine = (21,101,192)
shadowColor = (104,159,56)
backgroundColor = (139,195,74)
# Определяем начальное положение фигур 
x = 200; y = 100
# Определяем размеры окна
windowWidth = 800
windowHeight = 700
# Задаем нулевые значения шагов изменения координат   
dx = 0;	dy = 0


# Опрелеляем ширину и высоту рабочей области окна, опрелеляем координаты области рисования
def initWindow():
    windowSize (windowWidth, windowHeight)
    canvasSize (windowWidth - 100, windowHeight - 100)
    brushColor(backgroundColor)
    rectangle(0, 0, windowWidth, windowHeight)


# Рендерим кубик
def renderCube():
    global shadow, partOfTheCube_1, partOfTheCube_2, partOfTheCube_3, partOfTheCube_4, partOfTheCube_5
    brushColor(shadowColor)
    penSize(0)
    shadow = circle(x+42, y+68, 43)
    penColor(blueLine)
    penSize(1)
    brushColor (blueForeground)
    partOfTheCube_1 = rectangle(x, y+80, x+50, y+30)
    brushColor (blueLight)
    partOfTheCube_2 = polygon([(x, y+30), (x+50, y+30), (x+30, y)])
    partOfTheCube_3 = polygon([(x+50, y+30), (x+80, y), (x+30, y)])
    brushColor (blueDark)
    partOfTheCube_4 = polygon([(x+50, y+80), (x+80, y+50), (x+50, y+30)])
    partOfTheCube_5 = polygon([(x+80, y+50), (x+80, y), (x+50, y+30)])


# Определяем обработчики событий
def keyPressed (event):
    global dx, dy
    if event.keycode == VK_LEFT:
        dx = -5; dy = 0
    elif event.keycode == VK_RIGHT:
        dx = 5; dy = 0
    elif event.keycode == VK_UP:
        dx = 0; dy = -5
    elif event.keycode == VK_DOWN:
        dx = 0; dy = 5
    elif event.keycode == VK_SPACE:
        dx = dy = 0
    elif event.keycode == VK_ESCAPE:
        close()


# Функция перемещения куба
def update():
    moveObjectBy(shadow, dx, dy)
    moveObjectBy(partOfTheCube_1, dx, dy)
    moveObjectBy(partOfTheCube_2, dx, dy)
    moveObjectBy(partOfTheCube_3, dx, dy)
    moveObjectBy(partOfTheCube_4, dx, dy)
    moveObjectBy(partOfTheCube_5, dx, dy)

# Функция проверки выхода фигуры за край поля 
def end():
    global dx, dy
    if coords(partOfTheCube_1)[0] < 0 or coords(partOfTheCube_1)[0] > windowWidth - 150:
        dx = 0
    elif coords(partOfTheCube_1)[1] < 0 or coords(partOfTheCube_1)[1] > windowHeight - 150:
        dy = 0


# Главная функция
def main():
    initWindow()
    renderCube()
    onKey (keyPressed)
    onTimer (update, 50)
    onTimer (end, 50)
    run()

main()