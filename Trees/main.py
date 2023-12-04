import turtle as t
import random as r

axiom = '22220'
rules = {'1': '21', '0': '1[-20][+20]'}

num_i = 12   # количество итераций
trunk = 10   # длина кусочка ствола
angle = 14   # угол кроны
thick = 16   # толщина ствола
thick_reduction_speed = 0.75
colors = ['#271d17', '#708a21', '#243219', '#4f6028']

angle_scale = 1    # множитель случайности угла кроны (от 0 до 2)
length_scale = 1    # множитель случайности длины дерева (от 0 до 2)

mod = int(input('Привет! Эта программа рисует уникальные деревья на основе генерации их генетических кодов.\n'
                'Введите модификатор дерева:\n\t\t'
                '0 - стоковое дерево\n\t\t'
                '1 - осеннее дерево\n\t\t'
                '2 - баобаб\n\t\t'
                '3 - бонсай\n'))
while True:
    if mod == 0:
        break
    if mod == 1:
        colors = ['#271d17', '#8B4513', '#808000', '#B8860B']
        break
    elif mod == 2:
        num_i = 6
        angle = 35
        trunk = 8
        thick = 50
        thick_reduction_speed = 0.4
        axiom = '2' * 8 + '0'
        angle_scale = 2
        break
    elif mod == 3:
        num_i = 7
        angle = 35
        trunk = 7
        thick = 20
        axiom = '0'
        break
    else:
        mod = int(input('Введите корректный модификатор.\n'))

print('-- Генерация генетического кода дерева...')

level = 0
for _ in range(num_i):
    tmp = ''
    for c in axiom:
        if c == '2':
            tmp += '3[^30]' if r.randint(0, 100) < 7 and level > 2 else '2'
        elif c == '[':
            level += 1
            tmp += '['
        elif c == ']':
            level -= 1
            tmp += ']'
        else:
            tmp += rules.get(c, c)
    axiom = tmp

# print(axiom)
print('-- Отрисовка дерева...')

t.hideturtle()
t.penup()
t.setpos(0, -300)
t.left(90)
t.pendown()
t.tracer(0)
t.pensize(thick)
t.pencolor(colors[0])

stack = []
for c in axiom:
    if c == '0':
        stack.append(thick)
        t.pensize(4)
        t.pencolor(colors[r.randint(1, 3)])
        t.forward(trunk - 2)
        t.pensize(stack.pop())
        t.pencolor(colors[0])
    elif c == '1' or c == '2' or c == '3':
        if r.randint(0, 100) > 40 * length_scale:
            t.forward(trunk)
    elif c == '[':
        stack.append(thick)
        stack.append(t.ycor())
        stack.append(t.xcor())
        stack.append(t.heading())
        thick *= thick_reduction_speed
        t.pensize(thick)
    elif c == ']':
        t.penup()
        t.setheading(stack.pop())
        t.setpos(stack.pop(), stack.pop())
        thick = stack.pop()
        t.pensize(thick)
        t.pendown()
    elif c == '^':
        t.left(r.randint(-angle, angle) * angle_scale * 3.93)
    elif c == '+':
        t.right(angle - r.randint(-13, 13) * angle_scale)
    elif c == '-':
        t.left(angle - r.randint(-13, 13) * angle_scale)

print('-- Дерево успешно построено.')

t.update()
t.mainloop()
